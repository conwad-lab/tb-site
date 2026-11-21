# Papercuts

One line per step that failed or needed a workaround, appended by the Builder (or Codex as builder) in the same commit as the work. The Judge logs its own under `## Papercuts` in its review file instead. The weekly retro (`.claude/skills/agent-team/team/CLOUD.md` § Routines) reads them and proposes fixes under **Förslag**; only the routine changes the status.

Format: `YYYY-MM-DD | role | what failed | workaround | status`, where status is `open`, `proposed <date of the Förslag row>`, `fixed <PR link>` or `dropped <date>`.

## Lines

2026-11-14 | Builder (Claude) | link check: 7 external hrefs (mondmodel.com, the r2.dev sample PDF, transformationbeyond.se, dignami.com/en, /en/proof ×2) return curl 000 from the cloud session (network policy); the fonts.googleapis.com CSS URL returns 200 | listed as **not checked** in the PR; the live-page Operatör check after merge covers them | proposed 2026-11-16

## Retro

<!-- The routine appends one line per week: YYYY-Www | Codex fixed <n> | Judge fixed <n> | failed @codex tasks <n> | escalations <n> | papercuts open <n> | cards <n> | human wait <h> h
     `cards` and `human wait` come from the card log on the PRs (CLOUD.md § Human approval 1); `human wait` is the hours inside that week of cards on Judge-approved PRs. -->
2026-W46 | Codex fixed 1 | Judge fixed 3 | failed @codex tasks 5 | escalations 0 | papercuts open 0 | cards 2 | human wait ≥0.1 h (#34: kortloggen saknar kortets starttid)
2026-11-17 | builder | `gh pr view` fails (GraphQL 403 in cloud sessions) | REST `gh api repos/…/pulls/25` | open
2026-11-17 | builder | @codex build task on issue #49 got no reply or reaction in an hour (story 021) | built it myself | open
2026-11-18 | Builder | `git fetch origin <branch>` in the cloud's shallow single-branch clone did not create `origin/<branch>` | fetch with an explicit refspec `+refs/heads/<b>:refs/remotes/origin/<b>` | open
2026-11-20 | Builder | full-page Playwright shot at scroll 0 shows the figure without dots and labels (scroll-driven fade-in, `animation-timeline: view()`) | extra screenshot with the figure scrolled into view | open
2026-11-21 | builder | cloud clone: git fetch of a bare sha from the submodule remote fails; fetched main then checked out the pinned sha | fetch origin main | open
