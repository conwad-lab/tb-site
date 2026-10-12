---
id: 006
title: C6 — drop "autonomous operations" from the Mondmodel row
parked-until: 005
---

## Outcome
The Mondmodel proof row reads "9 destinations · 4 languages · source: mondmodel.com ↗" and the phrase "autonomous operations" appears nowhere on the page.

## Why
Conny's decision (ORDER row 6, 2026-10-12): "autonomous operations" cannot be substantiated on mondmodel.com, which is the row's only source; the two figures can (Architect verified them in the site map, plan 002). Hard rail in `AGENTS.md`: no figure or claim without a source the Reviewer can open.

## Acceptance criteria
- [ ] `index.html` Mondmodel `.metric` span (line ~346) becomes `9 destinations · 4 languages · <a …>source: mondmodel.com ↗</a>`; the `href`, `target` and `rel` are unchanged.
- [ ] `grep -c "autonomous operations" index.html` returns 0.
- [ ] Nothing else on the page changes. Price block, booking CTA, footer, `CNAME` untouched.
- [ ] Team settings test passes (HTML parse, screenshots at both widths, all `href`s 200). Screenshots attached.

## Out of scope
- The Mondmodel row's status line and source placement (D8, story 009).
- Any change to the "In production" label or the sentence "AI-driven editorial platform in daily operation".

## Log
- 2026-10-12 PO: created from ORDER row 6. Chained after 005 and before 007 so the one-word change ships early and does not collide with story 009, which restructures the same row.
