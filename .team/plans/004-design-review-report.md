---
id: 004
verdict: plan
---

# Plan 004 — Design review report with screenshots (no code change)

Story: `.team/backlog/004-design-review-report.md`

## Approach
Deliverable is a report, not code: `docs/design-review-2026-10.md` plus PNGs in `docs/design-review-2026-10/`, reviewed against master `a2363fc` (page content = `0015908`). One Playwright script (kept outside the repo or under the screenshot folder as `capture.mjs`, your call) produces every screenshot and every measured value; the report quotes those values. The Architect already ran the baseline today, so the expected answers below are known — your job is to measure them again, attach the evidence, and write the findings and proposals. Where my numbers and yours differ, yours win; say so in the report.

Copy strings changed: none. Price block, booking CTA, footer: untouched. `index.html` must be byte-identical to master in the PR.

## Files
- `docs/design-review-2026-10.md` — the report (structure below).
- `docs/design-review-2026-10/*.png` — `1440-full`, `390-full` (scrolled), `1440-nojs`, `390-nojs`, `1440-reduced-motion`, `390-reduced-motion`, `1440-noscroll`, `390-noscroll` (full-page, no scrolling), `focus-cta.png`, and crops for the mobile findings (`390-hero.png`, `390-nav.png`, `390-stages.png`, `390-handoff.png`, `390-offer.png`, `390-footer.png`). Chromium, `deviceScaleFactor:1` (keeps each full-page PNG near 1 MB), crops via `clip`.
- Nothing else. `docs/screenshots/` stays as it is.

## Report structure (in this order)
1. Header: commit, date, viewports, Playwright version (`1.58.2` is the global install at `/Users/connywadbro/.nvm/versions/node/v22.21.1/lib/node_modules/playwright`), contrast method (WCAG 2.1 relative-luminance formula in your script; read colours with `getComputedStyle` so the table shows rendered values, not just CSS), the three lenses from the brief.
2. Findings D1… Must first, each: severity, location (`selector` + line), evidence (file or value), proposal.
3. Topic sections: Contrast table · Scroll-reveal · Mobile 390 · Focus/keyboard · Evidence language · Hand-off block · Sister-site interplay.
4. Closing table: ID · severity · one line.

