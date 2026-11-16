---
id: 019
verdict: plan
---

# Plan 019 — Two stories in flight on the strict ruleset

Story: `.team/backlog/019-strict-ruleset-two-stories.md`

## Approach
Three one-line edits in `AGENTS.md` § Team settings, nothing else. The Builder reads the ruleset first (`gh api repos/conwad-lab/tb-site/rules/branches/master`) and stops with a message to the Coordinator if it is not strict with `pr-check`. Touches: price block no, booking CTA no, footer no. No visible copy string changes.

## Estimate
size: S
risk: human-merge
files: 1
codex-rounds: 2
builder: claude — a three-line settings edit; the Builder checks the ruleset by reading it, which Codex's environment cannot do
model: light — the ORDER row for 019 sets it for this pure settings change (CLOUD.md [T2]: an ORDER row wins over the strongest default for a `Rulebook story.`)

## Files
- `AGENTS.md` — **Stories in flight:** 1 → 2; **CI-only checks:** `pr-check` text; **Human-merge paths:** add `.github/workflows/pr-check.yml` and `.github/scripts/check_html.py`.

## Steps
1. Read the ruleset as above; require `strict_required_status_checks_policy: true` and context `pr-check`.
2. Edit the three lines in `AGENTS.md`; no other file.
3. Test, PR with `Rulebook story.` as the first line of the body, `@codex review`.

## Tests
- `python3 -m html.parser index.html` exits 0.
- `git diff master --stat` lists only `AGENTS.md` and `.team/**`.
- `grep -n "Stories in flight" AGENTS.md` shows 2; the Human-merge paths line names both new paths.
- No screenshots (no site change): say so in the PR.

## Risks / watch out for
- With two in flight, the next story's plan must pass CLOUD.md § Flow 3 (a)–(e) (disjoint files, no data change, open-PR cap, no `codex-quota` stall); this story does not start one.
- The Human-merge paths line is what keeps a `merge: auto` PR from rewriting `pr-check`; keep both paths in it.

## Out of scope
- Ruleset, workflow, script, `.team/team.md`.

## Suggestions for PO
- Once merged, put two small stories in the Kö so the parallel flow is exercised (018 is queued).
