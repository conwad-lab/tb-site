---
id: 015
title: "Codex builds tb-site stories (builder: codex)"
parked-until: "an @codex task succeeds in tb-site (Codex environment, see ORDER.md § Operatör)"
---

Rulebook story.

## Outcome
tb-site runs with `builder: codex`: Codex writes the code for each story from a `@codex` task on the story's issue, and the Builder thread drives the rest.

## Why
Conny has spare Codex capacity and Claude turns are the scarce resource (decision card "Ja, punkt 1–3", 2026-11-01). Mondmodel shows the practice works (issues #851, #862, #871: a buildable diff in about ten minutes). Split out of story 014 on 2026-11-02 because `@codex` tasks in tb-site do not run yet (issue #23: "create an environment for this repo").

## Signal
The next tb-site story after this one merges with its code commits from Codex (issue `NNN:` with a `@codex` task and Codex's PR or diff), with no "Codex failed twice" line in its response file. Read off GitHub.

## Acceptance criteria
- [ ] Before the build: a test `@codex` task on a tb-site issue returns a diff or PR (not "create an environment"). Link it in the PR.
- [ ] `.team/team.md` says `builder: codex` with a comment naming CLOUD.md § Builder and the Codex environment; the `models:` coder line says Codex builds from a `@codex` task on the story's issue, the Builder thread drives.
- [ ] `AGENTS.md` § Team settings has a **Builder** line: `builder: codex` per CLOUD.md § Builder (issue `NNN: <story title>` with the `@codex` task, Codex writes code and fixes, the Builder thread runs Test before commit on Codex's head incl. the Playwright screenshots and link check, which Codex's environment may not run; Codex fails twice → the Builder thread builds).
- [ ] `AGENTS.md` § "If you are Codex" no longer says "the Builder is a Claude thread"; it says Codex builds when a task asks it to, and attacks in review, reviewing its own PRs as if someone else wrote them.
- [ ] `python3 -m html.parser index.html` exits 0 and `index.html` is unchanged.

## Out of scope
- Any change to the site itself.
- The submodule pin (story 014).
- `merge:` and Human-merge paths.

## Log
- 2026-11-02 PO: created from story 014's Codex part (Judge note N2 on PR #24). Parked until an `@codex` task succeeds in tb-site. Human merge (rulebook story).
