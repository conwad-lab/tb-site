# Papercuts

One line per step that failed or needed a workaround, appended by the Builder (or Codex as builder) in the same commit as the work. The Judge logs its own under `## Papercuts` in its review file instead. The weekly retro (`.claude/skills/agent-team/team/CLOUD.md` § Routines) reads them and proposes fixes under **Förslag**; only the routine changes the status.

Format: `YYYY-MM-DD | role | what failed | workaround | status`, where status is `open`, `proposed <date of the Förslag row>`, `fixed <PR link>` or `dropped <date>`.

## Lines

2026-11-14 | Builder (Claude) | link check: 7 external hrefs (mondmodel.com, the r2.dev sample PDF, transformationbeyond.se, dignami.com/en, /en/proof ×2) return curl 000 from the cloud session (network policy); the fonts.googleapis.com CSS URL returns 200 | listed as **not checked** in the PR; the live-page Operatör check after merge covers them | open

## Retro

<!-- The routine appends one line per week: YYYY-Www | Codex fixed <n> | Judge fixed <n> | failed @codex tasks <n> | escalations <n> | papercuts open <n> | cards <n> | human wait <h> h
     `cards` and `human wait` come from the card log on the PRs (CLOUD.md § Human approval 1); `human wait` is the hours inside that week of cards on Judge-approved PRs. -->
