---
id: 020
verdict: approve
---

# Review 020 — Rulebook story. Upgrade agent-team to v0.8.7

PR: #46 · 2026-11-16 · reviewed head `a636665ba2e7cf5e8af605bdbd47a2212a3b85e7`

Judged against story and plan `020-agent-team-v0.8.7`, `AGENTS.md` and `.claude/skills/agent-team/team/CLOUD.md` at the new pin 1d13b7c.

## Must fix
- none

## Should fix
- none

## Nits
- none

## Evidence
| Acceptance criterion | Shown by | Result |
|---|---|---|
| Submodule b25d713 → 1d13b7c | PR diff `Subproject commit`; `git submodule update` checks out 1d13b7c ("v0.8.7 … (#28)") | pass |
| `.team/team.md` pin line | `.team/team.md:27` = `team: .claude/skills/agent-team @ v0.8.7 (1d13b7c; tag not pushed, pinned by commit)` | pass |
| Only submodule, `.team/team.md`, `.team/**`; `index.html` unchanged, html.parser exits 0 | `git diff origin/master --stat` (master ca393c9): 2 files, `.claude/skills/agent-team`, `.team/team.md`; `python3 -m html.parser index.html` exit 0 | pass |
| Merge workflow unchanged, v0.8.7 does not touch `assets/root/` | `git diff --stat b25d713 1d13b7c` in the submodule: `assets/cloud/project-instructions.md`, `bin/watch`, `team/CLOUD.md`, `team/WHY.md`, `tests/watch.test.sh` only; `git diff origin/master -- .github` empty | pass |
| C1: CLOUD.md not longer | `wc -w`: 3 485 at b25d713, 3 479 at 1d13b7c | pass |
| Test before commit | no site file changed; submodule `bash tests/watch.test.sh`: 1..106, all ok | pass |
| Required checks | `pr-check` on a636665: completed, success | pass |
| Sync gate | `git merge-base --is-ancestor origin/master a636665` true (master ca393c9) | pass |

## Codex findings
- Round on a636665 (the last commit outside `.team/reviews/**`): finished, receipt "Didn't find any major issues" (2026-11-16 23:54Z), review state `has_any_findings: false`. No findings to rule on, no Builder disputes.

## What I checked
- tried to break: whether v0.8.7 asks anything of tb-site's own files (no: `assets/root/` untouched, so `AGENTS.md` and the workflow stay; `assets/cloud/project-instructions.md` is the Coordinator's text, not tb-site's); whether the head contains master (yes).
- scope vs story: exactly the two files the story names.
- Remove: nothing, because this PR only applies the rulebook in a product repo; CLOUD.md shrank upstream (3 485 → 3 479).

## Papercuts
- The Builder left the PR as a draft; the merge workflow refuses drafts, so the Judge marked it ready before the merge line.

— Judge (Claude) on behalf of Conny
