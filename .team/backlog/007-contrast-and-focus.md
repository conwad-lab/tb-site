---
id: 007
title: D2 + D3 — more contrast margin for small mono text and a visible focus ring on dark
---

## Outcome
Every small mono label keeps WCAG AA with a comfortable margin, and a keyboard user sees a clear focus ring on the dark booking band, all within the existing bronze, grey and paper hues.

## Why
Design review D2 and D3 (Should), `docs/design-review-2026-10.md`. Measured today: bronze `#8A6430` on paper 4.88:1, muted `#6B6E72` on paper 4.70:1, `.book-sub #8F887C` on dark 4.66:1 — all pass 4.5:1 by less than 0.4. The bronze focus outline on the dark band is 3.08:1, passing the 3:1 non-text threshold by 0.08. Conny chose D2 and D3 (ORDER row 5) within the current identity.

## Acceptance criteria
- [ ] D2 — the values of `--muted`, `--bronze` and `.book-sub`'s colour are darkened or lightened within their own hue family so that every small mono pair in the report's contrast table reaches **at least 5.5:1** on paper `#F7F5F0`, on the tint `#FDFCF8` and on dark `#231F1A` respectively. Report's starting points: muted `#5B5E62`, bronze `#7A5729`, book-sub `#A39C8F`. The plan lists the final values with computed ratios for every pair in the table (`.eyebrow`, `.k`, `.who`, `.status`, `.src`, `.mk`, `.proof .t`, `.proof .metric a`, `.cta`, `.price span`, `.foot .mono`, `.book-sub`, hero `em`, `.lead-stmt`).
- [ ] D2 — the change is in the `:root` tokens and the one `.book-sub` rule, not per-element overrides, so bronze and muted stay one colour each across the page. `--bronze-deep`, `#B69463`, the dark-band colours and the CTA colours are unchanged.
- [ ] D3 — inside `.dark`, `a:focus-visible` uses the existing light bronze `#B69463` (5.77:1 on dark) with the same 2 px width and 3 px offset. Verified on the booking CTA and on the email link; a screenshot of each focused state is attached to the PR.
- [ ] A screenshot at 1440 of the hero, a stage card and the proof rows is compared side by side with the pre-change capture in `docs/design-review-2026-10/1440-full.png`; the page still reads as paper/bronze (Reviewer judges; no new hue).
- [ ] No copy, layout or typography change. Price block, booking CTA, footer text, `CNAME` untouched.
- [ ] Team settings test passes; screenshots at both widths attached.

## Out of scope
- D4–D8. D9 not taken.
- Any new palette colour, any change to fonts.

## Log
- 2026-10-12 PO: created from ORDER row 5 (D2 + D3 together: both are pure colour-value changes, one small PR). 5.5:1 target chosen by PO as "comfortable margin" since the report gives none; the Architect may pick higher.
- 2026-10-12 PO: un-parked after 006 merged.
