// Run: node --test workers/beyond-signup/test/  (Node 22+, no dependencies)
import { test, beforeEach } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { DatabaseSync } from "node:sqlite";
import worker, { purgePending, signedLink, normalise } from "../src/index.js";

const SITE = "https://transformationbeyond.se";
const WORKER = "https://lista.transformationbeyond.se";
let env, mails;

// Minimal D1 stand-in over node:sqlite: prepare().bind().first()/run()/all().
function fakeD1() {
  const db = new DatabaseSync(":memory:");
  db.exec(readFileSync(new URL("../schema.sql", import.meta.url), "utf8"));
  return {
    raw: db,
    prepare(sql) {
      let args = [];
      const stmt = {
        bind: (...a) => ((args = a), stmt),
        first: async () => db.prepare(sql).get(...args) ?? null,
        run: async () => ({ meta: { changes: Number(db.prepare(sql).run(...args).changes) } }),
        all: async () => ({ results: db.prepare(sql).all(...args) }),
      };
      return stmt;
    },
  };
}

beforeEach(() => {
  mails = [];
  env = {
    DB: fakeD1(), SITE_URL: SITE, WORKER_URL: WORKER, TOKEN_SECRET: "test-secret", ADMIN_TOKEN: "admin",
    POSTMARK_TOKEN: "pm", MAIL_FROM: "Conny Wadbro <beyond@transformationbeyond.se>",
  };
  globalThis.fetch = async (url, init) => {
    mails.push({ url, body: JSON.parse(init.body), headers: init.headers });
    return new Response("{}", { status: 200 });
  };
});

const post = (fields, headers = { Origin: SITE }) => {
  const body = new URLSearchParams(fields);
  return worker.fetch(new Request(`${WORKER}/subscribe`, { method: "POST", body, headers }), env);
};
const rows = () => env.DB.raw.prepare("SELECT * FROM subscribers").all();

test("subscribe sends one untracked confirmation and stores a pending row", async () => {
  const res = await post({ email: " Anna@Example.se ", consent: "yes" });
  assert.equal(res.status, 303);
  assert.equal(res.headers.get("Location"), `${SITE}/beyond/tack/`);
  assert.equal(rows().length, 1);
  assert.equal(rows()[0].email, "anna@example.se");
  assert.equal(rows()[0].status, "pending");
  assert.equal(mails.length, 1);
  assert.equal(mails[0].url, "https://api.postmarkapp.com/email");
  assert.equal(mails[0].body.TrackOpens, false);
  assert.equal(mails[0].body.TrackLinks, "None");
  assert.match(mails[0].body.TextBody, new RegExp(`${WORKER}/confirm\\?e=`));
});

test("confirm link confirms; a tampered link does not", async () => {
  await post({ email: "anna@example.se", consent: "yes" });
  const link = await signedLink(env, "confirm", "anna@example.se");
  const bad = link.replace(/t=./, "t=X");
  let res = await worker.fetch(new Request(bad), env);
  assert.equal(res.headers.get("Location"), `${SITE}/beyond/?fel=lank`);
  assert.equal(rows()[0].status, "pending");
  res = await worker.fetch(new Request(link), env);
  assert.equal(res.headers.get("Location"), `${SITE}/beyond/bekraftad/`);
  assert.equal(rows()[0].status, "confirmed");
});

test("an unsubscribe token cannot confirm and a confirm token cannot unsubscribe", async () => {
  await post({ email: "anna@example.se", consent: "yes" });
  const unsub = await signedLink(env, "unsubscribe", "anna@example.se");
  const asConfirm = unsub.replace("/unsubscribe?", "/confirm?");
  await worker.fetch(new Request(asConfirm), env);
  assert.equal(rows()[0].status, "pending");
  const conf = await signedLink(env, "confirm", "anna@example.se");
  await worker.fetch(new Request(conf.replace("/confirm?", "/unsubscribe?"), { method: "POST" }), env);
  assert.equal(rows().length, 1);
});

test("GET unsubscribe only shows a button; POST deletes the address", async () => {
  await post({ email: "anna@example.se", consent: "yes" });
  await worker.fetch(new Request(await signedLink(env, "confirm", "anna@example.se")), env);
  const link = await signedLink(env, "unsubscribe", "anna@example.se");
  const page = await worker.fetch(new Request(link), env);
  assert.equal(page.status, 200);
  assert.match(await page.text(), /<form method="post"/);
  assert.equal(rows().length, 1);
  const res = await worker.fetch(new Request(link, { method: "POST" }), env);
  assert.equal(res.headers.get("Location"), `${SITE}/beyond/avregistrerad/`);
  assert.equal(rows().length, 0);
});

