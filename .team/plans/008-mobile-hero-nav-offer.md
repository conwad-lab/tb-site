---
id: 008
verdict: plan
---

# Plan 008 — D4 + D5 + D7 — mobile hero, navigation and offer rows at 390 px

Story: `.team/backlog/008-mobile-hero-nav-offer.md`

## Approach
Two new `@media` blocks in the inline CSS of `index.html`, no markup, no script, no copy. Measured on master and with these exact rules injected (Chromium 1440×900 and 390×844, `networkidle` + 1 s, scrolled to bottom); the Coder's run must reproduce the numbers below.

D4 — `@media(max-width:480px){h1{font-size:calc((100vw - 40px) * 38 / 350);max-width:none}}`. 38 px at 390, scaled to the text column (40 px = the `.wrap` padding at this width) so the same four lines hold from 360 to 430 px. `max-width:none` lifts the `15ch` cap, which at 38 px would shrink the measure to ≈277 px. The `<br>` stays: hiding it fuses "AI —in one" because there is no space before the `<em>`. `text-wrap:balance` stays. Lines at 390: `Commercial excellence,` / `law and AI —` / `in one advisor, not` / `three consultancies.` — four lines, 149 px (was six, 282 px, "three" alone). At 480 it computes to 47.8 px and shows the five-line form that 481 px shows today; continuous.

D5 — stack. `@media(max-width:480px){.nav{flex-direction:column;align-items:flex-start;height:auto;padding-top:16px;padding-bottom:18px;gap:12px}}`. Mark on row one (226×34, one line), CTA on row two (159×43, one line, same padding as desktop), left-aligned under the mark, header rule below. Nav 74 → 123 px. Use `padding-top`/`padding-bottom`, not the `padding` shorthand: `.nav` is the same element as `.wrap`, and the shorthand wipes its horizontal padding (mark lands at x = 0). The one-row alternative (mark 18 px + CTA padding 12 px 16 px) fits at 390 with 11 px to spare but wraps again at 375 and 360, so it is not chosen. Nav links at 390 today: the four text links are `display:none` via the existing `@media(max-width:760px)` rule, only the CTA is visible; unchanged. DOM order unchanged, so Tab order (mark → CTA) is unchanged.

D7 — `@media(max-width:520px){.mrow{grid-template-columns:1fr;gap:6px}.mk{padding-top:0}}`. Label above description, full width (292 px at 390), hairline `border-top` rules untouched. Rows 235/213/145/123 → 168/145/123/123; `.offer-mech` 716 → 558; `.offer` 1187 → 1028 px. `.price`, `.cta-big`, the sample-PDF link and `#kontakt` are not in the changed rules and measure identically.

Page height at 390: 8077 → 7823. At 1440: 6676, every measured rect (h1, nav, mark, cta, offer, mrows, price, cta-big) identical to master. No overflow at either width. Copy strings changed: none. Price block, booking CTA, footer: untouched (D7 changes layout only inside `.offer-mech`).

## Files
- `index.html` — one `@media(max-width:480px)` block (h1 + `.nav`) and one `@media(max-width:520px)` block (`.mrow` + `.mk`); place them next to the rules they override (after line 47 and after `.mk`, line 153) or together at the end of the layout rules. Match the file's `@media(max-width:NNNpx)` spelling without spaces. Nothing else.
- `docs/screenshots/008-mobile-hero-nav-offer/` — `desktop.png`, `mobile.png` (full page, scrolled to bottom, as in PR #7), `390-hero.png` (clip 0,0,390,520 after scrolling back to top), `390-nav.png` (element shot of `header`), `390-offer.png` (element shot of `.offer`), for side-by-side with `docs/design-review-2026-10/390-{hero,nav,offer}.png`.

## Steps
1. Branch `feat/008-mobile-hero-nav-offer`. Add the two blocks.
2. Run the checks under Tests with a throwaway Playwright script (not committed); save the five PNGs.
3. PR body: before/after at 390 for h1 lines and height, nav height, mark/CTA line count, each `.mrow` height, `.offer-mech` and `.offer` height, page height; 1440 unchanged; screenshots linked by commit SHA; "no copy change".

## Tests
- `python3 -m html.parser index.html` exits 0; `git diff master --stat` shows `index.html` plus five PNGs.
- `grep -n '@media' index.html`: six on master, eight on the branch; `grep -c '@media(max-width:480px)'` → 1, `grep -c '@media(max-width:520px)'` → 1.
- 390×844: h1 computed `font-size` ≈ 38 px (37.99–38.01), `getBoundingClientRect().width` 350, height 149, and the four line strings above (line boxes via a per-character `Range`, grouped by `top`); `.nav` height 123; `.mark` 226×34 at x 20; `.cta` 159×43 at x 20, one line; the four `.nav-r a:not(.cta)` computed `display:none`; `.mrow` `gridTemplateColumns` `292px`, heights 168/145/123/123; `.offer` 1028; `.price` 292×43 and `.offer .cta-big` 181×49 same as master; page height 7823; `scrollWidth === innerWidth`; 0 `.r-fade` with opacity < 1, 7 `.revealed`.
- 1440×900: page height 6676; the same rects as master to the pixel (h1 1008×549 at 112 px, `.nav` 74, `.mrow` columns `110px 340px`, `.offer` 500).
- Spot-check 375×844 and 430×932: four h1 lines identical to 390, no overflow (robustness, not an AC).
- Link check as in review 007: every `http(s)` `href`, `og:image`, both band `<img src>` and the Cal.com URL return 200; the two `rel=preconnect` bare hosts excluded. `mondmodel.com` answers 403 to a bare `fetch` and 200 with a browser User-Agent; use curl with `-A`.

## Risks / watch out for
- `padding` shorthand on `.nav` (see D5). `max-width` left at `15ch` (see D4). Hiding the `<br>` (see D4). Any of these fails the line-count test.
- At 390 the hero headline (38 px) is now smaller than `.dark h2` (40 px). Accepted: the hero is the first screen, and 40 px would put "Commercial" and "excellence," on single-word lines, which the story forbids.
- `.mrow` `gap:6px` is the only new spacing value; `.mk` `padding-top:0` removes the 3 px that aligned the label with the first text line in the two-column form.
- The hero's `.r-fade` settle and the reveal script are untouched; the hero still reveals on load.
- Do not touch `.cta` padding, `--bronze`, `.cta-bronze`, section order, any copy, `CNAME`, hosts.

## Out of scope
- D6, D8 (story 009), D9. Desktop layout. The lede, eyebrow or any other hero element. Widths other than 390 beyond the spot-check.

## Suggestions for PO
- Review 007 N1 (a comment on the `.cta-bronze` pin) is still open; a one-line ride-along on a future CSS story.
- The 480 px hero breakpoint leaves 481–520 px at 48 px with the five-line form; if a tablet-portrait pass is ever wanted, that band is where to look.
