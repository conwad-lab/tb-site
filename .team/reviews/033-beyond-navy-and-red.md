---
id: 033
verdict: approve
---

# Review 033 — The & Beyond archive in navy and red

PR: #85 · 2026-11-23

## Must fix
- none

## Should fix
- none

## Nits
- N1 `assets/beyond.css:4` — `--hair` is now fog #F6E6DA (the plan's token), so the eyebrow rule, the `.issues li` dividers and the `.follow a` underline are close to invisible on paper (≈1.05:1; before #E3DFD5 ≈1.2:1). Decorative only, the work order fixed the value; a later story could pick a visible hairline if Conny misses it.
- N2 `assets/beyond.css` — `.foot .mono` keeps its class name though it is no longer monospace (the plan's own Risks note).

## Evidence
| Acceptance criterion | Shown by (test, command + output, screenshot) | Result |
|---|---|---|
| beyond.css only site.css `:root` colours + #FFFFFF; no bronze, no `--mono` | `python3 bin/test-beyond-palette.py` → ok (checks a, b); diff read | pass |
| Navy header/footer with paper text; `&`, eyebrow, week labels, links, blockquote red; headings navy | My Playwright on a Jekyll build with an uncommitted fixture letter, `/beyond/`, letter, `/404.html` at 1440 and 390: header/footer bg rgb(12,34,51), eyebrow rgb(207,35,24), h1 rgb(12,34,51) weight 500; Builder screenshots `.team/screenshots/033-beyond-after-*` | pass |
| beyond-base and 404 load exactly index.html's font URL, nothing else from a font host | Test check c ok; Playwright: font requests only css2 (Familjen Grotesk + Newsreader) and their gstatic woff2; body font-family starts "Familjen Grotesk" on all three pages | pass |
| Footer mark and favicon in paper/navy/red only | Test check d ok; diff read | pass |
| WCAG AA for every changed pair; focus rings visible | My arithmetic: navy/paper 15.05, black/paper 16.53, red/paper 4.98, deep red/paper 6.44, grey/paper 5.94, red/navy 3.02 (wordmark/border, non-text), white on red selection 5.38; focus ring paper on navy via `outline-color`, red on paper; Builder's focus screenshot | pass |
| Proof green; Test before commit green | Both run by me on the head: `ok` / exit 0; `pr-check` success on ec8a330 | pass |
| Screenshots 1440×900 and 390×844, before/after, three pages | 12 PNGs + focus shot in `.team/screenshots/033-beyond-*` on the branch; checked archive 1440 and letter 390 | pass |
| No text, link, price, Cal.com, contact, founder, RSS, `_config.yml` or home markup change; home pages only by favicon | Diff touches only the font `<link>` and two `fill` values per HTML file; `index.html`, `sv/index.html`, `_config.yml` untouched; href lists on the three pages are the same set as before | pass |

## Codex findings
- M1 (P1, on 799800d) screenshots not attached — valid — fixed: committed under `.team/screenshots/` in ec8a330 (repo convention, as 031).
- Codex review on ec8a330 (last code head): "Didn't find any major issues."

## What I checked
- tests run: `bin/test-beyond-palette.py`, `check_html.py` on every page, Jekyll 4 build + Playwright (computed styles, font requests, compatMode CSS1Compat, no horizontal scroll at 390).
- tried to break: selector specificity of the focus override (0,1,2/0,1,1 over `a:focus-visible` 0,1,1, later in the file), `.mark` inheriting paper on navy, inline colours in `beyond-letter.html`/`beyond/index.html` (none). Read the whole Codex-built diff: it is the work order verbatim.
- Sync gate: branch was cut before #82/#79 (board-only, `.team/ORDER.md`); I merged master into the branch with the review commit, no conflict.
- not checked: the live site and external links (cloud proxy). Signal is Conny's look after deploy.

— Judge (Claude) on behalf of Conny
