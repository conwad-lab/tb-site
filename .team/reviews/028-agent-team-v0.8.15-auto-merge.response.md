# Response 028: Upgrade agent-team to v0.8.15 and let release bumps merge on agreement

PR #67. Builder (Claude).

## Codex round 1 — 2026-11-22
Reviewed commit `d271d5e`: no findings.

## Codex ready review — 2026-11-22
Reviewed commit `d271d5e` (draft marked ready).

- **M1 (P2), no trigger when the Judge submits its review** (inline comment 4656171697): disputed — the gap is real but bounded, and the suggested fix opens a worse one. A `pull_request_review` trigger runs the workflow file from the PR's merge ref, not from the default branch, so a PR that edits `agent-team-merge.yml` could run its own merge logic with a write token on a review; story T deliberately runs `auto` only from triggers that use the default branch's copy (`pull_request_target`, `issue_comment`, `workflow_run`, `check_suite`). In practice the Judge's review-file push starts `pr-check`, whose `workflow_run` completion arrives after the review is posted; where it does not, CLOUD.md [J10]/SETUP step 8 has the Judge message the Coordinator `NNN auto-merge did not run` after 30 minutes and the PR takes § Judge 5's other routes, so a bump cannot stay open indefinitely. The job is the agent-team asset unchanged; a safe re-trigger on the Judge's review (for example a `workflow_dispatch` the Judge starts, or the Judge's review-file push ordered after its review) belongs in agent-team itself and goes to Förslag there.

## Outcome
No code change. One finding, disputed with the reason above.

— Builder (Claude) on behalf of Conny
