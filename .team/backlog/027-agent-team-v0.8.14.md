---
id: 027
title: "Upgrade agent-team to v0.8.14 and make codex-cli the builder fallback"
---

Rulebook story.

## Outcome
tb-site runs agent-team v0.8.14 and its Team settings name `codex-cli` as the builder fallback: the submodule `.claude/skills/agent-team` is pinned to f1fde0f, `.team/team.md` says `builder: codex-cli`, and `AGENTS.md` § Team settings **Builder** says the same, so the next plan without a builder line is built by Astra or Sol through the host poller.

## Why
agent-team #35 (v0.8.14, story S, merged 2026-11-21 as f1fde0f) makes Codex the default builder: [T2] picks `codex-cli` where the host poller lists the repo, else `codex`, and `claude` only by exclusion; a plan holds its own `## Work order` with a `Proof:` line, and the poller runs Sol or Astra per order (`Model:`). Conny asked for this on 2026-11-21 (too much of the weekly usage on Claude). Story S leaves the per-repo bump to one `Rulebook story.` per repo. tb-site is pinned at v0.8.11 (7ed9768) and its fallback still says `builder: codex` (the `@codex` path, not the poller).

`git diff --stat 7ed9768 f1fde0f` in agent-team (v0.8.12–v0.8.14) touches no path under `assets/root/`, so no workflow, settings or `AGENTS.md` port beyond the Builder line. CLOUD.md is 3 450 words at both pins: [C1] holds.

## Signal
`bin/watch --estimates` shows `built-by: codex-cli` or `codex` on at least 70 % of tb-site's merged non-board, non-rulebook stories in the two weeks after merge (story S's Signal, read at the first weekly retro after the bumps).

## Acceptance criteria
- [ ] `.claude/skills/agent-team` points at f1fde0f (7ed9768 → f1fde0f).
- [ ] `.team/team.md`: pin line `team: .claude/skills/agent-team @ v0.8.14 (f1fde0f; tag not pushed, pinned by commit)`; `builder: codex-cli` with the comment in the plan; the `coder:` line under `models:` names the poller first.
- [ ] `AGENTS.md` § Team settings **Builder**: the fallback sentence names `codex-cli`, with `codex` when the poller does not pick up the order (`team/CODEX-CLI.md`), exactly as in the plan. Nothing else in `AGENTS.md` changes.
- [ ] `git diff master --stat` lists only `.claude/skills/agent-team`, `.team/team.md`, `AGENTS.md` and `.team/**`.
- [ ] `git -C .claude/skills/agent-team diff --stat 7ed9768 f1fde0f -- assets/root/` lists nothing; anything else → stop and tell the Coordinator.
- [ ] `tests/watch.test.sh` and `tests/codex-cli.test.sh` pass inside the submodule; Test before commit passes.

## Out of scope
- Any plan's `## Work order` (the next product story is the first one planned with it).
- `merge:`, Stories in flight, the merge workflow and `.claude/settings.json`.
- The Judge's nits N1–N4 on agent-team #35 (Förslag row).
- The poller's host config (`MODELS`): Conny re-runs the install line on the MacBook (agent-team plan S, Operatör 1).

## Log
- 2026-11-21 Coordinator's planner (thread "Bumpa fyra repon till v0.8.14"): written after agent-team #35 merged, on Conny's yes 06:10Z to story S and the standing goal cmsg_016Rw4YNn4Cnv18u3K3Ttc76CKEW4sFQ5zrQr1YaFTmZXF.

— Coordinator (Claude) on behalf of Conny
