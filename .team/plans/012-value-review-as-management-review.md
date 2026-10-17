---
id: 012
verdict: plan
---

# Plan 012 — The AI Value Review as a management review

Story: `.team/backlog/012-value-review-as-management-review.md`

## Approach
Copy-only change in `index.html`: six visible strings change, one row is added inside the existing `.offer-mech` block using the existing `.mrow`/`.mk` markup (no CSS), and the JSON-LD description is updated. Nothing else. Baseline on master 2026-10-17: HTML parses.

Strings (old → new), lines on master `dafb1d4`:
1. L291 stage 01, visible: "The AI Value Review — a board-standard answer on where your AI operation stands and what to do next. Strategy, AI governance, regulatory gap analysis, project scoping." → "The AI Value Review — a management review: where your AI operation stands, who owns which decision, and what leadership should decide next. Strategy, AI governance, regulatory gap analysis, project scoping."
2. L318 `.offer-lede`, visible: "One question, answered to board standard: <b>where does your AI operation actually stand, and what should you do next?</b> Scoped to the six questions above — no implementation, no vendor theatre." → "A management review for your leadership team: <b>where does your AI operation actually stand, who owns which decision, and what should management decide next?</b> Scoped to the six questions above — no implementation, no vendor theatre."
3. L324 Week 1, visible: "Intake interview and an agentic-maturity assessment — where your automation stands today, measured by who actually uses what, not by what is licensed. Placed on a six-rung capability ladder." → "Interviews with the leadership team and an agentic-maturity assessment — where your automation stands today, measured by who actually uses what, not by what is licensed, and who owns each AI decision. Placed on a six-rung capability ladder."
4. L325 Week 2, visible: "Gap analysis and a decision memo — what to automate, what not to, in which order, and which processes and data foundations must change first for the investment to pay off." → "Gap analysis and a management decision memo — the decisions your leadership team needs to take: what to automate, what not to, in which order, and which processes and data foundations must change first for the investment to pay off."
5. L326 You receive, visible: "A board-readable memo where every claim carries a resolvable citation, sealed with a verification hash." → "A decision memo for the leadership team and the board, where every claim carries a resolvable citation, sealed with a verification hash."
6. New `.mrow` directly after "Method" (L327), visible: `<span class="mk">Then</span><span>Management's decisions are the starting point for Dignami Assurance — Understand · Rethink · Rebuild.</span>`
7. L427 JSON-LD `description` (not visible): "Fixed-scope two-week AI value review: agentic-maturity assessment, gap analysis, board-readable decision memo with resolvable citations." → "Fixed-scope two-week AI value review for the leadership team: agentic-maturity assessment, gap analysis, management decision memo with resolvable citations."

Price block: unchanged. Booking CTA texts and `href`s: unchanged. Footer: unchanged.

## Files
- `index.html` — the seven edits above, nothing else.

## Tests
- `python3 -m html.parser index.html`.
- `grep -c "board-standard\|board standard" index.html` → 0; `grep -c "management review" index.html` → 2; `grep -c "Understand · Rethink · Rebuild" index.html` → 2.
- `git diff --stat` shows only `index.html`; diff touches only the seven lines/one insertion above.
- Screenshots 1440×900 and 390×844 after scrolling; the new "Then" row must not overflow at 390 px. External `href` check, reporting any blocked URL as not checked.

## Risks / watch out for
- "Understand · Rethink · Rebuild" must use the same middle dots as stage 02.
- Keep `<b>` inside the lede as today; the question mark stays inside it.

## Out of scope
- ISO 42001, CSS, layout, nav, title/meta/OG, price, URLs.

## Suggestions for PO
- Meta/OG descriptions still say only "Fixed-price AI Value Review"; fine, but could mention "management review" in a later story.
