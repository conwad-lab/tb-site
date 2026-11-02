---
id: 017
title: "& Beyond e-mail sign-up — T&B's own subscriber list, double opt-in, no tracking"
---

## Outcome
A visitor on `/beyond/` can sign up for *& Beyond* by e-mail; the list lives in T&B's own database, every address is confirmed by double opt-in, and no opens or clicks are tracked.

## Why
Step 2 of the proposal of 2026-11-02: T&B should own its subscriber list instead of relying only on LinkedIn. Recommended option 1 (own database on Cloudflare D1, mail through Postmark with tracking off, as techbyjohan.com does). Built as a draft on Conny's "Kör autonomt i natt" (2026-11-02); **Conny has not yet chosen the e-mail option** — this story is under Förslag until Conny does.

## Signal
After go-live: confirmed addresses in the export grow week by week; no Postmark bounce or spam complaint above 0.1 %.

## Acceptance criteria
- [ ] Plain HTML form on `/beyond/` (no third-party script), shown only when `beyond_signup_url` is set.
- [ ] Double opt-in: an address is `confirmed` only through the link in the confirmation mail; unconfirmed addresses are deleted after 7 days.
- [ ] Unsubscribe deletes the address; a GET only shows a button, so link scanners cannot unsubscribe.
- [ ] Same response whether or not an address is on the list; per-address resend cooldown and an hourly cap on confirmation mail.
- [ ] Postmark with `TrackOpens: false` and `TrackLinks: "None"`; no IP address or name stored.
- [ ] Confirmed list exportable as CSV behind an admin token.
- [ ] Privacy page `/beyond/integritet/` that Conny writes or approves.
- [ ] Worker tests pass (`node --test`), site builds with the github-pages gem, screenshots at both widths.

## Out of scope
- Sending the letter to the list (next story: send script, `List-Unsubscribe` one-click headers).
- Creating the Cloudflare, Postmark or DNS setup (Operatör: Conny).

## Log
- 2026-11-02 PO (project thread): drafted overnight on Conny's go-ahead to run autonomously; stacked on 016.
