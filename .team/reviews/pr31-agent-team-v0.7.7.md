---
id: pr31
verdict: approve
---

# Review PR #31 — Upgrade agent-team to v0.7.7

PR: #31 · 2026-11-04 · head reviewed: 65e8f1b

Rulebook story (outside the story flow, no backlog file; the PR body's story line is `Rulebook story.`, as #30): approval goes to Conny on a merge card (CLOUD.md § Judge 5, § Human approval). I do not merge without that yes.

## Must fix
- none

## Should fix
- none

## Nits
- N1 `.team/team.md:22` — pinned by commit because the v0.7.7 tag is not pushed yet. Correct for now; drop "tag not pushed yet" once the tag exists.
- N2 External links not checked from this cloud session (proxy), as in #30. `index.html` is unchanged, so the change needs no link check; Conny's standing Operatör check of the live page covers them.

## Evidence
| Acceptance criterion | Shown by (test, command + output, screenshot) | Result |
|---|---|---|
| Submodule `.claude/skills/agent-team` 7dd938e → 6e7052d, the v0.7.7 merge of conwad-lab/agent-team#14 | PR diff `Subproject commit 7dd938eb… → 6e7052db…`; agent-team `origin/main` head is `6e7052d Rulebook story. v0.7.7: a change-classifier skip after ready counts as green (#14)`, parent `7dd938e` (v0.7.6) | pass |
| `.team/team.md` pin line says v0.7.7 | `.team/team.md:22` `team: .claude/skills/agent-team @ v0.7.7 (6e7052d; tag not pushed yet, pinned by commit)` | pass |
| Nothing changes in practice (no workflows, so the classifier-skip rule has nothing to apply to) | `ls .github/workflows` → no such directory; GitHub reports 0 check runs and 0 statuses on 65e8f1b | pass |
| Site unchanged | `git diff --stat 36cde19 pr31` → only the submodule and `.team/team.md`; `python3 -m html.parser index.html` exit 0; Playwright full-page screenshots at 1440×900 and 390×844 after scrolling, sha256 e1f450f5… and f0e00c0f…, identical to the committed `.team/screenshots/015-builder-codex-{1440,390}.png` (a first 1440 run differed by animation timing; the rerun is byte-identical, PIL diff bbox None) | pass |

## Codex findings
- Round 1 on 65e8f1b (`@codex review`, 06:49): "Didn't find any major issues."
- Ready-for-review review on 65e8f1b (06:51): **M1** `.team/team.md:22` — rulebook file changed without a `Rulebook story.` backlog story. Builder: valid on form, PR body lacked the `Rulebook story.` line, fixed in the body; disputed that a backlog file is needed. Ruling: **valid — fixed**. Rulebook upgrades in tb-site run outside the story flow with the PR body as the story (precedent #30, `.team/reviews/pr30-agent-team-v0.7.6.md`); the body now carries `Rulebook story.` as its story line after the required attribution block, and approval is Conny's merge card, which satisfies `AGENTS.md:57`'s intent (rulebook changes only on the human's order).
- Round 2 on 65e8f1b (`@codex review`, 06:52): "Didn't find any major issues." Summary status completed on 65e8f1b. All requested reviews on the head finished, no open finding.

## What I checked
- tests run: `python3 -m html.parser index.html` (exit 0); Playwright screenshots at both widths (above); `git diff --check` clean; required checks: none exist (no workflows), so § Judge 2 has nothing to apply to.
- tried to break: read the full agent-team diff 7dd938e..6e7052d (`team/CLOUD.md` § Builder 5 and § Judge 2, `assets/cloud/project-instructions.md` version line; 3+/3−). The new exception is narrow (classifier job must run after ready and succeed, skipped code must have had its gate pass after ready; draft-guard skips never count) and does not loosen anything tb-site relies on. Grepped `AGENTS.md` and `.team/team.md` for skip/classifier rules that could contradict it: none. `_config.yml` still excludes `.claude` and `.team`, so nothing new is published. No hard rail, `CNAME` or other Human-merge path touched beyond the rulebook itself.
- scope vs story: two-line diff exactly as the PR body says.

— Judge (Claude) on behalf of Conny
