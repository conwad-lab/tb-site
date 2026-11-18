---
id: 022
title: "Upgrade agent-team to v0.8.9 and make Test before commit runnable by the Codex CLI poller"
---

Rulebook story.

## Outcome
tb-site runs agent-team v0.8.9 (230dee6), and the **Test before commit** line in `AGENTS.md` § Team settings is a command the Codex CLI poller on the host Mac can run as is, so a `builder: codex-cli` story in tb-site (023 first) can end `done` instead of `bounced`.

## Why
agent-team #30 (v0.8.9, merged 2026-11-18 as 230dee6) adds `builder: codex-cli`: a poller on Conny's MacBook (installed 2026-11-18) builds from a work order with Codex CLI on `gpt-6-astra` (`team/CODEX-CLI.md`). The pinned submodule is v0.8.7, so `team/CODEX-CLI.md` and the CLI work order in `team/templates/codex.md` are not in tb-site's rulebook yet.

The poller reads **Test before commit** from `AGENTS.md` on `master` and runs every backticked span on that line, joined with `&&` (`bin/codex-cli-poll` lines 335–339 at 230dee6). tb-site's line today has four spans: `python3 -m html.parser index.html`, `index.html`, `href` and `mailto:`. The poller's extraction (checked 2026-11-18) gives `python3 -m html.parser index.html && index.html && href && mailto:`, which fails on `index.html: command not found`, and bounce every run with "test red". `python3 -m html.parser index.html` also checks nothing (the module has no command line and exits 0 on any file). The real HTML check is `pr-check`'s (`.github/scripts/check_html.py` on every `*.html` outside `.claude/`).

## Signal
- `git ls-tree origin/master .claude/skills/agent-team` shows 230dee6 the day after merge.
- Story 023's first `codex-cli: build` run reports `Test before commit: green (…check_html.py…)` in its outcome comment (or red for a real HTML error), never "test red" from `href`.

## Acceptance criteria
- [ ] `.claude/skills/agent-team` points at 230dee6 (1d13b7c → 230dee6); the `.team/team.md` pin line reads `team: .claude/skills/agent-team @ v0.8.9 (230dee6; tag not pushed, pinned by commit)`.
- [ ] **Test before commit** in `AGENTS.md` has exactly one backticked span, the same command `pr-check` runs: `find . -name '*.html' -not -path './.claude/*' -not -path './.git/*' -print0 | xargs -0 python3 .github/scripts/check_html.py`. The Playwright screenshots and the link check stay on the line as prose without backticks (they are the Builder's and the Judge's, not the poller's). Shown by running the poller's own extraction (the `grep`/`sed` from `bin/codex-cli-poll` 335–339) on the new `AGENTS.md` and getting exactly that command, and by that command exiting 0 on the branch.
- [ ] No other backtick on that line; the rest of `AGENTS.md` keeps its meaning.
- [ ] **Builder:** in Team settings names `codex-cli` (`team/CODEX-CLI.md`): the Builder thread posts the CLI work order and adds the label `codex-cli`; it still runs the full **Test before commit** (screenshots at both widths, link check) on the poller's head before each review or Judge request. One sentence; `builder: codex` stays the fallback in `.team/team.md`.
- [ ] § "If you are Codex" gets the template's sentence: started by the host poller as Coder (`codex-cli`), follow the work order and end the last message with the `Hinder:` line it asks for.
- [ ] `.github/workflows/agent-team-merge.yml`, `_config.yml`, `pr-check.yml`, `check_html.py` and every site file unchanged; `git diff master --stat` lists only the submodule, `AGENTS.md`, `.team/team.md` and `.team/**`.

## Out of scope
- Any site change; the label `codex-cli` (story 023's Builder creates it if missing).
- Adding Playwright or a link checker as a script (a later story if the retro asks for it).
- The private repos' bumps (1 December).

## Log
- 2026-11-18 Coordinator's planner: written for the first `builder: codex-cli` run in tb-site (thread "Planera första Astra-bygget i tb-site"). Found that the poller cannot run tb-site's Test before commit line. Rulebook story: the Judge merges on agreement with Codex.

— Coordinator (Claude) on behalf of Conny
