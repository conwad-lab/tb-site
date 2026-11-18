---
id: 022
verdict: approve
---

# Review 022 — Rulebook story. agent-team v0.8.9 and a runnable Test before commit

PR: #53 · 2026-11-18 · reviewed head `8d4d13082cb26554725a77e14aef29edb745b0a1`

Judged against story and plan `022-agent-team-v0.8.9-codex-cli`, `AGENTS.md` and `.claude/skills/agent-team/team/CLOUD.md` at the new pin 230dee6.

## Must fix
- none

## Should fix
- none

## Nits
- N1 `AGENTS.md:45` — **Where checks run in the cloud** still says `python3 -m html.parser` everywhere, the no-op check this story replaced. Harmless (that line is not read by the poller), but it now contradicts **Test before commit**. Suggested: name the `check_html.py` command there at the next rulebook touch. Not a blocker; for Förslag.

## Evidence
| Acceptance criterion | Shown by | Result |
|---|---|---|
| Submodule 1d13b7c → 230dee6; `.team/team.md` pin line | PR diff `Subproject commit 230dee6…`; `git submodule update` checks out 230dee6 "v0.8.9 … (#30)"; `.team/team.md:27` = `team: .claude/skills/agent-team @ v0.8.9 (230dee6; tag not pushed, pinned by commit)` | pass |
| Test before commit = one backticked span, the pr-check command; poller extraction gives exactly it; exits 0 | Poller's own `grep`/`sed`/`awk` (`bin/codex-cli-poll` 335–339 at 230dee6, read) on the branch's `AGENTS.md` prints `find . -name '*.html' -not -path './.claude/*' -not -path './.git/*' -print0 \| xargs -0 python3 .github/scripts/check_html.py`; `bash -c` on it: exit 0 | pass |
| The command really checks something | `check_html.py` on a file with `<div><p>x</span>`: "unexpected </span>", "<div> never closed", exit 1 | pass |
| No other backtick on that line; rest of AGENTS.md keeps its meaning | the line has two backticks; "pr-check", "mail links" in prose. Rest of diff: two added sentences only (see N1) | pass |
| **Builder:** names `codex-cli`, one sentence, codex stays fallback | `AGENTS.md:46`; `.team/team.md` builder line untouched | pass |
| § If you are Codex gets the template's sentence | `AGENTS.md:54` matches `assets/root/AGENTS.md` at 230dee6 word for word | pass |
| Workflow, `_config.yml`, `pr-check.yml`, `check_html.py`, site files unchanged | `git diff f09ec5a 8d4d130 --stat`: submodule, `.team/team.md`, `AGENTS.md` only; submodule `git diff --stat 1d13b7c 230dee6 -- assets/root/`: only `assets/root/AGENTS.md` (ported by hand) | pass |
| C1: CLOUD.md not longer | `wc -w`: 3 479 at 1d13b7c, 3 455 at 230dee6 | pass |
| Submodule tests | `bash tests/codex-cli.test.sh`: all 58 passed | pass |
| Required checks | `pr-check` on 8d4d130: completed, success | pass |
| Sync gate | master = f09ec5a, the branch's parent | pass |
| Signal (023's first run green) | after merge, not before | not yet |

## Codex findings
- Round on 8d4d130 (the last commit outside `.team/reviews/**`): finished 2026-11-18 13:22Z, "Didn't find any major issues", review state `has_any_findings: false`. No findings to rule on, no Builder disputes.

## What I checked
- tests run: poller extraction + command, `check_html.py` negative test, `codex-cli.test.sh`.
- tried to break: a stray backtick joining into the poller command (none); `find`/`xargs -0` on macOS (both BSD tools take `-print0`/`-0`); empty file list (xargs runs the script once with no args; not the case here, `index.html` exists); whether v0.8.9 asks for workflow changes (no, `assets/root/.github/` untouched).
- scope vs story: exactly the three files the plan names.
- Remove: nothing, because this PR only applies the rulebook in a product repo; CLOUD.md shrank upstream (3 479 → 3 455).

## Papercuts
- The Builder left the PR as a draft; the merge workflow refuses drafts, so the Judge marks it ready before the merge line.

— Judge (Claude) on behalf of Conny
