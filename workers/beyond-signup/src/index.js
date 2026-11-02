// & Beyond sign-up (story 017): a Cloudflare Worker that keeps T&B's own subscriber list in D1.
//
//   POST /subscribe            form post from transformationbeyond.se/beyond/ -> confirmation e-mail
//   GET  /confirm?e=…&t=…      double opt-in: marks the address confirmed
//   GET  /unsubscribe?e=…&t=…  shows a button (link scanners must not unsubscribe anyone)
//   POST /unsubscribe          deletes the address (also RFC 8058 one-click from mail clients)
//   GET  /export               confirmed addresses as CSV, Bearer ADMIN_TOKEN only
//   scheduled                  deletes unconfirmed addresses older than PENDING_DAYS
//
// Tokens are HMAC-SHA256(TOKEN_SECRET, purpose + ":" + email): nothing secret is stored, and the
// send step can derive each subscriber's unsubscribe link. Mail goes through Postmark with open and
// link tracking off. Every response to /subscribe is the same redirect, so the form does not reveal
// whether an address is already on the list.

const CONSENT_VERSION = "2026-11-03";
const EMAIL_RE = /^[^\s@<>()[\],;:"]+@[^\s@<>()[\],;:"]+\.[^\s@<>()[\],;:"]{2,}$/;

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    try {
      if (url.pathname === "/subscribe" && request.method === "POST") return await subscribe(request, env);
      if (url.pathname === "/confirm" && request.method === "GET") return await confirm(url, env);
      if (url.pathname === "/unsubscribe" && request.method === "GET") return await unsubscribePage(url, env);
      if (url.pathname === "/unsubscribe" && request.method === "POST") return await unsubscribe(request, url, env);
      if (url.pathname === "/export" && request.method === "GET") return await exportCsv(request, env);
      return text("Not found", 404);
    } catch (err) {
      console.error(err);
      return text("Något gick fel. Försök igen senare.", 500);
    }
  },

  async scheduled(_event, env) {
    await purgePending(env);
  },
};

// ---------- handlers ----------

async function subscribe(request, env) {
  const site = env.SITE_URL;
  const origin = request.headers.get("Origin");
  if (origin && origin !== new URL(site).origin) return text("Forbidden", 403);

  const form = await request.formData();
  const thanks = redirect(`${site}/beyond/tack/`);
  if ((form.get("website") || "").toString().trim() !== "") return thanks; // honeypot
  if (form.get("consent") !== "yes") return redirect(`${site}/beyond/?fel=samtycke#prenumerera`);

  const email = normalise(form.get("email"));
  if (!email) return redirect(`${site}/beyond/?fel=adress#prenumerera`);

  const now = new Date();
  const stamp = now.toISOString();

  // 1. Per-address reservation, also one atomic statement: insert a new pending row, or take over a
  //    pending row whose last confirmation is older than the cooldown. A confirmed address, or one
  //    inside the cooldown, changes nothing and gets the same answer.
  const cooldownStart = new Date(now.getTime() - Number(env.RESEND_MINUTES || 10) * 60_000).toISOString();
  const reserved = await env.DB.prepare(
    `INSERT INTO subscribers (email, status, consent, created_at, confirm_sent_at) VALUES (?, 'pending', ?, ?, ?)
     ON CONFLICT(email) DO UPDATE SET consent = excluded.consent, confirm_sent_at = excluded.confirm_sent_at
     WHERE subscribers.status = 'pending' AND subscribers.confirm_sent_at < ?`
  ).bind(email, CONSENT_VERSION, stamp, stamp, cooldownStart).run();
  if (changes(reserved) !== 1) return thanks;

  // 2. Global cap: reserve one send in the hourly budget, only for a request that will send.
  //    A single INSERT … SELECT is atomic in D1, so concurrent requests cannot all pass.
  const hourAgo = new Date(now.getTime() - 3600_000).toISOString();
  const slot = await env.DB.prepare(
    "INSERT INTO sends (at) SELECT ? WHERE (SELECT COUNT(*) FROM sends WHERE at > ?) < ?"
  ).bind(stamp, hourAgo, Number(env.MAX_CONFIRMATIONS_PER_HOUR || 50)).run();
  if (changes(slot) !== 1) {
    console.warn("confirmation cap reached");
    await release(env, email, stamp);
    return thanks;
  }
  const slotId = slot.meta.last_row_id;

  const link = await signedLink(env, "confirm", email);
  try {
    await sendConfirmation(env, email, link, site);
  } catch (err) {
    // Same answer as every other case (no enumeration through a mail outage).
    console.error("confirmation mail failed", err);
    // Postmark answered and refused: nothing was sent, so release the reservation and give the
    // budget slot back. A network error is ambiguous (the mail may have gone out): keep the pending
    // row, its cooldown and the slot, so a delivered confirm link still works.
    if (err.definitive) {
      await release(env, email, stamp);
      await env.DB.prepare("DELETE FROM sends WHERE rowid = ?").bind(slotId).run();
    }
  }
  return thanks;
}

