---
id: 020
verdict: plan
---

# Plan 020 — Upgrade agent-team to v0.8.7

Story: `.team/backlog/020-agent-team-v0.8.7.md`

## Approach
Same shape as #38 without the workflow port: move the submodule pin and the pin line, nothing else. Touches: price block no, booking CTA no, footer no. No visible copy string changes.

## Estimate
size: S
risk: human-merge
files: 2
codex-rounds: 1
builder: claude — a submodule pin; Codex's environment has no git remote for the submodule
model: light — a pin bump with no rule text of tb-site's own (CLOUD.md [T2]: an ORDER row wins over the strongest default for a `Rulebook story.`)

## Files
- `.claude/skills/agent-team` — b25d713 → 1d13b7c.
- `.team/team.md` — the pin line (line 27 on master).

## Steps
1. `git submodule update --init .claude/skills/agent-team`, then `git -C .claude/skills/agent-team fetch origin main && git -C .claude/skills/agent-team checkout 1d13b7c`.
2. `git -C .claude/skills/agent-team diff --stat b25d713 1d13b7c`: require no path under `assets/root/`; otherwise stop and tell the Coordinator.
3. Edit the pin line in `.team/team.md` to `@ v0.8.7 (1d13b7c; tag not pushed, pinned by commit)`.
4. Test, PR with `Rulebook story.` as the first line of the body, `@codex review`.

## Tests
- `git ls-tree HEAD .claude/skills/agent-team` shows 1d13b7c.
- `grep -n 'agent-team @' .team/team.md` shows v0.8.7 and 1d13b7c.
- `python3 -m html.parser index.html` exits 0; `git diff master --stat` lists only the submodule, `.team/team.md` and `.team/**`.
- `bash .claude/skills/agent-team/tests/watch.test.sh` passes inside the submodule.
- No screenshots (no site change): say so in the PR.

## Risks / watch out for
- Master requires `pr-check` and up to date: rebase on master before asking the Judge if another story merges first.
- Do not port anything into `.github/workflows/agent-team-merge.yml`; v0.8.7 has no workflow change.

## Out of scope
- `AGENTS.md`, the merge workflow, `AGENT_ACCOUNT`.
