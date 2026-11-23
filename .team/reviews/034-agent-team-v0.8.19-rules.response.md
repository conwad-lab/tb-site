## Codex round 1 — 2026-11-23 (findings across the six install PRs, answered in every one)
- M1 relationsmodellen-site #80: a guarded Team settings key's continuation lines could change as green — valid, fixed: each guarded top-level bullet is compared whole at both ends (agent-team #42).
- M1 tb-site #81 / dignami-aos #82: lines nested under `seats:` in `.team/team.md` could change as green — valid, fixed: the guarded keys' blocks are compared whole at both ends (agent-team #42).
- M1 mondmodel #963: Team settings here hold walls the workflow cannot name (e.g. Workflow changes) — valid, fixed: `Guard paths: \`AGENTS.md\``, so any AGENTS.md rule change takes a card; the green class here is `.team/` board, review files and `.team/team.md` version and model lines.
- M2 mondmodel #963: an unclosed `<!--` in Team settings could hide a guarded entry — valid, fixed: changed AGENTS.md lines with unbalanced comments, raw HTML blocks, fences or heading underlines are red (agent-team #42, tests 164 → 170).

## Codex round 2 — 2026-11-23
- M1 `.github/workflows/agent-team-merge.yml:430` an unindented comment line inside seats: let a new seat through — fixed in agent-team #42 (da63958), ported here in 260fe70: .team/team.md may change only the values of its team, builder, project and model lines, in place

## Codex round 3 — 2026-11-23
- no findings on 70aa75e
- after the round: agent-team #42 merged as b16e2a5; the submodule moves from 2bed8ec to b16e2a5 (v0.8.20 with #41 and #42), so the pinned suite tests the workflow installed here

## Codex round 4 — 2026-11-23
- no findings on 1558169

## Outcome
built-by: claude
model: Claude (Builder thread)
parts: none
missed: nothing (rulebook install without a plan Estimate). Codex took four rounds; rounds 1–2 found real holes in the green class, fixed upstream in agent-team #42 and pinned here at b16e2a5.
