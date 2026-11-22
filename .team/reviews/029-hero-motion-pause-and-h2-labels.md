---
id: 029
verdict: approve
---

# Review 029 — A pause button for the moving hero, and two section labels as headings

PR: #70 · 2026-11-22 · reviewed head `d2ccce6c3d26f7a453ebb8905a8c51710582be0c` (last commit outside `.team/reviews/**`, Codex-reviewed)

Judged against story `.team/backlog/029-hero-motion-pause-and-h2-labels.md`, plan `.team/plans/029-hero-motion-pause-and-h2-labels.md`, `AGENTS.md` § Team settings and `.claude/skills/agent-team/team/CLOUD.md` § Judge. Codex-built (codex-cli, Astra): whole diff read.

## Must fix
- none

## Should fix
- none

## Nits
- N1 `index.html`/`sv/index.html` script — when the film fails to load (`.hero.no-film`), the button still reads "Pause film" / "Pausa filmen" although it now pauses the line animation. It works (WCAG 2.2.2 is met); a neutral label ("Pause motion" / "Pausa rörelsen") would be more exact. Förslag, not this PR: the copy is the order's settled choice.
- N2 `.team/screenshots/029-*` — only first-screen and paused shots are committed; the full-page before/after comparison is described, not attached. My own full-page comparison below closes the evidence gap.

## Evidence
| Acceptance criterion | Shown by | Result |
|---|---|---|
| `video.film` has `data-src`, no `src`; script sets `src` only without reduced motion; poster/muted/loop/playsinline/autoplay/onerror kept | diff: one attribute renamed on that element; Playwright on a Jekyll build of the head, both pages: reduced motion → `src` null, no request for `sluseholmen-720.mp4`; motion on → `src` set, film requested | pass |
| `button.motion` hidden inside `.hero`, revealed by script; click → `.hero.paused`, film paused, `.flow` paused, label swaps; second click resumes; en/sv copy | Playwright, both pages at 1440×900: button visible, click → `paused` class, `video.paused` true, `.flow .f1` and `.f2` (the animated `svg`s) `animationPlayState: paused`, label "Play film" / "Spela filmen"; second click → playing, `running`, label back; Enter key on the focused button also toggles | pass |
| No JS: no film request, no button; reduced motion: no film request, no button, `.flow` static | Playwright with `javaScriptEnabled: false` and with `reducedMotion: 'reduce'`, both pages: no film request, button `display: none` | pass |
| Four labels are `h2.tag`, no visible change | Playwright full page, reduced motion, master 73cfb96 vs head, both pages at 1440×900 and 390×844: page heights identical (en 9718/10329, sv 10580/11007); each label's top, height, width, font size, family, weight, line height, letter spacing and margins identical, only the tag name differs | pass |
| `bin/test-hero-motion.py` green; Test before commit green | `python3 bin/test-hero-motion.py` exit 0; `check_html.py` over every page exit 0; `pr-check` on d2ccce6 success | pass |
| Price, booking CTA, Cal.com URL, contact, founder claims, other copy unchanged | `git diff 73cfb96 d2ccce6 -- index.html sv/index.html assets/site.css`: 42+/6−, only the video attribute, the button, the four labels, the new script and four CSS lines; CALCOM_URL script and JSON-LD untouched | pass |
| Screenshots at both widths; button text AA | `.team/screenshots/029-*` (1440 and 390 first screen, paused); my 390×844 shot: button under the nav, clear of the h1, no horizontal scroll (scrollWidth 390). Contrast: #F8F6F1-ish on navy 72 % over white ≈ 6.0:1 (recomputed), AA | pass |
| Sync gate | master = 73cfb96, ancestor of the head | pass |
| Signal (live button, no film request under reduced motion) | after merge, from the Mac | not yet |

## Codex findings
- Code review on d2ccce6 (22:33Z): "Didn't find any major issues." No findings to rule on; no Builder disputes.

## What I checked
- tests run: `check_html.py`, `bin/test-hero-motion.py`, Jekyll build of master and head, Playwright (reduced motion, no JS, motion on, keyboard, 390 layout, full-page geometry of the labels).
- tried to break: whether `animation-play-state` on `.flow svg` reaches the animation (it does: `.f1`/`.f2` are the `svg` elements themselves); whether `onerror` still fires once `src` is set by script (the media error fires on the element, so `no-film` still works); whether the button overlaps the nav or h1 at 390 (no, y 96–132, nav ends at 86); page errors (none).
- scope vs story: the four files the plan names plus the Builder's response file and screenshots. Not checked: external links and the live site (cloud network); no link changed in this diff.

## Route
`merge: auto`, no Human-merge path touched (no price, Cal.com URL, contact or founder change), not a rulebook story: merge on the Judge's word [J9].

## Papercuts
- 2026-11-22 | reviewer | `gh pr checkout`/`gh pr review` use GraphQL, refused in the session | fetched the branch by name, posted the review via REST | open

— Judge (Claude) on behalf of Conny
