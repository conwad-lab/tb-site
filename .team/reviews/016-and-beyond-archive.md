---
id: 016
verdict: request-changes
---

# Review 016 — & Beyond archive on /beyond/ with RSS (round 2)

PR: #25 · 2026-11-17 · head `30d3902` (last code commit `655c60b`)

Round 1's M1 (sync gate) and S1 (Liquid) are fixed and the sync gate holds: `git merge-base --is-ancestor origin/master 30d3902` passes (master `27805b1`). `pr-check` is green. Two things stand: Codex round 11's M1 is real and breaks the story's verbatim promise, and a compiled Python file was committed.

## Must fix
- `bin/import-beyond.py:267` — **M1** (Codex round 11 M1, upheld) Image syntax shown inside a fenced block or an inline code span is rewritten as a real image and its file copied. Shown: fixture with a real `![Riktig](bilder/real.png)` plus ```` ``` ![Exempel](bilder/chart.png) ``` ```` and `` `![x](bilder/chart.png)` `` → exit 0, both code examples published as `/assets/beyond/2026-v45/chart.png`, `chart.png` copied, and the script reports "3 bilder" for 2 files. The story's criterion is "body … as in the published text". Fix the Builder's option (b): refuse a letter that has `![` inside a fenced block or a code span, with a clear line ("bildsyntax i kod stöds inte"), and add the fixture. Do not parse further: rounds 5–11 show that each new parser branch finds a new edge case; refusing is the rule this script already follows for every other form it cannot keep verbatim.

## Should fix
- `bin/__pycache__/import-beyond.cpython-313.pyc` — **S1** A compiled bytecode file was committed in `65823c6`. It is not published (`bin` is excluded) but it is a stale binary in the repo that goes out of date with every edit. Remove it and add `__pycache__/` to a `.gitignore`.

## Nits
- N1 `bin/import-beyond.py` — the "skrev … och N bilder" count counts references, not files written; count the files.
- Round 1 N3 kept as is by the Builder: accepted.

## Evidence
| Acceptance criterion | Shown by (test, command + output, screenshot) | Result |
|---|---|---|
| Archive, letter page, Atom feed, identity at 390 px, AA contrast, footer link, exclusions | Round 1 evidence on `af1472b` (in git history of this file). Since then `index.html`, `_layouts/`, `beyond/`, `assets/beyond.css` and `_data/` are unchanged except `xml:base` on the feed (Judge round 1 N2); only `bin/import-beyond.py`, `_config.yml` (unchanged since round 1 apart from master's merge) and team files moved. `python3 -m html.parser index.html` → ok on `30d3902`. Jekyll build not re-run this round (no Gemfile in the repo; github-pages gem not in this session) — re-run on the fix head | pass (carried), build to re-run |
| Import script refuses non-`publicerad`, no title/sources, missing image, internal material, and keeps wording | Code-example fixture above → exit 0 with changed text (M1). Round 4–10 refusals per the response file, not re-run individually | **fail (M1)** |
| CI | `pr-check` on `30d3902`: success | pass |

## Codex findings
- Rounds 1–10: all ruled valid — fixed, as recorded in the response file; spot-checked against the code (`outside_fences`, `article`, `KEEP`, `SOURCES`, `ENDRAW` on sidecars).
- Round 11 M1 (image syntax in code rewritten): **valid — still open** (M1 above).
- Builder disputes: none.

## What I checked
- tests run: `html.parser` on `index.html`; the importer on a scratch fixture (`--out` scratch dir); `pr-check` status; sync gate.
- tried to break: image syntax in fenced and inline code (breaks, M1); file list of the diff (found the `.pyc`, S1).
- scope vs story: matches. `_config.yml` is a Human-merge path, so after the fixes this merges on agreement only with a finished Codex review on the new head without new M/S or P0/P1, else Conny's card.
- process: Codex has run eleven rounds; after this fix, one Codex round on the new head and then back to the Judge, whatever it finds.

## Papercuts
- 2026-11-17 | reviewer | no Gemfile in the repo, so `bundle exec jekyll build` cannot run from a fresh clone | carried round 1's build evidence; next round should run it with github-pages 232 as the Builder does | open
- 2026-11-15 | reviewer | `gh pr view` / `gh pr checkout` fail (GraphQL 403 in cloud sessions) | REST `gh api repos/…/pulls/25` and `git fetch` of the head ref | open
