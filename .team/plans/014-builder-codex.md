---
id: 014
verdict: plan
---

# Plan 014 — Codex builds tb-site stories (builder: codex, agent-team v0.7.5)

Story: `.team/backlog/_014-builder-codex.md` (rename to `014-builder-codex.md` when agent-team v0.7.5 is merged).

## Approach
Rulebook-only change, no site file. Re-pin the submodule from v0.7.3 (141623c) to the v0.7.5 merge commit, switch `builder:` and align `AGENTS.md`. This story itself is built by the Builder thread (it changes the rule it would run under), and gets a Codex plan attack first (v0.7.5 Flow: rulebook story).

Touches: price block no, booking CTA no, footer no. No visible copy string changes.

## Files
- `.claude/skills/agent-team` — submodule pin → v0.7.5 merge sha.
- `.team/team.md` — `builder: codex` + comment; `models:` coder line; `team:` line → `v0.7.5 (<short sha>)`.
- `AGENTS.md` — new **Builder** line after **Where checks run in the cloud**; rewrite the first sentence of "## If you are Codex"; one Code Review Rules bullet "When you review a PR you built yourself, review it as if someone else wrote it."
- `.team/backlog/_014-builder-codex.md` → `014-builder-codex.md` (the Builder renames when it starts; PO lane exception noted in the PR).

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
