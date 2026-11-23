---
id: 034
title: "Upgrade agent-team to v0.8.19 and let green rule changes merge on agreement"
---

Rulebook story.

## Outcome
tb-site runs agent-team v0.8.19 and its merge workflow's job `auto` knows the `rules` class: a later `Rulebook story.` PR that changes only `.team/` board and review files, `.team/team.md` version and model lines or ordinary Team settings lines merges by itself once the Judge's approving review is on the head, Codex found nothing blocking and every check is green. Changes to the walls (workflows, `.claude/`, `REVIEW.md`, the submodule outside a release bump, the guarded Team settings keys, Human-only paths, Guard paths) keep their card, and every card says why Conny is needed (`Varför du:`).

## Why
agent-team #40 (v0.8.19, story X, merged 2026-11-23 as 2bed8ec) on Conny's yes 2026-11-23 10:26Z: "jag ska inte behöva klicka manuellt på något varje gång som jag inte läser för att båda agenterna har varit överens." `team/SETUP.md` step 8 leaves the switch to each repo: copy the workflow again and set `- **Auto-merge:** release, rules` and `- **Guard paths:**`. This install is red (it changes the workflow and the guarded keys), so it takes one card.

The pin moves 495c6f8 (v0.8.15) → 2bed8ec (v0.8.19), so v0.8.16 (U, the watch and Codex receipts) and v0.8.17 (V, the routine writes work orders) come with it. v0.8.18 (W, model guard) is not on agent-team main yet.

tb-site only: job `merge` keeps its GitHub Pages step; job `auto` needs none, since a green rule change touches no published file.

## Signal
In the four weeks after merge, at least one green `Rulebook story.` PR in tb-site gets `Merged by agent-team-merge (rules, green)` from `github-actions[bot]` with no card, and no rule PR here is reverted for a fault Codex or the Monday sample should have caught (story X's Signal, read at the weekly retro).

## Acceptance criteria
- [ ] `.claude/skills/agent-team` points at 2bed8ec; the `.team/team.md` pin line reads `@ v0.8.19 (2bed8ec; tag not pushed, pinned by commit)`.
- [ ] `.github/workflows/agent-team-merge.yml`: job `auto` taken again from agent-team `assets/root` at 2bed8ec with only this repo's existing local changes kept (runs-on); triggers, permissions and job `merge` unchanged.
- [ ] `AGENTS.md` § Team settings: `- **Auto-merge:** release, rules` and a new `- **Guard paths:** none` line, each with its comment.
- [ ] The workflow parses as YAML and each job's script passes `bash -n`; agent-team's `tests/agent-team-merge.test.sh` passes at 2bed8ec (164/164).

## Out of scope
- Code, content and data PRs: their merge rules here are unchanged.
- Widening the green class (it lives in the workflow; widening it is red).
- The Monday sample and the pause PRs (Coordinator and routine, `CLOUD.md` § Routines [R13]).

## Log
- 2026-11-23 Builder thread "Slå på riskklassad automerge i sex repon", on the Coordinator's request after agent-team #40 merged. Story and plan ride in the install PR, as for v0.8.15 (one install PR per repo).
