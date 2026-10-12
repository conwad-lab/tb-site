---
id: 008
title: D4 + D5 + D7 — mobile hero, navigation and offer rows at 390 px
parked-until: 007
---

## Outcome
At 390 px the hero headline breaks cleanly without a stranded word, the header mark and the "Book the review" CTA each sit on a deliberate line, and the four offer rows show their label above the description instead of a 164 px text column.

## Why
Design review D4, D5 and D7 (Should), `docs/design-review-2026-10.md`, with crops in `docs/design-review-2026-10/390-hero.png`, `390-nav.png`, `390-offer.png`. Today the 48 px h1 takes six lines with "three" alone on one; the mark (205 px) and CTA (145 px) both wrap inside a 350 px row; each `.mrow` reserves 110 px for the label so "Week 1" alone is 202 px tall and the offer block is 1 187 px. Conny chose these (ORDER row 5) within the current identity.

## Acceptance criteria
- [ ] D4 — at 390 px the h1 keeps the same words, typefaces and emphasis; "in one advisor" stays on one line and no line holds a single word. Achieved with a mobile-only measure/size/line-break rule (e.g. a media query on the `<br>` or on `h1` size); the 1440 rendering is pixel-identical to today's `1440-full.png` hero crop.
- [ ] D5 — at 390 px the mark and the CTA no longer both wrap to two lines: either tune spacing and CTA padding so each fits one line, or stack mark and CTA on separate rows with deliberate spacing. Both stay visible and keyboard reachable; the nav links' behaviour at 390 is unchanged from today (the plan states what that is).
- [ ] D7 — at ≤ 520 px (the plan picks the breakpoint) each `.mrow` places `.mk` above its description full-width, keeps the hairline rules between rows, and the offer block's height drops measurably (the PR states before/after heights at 390). Price line, `.cta-big`, sample-PDF link and the `#kontakt` CTA target are untouched.
- [ ] No horizontal overflow at 390 (`scrollWidth === innerWidth`). No change at 1440 anywhere except where the plan explicitly says so.
- [ ] No visible copy changes. Price block, booking CTA, footer, `CNAME` untouched. No new fonts or colours.
- [ ] Team settings test passes; screenshots at both widths attached, plus 390 crops of hero, nav and offer for comparison with the report's crops.

## Out of scope
- D6, D8 (story 009). D9 not taken.
- Any change to the desktop layout or to the section order.

## Log
- 2026-10-12 PO: created from ORDER row 5. D4, D5 and D7 grouped because all three are 390-px CSS changes with no copy; one PR.
