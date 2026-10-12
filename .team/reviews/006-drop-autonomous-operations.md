---
id: 006
verdict: approve
---

# Review 006 — C6 — drop "autonomous operations" from the Mondmodel row

PR: #6 · 2026-10-12

## Must fix
- none

## Should fix
- none

## Nits
- N1: PR body — the two screenshot links point at the `feat/006-…` branch blob, which disappears when the branch is deleted on squash-merge. The PNGs are committed, so they survive on `master`; only the links in the PR text go stale. Nit: link `docs/screenshots/006-…/desktop.png` by commit SHA next time. No action on this PR.

## What I checked
- tests run: `python3 -m html.parser index.html` clean; `git diff master...HEAD --check` clean; `git diff master...HEAD --name-only` is `index.html` (1 line, −`autonomous operations · ` only) plus `docs/screenshots/006-drop-autonomous-operations/{desktop,mobile}.png` (1440×6676, 390×8077). `grep -c "autonomous operations" index.html` → 0; the source-link grep and `9 destinations · 4 languages · <a` grep → 1 each; no `· ·` left behind. Playwright 1.58.2 Chromium, my own script, `networkidle` + 1 s, scrolled to bottom in 400 px steps: 1440×900 → height **6676**, 0 hidden `.r-fade`, 7 `.revealed`, no horizontal overflow, metric on 1 line; 390×844 → height **8077**, 0 hidden, 7 `.revealed`, no overflow, metric on 2 lines. Baseline on `master` with the same script: 6694 / 8077, metric text still contains the phrase, so the 18 px desktop delta is exactly the metric dropping from two lines to one, as the plan predicted. Page text (`innerText`) contains no "autonomous operations" at either width. Link check with curl: every `http(s)` `href`, both band `<img src>`, `og:image`, the sample PDF and the Cal.com URL return 200; the two `rel=preconnect` bare hosts 404 as in every earlier review (excluded); five `#id` anchors resolve; `assets/favicon.svg` exists. `gh pr checks 6`: no checks configured. PR is `MERGEABLE / CLEAN` against `master`.
- Review checks (factual claims): the two figures that remain are sourced. I fetched https://mondmodel.com/sitemap.xml today (327 KB, 200): nine top-level destination sections with `/guide`, `/hotels` or `/pillar` children (barcelona, basque-country, copenhagen, costa-brava, costa-del-sol, costa-dorada, ibiza, mallorca, menorca), and `hreflang` de / en / es / sv = four languages. Matches plan 002 and plan 006. No Dignami wording changes, so nothing to compare against dignami.com/en/proof or /en/about. No colour changes, so no contrast to measure. Screenshots at both widths committed and linked from the PR; I viewed the Mondmodel row in both and it reads "9 destinations · 4 languages · source: mondmodel.com ↗" with the link styled as before.
- PR description: every claim checked against the diff and my own runs — old → new string, unchanged `href`/`target`/`rel`, baseline heights 6694/8077, post-edit 6676/8077, 7 revealed, 0 hidden, no overflow, grep counts 0/1/1, `diff --check`, link results, preconnect 404s, both screenshot URLs (200). All hold. "Story 009 owns the Mondmodel status wording": `.team/backlog/_009-handoff-and-evidence-language.md` exists.
- rulebook: no change to `AGENTS.md`, `.team/team.md`, `REVIEW.md` or `.team/roles/`. Price block, booking CTA, footer, `CNAME`, `_config.yml`, hosts: untouched.
- tried to break: searched for the phrase in `innerText`, the raw HTML and the OG/meta tags — gone everywhere; checked the separator around the deleted phrase (no stray `·`); confirmed line 346 ("AI-driven editorial platform in daily operation") and the "In production" label are byte-identical to master, as the story's out-of-scope list requires.
- scope vs story: all four acceptance criteria met; the diff is exactly the plan's one line plus the two PNGs. No scope creep.
- Second reviewer: not run — Team settings list no Second-reviewer paths.

## For PO
- Merge deploys to production (Operatör trigger): Conny should open https://transformationbeyond.se/ once and confirm the Mondmodel row now reads "9 destinations · 4 languages · source: mondmodel.com ↗".
- The Architect's note stands: "In production" and "in daily operation" on the same row are no more verifiable on mondmodel.com than the phrase just removed. Story 009 is the place to decide.

Verdict: approve. Merging per `merge: auto` in `.team/team.md`.

— Reviewer (Fable 5.1) on behalf of Conny Wadbro
