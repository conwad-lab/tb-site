---
id: 026
verdict: approve
---

# Review 026 — The English home page in the poster design

PR: #62 · 2026-11-20 · reviewed head `9b2eb61`

## Must fix
- none

## Should fix
- none

## Nits
- N1 `index.html` (master line 231): the old strata SVG's `<title>Transformation &amp; Beyond — the gap</title>` goes with the SVG. The plan covers replacing the strata SVG, so this is in scope, but the Builder's visible-text diff in the response file does not show the line (its extractor skipped SVG `<title>`). No change needed.
- N2 `_includes/latest-letter-cover.html:10`: the "Week NN · date" line now renders on `/` only, so the English cover has one line the Swedish cover lacks. Matches the plan (Codex M1 kept English text unchanged; `/sv/` must stay as 025). If the two covers should match, that is a later copy decision for Conny, not this story.

## Evidence
| Acceptance criterion | Shown by (test, command + output, screenshot) | Result |
|---|---|---|
| Same structure as `/sv/`, no Skåne section | Jekyll 4.4.1 build + Playwright 1440×900 and 390×844 (my own shots): hero with film and `&`, gap figure, offer fact sheet, six questions + Optional + roles, `#efter`, proof rows, cover, contact bands, footer; no Skåne section; `/assets/site.css` linked | pass |
| Visible text only as the Copy strings | My own visible-text diff (HTML parser over master vs branch `_site/index.html`, with a scratch letter): every removed/added string maps to a Copy-strings line (nav button, eyebrow, h1 reflow, mat-band alts, strata SVG, "Why we exist", 01/02/03 keys, dashes in proof rows, founder row split, new figure, Optional row, roles block, `#efter`, cover labels). Only extra: N1 | pass |
| Hard rails unchanged | `grep -c` master/branch: "75 000 SEK" 3/3, "ex VAT · fixed scope · two weeks" 2/2, cal.com URL 1/1, `mailto:` 2/2, "your counsel gives legal advice" 1/1, founder sentence 1/1, "One borderland, one advisor." 1/1; "Your lawyer gives the legal advice" 0→1 is the approved Optional row; `grep -n SEK`: meta, price, contact line, JSON-LD only, none in `#efter` | pass |
| `<head>` | `diff` of lines 1–19 and the last 23 lines (Cal.com script, JSON-LD) against master: empty; lines 20 and 22 are the Fonts URL (same as `sv/index.html`) and the stylesheet link | pass |
| Cover include takes `lang`, old include deleted, nothing without letters | Build without letters: 0 `id="beyond"`; with a scratch letter: English tag, "Week 47 · 16 November 2026", "Read the letter →", "All letters", `aria-label="Latest letter: …"`, title and lead `lang="sv"`; `_includes/latest-letter.html` removed, no reference left | pass |
| No h-scroll, h1 clear of `&`, AA | `scrollWidth` 1440/1440 and 390/390; at 1440×900 h1 box ends x=835, `&` box starts x=880 (computed font-size 77.76px from the `:lang(en)` rule); screenshot at 390 shows h1 glyphs below the `&` ink; colours unchanged from 025; Builder's film contrast 3.27 (large text) / 4.05 not re-measured | pass |
| Test before commit, screenshots, link check | `check_html.py` exit 0; `pr-check` success on `9b2eb61`; screenshots in `.team/screenshots/026/` plus my own; local `href`/`src` 200 (`/`, `/sv/`, `/beyond/`, the letter, CSS, favicon, film); all `#` anchors exist. **Not checked** (session proxy): transformationbeyond.se, dignami.com ×3, mondmodel.com, cal.com, the R2 PDF, Google Fonts; all unchanged from master | pass (externals not checked) |
| `sv/index.html` unchanged; `site.css` one named rule | `sv/index.html` not in the diff; `cmp` of `_site/sv/index.html` master vs branch: identical without and with a letter; `site.css` +1 line `.hero h1:lang(en){…}`, named in the response file | pass |

## Codex findings
- Round 1 M1 (P1) `index.html:141` week/date line removed without an approved copy change — **valid — fixed** in `9b2eb61` (confirmed in my build).
- Round 2 on `9b2eb61`: completed, no findings.

## What I checked
- tests run: `check_html.py` over every `*.html`; Jekyll 4.4.1 builds of master and branch with and without a scratch letter; Playwright at 1440×900 and 390×844 on `/` and `/sv/`; local link check.
- tried to break: text dropped outside the Copy strings (own extractor, alt/aria included); hard-rail strings; the Swedish build through the shared include; the longer English h1 at both widths; empty collection.
- scope vs story: three site files plus `.team/**`; no `_config.yml`, `404.html`, `beyond.css`, JSON-LD or Human-merge path touched. Route: `merge: auto`, not a rulebook story, no Human-merge path → merge on the Judge's word.

## Papercuts
2026-11-20 | reviewer | repo has no Gemfile, `bundle exec jekyll` fails in the cloud clone | `gem install jekyll` (4.4.1) and plain `jekyll build` | open

— Judge (Claude) on behalf of Conny