## What to measure, and what I expect
- **Contrast.** Pairs: `--ink`, `--body`, `--muted`, `--bronze` on `--paper` and on `#FDFCF8`; `.book-sub #8F887C` on `--dark #231F1A` (it sits in the dark section — the story's list does not say so); `--paper` on `--ink` (`.cta`, `.cta-big`); `#fff` on `--bronze` (`.cta-bronze`) and on `--bronze-deep` (hover); `#B69463` and `--dark-ink` on `--dark`; `--muted` at 14 px (`.nav-r a`, `.proof-link`), 13.5 px (`.hero-base`, `.stage p`), 13 px (`footer`); every 10.5–13 px mono string the story lists. Baseline today: bronze 4.88, muted 4.70, body 9.87, ink 15.07 on paper; 5.18 / 4.99 / 10.47 / 15.99 on `#FDFCF8`; book-sub 4.66 on dark; paper on ink 15.07; white on bronze 5.32; `#B69463` on dark 5.77. **Everything passes AA.** Do not invent a failure; report the margins (bronze, muted, book-sub are within 0.4 of the limit at 10.5–11 px tracked mono) as one Should finding at most, with same-hue candidates if you propose any (e.g. muted `#5B5E62` 5.98, bronze `#7A5729` 5.98, book-sub `#A39C8F` 6.01).
- **Scroll-reveal.** 25 `.r-fade`, 6 `.r-rule-top`, 7 sections get `.reveal`. Expected: no JS → all visible (the hidden state exists only under a JS-added class); reduced motion → all visible (script returns on the first line); crawler → content in HTML, `og:*` and `twitter:card` present, `og:image` on R2 returns 200; **full-page screenshot without scrolling → 19 of 25 `.r-fade` at `opacity:0`** (Playwright's full-page capture does not fire IntersectionObserver). That last one is a Must per the story; it affects link-preview and screenshot bots, not readers. Propose the fix in words (e.g. keep content visible by default and reveal everything on a timer fallback after load, or widen `rootMargin` so the observer fires for the whole document).
- **Mobile 390.** From the baseline: h1 renders at 48 px in 6 lines with the forced `<br>` after "AI —" (judge the rag and the orphan); nav mark wraps to two lines next to the CTA (`.mark` 205 px + `.cta` in a 350 px row); `.mrow` grid gives the text column 164 px (`110px 164px`); stage cards and hand-off stack full width; `.foot` wraps to three stacked lines. One crop per finding.
- **Focus.** Tab through in order; log `activeElement` and its outline at each stop; crop `.cta-big` focused for `focus-cta.png`. Ring is `2px solid --bronze`, offset 3 px, so it lands on the surrounding background: 4.88:1 on paper, **3.08:1 on `--dark`** around `.cta-bronze` and the mailto link — passes 3:1 by 0.08; expect a Should finding proposing an existing light colour (`#B69463` or `--dark-ink`) for the ring inside `.dark`. No `<button>` on the page; `#book-cta` has `target=_blank` only after JS.
- **Evidence language.** Compare with dignami.com/en/proof, /en and /en/about (fetched today): Dignami uses a status word plus qualifier ("In place", "In use on our own analyses · not yet in a client engagement", "Unproven", "Built and tested", "Synthetic test", "scheduled", "Available today"), a "Shown / Not yet shown" pair, claim-support classes ("verified · approved memory", "plausible", "unsupported"), numbered "EXHIBIT n" sheets, and amber dashes for missing artefacts. Borrow the status-plus-qualifier grammar and the "source" line placement; do not borrow the exhibit sheets, the amber, or the petrol palette. Sketch (ASCII) one T&B status line used identically on the Platform card, the Platform row and the Mondmodel row — label register (`.status` 10.5 px mono uppercase) above, source line (`.src`/`.metric` 11.5 px mono sentence) below.
- **Hand-off block** (`.handoff`, line 294): critique hierarchy vs the three cards (same tint as `.stage.here`, 3 px bronze left border, 46 em cap), the two sentences plus slogan link, and how it mirrors Dignami's footer "Advise → Transformation & Beyond ↗". Proposal with a sketch.
- **Sister-site interplay.** ≤ 3 proposals; none touches palette, fonts, logo or dignami.com. Note the gap the Reviewer flagged in 003: "in demo / not in operation" wording lives on /en and /en/products/aos, not on /en/proof; /en links the status table as `/en/proof#status-table`.

## Tests
- `python3 -m html.parser index.html` exits 0; `git diff master --stat` shows only the two docs paths.
- Team settings Playwright run at both widths (0 unrevealed after scrolling, `scrollWidth === innerWidth`, heights 6694 / 8077 px as on master) and the link check (every `http(s)` `href` + `og:image` + the Cal.com URL return 200; the two `rel=preconnect` bare hosts 404 as in every earlier review and are excluded). State in the PR that the page did not change.
- Every PNG the report names exists and is referenced with a relative path that renders on GitHub.

## Risks / watch out for
- No-JS context: `browser.newContext({javaScriptEnabled:false})`; reduced motion: `page.emulateMedia({reducedMotion:'reduce'})` before `goto`. Fonts and band images load from the network; wait for `networkidle` so screenshots are not fallback-font renders.
- Playwright's full-page screenshot is the "without scrolling" case — take it before any scroll, in a fresh page, or the IO has already fired.
- Severity discipline: Must only where content is hidden or a WCAG threshold fails; the rest is Should/Nice. Conny picks from the closing table, so one finding per row, no bundling.
- Nothing in the brief's "Utanför scope" (palette, fonts, logo, Swedish, dignami.com, price, booking). Proposed replacement colours stay in the same hue family and are proposals, not changes.

## Out of scope
- Any edit to `index.html`, `assets/`, `_config.yml`, `README.md`.
- Performance, SEO beyond the preview check, analytics, reviewing dignami.com.

## Suggestions for PO
- `docs/screenshots/NNN-slug/` PNGs from PRs 1–3 keep growing the repo; a later housekeeping row could cap or prune them.
- Reviewer N1 from 003 (`/en/proof#status-table` anchor) is cheap and fits whichever row builds the evidence-language findings.
