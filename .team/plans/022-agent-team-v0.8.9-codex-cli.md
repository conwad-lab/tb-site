---
id: 022
verdict: plan
---

# Plan 022 — agent-team v0.8.9 and a runnable Test before commit

Story: `.team/backlog/022-agent-team-v0.8.9-codex-cli.md`

## Approach
Same shape as 020 (pin bump) plus three small edits in `AGENTS.md` § Team settings and § If you are Codex. The Test before commit line becomes one command in backticks (the `pr-check` command) and prose for the screenshots and link check. Touches: price block no, booking CTA no, footer no. No visible copy string changes.

## Estimate
size: S
risk: human-merge
files: 3
codex-rounds: 1
builder: claude — a submodule pin and rulebook text; the poller's guard refuses submodule diffs unless listed, and this story is what makes the poller usable here
model: light — a pin bump and three short rule edits written out below (ORDER row wins over strongest for a `Rulebook story.`)

## Files
- `.claude/skills/agent-team` — 1d13b7c → 230dee6.
- `.team/team.md` — the pin line.
- `AGENTS.md` — Team settings **Test before commit** and **Builder:**; § If you are Codex, one sentence.

## Steps
1. `git submodule update --init .claude/skills/agent-team`, then in it `git fetch origin main && git checkout 230dee6`.
2. `git -C .claude/skills/agent-team diff --stat 1d13b7c 230dee6 -- assets/root/`: expect only `assets/root/AGENTS.md` (the Builder placeholder comment and the Codex section sentence, which this plan ports by hand). Anything under `assets/root/.github/` → stop and tell the Coordinator; do not touch the merge workflow.
3. Pin line in `.team/team.md`: `team: .claude/skills/agent-team @ v0.8.9 (230dee6; tag not pushed, pinned by commit)`.
4. `AGENTS.md`, replace the Test before commit bullet with exactly:
   `- **Test before commit:** `find . -name '*.html' -not -path './.claude/*' -not -path './.git/*' -print0 | xargs -0 python3 .github/scripts/check_html.py` (the same check as pr-check). Then, by the Builder and the Judge, not the Codex CLI poller: open each changed page with Playwright at 1440×900 and 390×844, take full-page screenshots after scrolling to the bottom (reveal animations), and check that every link returns 200 (mail links excluded).`
   (In the file the outer backticks above are not part of the line; the only backticks in the line are the two around the `find` command.)
5. `AGENTS.md` **Builder:** add after the first sentence: "With codex-cli (`team/CODEX-CLI.md`), the Builder thread posts the CLI work order on the story's issue and adds the label `codex-cli`; it runs the full Test before commit (screenshots, link check) on the poller's head before each review or Judge request, as for codex." Leave the rest of the bullet as is.
6. § If you are Codex: after the first sentence add "Started by the host poller as Coder (`codex-cli`), follow the work order and end your last message with the `Hinder:` line it asks for."
7. Tests, PR with `Rulebook story.` as the first body line, `@codex review`.

## Tests
- Poller extraction, run from the repo root against the branch's `AGENTS.md`:
  `grep -m1 -F '**Test before commit:**' AGENTS.md | sed -e 's/.*\*\*Test before commit:\*\*//' -e 's/<!--.*-->//g' | grep -o '`[^`]*`' | tr -d '`' | awk 'NF { printf "%s%s", (n++ ? " && " : ""), $0 }'`
  prints exactly the `find … check_html.py` command; paste the output in the PR.
- That command exits 0 on the branch (`bash -c "<output>"`).
- `git ls-tree HEAD .claude/skills/agent-team` shows 230dee6; `git diff master --stat` lists only the three files and `.team/**`.
- `bash .claude/skills/agent-team/tests/codex-cli.test.sh` inside the submodule (say if it cannot run in the cloud).
- No screenshots (no site change): say so in the PR.

## Risks / watch out for
- Master requires `pr-check` and up to date: rebase before asking for a Judge if 023 or anything else lands first (it cannot: 023 is parked on this story).
- A backtick anywhere else on the Test before commit line becomes part of the poller's command. Keep "pr-check", "mailto" and "href" out of backticks.

## Out of scope
- The `codex-cli` label, any site file, `.github/**`, `_config.yml`.
