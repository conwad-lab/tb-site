---
id: 015
verdict: approve
---

# Review 015 — Codex builds tb-site stories (builder: codex)

PR: #27 · 2026-11-03 · head reviewed: 3220144 (rulebook commit b13c29d, built by the Builder thread)

Rulebook story: approval goes to Conny on a merge card (CLOUD.md § Judge 5, § Human approval). I do not merge without that yes.

## Must fix
- none

## Should fix
- none

## Nits
- N1 `AGENTS.md:46` — the "If you are Codex" paragraph now says twice that a build request makes Codex the Coder (new first sentence, and the kept "If a task or comment instead asks you to build, you are the Coder …"), and "instead" no longer has anything to contrast with. The plan kept the second sentence on purpose for its hard rails, so the meaning is right. Next time this paragraph is touched: fold the two into one sentence.
- N2 Link check: seven external URLs could not be reached from any cloud session (proxy 403), same as on master. `index.html` is unchanged, so the change itself needs no link check; Conny's standing Operatör check of the live page after merge covers them.

## Evidence
| Acceptance criterion | Shown by (test, command + output, screenshot) | Result |
|---|---|---|
| A test `@codex` task runs in the tb-site environment and returns a real result, linked in the PR | Issue #23 comment 6588920658 (21:29Z, `@codex … ls`) → chatgpt-codex-connector reply 21:30:24Z with the repo-root `ls` listing; issue #26 21:34:54Z: Codex plan attack quoting repo files. Both linked in the PR body. No "create an environment" reply. | pass |
| `.team/team.md`: `builder: codex` with a comment naming CLOUD.md § Builder and the environment; `models:` coder line | `.team/team.md:20` and `:9`, byte-for-byte the plan's new lines (`git diff origin/master...HEAD -- .team/team.md`) | pass |
| `AGENTS.md` § Team settings **Builder** line (issue task, Codex code + fixes, Builder runs Test before commit incl. Playwright + link check, fails twice → Builder builds) | `AGENTS.md:42`, plan text verbatim; read against CLOUD.md v0.7.5 § Builder "With `builder: codex`" (issue task, `@codex fix M2:`, three failure kinds, response-file line): consistent | pass |
| "If you are Codex" no longer says "the Builder is a Claude thread"; Codex builds on a task, attacks in review incl. own PRs | `grep -c "the Builder is a Claude thread" AGENTS.md` → 0; `AGENTS.md:46` new first sentence; Code Review Rules bullet `AGENTS.md:58` | pass |
| `python3 -m html.parser index.html` exits 0, `index.html` unchanged | `python3 -m html.parser index.html` → exit 0; `git diff --exit-code origin/master -- index.html _config.yml .claude/skills/agent-team` → no diff | pass |

## Codex findings
- Plan attack (issue #26) M1–M4, S1: all answered `changed in plan` under `## Plan attack` in the plan; the diff follows the changed plan. Nothing open.
- Round 1 on b13c29d, M1 (link check missed `<link href>` values, false "all 200" claim): **valid — fixed** in the PR body. I reproduced it: 17 distinct `href` values in the DOM, of which the Google Fonts stylesheet → 200, the two preconnect origins → 404 (expected for `rel="preconnect"`, same on master), seven external URLs → proxy-blocked, listed as not checked; in-page anchors and `assets/favicon.svg` exist.
- Round 1, S1 (screenshots committed beyond the planned files): Builder disputes. **not valid** — AGENTS.md § Review checks requires screenshots at both widths attached to the PR, the cloud session cannot upload images to a comment, `.team/screenshots/` is the repo's precedent (story 013 on master), and `_config.yml` excludes `.team` from the published site.
- Round 2 on 3220144: "Didn't find any major issues." Nothing to rule on.

## What I checked
- tests run: `python3 -m html.parser index.html` (exit 0); Playwright full-page screenshots at 1440×900 and 390×844 after scrolling to the bottom — sha256 identical to the Builder's committed `.team/screenshots/015-builder-codex-{1440,390}.png` (e1f450f5…, f0e00c0f…), page renders fully (r2.dev backgrounds blocked by the proxy, as on master); link check as above; `git diff --check` clean; GitHub reports no checks on 3220144, mergeable clean.
- tried to break: read the whole diff myself. Compared every edit to the plan's old → new lines; checked the Builder line's failure rules and fix comment against pinned CLOUD.md v0.7.5 (93a678a) § Builder; checked the environment claim against issue #23 and #26 (the M1 of review 014 is resolved by a real run). Submodule, `_config.yml`, `merge:` and Human-merge paths untouched.
- scope vs story: rulebook-only, first line `Rulebook story.`; site unchanged; files beyond the plan are the response file (allowed by plan Step 2) and the screenshots (ruled above).

— Judge (Claude) on behalf of Conny
