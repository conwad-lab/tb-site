---
id: 027
verdict: plan
---

# Plan 027 — Upgrade agent-team to v0.8.14 and make codex-cli the builder fallback

Story: `.team/backlog/027-agent-team-v0.8.14.md`

## Approach
Same shape as the earlier pin bumps (022, 024), plus the builder fallback that story S asks each repo to set: move the submodule pin, rewrite three lines in `.team/team.md` and one sentence in `AGENTS.md`. No other rule text.

## Estimate
size: S
risk: human-merge
files: 3
codex-rounds: 1
builder: claude — a `Rulebook story.` with a submodule pin, which the poller's push guard refuses ([T2])
codex-model: —
model: light — a pin bump and four given lines

## Files
- `.claude/skills/agent-team` — 7ed9768 → f1fde0f.
- `.team/team.md` — the `coder:` line (line 9), the `builder:` line (line 20) and the pin line (line 27) on master.
- `AGENTS.md` — § Team settings **Builder** (line 46), one sentence.

## Steps
1. `git submodule update --init .claude/skills/agent-team`, then `git -C .claude/skills/agent-team fetch origin main && git -C .claude/skills/agent-team checkout f1fde0f`.
2. `git -C .claude/skills/agent-team diff --stat 7ed9768 f1fde0f -- assets/root/`: expect no output; otherwise stop and tell the Coordinator.
3. `.team/team.md`, replace the three lines with:
   - `  coder: codex — Astra or Sol through the host poller (codex-cli, team/CODEX-CLI.md), else a @codex task on the story's issue NNN: <story title>; the Claude Builder thread drives the rest (team/CLOUD.md § Builder)`
   - `builder: codex-cli  # fallback when a plan's ## Estimate names no builder (team/CLOUD.md [T2], v0.8.14); the host poller lists tb-site. codex (environment since 2026-11-02, issue #23) when the poller does not pick up the order. Codex fails twice → the Builder thread builds`
   - `team: .claude/skills/agent-team @ v0.8.14 (f1fde0f; tag not pushed, pinned by commit)`
4. `AGENTS.md` line 46: replace `` `builder: codex` in `.team/team.md` is the fallback for a plan without one. `` with `` `builder: codex-cli` in `.team/team.md` is the fallback for a plan without one, and `codex` when the poller does not pick up the order (`team/CODEX-CLI.md`). `` Leave the rest of the bullet as it is.
5. Test, PR with `Rulebook story.` as the first body line, `@codex review`.

## Tests
- `git ls-tree HEAD .claude/skills/agent-team` shows f1fde0f; `grep -n 'agent-team @\|^builder:' .team/team.md` shows v0.8.14 and `codex-cli`.
- `bash tests/watch.test.sh` and `bash tests/codex-cli.test.sh` pass inside the submodule.
- the **Test before commit** command from `AGENTS.md` (the `check_html.py` run) exits 0.
- `git diff master --stat` lists only the submodule, `.team/team.md`, `AGENTS.md` and `.team/**`.
- No screenshots (no site change): say so in the PR.

## Required checks and deploys
- Triggers the required check `pr-check` (no site file changes). Public repo, GitHub-hosted. A merge to master publishes nothing new on transformationbeyond.se.

## Risks / watch out for
- Actions minutes: keep the PR a draft during the Codex round, one push per round, mark ready once so CI runs once.
- The default branch has a strict ruleset: merge master in before asking for the Judge if anything lands first.
- Do not port anything into `.github/workflows/agent-team-merge.yml`.

## Out of scope
- `merge:`, Stories in flight, the merge workflow, `.claude/settings.json`.
