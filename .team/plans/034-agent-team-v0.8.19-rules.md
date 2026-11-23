---
id: 034
verdict: plan
---

# Plan 034: agent-team v0.8.19 with Auto-merge: release, rules

Story: `.team/backlog/034-agent-team-v0.8.19-rules.md`. Branch `feat/034-agent-team-v0.8.19-rules`. Title `034: Rulebook story. Upgrade agent-team to v0.8.19 and let green rule changes merge on agreement`.

## Approach
1. Move the submodule to 2bed8ec; update the pin line in `.team/team.md`.
2. Replace job `auto` in `.github/workflows/agent-team-merge.yml` with the asset's at 2bed8ec, keeping this repo's local changes to it (a three-way merge of old asset, this repo's copy and the new asset). Add one header comment line. Nothing else in the file moves.
3. `AGENTS.md` Team settings: `Auto-merge: release, rules` with a comment naming both classes, and `Guard paths: `AGENTS.md`` (Team settings here hold walls the workflow cannot name; Codex M1 on mondmodel #963), so the green class is `.team/` board and review files and `.team/team.md` version and model lines.
4. Check: YAML parses, `bash -n` on each script block, agent-team merge tests at 2bed8ec.

## Estimate
size: S
risk: human-merge
files: 5 (+ story and plan)
codex-rounds: 2
builder: claude — `Rulebook story.` on the merge workflow
model: standard

## Files
`.claude/skills/agent-team` (pin), `.team/team.md`, `.github/workflows/agent-team-merge.yml`, `AGENTS.md`, `.team/backlog/034-agent-team-v0.8.19-rules.md`, `.team/plans/034-agent-team-v0.8.19-rules.md`.

## Risks
- The install itself is red (workflow, guarded keys): one card, the last of its kind for this repo.
- A green rule change can still be wrong; the Monday sample [R13] and the 14-day pause are the net.

## Plan attack
Rulebook story: Codex attacks plan and diff together on the PR. Focus: can a diff that loosens a wall pass as green here, and did the port drop any local change to job `auto`.
