---
id: 021
title: "& Beyond on the home page — menu link and latest letter"
---

## Outcome
A visitor to https://transformationbeyond.se/ or /sv/ finds *& Beyond* from the menu, and once a letter is published the home page shows the latest letter's title and date with a link to it, updated by the Jekyll build without hand edits.

## Why
The vault's `Transformation & Beyond innehall/mal.md` says the weekly letter should reach readers, and the idea board's goal for T&B (`idetavlor/transformation-beyond/ideas.md`) is a named buyer saying yes to a first paid engagement; the letter is the way a buyer meets Conny's thinking before a scoping call. Today *& Beyond* is only a footer link on the English page (`index.html:388`, added by story 016) and not linked at all from `/sv/`, although the letter is in Swedish. Source: Förslag "Mål 2/3" (Coordinator's goal reading, 2026-11-17).

## Signal
- After merge: the menu on `/` and `/sv/` has a link to `/beyond/` that returns 200.
- After the first letter is imported into `_beyond/`: both home pages show its title and date and link to its page, with no change to `index.html` or `sv/index.html` in that import PR.
- Not measurable as readers yet (no analytics on the site, by design); the Coordinator logs seen / not seen for the two points above.

## Acceptance criteria
- [ ] The menu (`nav.nav-r`) on `index.html` and `sv/index.html` has one new link to `/beyond/` ("& Beyond" on both), before the booking button; the mobile menu at 390 px shows it without horizontal scroll.
- [ ] `sv/index.html` gets the footer link the English page already has, in Swedish ("& Beyond — veckobrev").
- [ ] A "Latest letter" / "Senaste brevet" block on both home pages, built with Liquid from `site.beyond` (newest by `date`): week, title, date, link; on the English page marked "(in Swedish)" with `lang="sv"` on the Swedish title. With no letters the block renders nothing (no empty heading).
- [ ] Shown with a test fixture letter in a local Jekyll build (not committed): block present with the right title and link; without it: block absent.
- [ ] Price block, booking CTA, Cal.com URL, contact address and founder claims unchanged (Human-merge rails); no other copy changes.
- [ ] No script, tracker or new font host; WCAG AA contrast for the block; Team settings tests and screenshots at 1440×900 and 390×844 of both pages, with and without a fixture letter, attached to the PR.

## Out of scope
- The e-mail sign-up (step 2 of & Beyond): waits for Conny's channel decision.
- UTM parameters on the Cal.com buttons: waits for Conny's yes (row 013 locked the URL).
- Importing a letter, or changing `/beyond/` itself.

## Vad blir publikt?
A menu link to `/beyond/` on both home pages, the Swedish footer link, and (once a letter exists) a "Latest letter" block showing that letter's title and date.

## Log
- 2026-11-17 PO: created from Förslag "Mål 2/3" on the Coordinator's assignment (thread "Planera första storyn per projekt"). Public repo: can be built now.

— Coordinator (Claude) on behalf of Conny
