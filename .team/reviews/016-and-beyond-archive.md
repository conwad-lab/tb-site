---
id: 016
verdict: approve
---

# Review 016 — & Beyond archive on /beyond/ with RSS (round 3)

PR: #25 · 2026-11-17 · head `d50851c` (code), this review commit on top

Round 2's M1, S1 and N1 are fixed, Codex round 12's M1 is fixed, and Codex round 13 on `d50851c` found nothing. The archive, letter page and feed build cleanly on github-pages 232, and the importer now refuses what it cannot keep verbatim instead of parsing it. Approve.

## Must fix
- none

## Should fix
- none

## Nits
- N1 `bin/import-beyond.py:228-233` — image syntax in an *indented* (4-space) code block is still rewritten: fixture `    ![x](bilder/chart.png)` → exit 0, path changed to `/assets/beyond/2026-v45/chart.png`. Same class as round 2 M1 but a form a LinkedIn/Substack letter practically never uses, and it changes only a code example's path, never breaks the build. Not blocking; a follow-up story that automates the import can refuse any `![` that is not a plain image (Förslag).

## Evidence
| Acceptance criterion | Shown by (test, command + output, screenshot) | Result |
|---|---|---|
| `/beyond/` lists every letter newest first with week, title, lead and date; `lang="sv"` | github-pages 232 (Jekyll 3.10.0) build of a scratch copy of `d50851c` with a `publicerad` fixture imported: archive lists "2026 · vecka 45", title, lead, date; `<html lang="sv">`; empty build of the branch itself shows the empty state | pass |
| Letter page at `/beyond/<year>-v<week>/` with cover, diagrams (alt from `.alt.txt`), body, sources | `/beyond/2026-v45/` 200; `alt="Riktig bild"` / `alt="Diagrambeskrivning"` from `real.alt.txt` / `chart.alt.txt`; body text with `{{ site.title }} och {% if x %}ja{% endif %}` rendered verbatim; escaped-backtick paragraphs around a real image import (exit 0) | pass |
| `/beyond/feed.xml` Atom, linked with `rel="alternate"` | ElementTree root `{http://www.w3.org/2005/Atom}feed`, 1 entry with the fixture, 0 on the branch's own build | pass |
| Identity, 390 px without horizontal scroll, WCAG AA | Playwright 1440×900 and 390×844, scrolled: `scrollWidth/innerWidth` 1440/1440 and 390/390 on `/`, `/beyond/`, `/beyond/2026-v45/`. CSS tokens unchanged since round 1 (contrast ≥ 4.5 measured there) | pass |
| Import script refusals and verbatim wording | Fenced `![…]` → exit 1 "bildsyntax i kod stöds inte"; inline ``` ``![x](…)`` ``` → exit 1; plain letter → exit 0 "1 bilder" (file count, N1 of round 2); indented code → see N1 | pass, with N1 |
| Home page: exactly one new link, in the footer | `_site/index.html` byte-identical to `index.html` (`cmp`); footer diff unchanged since round 1 | pass |
| No third-party script/tracker/new font host; team files and `bin/` excluded | `_site` of the branch = `CNAME`, `index.html`, `sv/index.html`, `robots.txt`, `sitemap.xml`, `assets/beyond.css`, `assets/favicon.svg`, `beyond/index.html`, `beyond/feed.xml`; no `.team/`, `docs/`, `bin/`, `AGENTS.md`, `README.md`; `.pyc` gone, `.gitignore` covers `__pycache__/` | pass |
| Team settings tests | `python3 -m html.parser` on `index.html`, archive and letter page: exit 0. `pr-check` green on `d50851c`. Links: local pages and assets 200; external URLs **not checked** (session network), none changed in this PR | pass |

## Codex findings
- Rounds 1–10: valid — fixed (response file; spot-checked in round 2).
- Round 11 M1 (image syntax in code rewritten): valid — fixed in `2f28b8d` (refusal; shown above), residual indented form = N1.
- Round 12 M1 (escaped backticks refuse an ordinary letter): valid — fixed in `d50851c` (shown above).
- Round 13 on `d50851c`: "Didn't find any major issues" (issue comment 6941468675).
- Builder disputes: none.

## What I checked
- tests run: github-pages 232 build of the branch and of a scratch copy with an imported fixture (no warnings), Playwright at both widths, `html.parser`, Atom parse, importer fixtures with `python3 -I`.
- tried to break: fenced, inline, double-backtick and indented code images; escaped backticks; Liquid in the body; overflow at 390.
- scope vs story: matches. Hard rails: no price, Cal.com URL, contact address, `CNAME` or founder-claim change. `_config.yml` is a Human-merge path → merge on agreement (Judge approve, no Codex finding ruled not valid, Codex round 13 clean on the last code commit, `pr-check` green).

## Papercuts
- 2026-11-17 | reviewer | no Gemfile in the repo, so a fresh clone cannot `bundle exec jekyll build` | scratch Gemfile with `github-pages 232` and `BUNDLE_GEMFILE` | open
- 2026-11-15 | reviewer | `gh pr view` / `gh pr checkout` fail (GraphQL 403 in cloud sessions) | REST `gh api repos/…/pulls/25` and `git fetch` of the head ref | open
