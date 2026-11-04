---
id: pr30
verdict: approve
---

# Review PR #30 — Upgrade agent-team to v0.7.6

PR: #30 · 2026-11-04 · head reviewed: 755cd77

Rulebook story (outside the story flow, no backlog file): approval goes to Conny on a merge card (CLOUD.md § Judge 5, § Human approval). I do not merge without that yes.

## Must fix
- none

## Should fix
- none

## Nits
- N1 `.team/team.md:22` — pinned by commit because the v0.7.6 tag is not pushed yet. Correct for now; when the tag exists, the line can drop "tag not pushed yet".
- N2 Link check: the five external page URLs (dignami.com ×2, the r2.dev PDF, mondmodel.com, cal.com) could not be reached from this cloud session (curl status 000, proxy), so they are **not checked**. `index.html` is unchanged, so the change needs no link check; Conny's standing Operatör check of the live page after merge covers them.

## Evidence
| Acceptance criterion | Shown by (test, command + output, screenshot) | Result |
|---|---|---|
| Submodule `.claude/skills/agent-team` 93a678a → 7dd938e, the v0.7.6 merge of conwad-lab/agent-team#13 | `git diff FETCH_HEAD(master) pr30` → `Subproject commit 7dd938eb…`; agent-team `origin/main` head is `7dd938e Rulebook story. v0.7.6: full CI once per story, not on every fix push (#13)` | pass |
| `.team/team.md` pin line says v0.7.6 | `.team/team.md:22` `team: .claude/skills/agent-team @ v0.7.6 (7dd938e; tag not pushed yet, pinned by commit)` | pass |
| No workflow changes needed (v0.7.6 draft guard + `ready_for_review` apply only to workflows) | `ls .github` → no such directory; GitHub reports 0 check runs on 755cd77 | pass |
| Site unchanged | `git diff --stat master pr30` → only the submodule and `.team/team.md`; `python3 -m html.parser index.html` exit 0; Playwright full-page screenshots at 1440×900 and 390×844 after scrolling, sha256 e1f450f5… and f0e00c0f…, identical to the committed `.team/screenshots/015-builder-codex-{1440,390}.png` from master | pass |

## Codex findings
- Round 1 on 755cd77 (triggered by "draft marked ready" and the Builder's `@codex review`): "Didn't find any major issues." Summary status completed on 755cd77. Nothing to rule on, no Builder disputes.

## What I checked
- tests run: `python3 -m html.parser index.html` (exit 0); Playwright screenshots at both widths (above); link check (in-page anchors exist; external URLs not checked, N2); `git diff --check` clean; required checks: none exist (no workflows, 0 check runs), so § Judge 2's "ran after ready, not skipped" has nothing to apply to.
- tried to break: read the full agent-team diff 93a678a..7dd938e (`team/CLOUD.md` § Builder 2 and 5, § Judge 2, § Quota "Actions minutes"; `assets/cloud/project-instructions.md` version line). Grepped `AGENTS.md` and `.team/team.md` for draft/ready rules that could contradict it: none. `AGENTS.md` § Team settings **Builder** line (Builder runs Test before commit on Codex's head before every review request) fits the new draft-through-rounds flow. `_config.yml` still excludes `.claude` and `.team`, so nothing new is published. No hard rail, `CNAME` or Human-merge path touched beyond the rulebook itself.
- scope vs story: rulebook-only, first line `Rulebook story.`; two-line diff exactly as the PR body says.

— Judge (Claude) on behalf of Conny
