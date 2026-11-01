---
id: 014
title: "Codex builds tb-site stories (builder: codex, agent-team v0.7.5)"
parked-until: agent-team v0.7.5 merged (conwad-lab/agent-team, rulebook PR "v0.7.5: Codex builds where a Codex environment exists")
---

Rulebook story.

## Outcome
tb-site runs on agent-team v0.7.5 with `builder: codex`: Codex writes the code for each story from a `@codex` task on the story's issue, and the Builder thread drives the rest.

## Why
Conny has spare Codex capacity and Claude turns are the scarce resource (decision card "Ja, punkt 1–3", 2026-11-01). tb-site has had a Codex environment since 2026-10-17, so `@codex` tasks can run here. Mondmodel shows the practice works (issues #851, #862, #871: a buildable diff in about ten minutes). tb-site is also pinned on v0.7.3 and misses v0.7.4's data rule and v0.7.5's Builder rules.

## Signal
The next tb-site story after this one merges with its code commits from Codex (issue `NNN:` with a `@codex` task and Codex's PR or diff), with no "Codex failed twice" line in its response file. Read off GitHub.

## Acceptance criteria
- [ ] `.claude/skills/agent-team` is pinned on the merge commit of agent-team v0.7.5, and `.team/team.md`'s `team:` line names v0.7.5 and that short sha.
- [ ] `.team/team.md` says `builder: codex` with a comment naming CLOUD.md § Builder and the Codex environment (2026-10-17); the `models:` coder line says Codex builds from a `@codex` task on the story's issue, the Builder thread drives.
- [ ] `AGENTS.md` § Team settings has a **Builder** line: `builder: codex` per CLOUD.md § Builder (issue `NNN: <story title>` with the `@codex` task, Codex writes code and fixes, the Builder thread runs Test before commit on Codex's head incl. the Playwright screenshots and link check, which Codex's environment may not run; Codex fails twice → the Builder thread builds).
- [ ] `AGENTS.md` § "If you are Codex" no longer says "the Builder is a Claude thread"; it says Codex builds when a task asks it to, and attacks in review, reviewing its own PRs as if someone else wrote them.
- [ ] `python3 -m html.parser index.html` exits 0 and `index.html` is unchanged (`git diff master --stat` lists no site file).

## Out of scope
- Any change to the site itself.
- `merge:` and Human-merge paths stay as they are.

## Log
- 2026-11-01 PO: created, parked until agent-team v0.7.5 is merged. Human merge (rulebook story).