test("same answer for a confirmed address, and no new mail", async () => {
  await post({ email: "anna@example.se", consent: "yes" });
  await worker.fetch(new Request(await signedLink(env, "confirm", "anna@example.se")), env);
  const res = await post({ email: "anna@example.se", consent: "yes" });
  assert.equal(res.headers.get("Location"), `${SITE}/beyond/tack/`);
  assert.equal(mails.length, 1);
});

test("resend cooldown and hourly cap limit confirmation mail", async () => {
  await post({ email: "anna@example.se", consent: "yes" });
  await post({ email: "anna@example.se", consent: "yes" });
  assert.equal(mails.length, 1);
  env.MAX_CONFIRMATIONS_PER_HOUR = "2";
  await post({ email: "b@example.se", consent: "yes" });
  await post({ email: "c@example.se", consent: "yes" });
  assert.equal(mails.length, 2);
  assert.equal(rows().length, 2);
});

test("honeypot, missing consent, bad address and foreign origin are refused without mail", async () => {
  assert.equal((await post({ email: "a@example.se", consent: "yes", website: "x" })).headers.get("Location"), `${SITE}/beyond/tack/`);
  assert.match((await post({ email: "a@example.se" })).headers.get("Location"), /fel=samtycke/);
  assert.match((await post({ email: "not-an-address", consent: "yes" })).headers.get("Location"), /fel=adress/);
  assert.equal((await post({ email: "a@example.se", consent: "yes" }, { Origin: "https://evil.example" })).status, 403);
  assert.equal(mails.length, 0);
  assert.equal(rows().length, 0);
});

test("export needs the admin token and lists confirmed addresses only", async () => {
  await post({ email: "anna@example.se", consent: "yes" });
  await post({ email: "bo@example.se", consent: "yes" });
  await worker.fetch(new Request(await signedLink(env, "confirm", "anna@example.se")), env);
  assert.equal((await worker.fetch(new Request(`${WORKER}/export`), env)).status, 401);
  assert.equal((await worker.fetch(new Request(`${WORKER}/export`, { headers: { Authorization: "Bearer nope" } }), env)).status, 401);
  const res = await worker.fetch(new Request(`${WORKER}/export`, { headers: { Authorization: "Bearer admin" } }), env);
  const csv = await res.text();
  assert.match(csv, /^email,confirmed_at,consent\nanna@example.se,/);
  assert.doesNotMatch(csv, /bo@example.se/);
});

test("scheduled purge deletes old unconfirmed rows only", async () => {
  await post({ email: "anna@example.se", consent: "yes" });
  await post({ email: "bo@example.se", consent: "yes" });
  await worker.fetch(new Request(await signedLink(env, "confirm", "anna@example.se")), env);
  await purgePending(env, new Date(Date.now() + 8 * 86400_000));
  assert.deepEqual(rows().map((r) => r.email), ["anna@example.se"]);
});

test("Postmark outage: same answer as for a known address, and the person can retry at once", async () => {
  await post({ email: "anna@example.se", consent: "yes" });
  await worker.fetch(new Request(await signedLink(env, "confirm", "anna@example.se")), env);
  globalThis.fetch = async () => new Response("down", { status: 503 });
  const orig = console.error;
  console.error = () => {};
  const unknown = await post({ email: "bo@example.se", consent: "yes" });
  const known = await post({ email: "anna@example.se", consent: "yes" });
  console.error = orig;
  assert.equal(unknown.status, 303);
  assert.equal(known.status, 303);
  assert.equal(unknown.headers.get("Location"), known.headers.get("Location"));
  globalThis.fetch = async (url, init) => (mails.push({ url, body: JSON.parse(init.body) }), new Response("{}"));
  await post({ email: "bo@example.se", consent: "yes" });
  assert.equal(mails.filter((m) => m.body.To === "bo@example.se").length, 1);
});

test("20 concurrent requests for one address send one mail", async () => {
  await Promise.all(Array.from({ length: 20 }, () => post({ email: "anna@example.se", consent: "yes" })));
  assert.equal(mails.length, 1);
});

test("the hourly cap counts sends, not addresses", async () => {
  env.MAX_CONFIRMATIONS_PER_HOUR = "2";
  env.RESEND_MINUTES = "0";
  await post({ email: "anna@example.se", consent: "yes" });
  await new Promise((r) => setTimeout(r, 5));
  await post({ email: "anna@example.se", consent: "yes" });
  await post({ email: "bo@example.se", consent: "yes" });
  assert.equal(mails.length, 2);
});

test("address normalisation", () => {
  assert.equal(normalise(" A@B.se "), "a@b.se");
  for (const bad of ["", "a@b", "a b@c.se", "<a@b.se>", "a@b.se\nBcc: x@y.se", "x".repeat(250) + "@b.se", null]) {
    assert.equal(normalise(bad), null, String(bad));
  }
});
