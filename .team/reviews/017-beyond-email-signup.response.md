# 017 — Builder's response

## Codex round 1 — 2026-11-02
- M1 (P1, cooldown not atomic; 20 concurrent requests sent 20 mails): fixed in 0cb4524. The per-address check and reservation is one `INSERT … ON CONFLICT DO UPDATE … WHERE status='pending' AND confirm_sent_at < cooldown`; mail goes out only when it changed a row. Test `20 concurrent requests for one address send one mail`.
- M2 (cap counted addresses, not sends): fixed in 0cb4524. New table `sends` (no personal data, purged after a day); one atomic `INSERT … SELECT … WHERE count < cap` per mail, taken only after the address reservation so cooldown hits do not burn the budget. Test `the hourly cap counts sends, not addresses`.
- M3 (500 on Postmark failure reveals membership): fixed in 0cb4524. Mail failure is logged and answered with the same 303 as every other case; a row this request created is deleted, an older pending row gets its cooldown back. Test `Postmark outage: same answer as for a known address, and the person can retry at once`.
- `@codex security review` on bb877c9 ended in "Unknown error"; requested once more on this head.

## Codex round 2 — 2026-11-02
- M4 (rollback could clear a newer reservation): fixed in c52cfca. Both rollback statements require `confirm_sent_at = <this request's stamp>`, so they cannot touch a row another request has reserved since. Test `a rollback does not clear a newer reservation`.
- S1 (refused sends keep consuming the hourly budget): fixed in c52cfca. The slot's row id is kept; when Postmark answers with an error the slot is deleted, while a network error (mail may have gone out) keeps it. Test `a refused mail gives its hourly slot back; a network error keeps it`.

## Codex round 3 — 2026-11-02
- M5 (network error released a reservation whose mail may have been delivered): fixed in bf6f291. Only a definitive Postmark refusal releases the row and the slot; a network error keeps the pending row, its cooldown and the slot. `confirm` now answers "link no longer valid" when no row was updated, instead of the thank-you page. Tests `a refused mail gives its hourly slot back; a network error keeps it` (extended) and `a confirm link for an address no longer on the list says so`.

Three Codex rounds reached (CLOUD.md § Builder 5): stopping the rounds here. The fix for M5 has not had its own Codex round; the Judge should read it. `@codex security review` (errored on bb877c9) requested once more on this head.
