---
id: 007
verdict: plan
---

# Plan 007 — D2 + D3 — more contrast margin for small mono text and a visible focus ring on dark

Story: `.team/backlog/007-contrast-margin-and-focus-ring.md`

## Approach
Four CSS edits in `index.html`, no markup, no script. D2: in `:root` set `--muted:#5B5E62` (was `#6B6E72`) and `--bronze:#7A5729` (was `#8A6430`); in `.book-sub` set `color:#A39C8F` (was `#8F887C`). These are the report's own values; same hue family (bronze H 35→34°, muted 214°, book-sub 38→39°), lightness only. D3: add `.dark a:focus-visible{outline-color:#B69463}` next to `.dark .eyebrow`; width and offset stay from the global rule. One pin: `.cta-bronze` uses `var(--bronze)` as its **background**, so set it to the literal `#8A6430` or the booking CTA darkens, which the story forbids. That is a background, not a text colour; bronze text stays one value page-wide.

D3 is not optional alongside D2: with the darker bronze the global focus ring on the dark band would fall to 2.51:1 (fails 3:1). Both land in one commit.

Measured today on master with these values injected (Chromium 1440×900, computed colours, effective solid backgrounds; the Coder's run must reproduce these):

| Pair | Before | After |
|---|---:|---:|
| bronze on paper `#F7F5F0`: `.eyebrow`, `.layer .k`, `.mk`, `.proof .t`, hero `em`, `.lead-stmt`, `.gap-stmt em` | 4.88 | **5.98** |
| bronze on tint `#FDFCF8`: `.stage.here .k`, `.stage.here .who`, `.handoff .k` | 5.18 | **6.35** |
| muted on paper: `.status`, `.src a`, `.proof .metric a`, `.price span`, `.foot .mono`, `.nav-r a`, `.proof-link`, `.hero-base`, non-here `.stage .k/.who/p` | 4.70 | **5.98** |
| muted on tint: `.stage.here p` | 4.99 | **6.35** |
| `.book-sub`, `.book-sub a` on dark `#231F1A` | 4.66 | **6.01** |
| `.cta` paper on ink (unchanged) | 15.07 | 15.07 |
| `.cta-bronze` white on `#8A6430` (pinned, unchanged) | 5.32 | 5.32 |
| `.dark .eyebrow` `#B69463` on dark (unchanged) | 5.77 | 5.77 |
| focus ring on dark (`#book-cta`, `.book-sub a`) | 3.08 | **5.77** |
| focus ring on paper (`.cta-big`, `.proof-link`) | 4.88 | 5.98 |

Copy strings changed: none. Price block: text unchanged, `.price span` colour darkens via the token. Booking CTA: background pinned, so unchanged; its focus ring changes (D3). Footer: text unchanged, colour darkens via the token. `CNAME`, hosts, Cal.com URL, `--bronze-deep`, `#B69463`, `::selection`, `.dark` colours: untouched.

## Files
- `index.html` — `:root` (line 20–21), `.book-sub` (line 159), `.cta-bronze` (line 121), one new rule after `.dark .eyebrow::after` (line 115). Nothing else.
- `docs/screenshots/007-contrast-margin-and-focus-ring/` — `desktop.png`, `mobile.png` (scrolled to bottom, as in PR #6), `focus-cta.png`, `focus-email.png` (element screenshot of `section.dark` at 1440 with the booking CTA / the email link focused via `page.focus`).

## Steps
1. Branch `feat/007-contrast-margin-and-focus-ring`. Make the four edits.
2. Run the checks under Tests with a throwaway Playwright script (do not commit it); drop the four PNGs in the screenshots folder.
3. PR body: the table above as measured on the branch, heights, counts, the four screenshots linked by commit SHA (review 006 N1), and "no copy change".

## Tests
- `python3 -m html.parser index.html` exits 0; `git diff master --stat` shows `index.html` (4 lines changed/added) plus four PNGs.
- `grep -c '#8A6430' index.html` → 1 (the `.cta-bronze` pin only); `grep -c '#7A5729' index.html` → 1; `grep -c '#5B5E62'` → 1; `grep -c '#A39C8F'` → 1; `grep -c '#6B6E72'` → 0; `grep -c '#8F887C'` → 0.
- Chromium 1440×900 and 390×844, `networkidle` + 1 s, scroll to bottom in ≈400 px steps: 0 `.r-fade` with opacity < 1, 7 `.revealed`, `scrollWidth === innerWidth`, heights **6676** / **8077** (today's master; a colour change moves nothing).
- Computed-style contrast at 1440 for every selector in the table (WCAG 2.1 relative luminance, foreground vs nearest non-transparent ancestor background): every value ≥ 5.5 and equal to the After column to two decimals. `getComputedStyle(document.querySelector('.cta-bronze')).backgroundColor` → `rgb(138, 100, 48)`.
- Focus: `page.focus('#book-cta')` then `page.focus('.book-sub a')`: `outlineColor` `rgb(182, 148, 99)`, `outlineWidth` `2px`, `outlineOffset` `3px`. `page.focus('.cta-big')`: `rgb(122, 87, 41)`.
- Link check: every `http(s)` `href`, `og:image`, both band `<img src>` and the Cal.com URL return 200 (the two `rel=preconnect` bare hosts excluded, as in every earlier review).

## Risks / watch out for
- Forgetting the `.cta-bronze` pin darkens the most prominent bronze surface on the page and breaks AC2's "CTA colours unchanged". Hover (`--bronze-deep`) is unaffected.
- Shipping D2 without D3 leaves the focus ring on dark at 2.51:1, a new AA failure where there was none.
- Decorative uses of `--bronze` darken with the token: `.handoff` 3 px left edge, `.proof-link` and `.handoff a` underlines, `.qs-grid span::before` ticks, the `&` in `.mark span` and `.amp-dev.own`, and the 1 px `.r-rule-top` section rules (on the dark band that rule goes from 3.08 to 2.51; it is decorative, not a control boundary, so no override). Expected; say so in the PR so the Reviewer's side-by-side is not a surprise.
- Do not touch `--bronze-deep`, `#B69463`, `#4A4238`, `#FDFCF8`, `--dark`, `--dark-ink` or `::selection`.
- `docs/design-review-2026-10.md` is not edited; its contrast table documents the pre-change page by design.

## Out of scope
- D4–D8, D9, any new hue, fonts, layout, copy, the report itself.

## Suggestions for PO
- After this story, `.cta-bronze` (white on `#8A6430`, 5.32) is the thinnest text pair left. Using the new bronze there would give 6.52 but changes the CTA's look; a decision for Conny if ever wanted.
- The report's contrast table is now historical. A one-line "superseded by 007" pointer at its top would stop a future reader re-measuring; not needed for this story.
- `docs/screenshots/` housekeeping row from plan 004 still stands.
