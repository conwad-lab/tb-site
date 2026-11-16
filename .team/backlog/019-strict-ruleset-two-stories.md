---
id: 019
title: "Two stories in flight on the strict ruleset"
---

Rulebook story.

## Outcome
tb-site's Team settings allow two stories in flight, name `pr-check` as the CI check, and list the files that define that check as Human-merge paths.

## Why
The strict ruleset (SETUP.md step 9) is in place on `master`: `main: PR only` requires `pr-check` and "up to date before merge" (Conny, 2026-11-16; check job merged in #39). That is the condition CLOUD.md § Flow 3 sets for **Stories in flight: 2**. `AGENTS.md` still says 1, still says **CI-only checks:** none, and does not list `pr-check.yml` or its script as Human-merge paths, so a `merge: auto` PR could change the check the ruleset relies on (Judge note on #39).

## Signal
`gh api repos/conwad-lab/tb-site/rules/branches/master` shows `strict_required_status_checks_policy: true` with `pr-check` (read today), and `AGENTS.md` § Team settings on master reads **Stories in flight:** 2. After the next two stories run side by side, `bin/watch` shows no merge refused by the ruleset that stayed unanswered.

## Acceptance criteria
- [ ] `AGENTS.md` § Team settings: **Stories in flight:** 2.
- [ ] **CI-only checks:** names `pr-check` (`.github/workflows/pr-check.yml`: every `*.html` outside `.claude/` passes `.github/scripts/check_html.py`), it is the ruleset's required check.
- [ ] **Human-merge paths:** also `.github/workflows/pr-check.yml` and `.github/scripts/check_html.py`.
- [ ] `git diff master --stat` lists only `AGENTS.md` and `.team/**`; `index.html` is unchanged and `python3 -m html.parser index.html` exits 0.
- [ ] The ruleset is read again on the PR head's day and still shows strict plus `pr-check` (no agent changes it).

## Out of scope
- The ruleset itself (Conny's, done), the workflow and script (merged in #39), `.team/team.md`.
- Any site change, `merge:`, `builder:`.

## Log
- 2026-11-16 PO: created from Conny's "klart" on the ruleset steps and the Coordinator's row. Rulebook story, so the PR is a human-merge path (card, or the Judge's merge when Codex and the Judge agree and Conny's standing rule applies).
