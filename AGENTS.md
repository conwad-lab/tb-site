# tb-site

This repo is worked on by an agent team. The team's rulebook, roles and templates are a pinned git submodule at `.claude/skills/agent-team/`.

**Read `.claude/skills/agent-team/team/TEAM.md` now.** It tells you which role you are, what you own, and how handoffs work. Who the human is and which models run which role: `.team/team.md`.

**Cloud mode is on** (`mode:` in `.team/team.md`): read `.team/CLOUD.md` right after `TEAM.md`. Where they disagree, `CLOUD.md` wins. `AGENTS.md`, `.team/team.md`, `.team/CLOUD.md` and `.team/roles/*` are the rulebook.

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
- **Second-reviewer paths:** none
- **Operator triggers:** every merged PR (it deploys to production — Conny checks the live page); any needed URL the brief says Conny must supply.
- **Coder extras:** keep `README.md` deploy notes current if hosting details change. Team files (`AGENTS.md`, `CLAUDE.md`, `.team/`, `docs/`, `README.md`) must stay excluded from the published site via `_config.yml`.
- **Docs to verify:** `README.md`

## If you are Codex, started by a task or an `@codex` comment

You are the **Coder** (`.claude/skills/agent-team/team/roles/coder.md`, with `.team/CLOUD.md` taking precedence). In short:

- The task or comment names a plan in `.team/plans/` and a story in `.team/backlog/`. Read both, this file and `.team/CLOUD.md`. Build exactly what the plan says; anything else you notice goes under **For PO** in the PR body.
- Run the **Test before commit** checks you can run in your environment. Say in the PR body which ran and which did not, and why. Never claim a check you did not run.
- PR against `master`, title `NNN: <story title>`, body: what, why, how you tested, deviations from the plan, **For PO**. Link the issue with `Closes #<n>`.
- On `@codex fix …`: answer every Must and Should fix named in the review file in `.team/reviews/NNN-slug.response.md` on the same branch — `M1: fixed in <sha>` or `M1: disputed — <reason>`. Never edit the review file. Push to the same branch.
- Never merge, never force-push, never touch the rulebook unless the story's first line is `Rulebook story.`, never cross a hard rail above.
- Sign PR bodies and commit messages `— Coder (Codex) on behalf of Conny Wadbro`.

## Code Review Rules

Codex's automatic PR review is **off** for this repo: the Reviewer is Claude (`.team/CLOUD.md`). If a Codex review appears anyway, it is input for the Reviewer, not a verdict; flag only P0/P1 and check the hard rails above.
