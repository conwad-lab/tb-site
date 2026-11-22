---
id: 028
verdict: approve
---

# Review 028 — Rulebook story. Upgrade agent-team to v0.8.15 and let release bumps merge on agreement

PR: #67 · 2026-11-22 · reviewed head `665fa089893a0dac6b233957c6f91eb07f74a3f9` (last commit outside `.team/reviews/**`: `d271d5e`)

Judged against story and plan `028-agent-team-v0.8.15-auto-merge`, `AGENTS.md` and `.claude/skills/agent-team/team/CLOUD.md` + `team/SETUP.md` at the new pin 495c6f8.

## Must fix
- none

## Should fix
- none

## Nits
- none

## Evidence
| Acceptance criterion | Shown by | Result |
|---|---|---|
| Submodule f1fde0f → 495c6f8; pin line v0.8.15 | `git ls-files -s .claude/skills/agent-team` = 495c6f8169…; `.team/team.md` line 27 reads `@ v0.8.15 (495c6f8; tag not pushed, pinned by commit)` | pass |
| Job `auto` copied unchanged from 495c6f8 | unified diff of the `auto:` block in the repo against `assets/root/.github/workflows/agent-team-merge.yml` at 495c6f8: empty (the asset's `runs-on` default already is `ubuntu-latest`, so not even that line differs) | pass |
| Triggers `issue_comment` (created, edited), `pull_request_target` (synchronize, ready_for_review), `check_suite`, `workflow_run` on `pr-check`; permissions `checks: read`, `statuses: read` | `yaml.safe_load` of the workflow: exactly these triggers and permissions; `pr-check` is the repo's only other workflow with a `pull_request` trigger (`name: pr-check`) | pass |
| Job `merge` behaves as before | diff against master: only `github.event.action == 'created' &&` added to `if`, concurrency group `agent-team-merge-<issue>` moved unchanged to job level; script and the tb-site Pages step untouched. `workflow_run` (`completed`), `pull_request_target` (`synchronize`/`ready_for_review`), `check_suite` (`completed`) and edited comments all fail `action == 'created'` | pass |
| `AGENTS.md`: `- **Auto-merge:** release`, nothing else | diff of `AGENTS.md` is that one added line in § Team settings | pass |
| YAML parses; agent-team tests at 495c6f8; Test before commit | python yaml: ok; `tests/agent-team-merge.test.sh`: PASS (82); `check_html.py` over every html: exit 0. No page changes, so no screenshots or link check are needed | pass |
| C1: CLOUD.md not longer | `wc -w`: 3 450 at f1fde0f, 3 444 at 495c6f8 | pass |
| Required checks | `pr-check` on 665fa08: completed, success | pass |
| Sync gate | `git merge-base --is-ancestor origin/master HEAD`: true (master = ecdd2c5) | pass |
| Signal (next bump merges by itself within 30 min) | after the next agent-team release, at the weekly retro | not yet |

## Codex findings
- Round 1 on d271d5e (02:12Z): "Didn't find any major issues".
- Ready review on d271d5e (02:17Z), **M1 (P2)** "no trigger when the Judge submits its review", Builder disputed: **not valid — for this PR.** The story requires the asset's job `auto` copied unchanged, and the suggested `pull_request_review` trigger would run the PR's own copy of the workflow with this job's write token, so a PR editing `agent-team-merge.yml` could loosen its own gate; that is the same trigger agent-team #36's Judge ruled out (S1). The gap Codex describes is real but bounded: when `pr-check` on the Judge's review-file push completes before the review is posted, `auto` only runs again on the next event, and [J10]/SETUP step 8 have the Judge message the Coordinator `NNN auto-merge did not run` after 30 minutes, so a bump cannot stay open unseen. The safe fix belongs upstream (Förslag in agent-team: let `auto` also run on a comment by the owner or `AGENT_ACCOUNT`, or have the Judge post its review before the review-file push is checked).

## What I checked
- tests run: `tests/agent-team-merge.test.sh` at 495c6f8, `check_html.py`, YAML parse.
- tried to break: whether any new trigger reaches job `merge` (no, every new event's action differs from `created`); whether moving concurrency to job level lets two `merge` runs of one PR race (no, same group, `cancel-in-progress: false`); whether `auto` and the tb-site Pages step interact (they do not: `auto` requests no Pages build, and a bump changes nothing Jekyll publishes, as `.claude/` and `.team/` are excluded); whether the pin moves forward (agent-team #36 merged f1fde0f's successor line; the tests and CLOUD.md at 495c6f8 are v0.8.15).
- scope vs story: the six files the plan names plus the Builder's response file.
- Remove: nothing, because this PR only applies the rulebook in a product repo; CLOUD.md gets shorter upstream (3 450 → 3 444).

## Route
`.github/workflows/agent-team-merge.yml` is on **Human-merge paths** and SETUP step 8 makes this install PR need Conny's yes naming it; M1 ruled not valid is also an [H1] disagreement. So: no merge line from the Judge; a card "Merga #67" via the Coordinator, and on the yes the Judge posts `Approved by Conny on a decision card` with the card's head.

## Papercuts
- 2026-11-22 | reviewer | `gh api repos/conwad-lab/agent-team/compare/...` refused (agent-team not in this session's scope) | checked the pin's tests and CLOUD.md in the checked-out submodule instead | open

— Judge (Claude) on behalf of Conny
