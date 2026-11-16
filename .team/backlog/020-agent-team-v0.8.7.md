---
id: 020
title: "Upgrade agent-team to v0.8.7"
---

Rulebook story.

## Outcome
tb-site runs agent-team v0.8.7: the submodule `.claude/skills/agent-team` is pinned to 1d13b7c and the pin line in `.team/team.md` says so.

## Why
agent-team #28 (v0.8.7, merged 2026-11-16 as 1d13b7c) teaches `bin/watch` the Coordinator's park line `Parked until YYYY-MM-DD: <reason>` (CLOUD.md [R8]) and skips `feat/` branches with nothing ahead of the default branch. The routine runs `bin/watch` from its own checkout of agent-team main, so the watch already works for tb-site; the pin keeps the rulebook the tb-site roles read (`CLOUD.md`, `WHY.md`) the same as the one the watch follows. tb-site is the public repo that gets each bump first (#37 v0.8.5, #38 v0.8.6); the private repos follow on 1 December.

## Signal
`git ls-tree origin/master .claude/skills/agent-team` shows 1d13b7c and `.team/team.md` on master reads `@ v0.8.7 (1d13b7c …)`, read the day after merge.

## Acceptance criteria
- [ ] `.claude/skills/agent-team` points at 1d13b7c (b25d713 → 1d13b7c).
- [ ] `.team/team.md` pin line: `team: .claude/skills/agent-team @ v0.8.7 (1d13b7c; tag not pushed, pinned by commit)`.
- [ ] `git diff master --stat` lists only `.claude/skills/agent-team`, `.team/team.md` and `.team/**` (review files); `index.html` is unchanged and `python3 -m html.parser index.html` exits 0.
- [ ] `.github/workflows/agent-team-merge.yml` is unchanged: v0.8.7 does not touch `assets/root/` (`git diff --stat b25d713 1d13b7c` in the submodule lists only `assets/cloud/project-instructions.md`, `bin/watch`, `team/CLOUD.md`, `team/WHY.md`, `tests/watch.test.sh`). If it does, stop and tell the Coordinator.

## Out of scope
- `AGENTS.md` § Team settings, `merge:`, `builder:`, Stories in flight (stays 2).
- `AGENT_ACCOUNT` for the routine (judge note N1 on agent-team #28; a Förslag row).
- Any site change.

## Log
- 2026-11-17 Coordinator: written after agent-team #28 merged, on the Coordinator's request in the routine thread. Rulebook story, so the PR is a human-merge path (the Judge merges on agreement with Codex under Conny's standing rule).
