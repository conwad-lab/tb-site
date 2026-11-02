---
id: 014
verdict: approve
---

# Review 014 — Codex builds tb-site stories (builder: codex, agent-team v0.7.5)

PR: #24 · 2026-11-02 · head reviewed: ce9f790 (code commit 4868333, built by Codex)

## Must fix
- M1 `.team/team.md:20` — `builder: codex — …; Codex environment created 2026-10-17` states a Codex environment that GitHub says does not exist today: both `@codex` tasks on issue #23 (2026-11-02 08:22 and 08:39 UTC) got "To use Codex here, create an environment for this repo". The pinned rulebook is explicit that `builder: codex` is for a repo **with** a Codex environment and `builder: claude` where there is none (`.claude/skills/agent-team/team/CLOUD.md:19`, and setup step `:142`: "`builder: codex` once the Codex environment exists (else `builder: claude`)"). Merged as is, the rulebook line is a false fact, every story starts with two failing `@codex` build tasks, and the story's own Signal ("next story's code from Codex, no 'Codex failed twice' line") cannot be met. The PR body repeats the claim ("uses the Codex environment established on 2026-10-17"). · Fix, in this order: (1) Conny creates the tb-site environment in Codex settings → Environments (the Operatör line already exists); (2) the Builder shows it works with one `@codex` task on issue #23 (the plan attack again is fine) that gets a real answer, not the "create an environment" reply; (3) change the comment to the date of that verified run and correct the PR body. If the environment is not to be created now, the alternative that matches the rulebook is to keep `builder: claude` (with a comment naming the missing environment) and land only the v0.7.5 pin and the AGENTS.md wording, which is Conny's call on the merge card.

## Should fix
- none

## Nits
- N1 PR body, Acceptance criteria: "`git diff master --stat` contains only the submodule, `.team/team.md`, and `AGENTS.md`" — the head now also adds `.team/reviews/014-builder-codex.response.md` (team file, excluded from the site by `_config.yml`). Harmless; refresh the line when the body is corrected for M1.

