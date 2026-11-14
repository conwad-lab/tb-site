---
id: pr35
verdict: approve
---

# Review PR #35 — merge workflow: decode the review file before matching

PR: #35 · 2026-11-14 · head reviewed: 84541b0

Outside the story flow (fix for agent-team story F / #24). Human-merge path (`.github/workflows/agent-team-merge.yml`) and no finished Codex review (usage limit, twice): needs Conny's yes on a card.

## Must fix
- none

## Should fix
- none

## Nits
- N1 GITHUB_TOKEN may be refused merging a PR that changes `.github/workflows/**` (open risk from #33 N2). If the workflow comments a refusal, this PR needs the per-PR route.
- N2 Pre-existing, not this diff: the Codex check counts any `chatgpt-codex-connector[bot]` comment, so a usage-limit reply passes it. Upstream Förslag.
- N3 This file is kept under 2.5 KB on purpose: master's workflow still has the bug and must read it.

## Evidence
| Criterion | Shown by | Result |
|---|---|---|
| Large approving review file merges | agent-team #24 test 14 on this file: ok (master's file: not ok) | pass |
| Unreadable review file refuses, names it | test 15: ok (master: not ok) | pass |
| Rest of script unchanged | test run 20/21 ok; only fail is 10 (generic board fixture lists `src/a.js`, refused by tb-site's own board check, as on master); script = asset #24 apart from that block | pass |
| No other pipe with the same early exit | read whole script: other `grep -q` read here-strings; `head`/`grep -c` pipes are `|| true` or unchecked | pass |
| YAML / bash syntax | `yaml.safe_load` ok; `bash -n` ok | pass |
| Site unchanged | diff is one file under `.github/`; `python3 -m html.parser index.html` exit 0 | pass |

## Codex findings
- None: both review requests (08:07, 09:08) answered "usage limits". No Builder disputes.

## What I checked
- `$(… | base64 -d) || refuse`: under pipefail a gh or decode failure refuses; `refuse` exits the main shell (the for body is not a subshell). Here-string to `grep -q` cannot SIGPIPE. Over-1 MB file → empty content → not approve (fail closed).
- No required checks exist on this repo, nothing pending.

— Judge (Claude) on behalf of Conny
