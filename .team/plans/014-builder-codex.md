---
id: 014
verdict: plan
---

# Plan 014 — Pin agent-team v0.7.5

Story: `.team/backlog/014-builder-codex.md` (unparked 2026-11-02; v0.7.5 merge sha: 93a678a).

**Scope change 2026-11-02:** the story now covers only the re-pin to 93a678a and the `team:` line (Judge note N2 on PR #24). The `builder: codex` switch and the AGENTS.md edits below moved to story 015 (parked until an `@codex` task succeeds in tb-site); 015 reuses this plan's Files and Steps for those parts.

## Approach
Rulebook-only change, no site file. Re-pin the submodule from v0.7.3 (141623c) to the v0.7.5 merge commit, switch `builder:` and align `AGENTS.md`. This story itself is built by the Builder thread (it changes the rule it would run under), and gets a Codex plan attack first (v0.7.5 Flow: rulebook story).

Touches: price block no, booking CTA no, footer no. No visible copy string changes.

## Files
- `.claude/skills/agent-team` — submodule pin → v0.7.5 merge sha.
- `.team/team.md` — `builder: codex` + comment; `models:` coder line; `team:` line → `v0.7.5 (<short sha>)`.
- `AGENTS.md` — new **Builder** line after **Where checks run in the cloud**; rewrite the first sentence of "## If you are Codex"; one Code Review Rules bullet "When you review a PR you built yourself, review it as if someone else wrote it."


## Steps
1. Check that agent-team v0.7.5 is merged; read its `team/CLOUD.md` § Builder and use its words for the **Builder** line (do not paraphrase beyond the tb-site specifics).
2. `git -C .claude/skills/agent-team fetch origin main && git -C .claude/skills/agent-team checkout <v0.7.5 merge sha>`; stage the pin.
3. Edit `.team/team.md` and `AGENTS.md` as in Files. tb-site specific in the Builder line: Codex's environment may not run Playwright; the Builder thread runs the screenshots and the link check on Codex's head before asking for a Judge, and attaches them to the PR.
4. Test, PR with `Rulebook story.` as the first line of the body, `@codex review`.

## Tests
- `python3 -m html.parser index.html` exits 0.
- `git diff master --stat` lists only `.claude/skills/agent-team`, `.team/**` and `AGENTS.md`.
- `git -C .claude/skills/agent-team log -1 --format=%H` equals the v0.7.5 merge sha; `grep -n "builder: codex" .team/team.md AGENTS.md` hits both files.
- No screenshots needed (no site change): say so in the PR.

## Risks / watch out for
- `_config.yml` must still exclude team files; it is not touched.
- Human merge: `AGENTS.md`, `.team/team.md` and the submodule pin are rulebook; Conny approves on a card.

## Out of scope
- Site content, `merge:`, Human-merge paths.

## Suggestions for PO
- The first story after this one is the real test of `builder: codex` here: pick a small copy change.

## Plan attack
- 2026-11-02: the `@codex` plan attack on issue #23 failed twice with "create an environment for this repo". No findings; the build goes on with the plan as it stands (CLOUD.md v0.7.5 § Builder step 0). Codex review on the PR is unaffected (it does not need an environment). Operatör line added for the tb-site Codex environment.
