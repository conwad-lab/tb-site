---
id: 016
verdict: request-changes
---

# Review 016 — & Beyond archive on /beyond/ with RSS

PR: #25 · 2026-11-15 · head `af1472b`

The build does what the story asks: archive, letter page, Atom feed, import script with its refusals, one footer link, nothing new published from team files. Two things stand before a merge: the branch does not contain master, and a letter with Liquid-looking text breaks the Pages build or silently changes Conny's wording.

## Must fix
- branch `feat/016-and-beyond-archive` — **M1** Sync gate (CLOUD.md § Judge 5 [J8]): master moved to `cb7db56` (#34, agent-team v0.8.3) after the branch was rebased on `14acd27`; `git merge-base --is-ancestor origin/master af1472b` fails. Fix: merge master into the branch (it merges cleanly: `git merge-tree --write-tree origin/master af1472b` has no conflicts), run Test before commit again on the new head, and request one Codex round on it.

## Should fix
- `bin/import-beyond.py:24` (FORBIDDEN) and `:191` (write) — **S1** The letter body goes into `_beyond/*.md`, which Jekyll renders as Liquid. A published letter that contains `{{` or `{%` (plausible in a letter about AI: prompt templates, code) either fails the whole Pages build or silently drops/changes text, which breaks the story's "wording is never changed" and the plan's risk note. Shown: fixture with `{{ site.title }} {% raw %}` in the body → script exit 0, then `jekyll build` (github-pages 232, Jekyll 3.10.0) → `Liquid syntax error (line 3): 'raw' tag was never closed`. Fix (pick one): wrap the written body in `{% raw %}…{% endraw %}` (Jekyll 3 has no `render_with_liquid: false`) and refuse a body that itself contains `{% endraw %}`; or refuse `{{` / `{%` with a clear message. Add a fixture for it.

## Nits
- N1 `.team/reviews/016-and-beyond-archive.response.md:4-7,12` — the shas `5673747` and `27c4bc5` are pre-rebase and not on the branch any more; name the rebased commit (`3266faa`) next to them so the trail resolves.
- N2 `beyond/feed.xml` — image and link paths inside `<content>` are root-relative (`/assets/beyond/…`); most readers resolve them against the feed URL, some do not. An `xml:base="{{ site.url }}/"` on `<feed>` would cover the rest. Not required.
- N3 `bin/import-beyond.py:29` — the `insikter/` needle also matches a published mention of the repo name `ai-insikter/…`; it refuses (safe direction), just a possible false alarm.

## Evidence
| Acceptance criterion | Shown by (test, command + output, screenshot) | Result |
|---|---|---|
| `/beyond/` lists every letter newest first with week, title, lead and date; `lang="sv"` | Scratch copy with a `publicerad` fixture imported → `_site/beyond/index.html`: entry "2026 · vecka 45 · 2 november 2026", title, lead; `<html lang="sv">`; empty build shows "Det första numret läggs upp här när det är publicerat." Screenshot archive-1440 (scratch) | pass |
| Letter page at `/beyond/<year>-v<week>/` with cover, diagrams (alt from `.alt.txt`), body, sources | Fixture `publiceras: 2026-11-02` → `/beyond/2026-v45/` 200; three images; `d1.png` alt = text of `d1.alt.txt` (brackets → parens); bare source URLs became links. Screenshot letter-390 (scratch) | pass |
| `/beyond/feed.xml` Atom, linked with `rel="alternate"` | ElementTree root `{http://www.w3.org/2005/Atom}feed`: 1 entry with fixture, 0 on the PR's own build; `<link rel="alternate" type="application/atom+xml">` in `beyond-base.html`, used by both pages | pass |
| Identity, 390 px without horizontal scroll, WCAG AA | Fonts from fonts.googleapis.com only (same URL as `index.html`); tokens copied from `index.html`. `scrollWidth/innerWidth` = 390/390 on home, archive, letter (long URL in the fixture). Contrast on `--paper` #F7F5F0: `--bronze` 5.98, `--muted` 5.98, `--body` 9.87, `--ink` 15.07, `--bronze-deep` 8.55 — all ≥ 4.5 | pass |
| Import script refuses non-`publicerad`, no title/sources, missing image, internal material | Fixtures: `status: utkast` → exit 1; `<!-- x -->` → exit 1; missing image → exit 1; titled image → exit 1; `publicerad` → exit 0, "3 bilder". Liquid in body → exit 0 but breaks the build (S1) | pass, with S1 |
| Home page: exactly one new link, in the footer | `git diff 14acd27 af1472b -- index.html`: one inserted `<span><a href="/beyond/">…</a></span>` in `.foot`, nothing else | pass |
| No third-party script/tracker/new font host; team files and `bin/` excluded | No `<script>` in the new files; `_site/` of the PR build = `CNAME`, `index.html`, `assets/beyond.css`, `assets/favicon.svg`, `beyond/index.html`, `beyond/feed.xml` (no `AGENTS.md`, `.team/`, `docs/`, `bin/`, `README.md`) | pass |
| Team settings tests on `_site/`, screenshots of home, archive, letter at both widths | `python3 -m html.parser` on `index.html`, `_site/beyond/index.html`, letter page: exit 0. `jekyll build` (github-pages 232): no warnings. `_site/index.html` byte-identical to `index.html` (`cmp`). Playwright 1440×900 + 390×844 full-page, scrolled: home, archive, letter. Home and empty archive screenshots in `docs/screenshots/016-and-beyond-archive/`; letter screenshots kept out of the public repo (unpublished letter) — acceptable, the letter page is shown from a fixture here | pass |
| Links | Local: `/`, `/beyond/`, `/beyond/2026-v45/`, `/beyond/feed.xml`, `/assets/beyond.css`, `/assets/favicon.svg`, image → 200. Google Fonts CSS → 200. **Not checked** (session network blocks them, none changed here): dignami.com, cal.com, mondmodel.com, r2.dev PDF and OG image, transformationbeyond.se | pass for what is reachable |

## Codex findings
- Round 1 M1 (front matter not parsed as YAML): valid — fixed (`yaml.safe_load`, `bin/import-beyond.py:37-50`).
- Round 1 M2 (titled / reference images not validated): valid — fixed (`:134`; my titled fixture → exit 1).
- Round 1 M3 (sidecar alt text not checked): valid — fixed (`:149`).
- Round 1 M4 (archive entry without date): valid — fixed (`beyond/index.html:23`).
- Round 2 on `27c4bc5`: no findings.
- Round 3 on `e581733`: failed twice (Codex usage limit, comments 6897170465 and 6897173722; the ready-review at 15:53 failed the same way). I checked the Builder's claim: `git diff 27c4bc5 af1472b` over `bin/ _layouts/ beyond/ assets/ _data/ _config.yml index.html README.md` is empty, so the code Codex last reviewed clean is the code on this head. It still means there is no finished Codex review on the last commit outside `.team/reviews/**` (CLOUD.md § Judge 5 (c), § Human approval): after M1/S1 this PR merges on agreement only if a Codex round on the new head finishes; otherwise it needs Conny's card (`_config.yml` is also a Human-merge path).
- Builder disputes: none.

## What I checked
- tests run: all of the above on a clean checkout of `af1472b` with github-pages 232 (Jekyll 3.10.0) under `bundle exec`, plus a scratch copy with fixtures for the script.
- tried to break: Liquid in the letter (S1, breaks); long URLs at 390 (holds); draft/comment/missing/titled images (refused); empty collection (feed valid, archive empty state); `_site` contents for leaked team files (none).
- scope vs story: matches; no letter is committed (V44 still `utkast`), which the story allows. Hard rails: no price, Cal.com URL, contact address or `CNAME` change; no founder credential claim (archive text names Conny as author only). `_config.yml` change is additive; existing excludes intact.

## Papercuts
- 2026-11-15 | reviewer | `gh pr view` / `gh pr checkout` fail (GraphQL 403 in cloud sessions) | REST `gh api repos/…/pulls/25` and `git fetch` of the head ref | open
