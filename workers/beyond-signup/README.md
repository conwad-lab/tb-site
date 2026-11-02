# beyond-signup

Cloudflare Worker that keeps the *& Beyond* subscriber list in T&B's own D1 database (story 017).
The site's form on `/beyond/` is a plain HTML form that posts here; no script runs on the site.

What it stores: the address, `pending`/`confirmed`, the version of the privacy text, and three timestamps.
No IP address, no name, no opens or clicks. Unconfirmed addresses are deleted after 7 days; unsubscribing
deletes the address. Mail goes through Postmark with open and link tracking off.

## Tests

    node --test test/*.test.mjs     # Node 22+, no install

## Going live (Conny only, nothing here deploys itself)

1. Cloudflare: `npx wrangler d1 create beyond-subscribers`, put the id in `wrangler.toml`, then
   `npx wrangler d1 execute beyond-subscribers --remote --file schema.sql`.
2. Postmark: a server with a transactional stream; verify the sender domain transformationbeyond.se
   (DKIM and Return-Path DNS records at the registrar). Tracking stays off (the Worker also sends
   `TrackOpens: false`, `TrackLinks: "None"`).
3. Secrets: `npx wrangler secret put TOKEN_SECRET` (long random string; changing it invalidates every
   confirm and unsubscribe link), `POSTMARK_TOKEN`, `ADMIN_TOKEN`.
4. DNS: `lista.transformationbeyond.se` as a Worker custom domain. The site's DNS is at the registrar,
   not Cloudflare, so either move the zone or use a `*.workers.dev` URL and change `WORKER_URL`.
5. `npx wrangler deploy`, then set `beyond_signup_url` in the site's `_config.yml` to
   `https://lista.transformationbeyond.se/subscribe`. The form appears on `/beyond/` only when it is set.

Export the list: `curl -H "Authorization: Bearer $ADMIN_TOKEN" https://lista.transformationbeyond.se/export`.

Sending the letter to the list is a later story: it derives each subscriber's unsubscribe link with
`signedLink(env, "unsubscribe", email)` and sends it in the body and as `List-Unsubscribe` +
`List-Unsubscribe-Post: List-Unsubscribe=One-Click` (RFC 8058).