// Undo a reservation when no mail went out: a row this request created is deleted (no address is
// kept without a confirmation mail), an older pending row gets its cooldown back so a retry works
// and its earlier confirm link stays valid.
// Both statements only touch the row while it still carries this request's reservation
// (confirm_sent_at = stamp), so a rollback can never clear a newer request's reservation.
export async function release(env, email, stamp) {
  await env.DB.prepare(
    "DELETE FROM subscribers WHERE email = ? AND status = 'pending' AND created_at = ? AND confirm_sent_at = ?"
  ).bind(email, stamp, stamp).run();
  await env.DB.prepare(
    "UPDATE subscribers SET confirm_sent_at = ? WHERE email = ? AND status = 'pending' AND confirm_sent_at = ?"
  ).bind(new Date(0).toISOString(), email, stamp).run();
}

function sendConfirmation(env, email, link, site) {
  return sendMail(env, {
    to: email,
    subject: "Bekräfta din prenumeration på & Beyond",
    text:
      `Hej!\n\nNågon, förhoppningsvis du, vill få veckobrevet & Beyond från Transformation & Beyond till den här adressen.\n\n` +
      `Bekräfta här:\n${link}\n\nOm det inte var du behöver du inte göra något. Adressen raderas automatiskt om ${env.PENDING_DAYS || 7} dagar.\n\n` +
      `Conny Wadbro\nTransformation & Beyond AB\n${site}/beyond/integritet/\n`,
  });
}

async function confirm(url, env) {
  const email = await verified(url.searchParams, env, "confirm");
  if (!email) return redirect(`${env.SITE_URL}/beyond/?fel=lank`);
  const res = await env.DB.prepare(
    "UPDATE subscribers SET status = 'confirmed', confirmed_at = COALESCE(confirmed_at, ?) WHERE email = ?"
  ).bind(new Date().toISOString(), email).run();
  // No row (purged after 7 days, or unsubscribed): say the link no longer works instead of "thanks".
  if (changes(res) !== 1) return redirect(`${env.SITE_URL}/beyond/?fel=lank#prenumerera`);
  return redirect(`${env.SITE_URL}/beyond/bekraftad/`);
}

async function unsubscribePage(url, env) {
  const email = await verified(url.searchParams, env, "unsubscribe");
  if (!email) return redirect(`${env.SITE_URL}/beyond/?fel=lank`);
  const e = escapeHtml(url.searchParams.get("e"));
  const t = escapeHtml(url.searchParams.get("t"));
  return html(
    `<!doctype html><html lang="sv"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">` +
      `<title>Avsluta & Beyond</title><style>body{font-family:system-ui,sans-serif;background:#F7F5F0;color:#1C2022;max-width:36em;margin:15vh auto;padding:0 20px;line-height:1.6}` +
      `button{font:inherit;background:#1C2022;color:#F7F5F0;border:0;padding:12px 22px;cursor:pointer}</style>` +
      `<h1>Avsluta prenumerationen</h1><p>Adressen ${escapeHtml(email)} tas bort från listan och raderas.</p>` +
      `<form method="post" action="/unsubscribe?e=${e}&amp;t=${t}"><button type="submit">Avsluta</button></form></html>`
  );
}

async function unsubscribe(request, url, env) {
  // Mail clients send RFC 8058 one-click as a form post to the List-Unsubscribe URL.
  const email = await verified(url.searchParams, env, "unsubscribe");
  if (!email) return redirect(`${env.SITE_URL}/beyond/?fel=lank`);
  await env.DB.prepare("DELETE FROM subscribers WHERE email = ?").bind(email).run();
  return redirect(`${env.SITE_URL}/beyond/avregistrerad/`);
}

