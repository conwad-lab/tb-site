---
id: 017
verdict: plan
---

# Plan 017 — & Beyond e-mail sign-up

Story: `.team/backlog/017-beyond-email-signup.md`. Stacked on 016 (needs `/beyond/`).

## Approach
A Cloudflare Worker (`workers/beyond-signup/`) with a D1 table holds the list. The site keeps no script beyond a 6-line inline one that shows a Swedish error message from `?fel=`. Tokens are HMAC-SHA256(TOKEN_SECRET, purpose:email), so nothing secret is stored and the later send step can derive unsubscribe links. Postmark sends the confirmation with tracking off.

## Files
- `workers/beyond-signup/src/index.js`, `schema.sql`, `wrangler.toml` (placeholders, no ids or secrets), `package.json` (`type: module`, no dependencies), `test/worker.test.mjs`, `README.md` (go-live steps for Conny).
- `_config.yml` (Human-merge path): `beyond_signup_url: ""`, `workers` excluded.
- `beyond/index.html`: the form inside `{% if site.beyond_signup_url %}`.
- `beyond/tack/`, `beyond/bekraftad/`, `beyond/avregistrerad/` (noindex), `beyond/integritet/` (draft privacy text).
- `_layouts/beyond-base.html`: `noindex` meta when the page asks for it. `assets/beyond.css`: form and page styles from existing tokens.

## Tests
- `node --test workers/beyond-signup/test/*.test.mjs`: subscribe, confirm, tampered and cross-purpose tokens, unsubscribe GET/POST, enumeration, cooldown and cap, honeypot/consent/address/origin, export auth, purge, Postmark failure, normalisation.
- Jekyll build with github-pages 232: form absent with an empty URL, present with one; `_site/` has no `workers/`; `index.html` unchanged; all pages parse.
- Playwright 1440 and 390 on `/beyond/` with the form, `/beyond/integritet/`, `/beyond/tack/`.

## Risks
- Hard rail "no third-party scripts": the form posts to a Worker on a T&B subdomain and loads nothing; the error message script is inline and first-party.
- Privacy text is a draft; Conny writes or approves it, and checks Cloudflare and Postmark terms (marked KONTROLLERA).
- DNS for `lista.transformationbeyond.se` is at the registrar, not Cloudflare (README step 4).
