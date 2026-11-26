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
- N1 The PR body leaves "Booking band visibility" unchecked and attaches no screenshots; the Judge's measurements below replace them (Test before commit lets Builder and Judge run the screenshot check). The Builder thread's before/after screenshots were never posted.
- N2 **Interplay with #98 (order 961).** #98 puts the mobile header in the normal flow (125 px tall at 390 px) and so pushes the hero down. On a build with #90 and #98 together the band's top is at 851 px at 390×844 (the viewport ends at 844), which breaks this story's criterion. I asked #98 to fix that (its review file); nothing to change here.

## Evidence
| Acceptance criterion | Shown by | Result |
|---|---|---|
| `.hero` has `min-height:86svh` instead of `100svh`, nothing else in that rule changes | Diff: one line in `assets/site.css`, only `100svh` → `86svh` | pass |
| `bin/test-hero-first-screen.py` pins 86svh and the diagram `aria-label` order on both pages | Read the script (parses the SVG, compares `aria-label` order with the visible axis texts, strips CSS comments, rejects any `.hero…` rule still on `100svh`); run on the merged head → `ok`, exit 0 | pass |
| Band visible on first screen at 1440×900 and 390×844, both pages; 125 % zoom on the English page | My Jekyll build + Playwright, viewport heights 900, 844, 720 (1152×720 = 125 % zoom): English band top at 774 / 726 / 619 px, Swedish 774 / 726 / 637 px, each inside the viewport (the Swedish zoom shot shows the band partly, top edge at 637 of 720). On master the band top is at 900 and 844, i.e. just below the fold. No horizontal scroll. | pass |
| Diagram `aria-label` follows the axes, left alone | The new test passes; `index.html` and `sv/index.html` not in the diff | pass |
| Test before commit green, `test-hero-motion.py` green | `check_html.py` over all HTML ok; `test-hero-motion.py`, `test-beyond-palette.py`, `test-check-html.py` exit 0; `pr-check` success | pass |
| Price, CTA, Cal.com URL, contact address, founder claims, footer, copy unchanged, no extra section | Diff stat: `site.css` 1 line, new test file; no HTML touched | pass |

## Codex findings
- A Codex review was missing (the PR was a draft and no `@codex review` was posted); I posted one and marked it ready. The result is added under this heading before merge.

## What I checked
- tests run: the four bin tests, check_html.py, Playwright at three viewports on both pages.
- tried to break: the longer English h1 at 125 % zoom (still inside the hero), the Swedish page at zoom (band top visible), horizontal scroll at 390 px.
- scope vs story: one CSS line and one test; no out-of-scope change.
- sync gate: main merged into the branch; checked again right before posting.

## Papercuts
2026-11-26 | reviewer | the Builder never posted `@codex review` or the screenshots on #90 | posted the request and took the screenshots myself | open
