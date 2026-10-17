---
id: 012
title: Present The AI Value Review as a management review that precedes Dignami Assurance
---

## Outcome
A leader reading the offer understands that The AI Value Review is a review for the leadership team — where the AI operation stands, who owns which decision, what management should decide next — and that Dignami Assurance takes those decisions further.

## Why
Conny, 2026-10-17: the review should read as a management review held before Dignami Assurance runs. Today the copy frames it as an architecture-and-maturity assessment answered "to board standard"; the decision owner (the leadership team) and the step after (Assurance) are implicit.

## Acceptance criteria
- [ ] Offer section (`#review`): lede, Week 1, Week 2 and "You receive" rows name the leadership team as audience and decision owner, and the memo as a management decision memo. Exact strings in the plan.
- [ ] A new row in the offer mechanics states that management's decisions are the starting point for Dignami Assurance, using only wording already on the page for Assurance (Understand · Rethink · Rebuild).
- [ ] Stage 01 · Advise text says "management review" and drops "board-standard answer".
- [ ] JSON-LD `makesOffer.description` matches the new framing; `name`, `price`, `priceCurrency` unchanged.
- [ ] Unchanged, verified by diff: price line, `<h2>The AI Value Review</h2>`, all CTA texts and `href`s (incl. `CALCOM_URL`, `#book-cta` mailto), sample-PDF link, the six questions, hand-off block, footer, `<title>`, meta/OG descriptions, `CNAME`.
- [ ] No claim of ISO 42001 conformity or any certification; nothing about Dignami beyond what the page already says.
- [ ] Team settings test passes (HTML parse, screenshots at 1440×900 and 390×844 after scrolling, all `href`s 200 or reported as not checked). Screenshots attached.

## Out of scope
- ISO/IEC 42001 9.3 structure (Conny chose leadership framing only).
- Price, duration, scope, URLs, Cal.com event, sample PDF, nav labels, layout or CSS.
- Changes on dignami.com.

## Log
- 2026-10-17 PO: created from Conny's ask; one question asked (framing) → "Ledningens genomgång". First real story through cloud mode (CLOUD.md), Codex started by direct task.
