---
id: 025
verdict: approve
---

# Review 025 — The Swedish home page in the poster design

PR: #60 · 2026-11-20 · reviewed head `954b451`

## Must fix
- none

## Should fix
- none

## Nits
- N1 `sv/index.html` figure: the dots and labels fade in on a scroll-driven timeline, so any full-page screenshot taken at scroll 0 (also the routine's Signal shots) shows empty axes. Not a defect on a real visit; the Builder logged it as a papercut.
- N2 at 390 px the red `&` sits behind the wordmark and the kept nav links ("Genomlysningen", "Vem du får", "& Beyond"); paper on red is 4.98:1, so AA holds, but it is the tightest pair on the page.

## Evidence
| Acceptance criterion | Shown by (test, command + output, screenshot) | Result |
|---|---|---|
| Sketch structure, chosen variants only | Jekyll 4.4.1 build + Playwright 1440/390: `.roles`, `.q7`, Tillval row, `#efter`, `#beyond` (sample letter) all displayed; no panel, no "Förslag", no portrait in the screenshots | pass |
| Copy only as listed | Builder's visible-text diff (response file) read line by line against the plan's Copy strings; every change maps to a listed string or the two noted layout splits | pass |
| Price, booking, contact, founder, legal unchanged | `grep -c` master vs branch: "75 000 kr" 3/3, "exkl. moms · fast omfattning · två veckor" 2/2, "er jurist ger juridisk rådgivning" 1/1, mailto 2/2 (same hrefs), cal.com 1/1, founder sentence 1/1; last 24 lines (Cal.com script + JSON-LD) `diff` empty; no price in `#efter` (new "Er jurist ger den juridiska rådgivningen" is the approved Tillval row) | pass |
| `<head>` | `diff` lines 1–21 empty; only the Fonts URL changes (Familjen Grotesk + Newsreader) and the stylesheet link is added; loaded font families in Chromium: Familjen Grotesk, Newsreader | pass |
| Film | `assets/film/sluseholmen-720.mp4` 2 298 159 B ISO MP4, poster JPEG 1280×720; attributes `autoplay muted loop playsinline preload="metadata" aria-hidden="true"` + poster; reduced motion → film `display:none`, `.flow` block; `*.mp4` aborted → `video.error.code` 4, `.hero.no-film`, `.flow` block; all hosts same-origin | pass |
| Cover from `beyond` collection | build as committed: 0 `id="beyond"`; scratch copy with one letter: 1, cover rendered (screenshot) | pass |
| No h-scroll, `&` clear of h1, AA | `scrollWidth` 1440/1440 and 390/390 (also reduced motion); 1440×900 screenshot shows h1 glyphs clear of the `&`; Builder's contrast table checked against `site.css` values, red on navy only on the decorative `&` | pass |
| Test before commit, screenshots, link check | `check_html.py` exit 0; `pr-check` success on `954b451`; screenshots in `.team/screenshots/025/` and my own at both widths; local hrefs 200. **Not checked** (session proxy blocks the hosts): dignami.com ×3, mondmodel.com, cal.com, the R2 PDF, transformationbeyond.se; all unchanged from master | pass (externals not checked) |
| Untouched files | `git diff 220d996 --stat -- index.html beyond _layouts assets/beyond.css _config.yml CNAME 404.html _includes/latest-letter.html .github .claude` empty | pass |

## Codex findings
- Round 1 (`027384a`, and the summary on `954b451`): no findings. Nothing to rule.

## What I checked
- tests run: Test before commit; Jekyll build with and without a sample letter; Playwright 1440×900, 390×844, 1440 reduced motion, 1440 with the film blocked; head/tail byte diffs; hard-rail greps; href set master vs branch (only the Fonts URL and the stylesheet link differ).
- tried to break: a body-class rule left over hiding a block (none: every switched block visible); film failing (fallback works); reduced motion (film hidden, lines still); empty collection (nothing rendered); a new external host (none; `site.css` has no URL).
- scope vs story: matches; no Human-merge path touched (price, Cal.com URL, contact address and founder claim unchanged in text), so `merge: auto` applies.

## Papercuts
2026-11-20 | reviewer | external link check impossible from the cloud session (proxy blocks dignami.com, cal.com, mondmodel.com, r2.dev, transformationbeyond.se) | listed as not checked; the Signal read after merge covers the live page | open
