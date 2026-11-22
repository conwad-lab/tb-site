# Plan 028: Upgrade agent-team to v0.8.15 and let release bumps merge on agreement

Story: `.team/backlog/028-agent-team-v0.8.15-auto-merge.md`. Rulebook story; builder: claude (a rulebook story, CLOUD.md [T2]); model: light.

## Files
- `.claude/skills/agent-team` (pin f1fde0f → 495c6f8)
- `.team/team.md` (pin line)
- `AGENTS.md` (§ Team settings: the Auto-merge line)
- `.github/workflows/agent-team-merge.yml`
- `.team/backlog/028-agent-team-v0.8.15-auto-merge.md`, `.team/plans/028-agent-team-v0.8.15-auto-merge.md`

## Steps
1. Pin the submodule at 495c6f8 and update the pin line.
2. Keep the job `merge` as it is; add the triggers and permissions the job `auto` needs, make `merge` react only to `created` comments and move its per-PR concurrency to job level (a workflow-level group keyed on the issue number would put every `pull_request_target` and `workflow_run` run of the repo in one group), and append the job `auto` from 495c6f8 with this repo's `runs-on` default.
3. Add `- **Auto-merge:** release` to Team settings.
4. Parse the YAML, run agent-team's tests at 495c6f8 and Test before commit.

## Risk
The new triggers start a short `auto` run on every PR push and every listed workflow's completion; it exits at once when the PR does not move the submodule. It runs on GitHub-hosted runners in this public repo (free minutes).

## Estimate
small; builder: claude; model: light.
