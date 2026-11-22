---
id: 028
title: "Upgrade agent-team to v0.8.15 and let release bumps merge on agreement"
---

Rulebook story.

## Outcome
tb-site runs agent-team v0.8.15 and its merge workflow has the job `auto`: a later PR that only moves the agent-team submodule forward merges by itself once the Judge's approving review is on the head, Codex found nothing blocking and every check is green, with no decision card. This install PR is the last bump in tb-site that needs Conny's yes.

## Why
agent-team #36 (v0.8.15, story T, merged 2026-11-22 as 495c6f8) adds the job `auto` to `assets/root/.github/workflows/agent-team-merge.yml`. Conny chose it on 2026-11-21 11:35Z ("Bara agent-team-bumpar") after the v0.8.14 bumps each needed a card although Judge and Codex agreed. `team/SETUP.md` step 8 leaves the switch to each repo: list the repo's PR workflows under `workflow_run` and set `- **Auto-merge:** release` in Team settings. tb-site is pinned at v0.8.14 (f1fde0f).

`git diff --stat f1fde0f 495c6f8 -- assets/root/` in agent-team touches only the merge workflow and `assets/root/AGENTS.md` (the new Auto-merge template line). CLOUD.md goes 3 450 → 3 444 words: [C1] holds.

tb-site's job `merge` also requests a GitHub Pages build after it merges; the job `auto` does not, and needs none, since a release bump changes no published file.

## Signal
In the two weeks after merge, the next agent-team bump PR in tb-site that reaches Judge approve with a clean Codex review gets `Merged by agent-team-merge (release bump)` from `github-actions[bot]` within 30 minutes, with no card (story T's Signal, read at the first weekly retro after the next agent-team release).

## Acceptance criteria
- [ ] `.claude/skills/agent-team` points at 495c6f8 (f1fde0f → 495c6f8); the `.team/team.md` pin line reads `@ v0.8.15 (495c6f8; tag not pushed, pinned by commit)`.
- [ ] `.github/workflows/agent-team-merge.yml` has the job `auto` copied unchanged from agent-team 495c6f8 (only `runs-on`'s default differs, as the job `merge` here), the triggers `issue_comment` (created, edited), `pull_request_target` (synchronize, ready_for_review), `check_suite` and `workflow_run` on `pr-check`, and the permissions `checks: read` and `statuses: read`.
- [ ] The job `merge` behaves as before: it runs only on a newly created comment (`github.event.action == 'created'`), its concurrency is per PR at job level, and its script is unchanged.
- [ ] `AGENTS.md` § Team settings has `- **Auto-merge:** release`. Nothing else in `AGENTS.md` changes.
- [ ] The workflow parses as YAML; agent-team's `tests/agent-team-merge.test.sh` passes at 495c6f8; Test before commit passes.

## Out of scope
- Wider auto-merge classes (content, noindex, the guard rules): each keeps its card.
- The repo variables `AGENT_ACCOUNT` and `AFTER_MERGE_WORKFLOWS` (Operatör, unchanged).
- Any other change to the job `merge`.

## Log
- 2026-11-22 Builder thread "Slå på automerge av bumpar i sex repon", on the Coordinator's request after agent-team #36 merged and Conny's yes to story T (2026-11-21 11:35Z). Story and plan ride in the install PR, as the coordinator asked for one install PR per repo.

— Builder (Claude) on behalf of Conny
