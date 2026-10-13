---
id: 009
title: D6 + D8 — hand-off as the outcome of the chain, one status-and-source pattern
---

## Outcome
The hand-off block reads as the result of the three-step chain rather than a fourth card, and every product claim (Platform stage card, Platform proof row, Mondmodel proof row) uses the same T&B pattern: a mono status line directly under the claim and one source/limit line directly under the status.

## Why
Design review D6 and D8 (Should), `docs/design-review-2026-10.md`, sections "Hand-off block" and "Evidence language", crops `390-stages.png`, `390-handoff.png`. Today the hand-off's `#FDFCF8` fill repeats the first stage card and its two sentences plus slogan link form a fourth text-heavy unit; the status and source lines sit in three different places on the three product claims. Dignami's proof page uses status + qualifier + adjacent evidence; T&B should borrow that grammar in its own mono register. Conny chose D6 and D8 (ORDER row 5) within the current identity. All Dignami wording below verified live 2026-10-12.

## Acceptance criteria
- [ ] D6 — the `.handoff` block keeps the bronze left rule but drops the `#FDFCF8` fill or otherwise visibly differs from `.stage.here`, and is tied to the chain (e.g. a bronze connector rule from the cards, per the report's sketch). Content in this order: label "Hand-off → Dignami" (mono, as today); one role sentence that keeps counsel's boundary — "Transformation & Beyond advises; Dignami builds and runs; your counsel gives legal advice." (dignami.com/en/about); one sentence "Review recommendations continue through Dignami Assurance."; one destination link to `https://www.dignami.com/en` whose text names the next step, "Explore Dignami Assurance ↗" (report's proposal). The slogan "Dignami — Your AI got faster. Your decisions didn't." may stay elsewhere on the page or go; the plan says which.
- [ ] D6 — at 390 px the block is visibly shorter than a stage card and reads as a conclusion, not a card (Reviewer judges from the screenshot against `390-handoff.png`).
- [ ] D8 — one shared pattern in three places (stage card "Platform — Dignami AOS", proof row "Platform", proof row "In production · Mondmodel"): line 1 existing `.k`/`.t` register; line 2 `.status` (10.5 px mono) with the status phrase; line 3 `.src`/`.metric` (11.5 px mono) with source and limit, placed directly below the status. The same CSS classes in all three; no per-place variants.
- [ ] D8 — AOS status line: `Built · In demo · Not in operation`. AOS source/limit line quotes Dignami's own qualifier, "some built, in demo, others not in operation; none operates with client records" (dignami.com/en, verified 2026-10-12), attributed to Dignami with a link to `https://www.dignami.com/en/proof#status-table` (anchor exists). The status phrase is descriptive, never a certification. Reviewer re-checks dignami.com/en and /en/proof on review day; if Dignami's published status changed, follow Dignami.
- [ ] D8 — Mondmodel: status line `In production · daily editorial operation`; source line `9 destinations · 4 languages · source: mondmodel.com ↗` (after story 006, "autonomous operations" is already gone and must not return). The sentence "AI-driven editorial platform in daily operation" may be shortened to avoid saying "daily operation" twice; the plan states the final wording.
- [ ] The plan lists every visible copy string that changes (old → new). Price block, booking CTA, Cal.com URL, footer, `CNAME` untouched. No new hosts, colours or fonts.
- [ ] `grep -c "Built · In demo · Not in operation" index.html` returns 2; `grep -c "status-table" index.html` returns at least 1; `grep -c "autonomous operations" index.html` returns 0.
- [ ] Team settings test passes; screenshots at both widths attached, plus 390 crops of the stage cards, hand-off and proof rows.

## Out of scope
- D9 (footer Dignami route) — not taken, Conny's decision.
- Any change to the three stage cards' body copy beyond the Platform card's status/source lines.
- Changes on dignami.com.

## Log
- 2026-10-12 PO: created from ORDER row 5. D6 and D8 grouped because both restructure the same section and the proof rows, with copy changes the Reviewer must trace to dignami.com; one PR. Last in the chain because it is the largest.
- 2026-10-13 PO: un-parked after 008 merged (PR #8).
