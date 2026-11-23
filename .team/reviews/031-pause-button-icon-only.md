---
id: 031
verdict: approve
---

# Review 031 — The film's pause button shows only a pause or play symbol

PR: #77 · 2026-11-23

## Must fix
- none

## Should fix
- none

## Nits
- N1 `assets/site.css:56` — worst case for the icon is 3.0:1 (off-white over the 50 % navy over a pure-white frame), right on the WCAG 1.4.11 line. The real frames under the button measured 11.1:1 (Builder) and the button sits over sky/the red ampersand in my screenshots, so it holds today; if the film is ever swapped for a brighter one, the backing's alpha is the knob.
- N2 `bin/test-hero-motion.py` — the Proof pins the CSS strings, not the cascade; that `.motion[hidden]` beats `display:grid` is shown only by Playwright (below). Fine for an S story; a later story could move the reduced-motion/no-JS display check into a Playwright test.

## Evidence
| Acceptance criterion | Shown by (test, command + output, screenshot) | Result |
|---|---|---|
| No visible text; two inline SVGs `svg.i-pause`/`svg.i-play`, `aria-hidden="true"`, `focusable="false"`, `currentColor`, no `style` | Diff read; `python3 bin/test-hero-motion.py` exit 0 (checks count, ancestor, attrs, no style); Playwright `button.textContent.trim() === ""` on `/` and `/sv/`; CSS `fill:currentColor` | pass |
| Accessible name = `aria-label`, swapped by script; CSS shows `.i-pause` playing, `.i-play` under `.hero.paused` | Playwright both pages, both widths: label "Pause film"→"Play film"→"Pause film", "Pausa filmen"→"Spela filmen"→"Pausa filmen"; `getByRole('button',{name})` matches after the click; computed display pause block/play none, then none/block | pass |
| 40×40 circle, 1 px border at half opacity, 50 % navy, 14 px icon; hidden until revealed; focus ring as today | Playwright computed: 40×40, `border-radius:50%`, border `rgba(248,246,241,.5) 1px`, bg `rgba(12,34,51,.5)`, svg 14px; `.motion:focus-visible` line unchanged in diff | pass |
| 029 unchanged: no film request and no button under reduced motion / no JS; click pauses film and `.flow`, second click resumes | Playwright `reducedMotion:'reduce'` and `javaScriptEnabled:false`, both pages: 0 `.mp4` requests, button `display:none`/not visible. Motion on: click → `.hero.paused`, `video.paused` true, `.flow svg` `animation-play-state: paused`; second click → not paused | pass |
| Icon ≥ 3:1 over poster and `.no-film`; target ≥ 24×24 | Builder's response file 11.1:1 / 15.0:1 / 3.0:1 worst case; my arithmetic for the white worst case agrees (≈3.0:1); box 40×40 | pass (N1) |
| `bin/test-hero-motion.py` updated and green; Test before commit green | Both run by me on a8a2df9: exit 0 / exit 0; `pr-check` success on the head | pass |
| Screenshots 1440×900 and 390×844, both pages, playing and paused, attached | `.team/screenshots/031-*` (6 files in the PR: en both widths playing+paused, sv both widths paused); my own screenshots of all four page×width paused states match | pass |
| Price, CTA, Cal.com URL, contact, founder claims, footer, other copy unchanged | `git diff` touches only the button line and one script line per page; `href` lists identical master vs head on both pages | pass |

## Codex findings
- Codex review on a8a2df9 (last commit, also the last code-touching head): "Didn't find any major issues." No findings, no disputes to rule on.

## What I checked
- tests run: `check_html.py` on every page (exit 0), `python3 bin/test-hero-motion.py` (exit 0), Playwright on a front-matter-stripped copy served locally at 1440×900 and 390×844, motion on / reduced motion / JavaScript off, both pages; `compatMode` CSS1Compat on both.
- tried to break: selector specificity (`.motion[hidden]` 0,2,0 over `.motion` 0,1,0; `.hero.paused .motion .i-play` 0,4,0 over `.motion .i-play` 0,2,0), the hidden/no-JS path, double toggle, accessible name after toggle, horizontal scroll at 390 (none). Read the whole diff: it is the work order verbatim.
- scope vs story: four files from the plan plus `.team/**`; no copy, link, price or footer change; no Human-merge path touched.
- not checked: external links and the live site (the cloud proxy answers 000 for transformationbeyond.se, dignami.com, mondmodel.com, r2.dev). The diff changes no `href`. Live check is the story's Signal (Operatör: Conny looks after deploy).

## Papercuts
2026-11-23 | reviewer | external link check from the cloud returns 000 for every site host | hrefs compared master vs head instead; live check left to the Signal | open

— Judge (Claude) on behalf of Conny
