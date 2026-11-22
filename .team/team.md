# Team config

human: Conny Wadbro
project: transformationbeyond.se

models:
  product-owner: claude-fable-5-1
  architect: claude-fable-5-1
  coder: codex — Astra or Sol through the host poller (codex-cli, team/CODEX-CLI.md), else a @codex task on the story's issue NNN: <story title>; the Claude Builder thread drives the rest (team/CLOUD.md § Builder)
  attacker: codex (GPT) — automatic review + @codex review on every round
  reviewer: claude-fable-5-1 — Judge thread per PR, without planning context

# One seat = one human's subscriptions; every commit carries `Seat: <name>`.
seats:
  conny: { claude: max, codex: plus }
auth: max-only — ingen API-nyckel i rollernas miljö (bin/check-auth stoppar starten)

merge: auto
mode: cloud — see .claude/skills/agent-team/team/CLOUD.md; the Judge merges on approve, and on Human-merge paths and rulebook stories only on agreement with Codex (CLOUD.md § Judge 5, AGENTS.md)
builder: codex-cli  # fallback when a plan's ## Estimate names no builder (team/CLOUD.md [T2], v0.8.14); the host poller lists tb-site. codex (environment since 2026-11-02, issue #23) when the poller does not pick up the order. Codex fails twice → the Builder thread builds

# cloud only: where CI runs. tb-site is public, so never mini (team/RUNNER.md); it has no CI workflows today.
runner: github
# cloud only: the GitHub login the agents act as (CLOUD.md § Walls); none = the human's login, signed "on behalf of".
agent-account: none

team: .claude/skills/agent-team @ v0.8.15 (495c6f8; tag not pushed, pinned by commit)
<!-- upgrade with /agent-team upgrade, or: git submodule update --remote .claude/skills/agent-team -->

Project specifics go in AGENTS.md § Team settings, not in role overrides: a file in `.team/roles/<role>.md` replaces the whole role and cuts the project off from team upgrades.
