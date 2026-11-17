---
id: pr37
verdict: approve
---

# Review pr37 — Rulebook story. Upgrade agent-team to v0.8.5

PR: #37 · 2026-11-16 · reviewed head `5ddedfc356313a9e203dedfae6520c45ac370185`

Rulebook story outside the story flow (no backlog file or plan, like #34). Judged against `.claude/skills/agent-team/team/CLOUD.md` at the new pin 99c0fdd and the assets there.

## Must fix
- none

## Should fix
- none

## Nits
- none

## Evidence
| Acceptance criterion (from the PR body) | Shown by | Result |
|---|---|---|
| Submodule pinned 6e34726 → 99c0fdd (v0.8.5), a commit on agent-team `main` | PR diff `Subproject commit 99c0fdd132bb…`; `git merge-base --is-ancestor 99c0fdd origin/main` in agent-team true (main tip 99c0fdd) | pass |
| `.team/team.md` pin line matches the submodule | `.team/team.md:27` = `v0.8.5 (99c0fdd; …)` | pass |
| Nothing else in tb-site needs to change | `git diff --stat 6e34726 99c0fdd` in agent-team: only `team/CLOUD.md`, `team/SETUP.md`, `team/WHY.md`, `bin/watch`, `tests/watch.test.sh`, `assets/cloud/project-instructions.md` (version line). `assets/root/**` (AGENTS.md template, merge workflow, `.claude/settings.json`) and `assets/team/**` unchanged, so tb-site's copies, matched at #34/#35, still match. CLOUD.md diff: [F3], [F5], [F8], [B1], [B5], [J2], [R7], [W5], [C1] wording only; no new Team settings key | pass |
| C1: CLOUD.md not longer | `wc -w`: 3 488 at 6e34726, 3 486 at 99c0fdd | pass |
| Site untouched | `git diff --stat origin/master..5ddedfc` = submodule, `.team/team.md`, response file only | pass |
| Test before commit | `python3 -m html.parser index.html` exit 0; `.claude/settings.json` parses. No site file changed, so screenshots and link check are not needed | pass |
| Required checks | no check runs or statuses on the head; `rules/branches/master` = deletion, non_fast_forward, pull_request (no required checks) | n/a |
| Sync gate | `git merge-base --is-ancestor origin/master 5ddedfc` true (master e63600c); compare ahead 2, behind 0 | pass |

## Codex findings
- Round 1 (04f0da6, the last commit outside `.team/reviews/**`): finished, "Didn't find any major issues"; summary state `completed`, no findings. 5ddedfc touches only the response file. No disputes.

## What I checked
- tests run: as in Evidence.
- tried to break: whether the restored conditions ([B1] retry and go, [F4] in flight until merged or closed, [W5] Claude GitHub App exception) or the dropped "the PR cuts at least as much" in [C1] ask anything of a product repo (they do not: tb-site has `agent-account: none`, `Stories in flight` default 1, and C1 is checked here by `wc -w` only); whether `bin/watch` changes need a repo file (no, it runs from the project routine).
- scope vs story: only the pin, the pin line and the response file.
- Remove: nothing, because this PR only applies the rulebook in a product repo; CLOUD.md shrank upstream (3 488 → 3 486).

## Papercuts
- none

— Judge (Claude) on behalf of Conny
