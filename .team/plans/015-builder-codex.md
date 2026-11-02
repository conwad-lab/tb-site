---
id: 015
verdict: plan
---

# Plan 015 — Codex builds tb-site stories (builder: codex)

Story: `.team/backlog/015-builder-codex.md`

## Approach
Rulebook-only change in two files, `.team/team.md` and `AGENTS.md`; no site file and no submodule change (the v0.7.5 pin landed in story 014, 93a678a). The Builder thread builds this story itself, because it changes the rule it runs under. Every edit is given below as old → new so the diff can be checked line by line. Replaces the builder parts of plan 014.

Touches: price block no, booking CTA no, footer no. No visible copy string changes.

## Files
- `.team/team.md`
  - line 9, old: `  coder: claude — Builder thread per story (team/CLOUD.md)`
    new: `  coder: codex — builds from a @codex task on the story's issue NNN: <story title>; the Claude Builder thread drives the rest (team/CLOUD.md § Builder)`
  - line 20, old: `builder: claude  # stays claude until a @codex task runs in tb-site: no Codex cloud environment on 2026-11-02 (issue #23); the switch is its own story`
    new: `builder: codex  # team/CLOUD.md § Builder; needs the tb-site Codex environment (working since 2026-11-02, issue #23). Codex fails twice → the Builder thread builds`
- `AGENTS.md` § Team settings — new bullet directly after **Where checks run in the cloud**:
  `- **Builder:** \`builder: codex\` per \`.claude/skills/agent-team/team/CLOUD.md\` § Builder. The Builder thread opens the issue \`NNN: <story title>\` and posts the \`@codex\` build task there; Codex writes the code and every fix (\`@codex fix Mn\` on the PR). The Builder thread drives the rest: it runs **Test before commit** on Codex's head before every review request and before asking for a Judge, including the Playwright screenshots at both widths and the link check, which Codex's environment may not run, and attaches the screenshots to the PR. Codex failing the same task twice (an error reply, no PR or diff within the hour, or a head that fails Test before commit) → the Builder thread builds that task and says so in the response file.`
- `AGENTS.md` § "If you are Codex" — first sentence, old:
  `You are the **attacker** in review (\`.claude/skills/agent-team/team/CLOUD.md\`): the Builder is a Claude thread and the verdict is the Judge's.`
  new:
  `You have two jobs here (\`.claude/skills/agent-team/team/CLOUD.md\`). When a \`@codex\` task on a story issue or a \`@codex fix\` comment asks you to build, you are the Coder. In review you are the **attacker**, also on a PR you built yourself: review it as if someone else wrote it. The Claude Builder thread drives each PR and the verdict is the Judge's.`
  The rest of the paragraph ("Follow **Code Review Rules** below. If a task or comment instead asks you to build, you are the Coder (…) Sign `— Coder (Codex) on behalf of Conny Wadbro`.") stays as is, so the build/review role selection and the hard rails are unchanged.
- `AGENTS.md` § Code Review Rules — one new bullet: `- When you review a PR you built yourself, review it as if someone else wrote it.`

## Steps
1. Branch `feat/015-builder-codex` from master.
2. Make the edits above exactly; `git diff master --stat` must list only `.team/team.md` and `AGENTS.md` (plus `.team/reviews/015-*` if a response file exists).
3. Run the full **Test before commit**: `python3 -m html.parser index.html`; Playwright full-page screenshots at 1440×900 and 390×844 after scrolling to the bottom; the link check on every non-`mailto:` `href` (blocked URLs listed as **not checked**). The site is unchanged, so the screenshots should match master's; attach them anyway (AGENTS.md requires it and the Judge reads them).
4. PR titled `015: Codex builds tb-site stories (builder: codex)`, body starting `Rulebook story.`, one line per acceptance criterion. For the first criterion link both https://github.com/conwad-lab/tb-site/issues/23#issuecomment-6588920658 (Codex's `ls` reply) and the plan attack on issue #26 (Codex ran commands in the tb-site environment).
5. `@codex review`.

## Tests
- `python3 -m html.parser index.html` exits 0; `git diff master -- index.html` is empty.
- `grep -n "builder: codex" .team/team.md AGENTS.md` hits both files; `grep -n "the Builder is a Claude thread" AGENTS.md` returns nothing.
- Playwright screenshots at both widths and the link check, as in Steps 3.

## Risks / watch out for
- Human merge: `AGENTS.md` and `.team/team.md` are rulebook; Conny approves on a merge card with the head sha.
- Do not touch `_config.yml` (still excludes team files) or the submodule.

## Out of scope
- Site content, `merge:`, Human-merge paths, the submodule pin.

## Suggestions for PO
- The first story after this one is the real test of `builder: codex`: pick a small copy change.

## Plan attack
Codex on issue #26 (2026-11-02 21:34Z), 4 M and 1 S:
- M1 (screenshots and link check skipped): changed in plan. Steps 3 runs the full Test before commit, including both Playwright widths and the link check, and attaches the screenshots.
- M2 (`models:` coder line too vague): changed in plan. Files gives the exact old → new line.
- M3 (Builder line misses failure paths): changed in plan. The Builder line names the issue and task, Codex writing code and fixes, the Builder thread driving and testing, and the twice-failed rule with CLOUD.md's three failure kinds.
- M4 (environment evidence is `ls` output, not a diff or PR): changed in story and plan. The criterion's purpose is proof that `@codex` tasks run in tb-site instead of answering "create an environment"; the `ls` reply and the plan attack on #26 show that. The PO reworded the criterion (story Log 2026-11-02), and the PR links both.
- S1 (no replacement text for "If you are Codex"): changed in plan. Files gives the full old → new first sentence and keeps the rest of the paragraph.
