---
id: 006
verdict: plan
---

# Plan 006 — C6 — drop "autonomous operations" from the Mondmodel row

Story: `.team/backlog/006-drop-autonomous-operations.md`

## Approach
One copy edit in `index.html`, line 347: delete the text `autonomous operations · ` from the Mondmodel `.metric` span. The `<a>` (href, target, rel, link text), the `.metric` class, the "In production" label and the sentence on line 346 all stay as they are. No CSS, no script, no other line.

Copy string changed (the only one):
- "9 destinations · 4 languages · autonomous operations · source: mondmodel.com ↗" → "9 destinations · 4 languages · source: mondmodel.com ↗"

Touches price block: no. Booking CTA: no. Footer: no. `CNAME`: no. New hosts: none.

Source for the two figures that remain: mondmodel.com sitemap, 9 destination sections and hreflang de/en/es/sv (verified in plan 002, link returns 200 today).

## Files
- `index.html` — line 347 only.
- `docs/screenshots/006-drop-autonomous-operations/` — `desktop.png`, `mobile.png` (scrolled to bottom, as in PR #5).

## Steps
1. Branch `feat/006-drop-autonomous-operations`. Make the one edit; keep the page's own `·` (U+00B7) between "languages" and the link.
2. Run the checks under Tests with a throwaway Playwright script (do not commit it); drop the two PNGs in the screenshots folder.
3. PR body: the grep counts, the two heights, the screenshots, and the old → new string above.

## Tests
- `python3 -m html.parser index.html` exits 0; `git diff master --stat` shows `index.html` (1 line) plus two PNGs.
- `grep -c "autonomous operations" index.html` → 0. `grep -c 'href="https://mondmodel.com" target="_blank" rel="noopener">source: mondmodel.com ↗' index.html` → 1. `grep -c "9 destinations · 4 languages · <a" index.html` → 1.
- Chromium 1440×900 and 390×844, `networkidle` + 1 s, scroll to bottom in ≈400 px steps, then: 0 `.r-fade` with computed opacity < 1, 7 `.revealed`, `scrollWidth === innerWidth`. Expected heights measured today on master with the edit applied in-page: **6676** at 1440 (the metric drops from two lines to one, so the page is 18 px shorter than master's 6694) and **8077** at 390 (unchanged; the metric still wraps to two lines there). Any other height difference means something else moved.
- Link check: every `http(s)` `href`, `og:image` and the Cal.com URL return 200 (the two `rel=preconnect` bare hosts 404 as in every earlier review; excluded).

## Risks / watch out for
- Delete the phrase and its trailing ` · ` together; leaving the separator gives "languages · · source".
- Do not touch line 346 ("AI-driven editorial platform in daily operation") or the "In production" label; story 009 (D8) owns that row's status line and source placement.
- Story 009 edits the same row later. Keep this diff to one line so the rebase there is trivial.

## Out of scope
- D8 (status line and source placement on the Mondmodel row), the "In production" label, any other row, any CSS.

## Suggestions for PO
- Line 346 still says "in daily operation" and the row label is "In production". Both are unsourced on mondmodel.com in the same way "autonomous operations" was. Worth deciding in story 009, where the row's status line is reworked.
