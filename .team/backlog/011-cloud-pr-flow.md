---
id: 011
title: Cloud mode — the team's roles rewritten for the PR flow (test until 2026-11-03)
---

Rulebook story.

## Outcome
The team can run without local clones: a Claude cloud session is PO and Architect, Codex in the cloud codes on an `@codex` comment, a Claude cloud session reviews, and the v0.6 review protocol still holds.

## Why
The local team (four clones, four terminals, `wait-for` loops) no longer fits on the MacBook, and the Mac mini decision falls on 2026-11-03. Before that, the cloud flow has to be tried on real stories. Claude coordinating *and* coding burns Claude quota while Codex sits idle, so the v0.6 split is kept: Claude plans and reviews, Codex codes.

## Acceptance criteria
- [ ] `.team/CLOUD.md` describes cloud mode: who runs which role and where, the flow from ORDER row to merge, the exact handoff comment to Codex, the exact fix comment, how status is read off the PR, and the quota rules.
- [ ] The v0.6 review protocol is kept and rewritten for the PR flow: numbered M/S/N findings, the review file with `verdict:` on the PR branch, Codex answers in `NNN-slug.response.md` (`fixed in <sha>` / `disputed — <reason>`), no approve past an open Must fix, `verdict: escalate` after three rounds → Operatör line.
- [ ] `AGENTS.md` tells Codex what to do when started by an `@codex` comment (read the named plan, implement only that, run the checks it can run, PR title `NNN: …`, answer review findings in the response file, never merge, never touch the rulebook), and names `.team/CLOUD.md` as part of the rulebook.
- [ ] `AGENTS.md` says what Codex's own automatic PR review is for in this repo (off: Claude is the Reviewer).
- [ ] `.team/team.md` records `mode: cloud (test until 2026-11-03)` and the merge setting for the test.
- [ ] Checks that cannot run in a cloud environment (Playwright screenshots, external `href` checks) are named, with who runs them instead; a check that did not run never counts as passed.
- [ ] Nothing in the submodule (`.claude/skills/agent-team/`) changes; the site (`index.html`, `CNAME`, `_config.yml`) is untouched.

## Out of scope
- A new agent-team release (v0.7) with cloud mode built in. Decided after the test.
- Projects (coordinator that starts threads). Not needed to start; added when the beta is on.
- The smoke test of measure point 1 (does Codex start on an `@codex` comment from a Claude session) — runs as its own throwaway issue/PR, not as a story.

## Log
- 2026-10-17 PO: created from ORDER row 011, ordered by Conny in the handover of 2026-10-17. Story, plan and rulebook change go in one PR, because this session is PO, Architect and author at once and Conny reviews rulebook changes himself; merge is Conny's, not auto.
