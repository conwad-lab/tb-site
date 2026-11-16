---
id: pr39
verdict: request-changes
---

# Review pr39 — ci: always-running pr-check job for the strict ruleset

PR: #39 · 2026-11-16 · reviewed head `0e8205cb9142ba1bea72af3edb4bd41207a436e1`

Opened outside the story flow (no backlog file, plan or ORDER row), as groundwork for the strict ruleset that `Stories in flight: 2` needs (SETUP.md step 9). Judged against the PR body, `AGENTS.md` and `.claude/skills/agent-team/team/CLOUD.md` at b25d713. Route: `merge: auto`, and neither file is on a Human-merge path (`AGENTS.md` lists only `.github/workflows/agent-team-merge.yml`), so this merges on my word (§ Judge 5 [J9]) once approved.

## Must fix
- M1 PR body — two claims the diff no longer supports since 0e8205c dropped the AGENTS.md edits: "`AGENTS.md`: names `pr-check` under CI-only checks and adds the workflow to Human-merge paths", and "Workflow file = human-merge path, needs Conny's yes on a card" (per `AGENTS.md` § Team settings it is not a Human-merge path, so no card). A reader of the merged PR, or the routine, gets the wrong picture of what landed and how it merged. Fix: edit the body to say what the PR does now (workflow + script only) and that naming `pr-check` in `AGENTS.md` is a later Rulebook story. Body edit only, no push needed for this one.
- M2 `.github/scripts/check_html.py:18-19` — Codex M3, upheld: `handle_startendtag` ignores `<span/>`, `<div/>` and other non-void HTML elements written self-closing, which browsers treat as an open tag. Reproduced: `<div><span/></div>` exits 0. The script's own docstring promises to fail on unbalanced tags, so this is a missing check for a stated behavior. Fix: in `handle_startendtag`, when the tag is not in `VOID` and no `svg`/`math` element is open on the stack, append an error (`line N: <tag/> is not a void element`); keep `<path/>` etc. inside SVG passing. Add the two cases to your local check (`<div><span/></div>` fails, `<svg><path d="x"/></svg>` passes).

## Should fix
- none

## Nits
- Nit: `.github/workflows/pr-check.yml:15` — `actions/checkout@v4` is a moving tag. Fine for a public repo with `contents: read`; pin by SHA if the strict ruleset later makes this the only gate.
- Nit: after merge, `AGENTS.md` § Team settings still says **CI-only checks:** none, and `pr-check.yml` (the job the ruleset will require) is changeable by any `merge: auto` PR. Both belong in the Rulebook story the Builder mentions; flagged to the Coordinator.

## Evidence
| Claim (from the PR body) | Shown by | Result |
|---|---|---|
| Job `pr-check` runs on every PR to `master`, no path filter | `pr-check.yml`: `on: pull_request: branches: [master]`, no `paths:`; check run `pr-check completed success` on 0e8205c | pass |
| Checks that every `*.html` outside `.claude/` parses | `find … -print0 \| xargs -0 python3 .github/scripts/check_html.py` locally: exit 0 on the four files (`index.html`, three in `docs/offert-ordforandens-fraga/`); fails on `<div><span></div>`, on an empty file and on a missing file; **passes** on `<div><span/></div>` | fail → M2 |
| `AGENTS.md` edits | not in the diff (dropped in 0e8205c) | fail → M1 |
| Workflow is a Human-merge path | `AGENTS.md` Human-merge paths name only `agent-team-merge.yml` | fail → M1 |
| Test before commit | `python3 -m html.parser index.html` exit 0; no page file changed, so screenshots and link check do not apply | n/a |
| Required checks | master has no required status checks yet (rules: deletion, non_fast_forward, pull_request) | n/a |
| Sync gate | `git merge-base --is-ancestor` master a5c3267 → 0e8205c: true | pass |

## Codex findings
- M1 (P1, 5a45300) `python3 -m html.parser` is a no-op: **valid — fixed** in 0e8205c (`check_html.py` feeds HTMLParser and exits 1 on errors; verified above).
- M2 (P1, 5a45300) AGENTS.md edits without a Rulebook story: **valid — fixed** in 0e8205c (edits removed; `AGENTS.md` untouched vs master).
- M3 (P2, 0e8205c) self-closing non-void elements pass: **valid — still open**, my M2. The Builder agreed it is valid and deferred it; a finding I would not let ship unfixed is not deferrable.
- Codex review on 0e8205c finished (summary "Complete", only M3).

## What I checked
- tests run: as in Evidence.
- tried to break: SVG self-closing inside `<svg>` (passes, correct); missing file (traceback, exit 1 — acceptable); workflow permissions (`contents: read`, `pull_request` not `pull_request_target`, so fork PRs cannot get a write token); whether `agent-team-merge` can merge a PR that adds a workflow file (yes: #35 changed a workflow and was merged by github-actions[bot]).
- scope vs PR body: M1.

## Papercuts
- 2026-11-16 | reviewer | `gh pr view` refused (GraphQL 403 in cloud sessions) | REST `gh api repos/…/pulls/39` | open

— Judge (Claude) on behalf of Conny
