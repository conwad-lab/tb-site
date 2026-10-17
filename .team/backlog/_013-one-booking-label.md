---
id: 013
title: One booking label — "Book a scoping call" on every booking button
---

parked-until: 012

## Outcome
Every button that books the intro call says "Book a scoping call", so a visitor sees one action under one name.

## Why
Review 012 (N5): after PR #15 the page has three labels for the same Cal.com intro call — "Book a scoping call" (offer), "Book the review" (nav) and "Book the AI value review" (hero, booking band). Conny decided 2026-10-17: "Book a scoping call" everywhere.

## Acceptance criteria
- [ ] Nav CTA, hero `.cta-big`, offer button and `#book-cta` all read "Book a scoping call". Exact strings and lines in the plan.
- [ ] Unchanged, verified by diff: every `href`, `CALCOM_URL`, the Cal.com script, the `mailto:` address in `#book-cta` (its `subject=` may stay `AI%20Value%20Review`), price, footer, `CNAME`.
- [ ] At 390 px the nav CTA does not wrap or overflow with the longer label (design review D5 fixed nav wrapping; do not regress it).
- [ ] Team settings test passes; screenshots at both widths attached.

## Out of scope
- Cal.com event title (Operatör line).
- Sample PDF link (waits for the new PDF; Operatör line).
- Any other copy, CSS beyond what keeps the nav from wrapping.

## Log
- 2026-10-17 PO: created from ORDER row 013, parked until 012 (PR #15) is merged because it edits the same lines.
