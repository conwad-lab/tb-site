---
id: pr38
verdict: request-changes
---

# Review pr38 — Rulebook story. Upgrade agent-team to v0.8.6

PR: #38 · 2026-11-16 · reviewed head `8f2801e973265774fddd9779a12ad06268fcddb6`

Rulebook story outside the story flow (no backlog file or plan, like #34, #37). Judged against `.claude/skills/agent-team/team/CLOUD.md` at the new pin b25d713 and the assets there.

## Must fix
- M1 `.github/workflows/agent-team-merge.yml.orig` (new file, 127 lines) — a leftover backup from applying the asset patch: it is byte-identical to master's old `agent-team-merge.yml` (old Codex rule, no receipt check, no card line). The PR body does not mention it, it is not part of the asset change, and it puts a second, outdated copy of the merge script on a Human-merge directory, where the next upgrade or a reader can take it for the live one. GitHub does not run it (`.orig` is not `.yml`), so this is scope and rulebook hygiene, not a live risk. Fix: `git rm .github/workflows/agent-team-merge.yml.orig`, push, `@codex review` on the new head.

## Should fix
- none

## Nits
- none

## Evidence
| Acceptance criterion (from the PR body) | Shown by | Result |
|---|---|---|
| Submodule 99c0fdd → b25d713 (v0.8.6) | PR diff `Subproject commit b25d7139c2f9…`; `git submodule update` checks out b25d713 | pass |
| `.team/team.md` pin line → v0.8.6 | `.team/team.md:27` = `v0.8.6 (b25d713; …)` | pass |
| Stories in flight stays 1 (no strict ruleset on master yet) | `AGENTS.md:41` = `1`, unchanged from master | pass |
| Workflow: asset change applied, tb-site's board check and Pages step kept | `diff` of the `begin/end agent-team-merge script` block against `assets/root/.github/workflows/agent-team-merge.yml` at b25d713: only difference is tb-site's own `board:` path check; Pages step unchanged. YAML parses (`yaml.safe_load`). b25d713's `tests/agent-team-merge.test.sh` run against tb-site's script: 32/33 pass, incl. 20–33 (receipt-only Codex, card line, other head, short sha, placeholders); the one failure is test 10 (board PR), expected because tb-site's script adds the board path check the generic test does not feed (known since #35) | pass |
| C1: CLOUD.md not longer | `git show <pin>:team/CLOUD.md \| wc -w`: 3 486 at 99c0fdd, 3 485 at b25d713 | pass |
| Nothing else in the PR | file list: submodule, `.team/team.md`, workflow, response file — and the `.orig` file | fail → M1 |
| Test before commit | no site file changed (`index.html` untouched), so html.parser/screenshots/link check do not apply | n/a |
| Required checks | no check runs or statuses on the head (master has no required checks) | n/a |
| Sync gate | `git merge-base --is-ancestor origin/master 8f2801e` true (master 728bc60) | pass |

## Codex findings
- Round on e6645af (the last commit outside `.team/reviews/**`), M1 (P1) "CLOUD.md grows 3,511 → 3,512 words": **not valid** — measured myself, 3 486 at 99c0fdd and 3 485 at b25d713; the new pin is one word shorter. I uphold the Builder's dispute.
- Round on 8f2801e (response file only): finished, "Didn't find any major issues".
- Consequence: a Codex P1 ruled `not valid` is a disagreement (CLOUD.md § Human approval [H1]), so this PR cannot merge on agreement (§ Judge 5 (b)) even after M1 is fixed; it goes to Conny on one decision card.

## What I checked
- tests run: as in Evidence.
- tried to break: whether the v0.8.6 changes to `assets/root/AGENTS.md` (Stories in flight comment) or SETUP.md ask anything of tb-site now (no: tb-site's own AGENTS.md text, and 2 waits for the ruleset Operatör row); whether the card-line regex accepts another head, a quoted line or placeholders (tests 29–31 refuse them).
- scope vs story: the `.orig` file is outside it (M1).
- Remove: nothing, because this PR only applies the rulebook in a product repo; CLOUD.md shrank upstream (3 486 → 3 485).

## Papercuts
- none

— Judge (Claude) on behalf of Conny
