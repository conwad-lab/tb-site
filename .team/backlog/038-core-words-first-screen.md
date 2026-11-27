---
id: 038
title: "The core words on the first screen"
---

## Outcome
On both home pages a short label line sits directly above the hero `h1`: "Understand · Rethink · Rebuild" on `/` and "Förstå · Ompröva · Bygg om" on `/sv/`, styled as the existing `.tag` labels, as text and not a heading. Nothing else changes.

## Why
Conny's decision 2026-11-23: "Understand · Rethink · Rebuild" becomes T&B's core words (Dignami borrows them for Assurance). The first screen should say them before the headline. Kö row "Kärnorden på första skärmen" in `.team/ORDER.md`.

## Signal
- After merge, on the live site from a connection that reaches it (the Mac): the label line shows above the headline on `/` and `/sv/` at 1440×900 and 390×844, and the red booking band still shows on the first screen (story 035).
- Conny says whether the line reads right. The Coordinator logs seen / not seen here.

## Acceptance criteria
- [ ] `index.html`: `<p class="tag">Understand · Rethink · Rebuild</p>` is the element directly before the hero's `<h1>`; `sv/index.html`: `<p class="tag">Förstå · Ompröva · Bygg om</p>` in the same place. The dots are U+00B7. No new `h` element.
- [ ] `assets/site.css`: the label sits above the `&` glyph (`position:relative`) and its square marker is in the text colour, as on the dark contact band (`.end .tag::before`). The dots are in the text colour: red `#CF2318` on the hero navy `#0C2233` is about 3.0:1, under WCAG AA's 4.5:1 for 15 px text, so the row's fallback applies.
- [ ] `bin/test-hero-core-words.py` (new) is green; `bin/test-hero-first-screen.py` and `bin/test-hero-motion.py` still green.
- [ ] Screenshots of the first screen of both pages at 1440×900 and 390×844, before and after, attached to the PR; the `h1` does not collide with the `&` glyph and the booking band is still in view in all four "after" shots.
- [ ] Test before commit green.
- [ ] Price block, booking CTA, Cal.com URL, contact address, founder claims, footer, links, colours and all other copy unchanged.

## Out of scope
- Uppercase or letter-spaced labels: the existing `.tag` style is bold 15 px in normal case with a square marker, and this story uses it as is (see the plan's Suggestions for PO).
- The film, the headline, the diagram, the hero height.

## Vad blir publikt?
Three words above the headline on both home pages: "Understand · Rethink · Rebuild" and "Förstå · Ompröva · Bygg om".

## Log
- 2026-11-26 Coordinator: written from the Kö row (after 035, merged as #90), builder codex-cli.

— Coordinator (Claude) on behalf of Conny
