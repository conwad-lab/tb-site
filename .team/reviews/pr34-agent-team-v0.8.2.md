---
id: pr34
verdict: approve
---

# Review pr34 — Rulebook story. Upgrade agent-team to v0.8.2

PR: #34 · 2026-11-14 · reviewed head `2b9f386a3e96956e9b5fa911f19e4b94da5c78b4`

Rulebook story outside the story flow (no backlog file or plan, like #30). Judged against `.claude/skills/agent-team/team/CLOUD.md` at the new pin 58fb481 and the assets there.

## Must fix
- none

## Should fix
- none

## Nits
- N1 `AGENTS.md:47` — Nit: Team settings has no `**Auto-queue:**` line, which `assets/root/AGENTS.md:42` carries (`none`) and CLOUD.md [R1] reads by name. Absent reads as none, and the gap predates this PR (the v0.7.6 template had it too), so it does not block. Add `- **Auto-queue:** none` in the next board or rulebook change.
- N2 PR body — Nit: the `.team/reviews/pr34-agent-team-v0.8.2.response.md` table row sits after the "Not changed" list, outside the table, so it renders as a stray line.
- N3 `.team/reviews/pr34-agent-team-v0.8.2.response.md:13` — Nit: Outcome says "Rounds: see the PR thread"; the count is two (e3a62aa, 2b9f386).

## Evidence
| Acceptance criterion (from the PR body) | Shown by | Result |
|---|---|---|
| Submodule pinned 7dd938e → 58fb481 (v0.8.2), a commit on agent-team `main` | `git ls-tree HEAD .claude/skills/agent-team` = 58fb481539b6…; `git branch -r --contains 58fb481` in agent-team = `origin/main` | pass |
| `.team/team.md` matches `assets/team/team.md` at 58fb481 for cloud keys (`builder` as fallback, `runner`, `agent-account`, pin line) | line-by-line compare with the asset | pass |
| `AGENTS.md` cloud hard rail and Team settings (`Data changes`, `Stories in flight`, `Human-only paths`, `.claude/settings.json` on Human-merge paths, Builder line per [T2]) | diff vs `assets/root/AGENTS.md:20,35-42` | pass (see N1) |
| `AGENTS.md` § Papercuts copied from the template | identical to `assets/root/AGENTS.md` § Papercuts | pass |
| `.team/PAPERCUTS.md` from `assets/team/PAPERCUTS.md` plus one line | `diff` = only the added line | pass |
| `.claude/settings.json` = deny list asset | `diff assets/root/.claude/settings.json .claude/settings.json` empty; parses as JSON | pass |
| Merge workflow needs no change | `diff` asset vs tb-site copy: tb-site only adds `pages: write`, the board-path check and the Pages step; nothing in the asset is missing | pass |
| C1: CLOUD.md not longer | `wc -w`: 4 357 at 7dd938e, 3 488 at 58fb481 | pass |
| Site untouched | `git diff --stat origin/master..HEAD -- index.html assets _config.yml CNAME` empty; `_config.yml` excludes `.team` and `.claude` | pass |
| Test before commit | `python3 -m html.parser index.html` exit 0; Playwright full-page screenshots after scrolling at 1440×900 and 390×844, 0 broken `#` anchors at both; `curl -L` on external hrefs: fonts CSS 200, the 6 unique site URLs 000 (blocked by the session network) → **not checked**, same as the Builder's papercut | pass, links not checked |
| Required checks | no check runs or statuses on the head; `rules/branches/master` = `[]` (no ruleset, so none required) | n/a |
| Sync gate | `git merge-base --is-ancestor origin/master 2b9f386` true (master e194877) | pass |

## Codex findings
- Round 1 (e3a62aa) M1 `.team/PAPERCUTS.md` — blocked link check not logged as a papercut: valid — fixed in ee3a126.
- Round 2 (2b9f386): finished, "Didn't find any major issues"; summary state `completed`, no findings. No disputes.

## What I checked
- tests run: as in Evidence.
- tried to break: whether anything v0.7.7–v0.8.2 asks of a product repo is missing (Data changes, Stories in flight, Human-only paths, Papercuts, deny list, runner/agent-account keys, merge workflow); whether `.claude/settings.json` deny rules could block the Judge's or Builder's normal pushes (they match only `main`/`master`, force and mirror); whether the omitted `Runner offline after` matters (tb-site is public, `runner: github`, never mini).
- scope vs story: only rulebook files, the pin, the papercut log and the response file.
- Remove: nothing, because this PR only applies the rulebook in a product repo; the cut itself landed upstream (CLOUD.md 4 357 → 3 488 words).
- For the Coordinator: tb-site has no main ruleset (§ Walls W1), already flagged in the PR body; it needs an Operatör line. #31 (v0.7.7) is superseded by this PR and should be closed after merge.

## Papercuts
2026-11-14 | reviewer | external link check: 6 site URLs return curl 000 from the cloud session | listed as not checked; the live-page Operatör check covers them | open

— Judge (Claude) on behalf of Conny

## Re-review 2026-11-14 (head b2a46e3)

verdict stays **approve**, with one exception for the human (CLOUD.md § Human approval H1): no finished Codex review on the last commit outside `.team/reviews/**` (3c678bb). Both requests (09:24Z, retry 10:25Z) hit the Codex usage limit; the summary state is `failed` on 3c678bb. So this PR does not merge on agreement (J10c); it needs a card.

What changed since 52b2c4c, all checked:
- `bd8b7c3` merges master (14acd27, #35): the sync gate now holds (`git merge-base --is-ancestor origin/master b2a46e3` true). The merge brings only #35's own files; `git diff --stat origin/master..b2a46e3` lists the same seven PR files as before plus the two review files.
- `3c678bb` pins agent-team 58fb481 → 6e34726 (v0.8.3, on agent-team `main`) and updates the pin line in `.team/team.md`. 58fb481..6e34726 changes only the merge workflow asset (the #35 decode fix), its test and the project-instructions version line. `team/CLOUD.md` is unchanged (3 488 words), so C1 holds. tb-site's workflow still matches the v0.8.3 asset plus its own board-path check and Pages step; `.claude/settings.json` still equals the asset.
- `b2a46e3` logs the failed Codex round in the response file (B7).
- Test before commit: `python3 -m html.parser index.html` exit 0; no site file changed (`index.html`, `assets/`, `_config.yml`, `CNAME` empty in the diff), so the screenshots and anchor check from the first round stand. No check runs on the head. `master` now has a ruleset (PR only, squash, no deletion, no force-push; no required checks), so the "no main ruleset" note in round 1 is out of date.

Nits added:
- N4 PR title and body — Nit: they still say v0.8.2 and "7dd938e → 58fb481"; the head pins v0.8.3 (6e34726). Update before the card goes out so the card describes what merges.

## Papercuts (re-review)
2026-11-14 | reviewer | Codex usage limit: no review possible on 3c678bb | exception to the human on a card (H1) | open

— Judge (Claude) on behalf of Conny
