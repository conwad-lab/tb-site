---
id: 005
title: D1 — content visible in unscrolled full-page renders (reveal fallback)
---

## Outcome
A fresh full-page capture of the page that never scrolls shows every section, while the scroll-reveal animation still plays for a normal visitor.

## Why
Design review finding D1 (Must), `docs/design-review-2026-10.md`: with JavaScript and normal motion, the script adds `.reveal` to all seven `main section`s and the IntersectionObserver only removes the hidden state when a section is scrolled into view. A screenshot-based link preview, a print, or any full-page render that does not scroll shows 19 of 25 `.r-fade` elements at `opacity: 0` (`docs/design-review-2026-10/1440-noscroll.png`, `390-noscroll.png`). The copy is in the HTML, so this is a rendering risk, not an indexing failure, but it is the one Must in the report. Conny ordered D1 first (ORDER row 5).

## Acceptance criteria
- [ ] A Playwright full-page screenshot at 1440×900 and at 390×844 taken right after `networkidle`, **without any scrolling**, shows all content: zero `.r-fade` elements with computed `opacity` below 1 after a bounded wait the plan names (the report's proposal: a load fallback that clears any JS-added hidden state within a short, fixed time even if the observer never fires). Screenshots of this exact condition attached to the PR, alongside the usual scrolled ones.
- [ ] The reveal still plays for a normal visitor: scrolling into a section below the fold adds `.revealed` as today, and sections already revealed by the fallback do not re-animate or flash. The plan says how the fallback and the observer coexist.
- [ ] With JavaScript disabled and with `prefers-reduced-motion: reduce`, behaviour is unchanged from today (everything visible, no `.reveal` class added).
- [ ] No visible copy changes. No change to the price block, booking CTA, Cal.com script, footer or `CNAME`. No new hosts.
- [ ] Team settings test passes: `python3 -m html.parser index.html` clean, Playwright screenshots at both widths after scrolling to bottom, all `href`s 200. Screenshots attached.
- [ ] `docs/design-review-2026-10.md` is not edited (the report is a record of the review, not a living checklist).

## Out of scope
- D2–D8 (stories 006–009). D9 is not taken (Conny's decision).
- Changing the reveal timing, easing, or which elements fade.

## Log
- 2026-10-12 PO: created from ORDER row 5 (D1 first). Row 5 split into stories 005, 007, 008, 009; row 6 (C6) became 006 and is chained between them. Stories are parked in a chain so one PR touches `index.html` at a time.
