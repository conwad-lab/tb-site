---
id: 027
verdict: approve
---

# Review 027 — Rulebook story. agent-team v0.8.14 and codex-cli as builder fallback

PR: #66 · 2026-11-21 · reviewed head `7bcc5a340e2a8f25e26b352183e2fef29f10ff22`

Judged against story and plan `027-agent-team-v0.8.14`, `AGENTS.md` and `.claude/skills/agent-team/team/CLOUD.md` at the new pin f1fde0f.

## Must fix
- none

## Should fix
- none

## Nits
- none

## Evidence
| Acceptance criterion | Shown by | Result |
|---|---|---|
| Submodule 7ed9768 → f1fde0f | PR diff `Subproject commit f1fde0f…`; `git ls-tree HEAD .claude/skills/agent-team` = f1fde0f; checkout shows "Rulebook story. v0.8.14 … (#35)" | pass |
| `.team/team.md`: pin line, `builder: codex-cli` with the plan's comment, `coder:` names the poller first | `.team/team.md` lines 9, 20, 27 match plan step 3 word for word | pass |
| `AGENTS.md` **Builder** fallback sentence as in the plan; nothing else changes | diff of `AGENTS.md` is that one sentence on line 46, matching plan step 4 | pass |
| `git diff master --stat` only submodule, `.team/team.md`, `AGENTS.md`, `.team/**` | `git diff 5ce5096 7bcc5a3 --stat`: those plus `.team/PAPERCUTS.md` (one appended line) | pass |
| `assets/root/` unchanged between pins | `git diff --stat 7ed9768 f1fde0f -- assets/root/`: empty | pass |
| Submodule tests; Test before commit | `tests/watch.test.sh`: 1..108 ok; `tests/codex-cli.test.sh`: all 89 passed; `check_html.py` over all html: exit 0 | pass |
| C1: CLOUD.md not longer | `wc -w`: 3 450 at 7ed9768, 3 450 at f1fde0f | pass |
| Required checks | `pr-check` on 7bcc5a3: completed, success | pass |
| Sync gate | master = 5ce5096, the branch's parent | pass |
| Signal (≥ 70 % codex-built in two weeks) | after merge, at the first weekly retro | not yet |

## Codex findings
- Round on 7bcc5a3 (the last commit outside `.team/reviews/**`): finished 2026-11-21 07:47Z, "Didn't find any major issues". No findings to rule on, no Builder disputes.

## What I checked
- tests run: both submodule suites, `check_html.py`.
- tried to break: whether `codex-cli` is a value [T2] knows (yes, CLOUD.md line 15 at f1fde0f); whether v0.8.12–v0.8.14 ask for a workflow or settings port (no, `assets/root/` untouched); whether the plan's `builder: claude` for this story fits [T2] (yes, a `Rulebook story.`); no site file changed, so no screenshots or link check are needed.
- scope vs story: the three files the plan names plus one papercut line.
- Remove: nothing, because this PR only applies the rulebook in a product repo; CLOUD.md length is unchanged upstream (3 450 → 3 450).

## Papercuts
- none

— Judge (Claude) on behalf of Conny
