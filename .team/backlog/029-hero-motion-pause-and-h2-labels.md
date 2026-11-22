---
id: 029
title: "A pause button for the moving hero, and two section labels as headings"
---

## Outcome
A visitor on either home page (`/`, `/sv/`) can stop everything that moves on the first screen with one button in the hero's corner: the film, and the line animation that takes over when the film does not load. A visitor who has asked their system for reduced motion never downloads or plays the film at all. The section labels "How we work" / "Arbetssätt" and "The questions we answer" / "Frågorna vi besvarar" become `h2` headings, so a screen reader's heading list and an agent reading the HTML see the page's real sections. Nothing else looks different.

## Why
Astra's counter-review on issue #63 (`docs/design-utforskning/granskning-063-codex.md` on branch `feat/063-design-review`, points 1, 4 and S1): the film is `autoplay muted loop` with no pause, the fallback `.flow` animation runs 55/90 s loops without end, and reduced motion only hides the video with CSS, which does not stop the download. WCAG 2.2.2 (Pause, Stop, Hide) asks for a way to stop motion that lasts more than five seconds. The two labels are `p.tag`, so the sections under them have no heading. ORDER row (Kö, "Rörelse och rubriker på startsidorna"), requested by the Coordinator 2026-11-20 under Conny's standing "fortsätt till målet är uppnått"; picked for tonight's Astra run on Conny's question 2026-11-22 ("Finns där något vi kan köra på inatt som kräver Astra?").

## Signal
- After merge, on the live site from a connection that reaches it (the Mac): the button is visible on `/` and `/sv/`, a click stops the film and changes the label to "Play film" / "Spela filmen"; with reduced motion on, the network panel shows no request for `sluseholmen-720.mp4`.
- The heading list of both pages (`document.querySelectorAll('h2')`) includes the two labels.
- The Coordinator logs seen / not seen here.

## Acceptance criteria
- [ ] Both home pages: the `<video class="film">` has no `src` attribute; its address is in `data-src`, and a script sets `src` only when `prefers-reduced-motion: reduce` does not match. Poster, `muted`, `loop`, `playsinline`, `autoplay` and the `onerror` fallback stay.
- [ ] Both home pages: a `<button class="motion" type="button" hidden>` inside `.hero`, revealed by the same script; a click pauses the film and the `.flow` animation (class `paused` on `.hero`) and swaps the label; a second click resumes. Copy: "Pause film" / "Play film" (en), "Pausa filmen" / "Spela filmen" (sv).
- [ ] Without JavaScript: no film request, no button, the poster shows; with reduced motion: no film request, no button, `.flow` static as today.
- [ ] The two labels per page are `h2.tag` with unchanged look: `assets/site.css` gets an `h2.tag` rule that resets the heading font, letter spacing, line height and text wrap to the `.tag` paragraph's values; before/after screenshots show no visible change.
- [ ] `bin/test-hero-motion.py` (stdlib Python) checks the markup, CSS and script facts above and is green; Test before commit is green.
- [ ] Price block, booking CTA, Cal.com URL, contact address, founder claims and every other copy string unchanged.
- [ ] Screenshots at 1440×900 and 390×844 of both pages (first screen with the button, full page) attached to the PR; the button's text meets WCAG AA against its background.

## Out of scope
- `<!doctype html>` and standards mode (story 030, next); a lower hero; colour changes; the diagram's aria-label (Astra's S2, a later row).

## Vad blir publikt?
A small "Pause film" / "Pausa filmen" button in the top right corner of the first screen on both home pages. The two section labels look the same but are headings in the HTML. Visitors with reduced motion no longer download the film.

## Log
- 2026-11-22 Coordinator's planner (thread "Använd Codex och Astra mer i natt"): written from the Kö row, builder codex-cli on Astra for tonight.

— Coordinator (Claude) on behalf of Conny