async function exportCsv(request, env) {
  const auth = request.headers.get("Authorization") || "";
  if (!env.ADMIN_TOKEN || !(await equal(auth, `Bearer ${env.ADMIN_TOKEN}`))) return text("Unauthorized", 401);
  const { results } = await env.DB.prepare(
    "SELECT email, confirmed_at, consent FROM subscribers WHERE status = 'confirmed' ORDER BY confirmed_at"
  ).all();
  const lines = ["email,confirmed_at,consent", ...results.map((r) => `${r.email},${r.confirmed_at},${r.consent}`)];
  return new Response(lines.join("\n") + "\n", {
    headers: { "Content-Type": "text/csv; charset=utf-8", "Cache-Control": "no-store" },
  });
}

export async function purgePending(env, now = new Date()) {
  const cutoff = new Date(now.getTime() - Number(env.PENDING_DAYS || 7) * 86400_000).toISOString();
  await env.DB.prepare("DELETE FROM subscribers WHERE status = 'pending' AND created_at < ?").bind(cutoff).run();
  await env.DB.prepare("DELETE FROM sends WHERE at < ?").bind(new Date(now.getTime() - 86400_000).toISOString()).run();
}

// ---------- helpers ----------

export function normalise(value) {
  if (typeof value !== "string") return null;
  const email = value.trim().toLowerCase();
  if (email.length > 254 || !EMAIL_RE.test(email)) return null;
  return email;
}

export async function token(env, purpose, email) {
  if (!env.TOKEN_SECRET) throw new Error("TOKEN_SECRET is not set");
  const key = await crypto.subtle.importKey(
    "raw", new TextEncoder().encode(env.TOKEN_SECRET), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]
  );
  const sig = await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(`${purpose}:${email}`));
  return b64url(new Uint8Array(sig));
}

export async function signedLink(env, purpose, email) {
  const e = b64url(new TextEncoder().encode(email));
  return `${env.WORKER_URL}/${purpose}?e=${e}&t=${await token(env, purpose, email)}`;
}

async function verified(params, env, purpose) {
  const e = params.get("e");
  const t = params.get("t");
  if (!e || !t) return null;
  let email;
  try {
    email = normalise(new TextDecoder().decode(fromB64url(e)));
  } catch {
    return null;
  }
  if (!email) return null;
  return (await equal(t, await token(env, purpose, email))) ? email : null;
}

async function sendMail(env, { to, subject, text: body }) {
  const res = await fetch("https://api.postmarkapp.com/email", {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
      "X-Postmark-Server-Token": env.POSTMARK_TOKEN,
    },
    body: JSON.stringify({
      From: env.MAIL_FROM,
      To: to,
      Subject: subject,
      TextBody: body,
      MessageStream: env.POSTMARK_STREAM || "outbound",
      TrackOpens: false,
      TrackLinks: "None",
    }),
  });
  if (!res.ok) {
    const err = new Error(`Postmark ${res.status}: ${await res.text()}`);
    err.definitive = true; // the provider answered: the mail was not accepted
    throw err;
  }
}

// Constant-time comparison via HMAC of both sides, so length and content leak nothing.
async function equal(a, b) {
  const key = await crypto.subtle.generateKey({ name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  const [x, y] = await Promise.all([a, b].map((s) => crypto.subtle.sign("HMAC", key, new TextEncoder().encode(s))));
  const ux = new Uint8Array(x), uy = new Uint8Array(y);
  let d = 0;
  for (let i = 0; i < ux.length; i++) d |= ux[i] ^ uy[i];
  return d === 0;
}

// D1 reports affected rows as meta.changes.
function changes(result) {
  return result?.meta?.changes ?? 0;
}

function b64url(bytes) {
  let s = "";
  for (const b of bytes) s += String.fromCharCode(b);
  return btoa(s).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}

function fromB64url(s) {
  const bin = atob(s.replace(/-/g, "+").replace(/_/g, "/") + "===".slice((s.length + 3) % 4));
  return Uint8Array.from(bin, (c) => c.charCodeAt(0));
}

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);
}

function redirect(location) {
  return new Response(null, { status: 303, headers: { Location: location, "Cache-Control": "no-store" } });
}

function text(body, status = 200) {
  return new Response(body, { status, headers: { "Content-Type": "text/plain; charset=utf-8" } });
}

function html(body) {
  return new Response(body, {
    headers: {
      "Content-Type": "text/html; charset=utf-8",
      "Cache-Control": "no-store",
      "Content-Security-Policy": "default-src 'none'; style-src 'unsafe-inline'; form-action 'self'",
    },
  });
}
