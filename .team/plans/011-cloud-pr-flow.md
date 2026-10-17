---
id: 011
verdict: plan
---

# Plan 011 — Cloud mode for the PR flow

Story: `.team/backlog/011-cloud-pr-flow.md`

## Approach
Project-level only: a new rulebook file `.team/CLOUD.md` that overrides the parts of v0.6 that assume local clones (wait loops, board script, Coder's branch naming), plus pointers in `AGENTS.md` and `.team/team.md`. The submodule stays at v0.6.4; a v0.7 with cloud mode is decided after the test. No site file changes, so the Pages build is unaffected.

## Files
- `.team/CLOUD.md` — new: roles, flow, exact `@codex` handoff and fix comments, review protocol, where each check runs, status table, merge and quota rules, what is measured.
- `AGENTS.md` — pointer to `CLOUD.md`, rulebook list, `## If you are Codex, started by an @codex comment`, `## Code Review Rules`.
- `.team/team.md` — `mode: cloud …`, role lines say where each runs.
- `.team/ORDER.md`, `.team/backlog/011-…`, this plan — in the same PR (see story Log).

## Tests
- `python3 -m html.parser index.html` (site untouched; sanity only).
- `git diff --stat master` shows only the files above; nothing under `.claude/skills/agent-team/`.

## Risks / watch out for
- Codex cloud picks its own branch names; status is keyed on `NNN:` in titles instead of `feat/NNN-*`.
- Codex cloud may have no Playwright and no network; the Reviewer covers those checks. The Claude cloud network allowlist may also block external `href`s — reported as not checked, not passed.
- A Claude session's comments appear as Conny's. Signing is what tells them apart.

## Out of scope
- v0.7 of agent-team, the Projects coordinator, the smoke test.

## Suggestions for PO
- After 2026-11-03, fold `CLOUD.md` into agent-team as a mode if the test holds.
