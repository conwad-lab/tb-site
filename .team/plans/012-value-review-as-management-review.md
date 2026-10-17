---
id: 012
verdict: plan
---

# Plan 012 — The AI Value Review as a management review (round 2, after the advisory panel)

Story: `.team/backlog/012-value-review-as-management-review.md`

## Why round 2
The advisory panel (vault `Transformation& Beyond/panel/2026-10-17-ai-value-review/uppdrag-svar/3-sammanfattning.md`, 7 roles, Claude + Codex) advised: do not merge PR #15 as is. Cap week 1, one scope, make the step after the memo management's choice. Conny decided 2026-10-17: strike "regulatory gap analysis"; the sample PDF is a management memo with the six-rung ladder; no cost data exists, so cap at six interviews.

## Approach
Copy-only change on top of PR #15 (branch `feat/012-value-review-as-management-review`, head `5a706ec`). Edit those lines in place; no CSS, no new markup classes, no URL, `href`, price or layout change.

Strings on the PR branch (old → new), line numbers on `5a706ec`:
1. L291 stage 01 `<p>`, visible: "The AI Value Review — a management review: where your AI operation stands, who owns which decision, and what leadership should decide next. Strategy, AI governance, regulatory gap analysis, project scoping." → "The AI Value Review — a two-week management review for the leadership team: where your AI operation stands, who owns which decision, and what management should decide next."
2. L295 hand-off `<p>`, visible: last sentence "Review recommendations continue through Dignami Assurance." → "If management decides to go further, review recommendations can continue through Dignami Assurance." (first sentence unchanged)
3. L313 eyebrow, visible: "The entry point — fixed price, fixed scope" → "Fixed price, fixed scope — a memo that stands on its own"
4. L318 `.offer-lede`, visible: "A management review for your leadership team:" → "A two-week management review for your leadership team:" (rest of the line, incl. `<b>…</b>`, unchanged)
5. L319 offer button text only: "Book the review" → "Book a scoping call" (`class`, `href="#kontakt"` unchanged). The nav CTA (L182), hero CTA and `#book-cta` are unchanged.
6. L320 sample-PDF link text, visible: "Read a sample review of our own orchestrator first — gaps included →" → "Read a sample management memo first — our own orchestrator on the six-rung ladder, gaps included →" (`href`, `target`, `rel` unchanged)
7. L323 Week 1, visible: "Interviews with the leadership team and an agentic-maturity assessment — where your automation stands today, measured by who actually uses what, not by what is licensed, and who owns each AI decision. Placed on a six-rung capability ladder." → "Up to six 45-minute interviews with the leadership team, booked within week 1, plus read-only access to your usage data. An agentic-maturity assessment — where your automation stands today, measured by who actually uses what, not by what is licensed, and who owns each AI decision. Placed on a six-rung capability ladder."
8. L324 Week 2, visible: "Gap analysis and a management decision memo — the decisions your leadership team needs to take: what to automate, what not to, in which order, and which processes and data foundations must change first for the investment to pay off." → "Gap analysis against the six questions and a management decision memo — the decisions your leadership team needs to take: what to automate and what not to, which processes and data foundations must change first, when an open-source model is enough, and how the economics and token costs work out."
9. L327 row: label "Then" → "After"; text "Management's decisions are the starting point for Dignami Assurance — Understand · Rethink · Rebuild." → "The memo stands on its own. Whether and with whom to go further — Dignami Assurance or anyone else — is management's decision; deciding not to invest is a valid outcome."
10. L428 JSON-LD `description` (not visible): → "Fixed-scope two-week AI value review for the leadership team: up to six leadership interviews, agentic-maturity assessment, gap analysis against six questions, management decision memo with resolvable citations." (`name`, `price`, `priceCurrency` unchanged)

Price block: unchanged. Booking CTA: only the offer-block button text changes; all `href`s and `CALCOM_URL` unchanged. Footer: unchanged.

## Files
- `index.html` — the ten edits above.

## Tests
- `python3 -m html.parser index.html`.
- `grep -c "regulatory gap analysis" index.html` → 0; `grep -c "board-standard\|board standard" index.html` → 0; `grep -c "Up to six 45-minute interviews" index.html` → 1; `grep -c "Book a scoping call" index.html` → 1; `grep -c "Book the review" index.html` → 1 (nav only); `grep -c "Understand · Rethink · Rebuild" index.html` → 1 (stage 02 only).
- `git diff 5a706ec -- index.html` touches only the ten places above.
- Screenshots 1440×900 and 390×844 after scrolling; offer rows must not overflow at 390 px. `href` check (unchanged set).

## Risks / watch out for
- Hard rail: nothing about Dignami beyond the page today; the new hand-off sentence makes Assurance conditional, it does not add a claim.
- The six-interview cap is a delivery commitment Conny accepted; no number beyond it.

## Out of scope
- A decision session in week 2 (panel idea; separate story).
- Contract, GDPR documentation, payment plan (Operatör, before first delivery).
- Nav, hero and booking-band CTA texts; price; URLs; CSS.

## Suggestions for PO
- Story: decision session with management in week 2, replacing part of the gap analysis (panel, förändringsledare + korsgranskning 1).
- Operatör: time budget for six interviews before the first delivery (CFO: zero margin at ten interviews at 1 250 SEK/h).
