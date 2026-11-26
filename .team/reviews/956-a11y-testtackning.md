---
id: 956
verdict: approve
---

# Review 956 — Granska tillgänglighet och testtäckning

PR: #97 · 2026-11-26 · head reviewed 3423ab3 (this file is the only later commit)

Order 956 (Astra work order, `Plan: .team/ORDER.md`, no ORDER row and no story file; the order text is the story). Merge route: `merge: auto`, no Human-merge path touched, the diff is one new file under `docs/` (excluded from the site by `_config.yml`), so the Judge merges on its word (CLOUD.md § Judge 5, J9).

## Must fix
- none

## Should fix
- none

## Nits
- N1 No ORDER row or story file names 956 (nor 961, 967); the only record is the order text in the project folder. Harmless for a report, but the flow's Signal check has nothing to hang on. A one-line ORDER entry would do.
- N2 The report says no verified finding reached P1. I did not hunt for P1s beyond the contrast re-measure below; I agree with the severity of the five P2s.

## Evidence
| Acceptance criterion (order 956) | Shown by | Result |
|---|---|---|
| Report `docs/revision-a11y-test-2026-11-25.md` exists, nothing else changed | `gh api pulls/97/files` → one added file, 49 lines | pass |
| Findings carry file, line and severity (P1/P2/P3) | Report read: every finding row has criterion, location and fix; 5 P2, 1 P3 + one conditional P3 | pass |
| Untested flows listed | Report section "Sidor och flöden som saknar återkommande test" (9 rows) | pass |
| Claims in the report are true | Contrast re-measured by me on a Jekyll build of master: hero-foot text over the poster, text hidden, worst pixel `#859098` → 3.02:1 against `#F8F6F1` (report: 2.98:1 at one point, same finding). Link/line check of the 13 local links: all targets exist, no line past EOF. `pr-check` does not run the three bin/test-* scripts: confirmed in `.github/workflows/pr-check.yml` | pass |
| Test before commit | `pr-check` success on 3423ab3 (check_html.py over all HTML) | pass |
| PR as a draft | draft until I marked it ready for the merge | pass |

## Codex findings
- Codex code review on 3423ab3 completed with no findings (receipt 2026-11-25T20:26Z). Nothing to rule on.

## What I checked
- tests run: pr-check result; my own Jekyll build + Playwright contrast sampling at 1440×900; markdown link/line-reference check.
- tried to break: looked for a claim the code contradicts (menu links hidden ≤860px: `assets/site.css:26` does `display:none` on `a:not(.keep)`: true).
- scope vs story: one docs file, nothing else.
- sync gate: `git merge-base --is-ancestor origin/master 3423ab3` → yes at review time.

## Papercuts
2026-11-26 | reviewer | `gh pr list` and `gh pr view` fail with a GraphQL 403 in the cloud | used `gh api repos/.../pulls/N` (REST) | open
