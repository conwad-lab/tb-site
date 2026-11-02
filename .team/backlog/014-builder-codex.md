---
id: 014
title: "Pin agent-team v0.7.5"
---

Rulebook story.

## Outcome
tb-site runs under agent-team v0.7.5 rules: the submodule is pinned on the v0.7.5 merge commit (93a678a). `builder:` stays as it is; the switch to `builder: codex` is story 015.

## Why
tb-site is pinned on v0.7.3 (141623c) and misses v0.7.4's data rule and v0.7.5's Builder rules (Codex fallback, plan attack on risky stories). Conny decided the v0.7.5 rollout on 2026-11-01 (decision card "Ja, punkt 1–3"). The Codex switch itself cannot land yet: `@codex` tasks in tb-site answer "create an environment for this repo" (issue #23).

## Signal
The pin is on master, and the next tb-site story's plan and PR follow v0.7.5 (CLOUD.md § Builder). Read off GitHub.

## Acceptance criteria
- [ ] `.claude/skills/agent-team` is pinned on 93a678a (the agent-team v0.7.5 merge commit), and `.team/team.md`'s `team:` line names v0.7.5 and that short sha.
- [ ] `builder:` in `.team/team.md` and AGENTS.md § Team settings are unchanged apart from what the re-pin requires.
- [ ] `python3 -m html.parser index.html` exits 0 and `index.html` is unchanged (`git diff master --stat` lists only `.claude/skills/agent-team` and `.team/**`).

## Out of scope
- Any change to the site itself.
- `builder: codex`, the AGENTS.md **Builder** line and § "If you are Codex" (story 015).
- `merge:` and Human-merge paths stay as they are.

## Log
- 2026-11-01 PO: created, parked until agent-team v0.7.5 is merged. Human merge (rulebook story).
- 2026-11-02 PO: unparked; agent-team v0.7.5 merged as 93a678a (PR #12). Pin the submodule on 93a678a.
- 2026-11-02 PO: scope narrowed to the v0.7.5 pin (Judge note N2 on PR #24). The `@codex` plan attack on issue #23 failed twice with "create an environment for this repo", so the Codex switch moved to story 015, parked until an `@codex` task succeeds in tb-site.
