---
id: 034
verdict: approve
---

# Review 034 — Upgrade agent-team to v0.8.20 (b16e2a5) and let green rule changes merge on agreement

PR: #81 · 2026-11-23 · Judge (Claude) on behalf of Conny, no planning context

## Must fix
- none

## Should fix
- none

## Nits
- N1 `.team/backlog/034-agent-team-v0.8.19-rules.md` acceptance criteria 1 and 4 and the PR title still say v0.8.19 / 2bed8ec / 164 tests; the head pins b16e2a5 (v0.8.20, contains 2bed8ec) and the suite there has 179 cases. The response file records the re-pin, so nothing is hidden; the story text is just stale.
- N2 (pre-existing since v0.8.15, upstream): the `release` class does not apply **Guard paths**. A PR that moves the submodule may still change unguarded Team settings entries in AGENTS.md (here e.g. Review checks, Data changes) without a card, while the comment on Guard paths says an AGENTS.md rule change takes a card. Judge and Codex still gate such a PR. Suggestion for agent-team: in the release class, a changed AGENTS.md line is red when AGENTS.md is on Guard paths, or only the version line may move.

## Evidence
| Acceptance criterion | Shown by | Result |
|---|---|---|
| Submodule pin and team.md pin line | `git ls-tree HEAD .claude/skills/agent-team` → b16e2a50811b5882928964caefde4b822d99fd4d (agent-team main, #42; `merge-base --is-ancestor 2bed8ec b16e2a5` true); team.md line `@ v0.8.20 (b16e2a5: …)` | met at b16e2a5 (supersedes 2bed8ec, N1) |
| Job `auto` from the asset, local changes kept; triggers, permissions, job `merge` unchanged | job `auto` extracted from the workflow is byte-identical to the asset's at b16e2a5 (`diff` empty; this repo keeps `ubuntu-latest`, as the asset does); every diff hunk of the workflow lies in the header comments or inside job `auto` (`git diff -U0 origin/master...HEAD`) | met |
| AGENTS.md: `Auto-merge: release, rules` and `Guard paths: \`AGENTS.md\``, each with its comment | diff of AGENTS.md § Team settings | met |
| YAML parses, `bash -n` on every script, agent-team merge tests pass | `yaml.safe_load` ok; `bash -n` ok on every `run:` block; `bash tests/agent-team-merge.test.sh` at b16e2a5 → PASS (179) | met |
| Required checks on the head | `pr-check` success, `agent-team-auto` success on a0b5f15 | not green for a cause outside the diff: no merge line before they are (CLOUD.md § Human approval 4) |

## Codex findings
- Round 1 M1 (continuation lines of a guarded key), M1 (seats children), M1 mondmodel (walls in Team settings the workflow cannot name → Guard paths `AGENTS.md`), M2 mondmodel (unclosed comment hides an entry): valid — fixed (agent-team #42, `guarded()`, markup check in `agents_check`, Guard paths line here).
- Round 2 M1 (unindented comment / flat seats in team.md) and M2 (Guard paths tightening skipped the markup check): valid — fixed (team.md value whitelist; added Guard paths line must be backticked globs plus at most one closed comment).
- Round 3 (dignami P2 placeholder in a model line; relationsmodellen calibration cases missing at 2bed8ec): valid — fixed (814f6c0; re-pin to b16e2a5 with all 179 cases).
- Last code commit: no findings on 1558169 (issuecomment receipt 2026-11-23 15:05Z); a0b5f15 touches only `.team/reviews/034-…response.md`.
- No finding ruled not valid, no Builder dispute.

## What I checked
- tests run: agent-team `tests/agent-team-merge.test.sh` at the pin (179/179); YAML + `bash -n`; repo Test before commit: `check_html.py` over every page → exit 0 (the same check as pr-check, which is green on the head)
- tried to break: release bump through Guard paths (N2, pre-existing); green class vs `.team/team.md` seats/merge/mode lines (whitelist holds); title regex `^([0-9A-Za-z]+: )?Rulebook story\.`; pause on main during a merge (refused by the branch-holds-main check)
- tb-site only: job `merge` keeps its GitHub Pages step, untouched by the diff (hunks lie only in the header and inside job `auto`).
- scope vs story: only the pin, team.md pin line, the workflow's header and job `auto`, AGENTS.md Team settings, story/plan/response. No app file.
- CLOUD.md length ([C1]): submodule CLOUD.md 3444 words at 495c6f8 → 3430 at b16e2a5, not longer.
- Remove: nothing, because this is an install of rules already judged upstream (agent-team #40, #41, #42); removal belongs in agent-team.
- Sync gate: `git merge-base --is-ancestor origin/master <head>` true at review time; checked again before any merge line.
- Route: a `Rulebook story.` that changes `.github/workflows/agent-team-merge.yml` and the guarded Auto-merge key is a red rule change (CLOUD.md § Human approval): it merges only on Conny's Merga on a decision card, never on agreement.

## Papercuts
2026-11-23 | reviewer | repo required checks not run: GitHub billing limit / MacBook runner disk | Test before commit run in the Judge's cloud container instead | open

