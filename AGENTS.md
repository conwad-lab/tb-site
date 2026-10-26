# tb-site

This repo is worked on by an agent team. The team's rulebook, roles and templates are a pinned git submodule at `.claude/skills/agent-team/`.

**Read `.claude/skills/agent-team/team/TEAM.md` now.** It tells you which role you are, what you own, and how handoffs work. Who the human is and which models run which role: `.team/team.md`.

**Cloud mode is on** (`mode:` in `.team/team.md`): read `.claude/skills/agent-team/team/CLOUD.md` right after `TEAM.md`. Where they disagree, `CLOUD.md` wins. `AGENTS.md`, `.team/team.md`, `REVIEW.md` and `.team/roles/*` are the rulebook.

## Project conventions

- Stack: one static page, `index.html` (inline CSS + a small inline script), `assets/favicon.svg`, `CNAME`. No build step, no framework, no package.json. Band images, OG image and the sample PDF live on R2 (`pub-4ef719d99967461999898e674993d796.r2.dev/brand/tb/`) and are not in this repo.
- Hosting: GitHub Pages from `master`, custom domain transformationbeyond.se. **A merge to master is a production deploy.**
- Sister site: dignami.com (separate repo). T&B advises; Dignami builds and runs. Copy on this site must never claim more than dignami.com claims about Dignami.
- Copy language: English. Team files and briefs may be in Swedish.
- Current work: `.team/briefs/2026-10-site-refresh.md`.
- Run tests: see Team settings.
- Lint / format: none.
- Default branch: master

## Hard rails (no role reasons around these)

- No claim about the founder's credentials, clients, figures or product status without a source the Reviewer can open. The founder holds a bachelor's degree; the commercial-law studies at Lund are master's-level courses, **not** a master's degree.
- No legal advice on the page; no certifications that are not held.
- Do not change the price, the Cal.com booking URL or the contact address without an ORDER row saying so.
- Do not touch `CNAME`.
- Do not add third-party scripts, trackers or fonts from new hosts.

## Team settings

- **Test before commit:** `python3 -m html.parser index.html` must not error; open `index.html` with Playwright at 1440×900 and 390×844, take full-page screenshots after scrolling to the bottom (reveal animations), and check every `href` returns 200 (`mailto:` excluded).
- **Baseline:** the same screenshot + link check on `master` before planning.
- **CI-only checks:** none (Pages build only).
- **A plan must name:** every visible copy string that changes (old → new), and whether the change touches the price block, booking CTA or footer.
- **Review checks:** every factual claim on the page traced to a source or to the brief; compare Dignami-related wording against https://www.dignami.com/en/proof and /en/about; WCAG AA contrast for any colour that changes; screenshots at both widths attached to the PR.
- **Operator triggers:** every merged PR (it deploys to production — Conny checks the live page); any needed URL the brief says Conny must supply.
- **Coder extras:** keep `README.md` deploy notes current if hosting details change. Team files (`AGENTS.md`, `CLAUDE.md`, `.team/`, `docs/`, `README.md`) must stay excluded from the published site via `_config.yml`.
- **Docs to verify:** `README.md`
- **Adversarial paths:** none
- **Human-merge paths:** `CNAME`, `_config.yml`, and any diff that changes the price, the Cal.com booking URL, the contact address or a claim about the founder (the hard rails above).
- **Signal sources:** the live page (https://transformationbeyond.se/ — every `href` 200, screenshots at both widths), the GitHub Pages build for the latest merge, open Dependabot alerts.
- **Where checks run in the cloud:** `python3 -m html.parser` everywhere; Playwright screenshots and the link check by the Builder and the Judge (a URL the session's network blocks is listed as **not checked**, never as passed). A check the change needs that could not run anywhere becomes an Operatör line before merge.

## If you are Codex

You are the **attacker** in review (`.claude/skills/agent-team/team/CLOUD.md`): the Builder is a Claude thread and the verdict is the Judge's. Follow **Code Review Rules** below. If a task or comment instead asks you to build, you are the Coder (`roles/coder.md`, with `CLOUD.md` winning): build exactly the plan, PR titled `NNN: <story title>`, never merge, never force-push, never cross a hard rail. Sign `— Coder (Codex) on behalf of Conny Wadbro`.

## Code Review Rules

Codex's automatic PR review is **on** for this repo. You are the attacker in this team's review: try to prove the change wrong. Your findings go to the Builder, who answers each one, and to the Judge, who rules on them. You do not give the verdict.

- Number findings `M1…` (Must fix: correctness, a hard rail above, the rulebook, a missing check for a stated behavior), `S1…` (Should fix), `N1…` (nit), each with `file:line`, what, and why it matters. Keep P0/P1 labels too if you use them.
- Check the diff against the story in `.team/backlog/NNN-*.md`: an acceptance criterion the diff does not meet, or a change the story did not ask for, is a finding.
- Check every claim in the PR body against the diff, and every factual claim on the page against a source or `.team/briefs/2026-10-site-refresh.md`.
- Run the **Test before commit** commands if your environment can; say which ran and which did not. Never report a check as passed that you did not run.
- A request comment may name a focus ("security", "failure paths", "story fit"): stay on it.
- Flag any change to `AGENTS.md`, `.team/team.md`, `REVIEW.md` or `.team/roles/*` when the story's first line is not `Rulebook story.`
