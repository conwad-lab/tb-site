# Cloud mode

Test mode until 2026-11-03. `.team/team.md` says `mode: cloud` while it applies. Part of the rulebook.

The team runs as cloud sessions instead of four local clones. `$TEAM/TEAM.md` and the role files still hold — lanes, one story = one plan = one PR, signing, hard rails, the rulebook rule — **except where this file says otherwise**. `bin/wait-for`, `bin/po-wait` and `bin/status` are not used.

## Who runs what

| Role | Runs as | Writes | Never |
|---|---|---|---|
| PO + Architect | **Coordinator**: one Claude cloud session (claude.ai/code; later the Projects coordinator) | `.team/backlog/`, `.team/ORDER.md`, `.team/plans/` on master; the handoff issue and its `@codex` comment | code, reviews |
| Coder | **Codex** in the cloud, started by an `@codex` comment | code + tests on its own branch, the PR, `.team/reviews/NNN-slug.response.md` | the rulebook, scope, merging |
| Reviewer | **Reviewer**: a Claude cloud session per PR, not the Coordinator's session | `.team/reviews/NNN-slug.md` on the PR branch, PR comments, `@codex fix` comments | code |
| Human | Conny | ORDER rows, the rulebook, merging | — |

The Reviewer is a separate session so it reads the PR without the planning context — same model family as the Architect, so independence comes from the session, not the vendor. Every GitHub comment from a Claude session is posted under the human's account; sign it per `$TEAM/TEAM.md` (`— Reviewer (Claude) on behalf of Conny Wadbro`).

## Flow

```
ORDER row → story + plan (master) → issue + @codex → Codex PR → review → @codex fix → … → approve → human merges
```

1. **Coordinator, as PO:** writes `.team/backlog/NNN-slug.md`, ticks the ORDER row. As Architect: reads the code, runs the **Baseline**, writes `.team/plans/NNN-slug.md`. Commits both to master (`team(po): …`, `team(architect): …`) and pushes. Team files are excluded from the site, so this push changes nothing live.
2. **Coordinator, handoff:** opens an issue titled `NNN: <story title>` with links to the story and the plan, then starts **one** Codex cloud task in the environment `tb-site` (Codex → Moln → tb-site; through the human's browser, or the human pastes it) with exactly:

   ```
   Implement .team/plans/NNN-slug.md for story .team/backlog/NNN-slug.md in conwad-lab/tb-site.
   Read AGENTS.md first. Open a PR against master titled "NNN: <story title>" whose body says "Closes #<issue>". Do not merge.
   ```
   Not an `@codex` comment: as of 2026-10-17 a non-review `@codex` comment gets "To use Codex here, create an environment for this repo" even though the environment exists (known Codex bug, issue #12). Smoke test via a direct task: PR #13, correct on the first try. Switch back to the comment when the bug is fixed. The Coordinator's part ends here. It does not watch the PR.
3. **Codex** implements, runs the checks it can run (see Checks), opens the PR.
4. **Reviewer:** a Claude cloud session is started on the PR (by the human, or by the Projects coordinator once it exists). It checks out the PR branch, reads story and plan, reads the whole diff, runs every check it can, tries to break it — per `$TEAM/roles/reviewer.md` steps 1–3 and **Review checks** in Team settings. It writes `.team/reviews/NNN-slug.md` from `$TEAM/templates/review.md`, commits it to the PR branch (`team(reviewer): review NNN`), pushes, and posts the file as a PR comment.
5. **Request-changes:** the Reviewer posts **one** more comment, exactly (as of 2026-10-17 it hits the same bug as step 2, so the same text goes into a direct Codex task naming the PR branch and saying "push to this branch, do not open a new PR" — tested on PR #13, worked first try):

   ```
   @codex fix M1, M2, S1 from .team/reviews/NNN-slug.md on this branch.
   Answer every Must and Should fix in .team/reviews/NNN-slug.response.md (one line each: "fixed in <sha>" or "disputed — <reason>"). Do not edit the review file. Do not merge.
   ```
   Codex pushes. The Reviewer re-reviews when the push lands (the session watches the PR; if it does not wake, the human says "re-review" in it). On re-review, append a dated section and update the verdict, as in v0.6.
6. **Approve:** the Reviewer stops watching the PR and says so in its last comment. The human merges (see Merge).
7. **Escalate:** a Must fix still disputed after the third round → `verdict: escalate` with `## Escalation`. The Reviewer stops watching. The Coordinator writes the Operatör line `(eskalerad NNN)` next time it runs.

## Review protocol (unchanged in substance from v0.6)

- Findings numbered `M1…`, `S1…`, `N1…`; each with `file:line`, what, why, suggested fix.
- `verdict:` in the review file on the PR branch is the decision. `approve` only when no Must fix is open — none new, none unanswered, none still disputed.
- Codex answers every M and S in the response file, never in the review file. A point without an answer stays open. A disputed point is either accepted in one line or kept with a one-sentence reply.
- Must fix includes: a claim in the PR body the diff does not support; a rulebook change without `Rulebook story.`; a check from Team settings that did not run and is not covered by the human.
- Codex's own GitHub review comments, if any appear, are input to the Reviewer, never a verdict.

## Checks in the cloud

Team settings' **Test before commit** has three parts. Where each runs:

| Check | Codex | Reviewer |
|---|---|---|
| `python3 -m html.parser index.html` | runs it | runs it |
| Playwright screenshots 1440×900 and 390×844 | runs it if its environment has Playwright; otherwise says so in the PR body | runs it, attaches the screenshots to the review comment |
| every `href` returns 200 | only if its environment has network | runs it; a URL the session's network blocks is listed as **not checked** |

A check that did not run is reported as not run, never as passed. If a check that the change needs could not run anywhere, the review says so and the human checks it before merging (it becomes an Operatör line).

## Status

Read off GitHub, keyed on the `NNN:` in the issue and PR titles:

| If | then | whose turn |
|---|---|---|
| story, no plan | ready | Coordinator |
| plan, no issue / Codex task | planned | Coordinator (handoff) |
| issue, no PR | in-progress | Codex |
| PR, no review file, or commits newer than it | in-review | Reviewer |
| review says `request-changes` and is newer than the last commit | changes-requested | Codex (after the `@codex fix` comment) |
| `escalate` | escalated | human, via Operatör |
| `approve` | approved | human merges |
| PR merged | done | — |

## Merge

During the test the human merges every PR, whatever `merge:` says: cloud verdicts are what is being tested. Merging to master deploys to production (Team settings).

## Quota

- One Codex task (or `@codex` comment) per handoff and one per review round. No re-pinging.
- Coordinator runs on a smaller model or lower effort; planning a story is not where the budget should go.
- Reviewer sessions stop watching the PR after `approve` or `escalate`.
- No polling loops in any session.

## Measured during the test (until 2026-11-03)

1. Does Codex start on an `@codex` comment posted from a Claude session? **No (2026-10-17):** Codex reads it but answers with the missing-environment bug. A direct task works (PR #13). `@codex fix` on a PR: same bug; a direct task on the PR branch works (PR #13, commit cb5b2e9).
2. Does the loop code → review → fix converge?
3. Does the Claude review find real faults?
4. Usage: Claude quota, Codex quota, GitHub Actions minutes.
