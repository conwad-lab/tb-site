---
id: pr33
verdict: approve
---

# Review PR #33 — Install the agent-team merge workflow (v0.7.12)

PR: #33 · 2026-11-07 · head reviewed: cfbd073

Outside the story flow (CLOUD.md § One-time setup 8, no backlog file). It changes `AGENTS.md` § Team settings and adds a file on a Human-merge path, so it needs Conny's yes. Conny said yes to installing the workflow in the team repos (2026-11-07 10:30), and Conny's standing rule (2026-11-07) is that what the team recommends merges without Conny stepping in.

## Must fix
- none

## Should fix
- none

## Nits
- N1 `.github/workflows/agent-team-merge.yml:113-125` — the tb-site-only Pages step could not be run against GitHub from this session (the proxy refuses `repos/…/pages`), so whether `POST pages/builds` with `GITHUB_TOKEN` and `pages: write` starts a build for this branch-published site is **not checked**. It fails loudly (PR comment + red job) if refused, and the standing Operatör check of the live page after every merge covers it. Check it on the first workflow merge.
- N2 Open risk carried from agent-team #20 N1: a PR that changes `.github/workflows/**` may be refused when merged with `GITHUB_TOKEN`. The workflow comments the refusal; such PRs keep the per-PR route.
- N3 The workflow does not itself enforce **Human-merge paths**; it trusts the Judge's `agent-team-merge:` line. That is the asset's design (merging stays the Judge's call), noted so no one reads the workflow as a second gate.

## Evidence
| Acceptance criterion | Shown by (test, command + output, screenshot) | Result |
|---|---|---|
| Workflow installed from agent-team v0.7.12 asset | `git diff master pr33` → new `.github/workflows/agent-team-merge.yml`; merge script between the begin/end markers matches the asset apart from the board-only path check (PR body; Codex reviewed) | pass |
| Workflow file on Human-merge paths | `AGENTS.md:39` now lists `.github/workflows/agent-team-merge.yml` | pass |
| Trigger only from owner / `AGENT_ACCOUNT` with OWNER/MEMBER/COLLABORATOR association, on `issue_comment: created` | job `if:` lines 22-27 | pass |
| Comment body never interpolated into shell | `BODY` passed via `env:`; script reads `$BODY` | pass |
| Merge pinned to the commented sha | `PUT pulls/$PR/merge -f sha="$sha"` after `head == sha` check | pass |
| Pages build only after this run's merge | gate: merged, head == pinned sha, `merged_at >= comment created_at`; bash string compare checked: `[[ "2026-11-07T10:50:00Z" > "2026-11-07T10:49:59Z" ]]` true, `"-"` (unmerged) false | pass |
| YAML parses | `yaml.safe_load` → steps `['Merge the pinned head', 'Request a GitHub Pages build after the merge']` | pass |
| Site unchanged and not published | `index.html` untouched, `python3 -m html.parser index.html` exit 0; `.github` is a dot-directory, which Jekyll does not publish | pass |

## Codex findings
- M1 (r1) Pages build missing after a `GITHUB_TOKEN` merge — valid — fixed in 6ff1679.
- S1 (r2) Pages request gated on historical `merged` — valid — fixed in fb9717f.
- M1 (r3) PR-lookup failure in the Pages gate exits 0 silently — valid — fixed in ee3bffc.
- Board-only path check and truncation guard (f7ce57c, cfbd073), from Codex M1 on sibling PRs — valid — fixed.
- Codex on cfbd073 (the head): "Didn't find any major issues"; summary status completed on cfbd073. No Builder disputes.

## What I checked
- tests run: YAML parse; `python3 -m html.parser index.html`; the timestamp comparison in the Pages gate. No required checks exist on this repo (no other workflows), so nothing to run after ready.
- tried to break: injection via comment body (env only); trigger by bots or Codex (login + association guard); stale or re-used verdict (head must equal pinned sha, PR must be open and not a draft); Pages step after a failed or no-op merge (a failed step stops the job; no-op exits 0 before the merge and the gate's `merged_at` check refuses a historical merge); `read < <(gh …)` on API failure (read gets EOF, so the failure branch runs); board PR with renames or >3000 files (previous_filename included, refused at 3000). `runs-on` defaults to `ubuntu-latest`, right for this public repo.
- scope vs story: exactly the two files the PR body names; no submodule bump (pin stays 7dd938e, as stated).

— Judge (Claude) on behalf of Conny
