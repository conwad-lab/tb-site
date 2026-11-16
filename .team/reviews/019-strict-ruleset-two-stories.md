---
id: 019
verdict: approve
---

# Review 019 — Two stories in flight on the strict ruleset

PR: #41 · 2026-11-16 · reviewed head `fa81ce51c5560482543b42e192e36b6dd5e52d8e`

`Rulebook story.` (first line of story and PR body). Route: on agreement (CLOUD.md § Judge 5 [J10]); Conny's standing rule of 2026-11-07 covers a merge when the Judge and Codex agree.

## Must fix
- none

## Should fix
- none

## Nits
- Nit: #25 (story 016) is still open while 019 ran, so two stories were in flight while the setting said 1, and CLOUD.md [F4](b) forbids a `Rulebook story.` beside another story in a product repo. No harm here: #25 touches no `AGENTS.md` and 019 touches nothing of #25's. Flagged to the Coordinator, not a fix for this PR.
- Nit: after merge, #25 must merge master in before its own merge (strict ruleset, sync gate).

## Evidence
| Acceptance criterion | Shown by | Result |
|---|---|---|
| **Stories in flight:** 2 | `AGENTS.md:41` on the head reads `- **Stories in flight:** 2` | pass |
| **CI-only checks:** names `pr-check`, the workflow, the script, and that it is the ruleset's required check | `AGENTS.md:33`; matches `.github/workflows/pr-check.yml` (job `pr-check`, `find . -name '*.html' -not -path './.claude/*' -not -path './.git/*'` → `check_html.py`) | pass |
| **Human-merge paths:** adds `pr-check.yml` and `check_html.py` | `AGENTS.md:42` names both, existing paths kept | pass |
| Diff only `AGENTS.md` and `.team/**`; `index.html` unchanged; html.parser exits 0 | `git diff --no-renames --name-only origin/master...fa81ce5` → `AGENTS.md`; `python3 -m html.parser index.html` exit 0; `check_html.py` on all pages exit 0 | pass |
| Ruleset read on the head's day, strict + `pr-check` | `gh api repos/conwad-lab/tb-site/rules/branches/master` 2026-11-16: `required_status_checks` with `strict_required_status_checks_policy: true`, context `pr-check`; also PR-only, squash only, no deletion, no force-push (SETUP.md step 9) | pass |
| Required checks on head | check run `pr-check` completed, success, on fa81ce5 | pass |
| Sync gate | `git merge-base --is-ancestor origin/master fa81ce5` (master 5b59441) → true | pass |
| § Rulebook changes [C1] | submodule pin unchanged (b25d713), so `CLOUD.md` word count is unchanged | pass |

Remove: nothing, because the change only fills in Team settings that CLOUD.md [F4] and SETUP.md step 9 already define; no rule is added to the rulebook.

## Codex findings
- Codex on fa81ce5: finished, "Didn't find any major issues" (https://github.com/conwad-lab/tb-site/pull/41#issuecomment-6922116426). No findings to rule on.

## What I checked
- tests run: as in Evidence.
- tried to break: whether the CI-only description is true of the workflow (it also skips `./.git/`, harmless); whether two in flight is allowed for a public repo's minutes (public repo, free Actions minutes; CLOUD.md [F4] "where minutes … can take double"); whether the new Human-merge paths close the Judge note on #39 (yes: a `merge: auto` PR changing `pr-check` now goes on agreement only); whether `merge: auto` in `.team/team.md` needs changing (no, out of scope).
- scope vs story: matches, one file.

## Papercuts
- 2026-11-16 | reviewer | `gh pr view` refused (GraphQL 403 in cloud sessions) | REST `gh api repos/…/pulls/41` | open

— Judge (Claude) on behalf of Conny
