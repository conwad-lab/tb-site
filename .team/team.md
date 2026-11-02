# Team config

human: Conny Wadbro
project: transformationbeyond.se

models:
  product-owner: claude-fable-5-1
  architect: claude-fable-5-1
  coder: codex — builds from a @codex task on the story's issue NNN: <story title>; the Claude Builder thread drives the rest (team/CLOUD.md § Builder)
  attacker: codex (GPT) — automatic review + @codex review on every round
  reviewer: claude-fable-5-1 — Judge thread per PR, without planning context

# One seat = one human's subscriptions; every commit carries `Seat: <name>`.
seats:
  conny: { claude: max, codex: plus }
auth: max-only — ingen API-nyckel i rollernas miljö (bin/check-auth stoppar starten)

merge: auto
mode: cloud — see .claude/skills/agent-team/team/CLOUD.md; the Judge merges on approve except on Human-merge paths (AGENTS.md)
builder: codex  # team/CLOUD.md § Builder; needs the tb-site Codex environment (working since 2026-11-02, issue #23). Codex fails twice → the Builder thread builds

team: .claude/skills/agent-team @ v0.7.5 (93a678a)
<!-- upgrade with /agent-team upgrade, or: git submodule update --remote .claude/skills/agent-team -->

Project specifics go in AGENTS.md § Team settings, not in role overrides: a file in `.team/roles/<role>.md` replaces the whole role and cuts the project off from team upgrades.
