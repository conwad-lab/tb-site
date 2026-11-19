---
id: 024
verdict: approve
---

# Review 024 — Rulebook story. Upgrade agent-team to v0.8.11

PR: #58 · 2026-11-19 · reviewed head `c8d60edd4fcc80be25bca1c72b972a1b5c9a4e6b`

Story `.team/backlog/024-agent-team-v0.8.11.md`, plan `.team/plans/024-agent-team-v0.8.11.md`. Judged against CLOUD.md at master's pin 230dee6 and at the new pin 7ed9768.

## Must fix
- none

## Should fix
- none

## Nits
- none

## Evidence
| Acceptance criterion | Shown by | Result |
|---|---|---|
| Submodule 230dee6 → 7ed9768 | `git ls-tree c8d60ed .claude/skills/agent-team` = 7ed976820bbe…; master = 230dee687ed7…; 7ed9768 is on agent-team `main` (`merge-base --is-ancestor`) | pass |
| `.team/team.md` pin line | diff: `@ v0.8.9 (230dee6; …)` → `@ v0.8.11 (7ed9768; tag not pushed, pinned by commit)`, exactly the story's text | pass |
| Diff lists only the submodule, `.team/team.md`, `.team/**` | PR files: `.claude/skills/agent-team`, `.team/team.md` | pass |
| No `assets/root/` change between pins | `git diff --stat 230dee6 7ed9768 -- assets/root/` in the submodule: empty | pass |
| `tests/watch.test.sh`, `tests/part-check.test.sh` pass | run at 7ed9768: 1..108 all ok, 1..42 all ok | pass |
| Test before commit | `check_html.py` over every `*.html` outside `.claude/`: exit 0. No site file changed, so screenshots and link check do not apply | pass / n/a |
| Required check `pr-check` | check run on c8d60ed: completed, success | pass |
| C1: CLOUD.md not longer | `git show <pin>:team/CLOUD.md \| wc -w`: 3 455 at 230dee6, 3 450 at 7ed9768 | pass |
| Sync gate | `git merge-base --is-ancestor origin/master c8d60ed` true (master 3bc3d41) | pass |

## Codex findings
- Round on c8d60ed (the last commit outside `.team/reviews/**`): finished, receipt "Didn't find any major issues" (https://github.com/conwad-lab/tb-site/pull/58#issuecomment-7010047049). No findings to rule on, no Builder disputes.

## What I checked
- tests run: as in Evidence.
- tried to break: whether the pin is a commit that exists only on a branch (no, on `main`); whether v0.8.10/v0.8.11 ask a port into tb-site's merge workflow, AGENTS.md or settings (no `assets/root/` change); whether `.team/team.md` is a Human-merge or Human-only path (AGENTS.md: neither; Human-only paths none).
- scope vs story: matches; nothing outside the plan's Files.
- Remove: nothing.
- Merge route: Rulebook story, on agreement (CLOUD.md § Judge 5 [J10]): approve with nothing open, no Codex finding ruled `not valid`, finished Codex review on the head, `pr-check` green. No § Human approval exception applies, so no card.

## Papercuts
- none

— Judge (Claude) on behalf of Conny
