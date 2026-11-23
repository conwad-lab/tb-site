---
id: 031
title: "The film's pause button shows only a pause or play symbol"
---

## Outcome
On both home pages (`/`, `/sv/`) the pause button in the hero's top right corner is a small, quiet round button that shows only a symbol: two bars (pause) while the film plays, a triangle (play) when it is paused. No visible text. A screen reader still hears "Pause film" / "Play film" (en) and "Pausa filmen" / "Spela filmen" (sv), and everything story 029 built still holds: one click stops the film and the line animation, reduced motion and no JavaScript mean no film request and no button.

## Why
Conny 2026-11-23 after seeing 029 live: "Jag vill bara ha en discret pausknapp. Bara symbolen för paus resp play." Story 029 (#70) made a text button ("Pause film" / "Pausa filmen") with a 2 px border and a 72 % navy panel, which reads louder than the film it controls.

## Signal
- After merge, on the live site from a connection that reaches it (the Mac): on `/` and `/sv/` the button shows only the pause symbol; a click stops the film and shows the play symbol; the accessible name (`button.getAttribute('aria-label')`) follows ("Play film" / "Spela filmen").
- Conny says whether it is discreet enough. The Coordinator logs seen / not seen here.

## Acceptance criteria
- [ ] Both home pages: `button.motion` has no visible text; it holds two inline SVG icons (`svg.i-pause`, `svg.i-play`), each `aria-hidden="true"` and `focusable="false"`, drawn in `currentColor`, with no `style` attribute.
- [ ] The button's accessible name is `aria-label`: "Pause film" initially and "Play film" when paused (en), "Pausa filmen" / "Spela filmen" (sv). The script swaps `aria-label`, not text; CSS shows `.i-pause` while playing and `.i-play` under `.hero.paused`.
- [ ] Look: a 40×40 px circle, 1 px light border at half opacity, a navy backing at 50 %, a 14 px icon. It stays hidden until the script reveals it (`.motion[hidden]{display:none}`, since `display:grid` would otherwise override `hidden`). Focus ring as today.
- [ ] Unchanged from 029: no film request and no button under reduced motion or without JavaScript; a click pauses the film and `.flow`; a second click resumes.
- [ ] The icon meets WCAG 1.4.11 (3:1) against the button's backing over the poster and over the `.no-film` navy; the target is at least 24×24 px (WCAG 2.5.8).
- [ ] `bin/test-hero-motion.py` updated to the new facts and green; Test before commit green.
- [ ] Screenshots at 1440×900 and 390×844 of both pages' first screen, playing and paused, attached to the PR.
- [ ] Price block, booking CTA, Cal.com URL, contact address, founder claims, footer and all other copy unchanged.

## Out of scope
- How long the film plays (its length or loop) — waits on Conny's answer in the 029 thread; a later row if it changes.
- Moving the button, a tooltip, `aria-pressed`.

## Vad blir publikt?
The "Pause film" / "Pausa filmen" text button becomes a small round button with only a pause or play symbol, in the same corner. Nothing else changes.

## Log
- 2026-11-23 Coordinator's planner (thread "Gör pausknappen till bara en symbol"): written from Conny's message 2026-11-23 08:27Z, builder codex-cli.

— Coordinator (Claude) on behalf of Conny