## Evidence
| Acceptance criterion | Shown by (test, command + output, screenshot) | Result |
|---|---|---|
| Submodule pinned on the v0.7.5 merge commit; `team:` names v0.7.5 and the short sha | `git -C .claude/skills/agent-team log -1 --format=%H` → `93a678a6a4ea42623e30822e4c234229d1ebaa3a` ("Rulebook story. v0.7.5: … (#12)"); `.team/team.md:22` `team: … @ v0.7.5 (93a678a)` | pass |
| `builder: codex` with a comment naming CLOUD.md § Builder and the environment (2026-10-17); `models:` coder line | `.team/team.md:20` and `:9` have the text | text present, but the environment claim is false today → **M1** |
| AGENTS.md § Team settings **Builder** line (issue task, Codex code + fixes, Builder runs Test before commit incl. Playwright + link check on Codex's head, fails twice → Builder builds) | `AGENTS.md:42`, read against CLOUD.md v0.7.5 § Builder "With `builder: codex`" — consistent, adds the tb-site Playwright specifics | pass |
| "If you are Codex" no longer says the Builder is a Claude thread; builds on task, attacks in review incl. own PRs | `AGENTS.md:46` and new Code Review Rules bullet `AGENTS.md:58` | pass |
| `python3 -m html.parser index.html` exits 0; no site file in the diff | `python3 -m html.parser index.html` → exit 0; `git diff --stat origin/master HEAD` → only `.claude/skills/agent-team`, `.team/reviews/014-builder-codex.response.md`, `.team/team.md`, `AGENTS.md` | pass |

## Codex findings
- Plan attack (issue #23): failed twice with "create an environment for this repo"; no findings to rule on. The failure itself is the evidence behind M1.
- Codex round 1 on 4868333 (story fit): "Didn't find any major issues." No findings to rule on. The Builder's response file has no disputes.
- ce9f790 (response file only) changes no code and needs no new Codex round.

## What I checked
- tests run: `python3 -m html.parser index.html` (exit 0); `git diff --check` (clean); submodule sha; `grep -n "builder: codex" .team/team.md AGENTS.md` (team.md:20, AGENTS.md:42); `_config.yml` still excludes `.team`, `.claude`, `AGENTS.md` and is untouched. No screenshots: no site file changed. GitHub reports no checks on ce9f790.
- tried to break: read the whole diff (Codex-built PR, CLOUD.md § Judge 3) against CLOUD.md v0.7.5 § Who builds, § Builder and § Setup; checked the environment claim against issue #23. The AGENTS.md Builder line and the Codex section match v0.7.5; the only contradiction is the environment.
- scope vs story: rulebook-only, first line `Rulebook story.`; `merge:` and Human-merge paths unchanged as the story requires. This is a human-merge PR (rulebook story): after M1, approval goes to Conny on a card.

— Judge (Claude) on behalf of Conny Wadbro

## Round 2 — 2026-11-02

Head reviewed: a26314f. Verdict: **approve** (rulebook story: human merge on a card).

### Round 1 answers
- M1 — valid — fixed in c4c23de: `.team/team.md:20` is back to `builder: claude` with a comment naming the missing environment and issue #23, which matches CLOUD.md v0.7.5 `:19` and `:142`. `AGENTS.md` is identical to master (the PR's file list no longer has it). The PR body no longer claims an environment.
- N1 — fixed in the PR body (the diff list now names `.team/reviews/014-*`).

### Scope change
The Coordinator, as PO, narrowed the story to the v0.7.5 pin after M1 (response file, Judge round 1; PR body). I judge against the narrowed scope: story criteria 2–4 (the codex switch) are **dropped by the PO**, not unmet. The story file on main still describes the codex outcome and Signal; that is the Coordinator's file to update (N2).

### Evidence (narrowed scope)
| Acceptance criterion | Shown by | Result |
|---|---|---|
| Submodule on the v0.7.5 merge commit; `team:` names v0.7.5 and the short sha | `git -C .claude/skills/agent-team log -1 --format=%H` → `93a678a6a4ea42623e30822e4c234229d1ebaa3a`; `.team/team.md:22` `@ v0.7.5 (93a678a)` | pass |
| `builder: claude` kept, consistent with v0.7.5 for a repo without a Codex environment | `.team/team.md:20`; issue #23 bot replies 08:22, 08:39 and 08:43 UTC "create an environment for this repo" | pass |
| `index.html` unchanged and parses | `python3 -m html.parser index.html` → exit 0; PR files: `.claude/skills/agent-team`, `.team/team.md`, `.team/reviews/014-builder-codex{,.response}.md` only | pass |
| Criteria 2–4 (codex switch) | dropped by PO after M1 | n/a |

### Codex findings
- Codex round 2 on c4c23de (focus: builder: claude kept, AGENTS.md = master, body matches diff): "Didn't find any major issues." Nothing to rule on.
- a26314f changes only the response file; no new Codex round needed.

### What I checked
- `git diff --check` clean; GitHub reports `mergeable: clean`, no checks on a26314f. Nothing in `bin/` parses the `builder:` line, so the trailing `# …` comment is safe.
- The submodule moves 141623c → 93a678a (v0.7.4 + v0.7.5). Nothing in v0.7.5 requires a repo-side change for `builder: claude`; the Data changes section applies by default (N3).

### Nits
- N2 (Coordinator) `.team/backlog/014-builder-codex.md` on main: add a Log line for the narrowing and adjust Outcome, criteria and Signal to the pin, and open the codex switch as its own story once a `@codex` task runs in tb-site. Otherwise the Signal check after merge reads a codex outcome this PR never promised.
- N3 `AGENTS.md` § Team settings has no **Data changes** line (v0.7.4). CLOUD.md § Data changes says the general case holds when it is missing, and a static site has no production data, so this is optional; a later settings story can add "Data changes: none".

— Judge (Claude) on behalf of Conny Wadbro
