---
id: 035
verdict: approve
---

# Review 035 — A lower first screen on the home pages

PR: #90 · 2026-11-26 · code head 8b085eb; main merged in (it had moved by 8 commits), the review file is the only other change

Story `.team/backlog/035-first-screen-lower-hero.md`, plan `.team/plans/035-first-screen-lower-hero.md`. Merge route: `merge: auto`, no Human-merge path touched (`assets/site.css` and a new `bin/` test only). The Judge merges on its word once a Codex review has finished on the head (CLOUD.md § Judge 5 and § Human approval H1).

## Must fix
- none

## Should fix
- none

## Nits
- N1 The PR body leaves "Booking band visibility" unchecked and the Builder never posted screenshots; the Judge took them (committed under `.team/reviews/035-screenshots/`, see Evidence).
- N2 **Interplay with #98 (order 961).** #98 puts the mobile header in the normal flow (125 px tall at 390 px) and so pushes the hero down. On a build with #90 and #98 together the band's top is at 851 px at 390×844 (the viewport ends at 844), which breaks this story's criterion. I asked #98 to fix that (its review file); nothing to change here.

## Evidence
| Acceptance criterion | Shown by | Result |
|---|---|---|
| `.hero` has `min-height:86svh` instead of `100svh`, nothing else in that rule changes | Diff: one line in `assets/site.css`, only `100svh` → `86svh` | pass |
| `bin/test-hero-first-screen.py` pins 86svh and the diagram `aria-label` order on both pages | Read the script (parses the SVG, compares `aria-label` order with the visible axis texts, strips CSS comments, rejects any `.hero…` rule still on `100svh`); run on the merged head → `ok`, exit 0 | pass |
| Band visible on first screen at 1440×900 and 390×844, both pages; 125 % zoom on the English page; before/after screenshots | Screenshots, before (master) and after (this head), in `.team/reviews/035-screenshots/`: `en-1440x900`, `en-390x844`, `en-zoom125`, `sv-1440x900`, `sv-390x844`, each `-before.jpg` and `-after.jpg` (I looked at the 390 px English and the 1440 px Swedish "after" shots: the red band is on the first screen). Measured with Jekyll build + Playwright, viewport heights 900, 844, 720 (1152×720 = 125 % zoom): English band top at 774 / 726 / 619 px, Swedish 774 / 726 / 637 px, each inside the viewport (the Swedish zoom shot shows the band partly, top edge at 637 of 720). On master the band top is at 900 and 844, i.e. just below the fold. No horizontal scroll. | pass |
| Diagram `aria-label` follows the axes, left alone | The new test passes; `index.html` and `sv/index.html` not in the diff | pass |
| Test before commit green, `test-hero-motion.py` green | `check_html.py` over all HTML ok; `test-hero-motion.py`, `test-beyond-palette.py`, `test-check-html.py` exit 0; `pr-check` success | pass |
| Price, CTA, Cal.com URL, contact address, founder claims, footer, copy unchanged, no extra section | Diff stat: `site.css` 1 line, new test file; no HTML touched | pass |

## Codex findings
- No Codex review existed on the draft; I posted `@codex review` and marked the PR ready. Codex on 0828f6f (2026-11-26T07:44Z) found **P1 "M1 Attach the required before-and-after screenshots"** (against N1 of the first version of this file): valid — fixed. The screenshots are now committed in `.team/reviews/035-screenshots/` and the Evidence row says what they show. The second Codex round on 9d57e83 (2026-11-26) finished with no findings (receipt "Didn't find any major issues", `has_unresolved_findings: false`). Main was merged into the branch once more afterwards (the diff against main is unchanged: `assets/site.css` and `bin/test-hero-first-screen.py`).

## What I checked
- tests run: the four bin tests, check_html.py, Playwright at three viewports on both pages.
- tried to break: the longer English h1 at 125 % zoom (still inside the hero), the Swedish page at zoom (band top visible), horizontal scroll at 390 px.
- scope vs story: one CSS line and one test; no out-of-scope change.
- sync gate: main merged into the branch; checked again right before posting.

## Papercuts
2026-11-26 | reviewer | the Builder never posted `@codex review` or the screenshots on #90 | posted the request and took the screenshots myself | open
