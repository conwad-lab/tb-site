---
id: 024
title: "Upgrade agent-team to v0.8.11"
---

Rulebook story.

## Outcome
tb-site runs agent-team v0.8.11: the submodule `.claude/skills/agent-team` is pinned to 7ed9768 and the pin line in `.team/team.md` says so, so a plan with `## Parts` can be built here.

## Why
agent-team #32 (v0.8.11, merged 2026-11-19 as 7ed9768) lets the Builder run a plan's independent parts as parallel subagents on narrow work orders and take each in only after `bin/part-check` passes (`team/PARTS.md`, CLOUD.md [B14], `templates/workorder.md`, an optional `## Parts` in `templates/plan.md`). v0.8.10 (#31, 0339a15) added `bin/runner-install` for the host Mac runner. tb-site is pinned at v0.8.9 (230dee6), so its Builder reads a CLOUD.md without [B14] and has no `PARTS.md` or `bin/part-check`.

`git diff --stat 230dee6 7ed9768` in agent-team touches no path under `assets/root/`, so no workflow, `AGENTS.md` or settings port. CLOUD.md goes 3 455 → 3 450 words: [C1] holds.

## Signal
`git ls-tree origin/master .claude/skills/agent-team` shows 7ed9768 and `.team/team.md` on master reads `@ v0.8.11 (7ed9768 …)`, read the day after merge.

## Acceptance criteria
- [ ] `.claude/skills/agent-team` points at 7ed9768 (230dee6 → 7ed9768).
- [ ] `.team/team.md` pin line: `team: .claude/skills/agent-team @ v0.8.11 (7ed9768; tag not pushed, pinned by commit)`.
- [ ] `git diff master --stat` lists only `.claude/skills/agent-team`, `.team/team.md` and `.team/**`.
- [ ] `git -C .claude/skills/agent-team diff --stat 230dee6 7ed9768 -- assets/root/` lists nothing; anything else → stop and tell the Coordinator.
- [ ] `tests/watch.test.sh` and `tests/part-check.test.sh` pass inside the submodule.

## Out of scope
- `AGENTS.md` § Team settings, `merge:`, `builder:`, `runner:`, Stories in flight.
- The merge workflow and `.claude/settings.json`.
- The judge's notes N1–N3 on agent-team #32 (Förslag rows in agent-team).
- Any first plan with `## Parts` (a later story).

## Log
- 2026-11-19 Coordinator's planner: written after agent-team #32 merged (thread "För ut regelbok v0.8.11 till sex repon", on Conny's standing goal cmsg_016Rw4YNn4Cnv18u3K3Ttc76CKEW4sFQ5zrQr1YaFTmZXF). Rulebook story: the Judge merges on agreement with Codex.

— Coordinator (Claude) on behalf of Conny
