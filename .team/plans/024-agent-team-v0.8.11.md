---
id: 024
verdict: plan
---

# Plan 024 — Upgrade agent-team to v0.8.11

Story: `.team/backlog/024-agent-team-v0.8.11.md`

## Approach
Same shape as the earlier pin bumps (020, 022): move the submodule pin and the pin line, nothing else.

## Estimate
size: S
risk: human-merge
files: 2
codex-rounds: 1
builder: claude — a submodule pin; no code for Codex to write
model: light — a pin bump with no rule text of tb-site's own

## Files
- `.claude/skills/agent-team` — 230dee6 → 7ed9768.
- `.team/team.md` — the pin line (line 27 on master).

## Steps
1. `git submodule update --init .claude/skills/agent-team`, then `git -C .claude/skills/agent-team fetch origin main && git -C .claude/skills/agent-team checkout 7ed9768`.
2. `git -C .claude/skills/agent-team diff --stat 230dee6 7ed9768 -- assets/root/`: expect no output; otherwise stop and tell the Coordinator.
3. Pin line in `.team/team.md`: `team: .claude/skills/agent-team @ v0.8.11 (7ed9768; tag not pushed, pinned by commit)`.
4. Test, PR with `Rulebook story.` as the first body line, `@codex review`.

## Tests
- `git ls-tree HEAD .claude/skills/agent-team` shows 7ed9768; `grep -n 'agent-team @' .team/team.md` shows v0.8.11.
- `bash tests/watch.test.sh` and `bash tests/part-check.test.sh` pass inside the submodule.
- the **Test before commit** command from `AGENTS.md` (the `check_html.py` run) exits 0.
- `git diff master --stat` lists only the submodule, `.team/team.md` and `.team/**`.
- No screenshots (no site change): say so in the PR.

## Required checks and deploys
- Triggers the required check `pr-check` (no site file changes, so it passes as on master). Public repo, GitHub-hosted. A merge to master publishes nothing new on transformationbeyond.se.

## Risks / watch out for
- Actions minutes: keep the PR a draft during the Codex round, one push per round, mark ready once so CI runs once.
- The default branch has a strict ruleset: merge master in before asking for the Judge if anything lands first.
- Do not port anything into `.github/workflows/agent-team-merge.yml`.

## Out of scope
- `AGENTS.md`, the merge workflow, `.claude/settings.json`.
