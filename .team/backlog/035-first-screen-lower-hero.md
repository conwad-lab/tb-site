---
id: 035
title: "A lower first screen on the home pages"
---

## Outcome
On both home pages (`/`, `/sv/`) the hero is a little lower, so the red booking band shows on the first screen at 1440×900 and 390×844, also with browser zoom and with the longer English headline. The diagram's `aria-label` already follows its visible axes and stays as it is. No visible text, price, link or colour changes.

## Why
Issue #63 point 2 and Conny's launch plan 2026-11-23 (& Beyond #1 goes out Monday 2026-11-30): the film-and-headline hero fills the whole first screen and pushes the booking band below the fold. Codex found the same in the design review (S2, `docs/design-utforskning/granskning-063-codex.md`, branch `feat/063-design-review`).

## Signal
- After merge, on the live site from a connection that reaches it (the Mac): at 1440×900 and 390×844, on `/` and `/sv/`, the red booking band is visible without scrolling.
- Conny says whether the first screen feels right. The Coordinator logs seen / not seen here.

## Acceptance criteria
- [ ] `assets/site.css`: the `.hero` rule has `min-height:86svh` instead of `min-height:100svh`; nothing else in that rule changes.
- [ ] `bin/test-hero-first-screen.py` (new) is green: it pins the 86svh value and that the diagram's `aria-label` on both pages still names the two axes in the order of the visible axis texts.
- [ ] Screenshots at 1440×900 and 390×844 of both pages' first screen, before and after, attached to the PR; the booking band is visible in all four "after" shots (also at 125 % zoom on the English page).
- [ ] Test before commit green; `bin/test-hero-motion.py` still green.
- [ ] Price block, booking CTA, Cal.com URL, contact address, founder claims, footer and all copy unchanged; no extra section.

## Out of scope
- The film, the headline size, the diagram's look, any new section.

## Vad blir publikt?
The first screen of both home pages becomes a little lower, so the red booking band is visible straight away. Nothing else changes.

## Log
- 2026-11-24 the daily routine (step 1b, story V): written from the Kö row (id 035), builder codex-cli.

— Coordinator (Claude) on behalf of Conny
