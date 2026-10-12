---
id: 004
verdict: approve
---

# Review 004 — Design review report with screenshots (no code change)

PR: #4 · 2026-10-12

## Must fix
- none

## Should fix
- none

## Nits
- N1: `docs/design-review-2026-10.md:11` — D1's location says `index.html:161–174`; the reveal CSS is 162–166 and the IntersectionObserver script is 395–410. `docs/design-review-2026-10.md:15` — D2 lists line 149, which is `.offer-mech`, not a label. Nit: fix the two line references so Conny lands on the right rules.
- N2: `docs/design-review-2026-10/1440-nojs.png` and `1440-reduced-motion.png` are byte-identical (same md5), which is correct — both render without `.reveal` — but a reader may suspect a copied file. Nit: one clause in the scroll-reveal table saying the two conditions produce the same render.
- N3: `docs/design-review-2026-10.md:100–101` — the Mondmodel sketch repeats "In production" on two consecutive lines (`IN PRODUCTION · MONDMODEL` then `In production · daily editorial operation`). Nit: make the status line carry the qualifier only, so the three-line pattern does not read as a duplicate.

## What I checked
- tests run: `python3 -m html.parser index.html` clean; `git diff master --check` clean; `git diff master --name-only` shows only `docs/design-review-2026-10.md` and 15 PNGs under `docs/design-review-2026-10/`. `index.html`, `assets/`, `CNAME`, `_config.yml`, `README.md` are byte-identical to master; `_config.yml` still excludes `docs`. Playwright 1.58.2 Chromium at 1440×900 and 390×844: scrolled to bottom, 0 of 25 `.r-fade` hidden, `scrollWidth === innerWidth`, heights 6694 / 8077 px, same as the committed PNGs (1440×6694, 390×8077). Link check with curl: every `http(s)` `href`, `og:image` and the Cal.com URL return 200; the two `rel=preconnect` bare hosts 404 as in every earlier review and are excluded; `assets/favicon.svg` exists; all five `#` anchors resolve. `gh pr checks 4`: no checks configured.
- measured again, independently of the Coder's script, with my own WCAG 2.1 luminance code and `getComputedStyle`: every ratio in the contrast table matches to two decimals (bronze/muted/body/ink 4.88 / 4.70 / 9.87 / 15.07 on paper, 5.18 / 4.99 / 10.47 / 15.99 on `#FDFCF8`, book-sub 4.66 on dark, paper on ink 15.07, white on bronze 5.32 and 9.32 on hover, `#B69463` 5.77, `#EFEBE2` 13.76, bronze ring on dark 3.08), and the three D2 candidates (5.98 / 5.98 / 6.01). Rendered colours and sizes of every 10.5–13 px mono selector the story lists (`.eyebrow`, `.k`, `.who`, `.status`, `.src`, `.cta`, `.cta-big`, `.foot .mono`, `.price span`, `.book-sub`, `.proof .metric a`, `.mk`) match the table's foreground values and backgrounds. No AA failure anywhere; the report does not invent one.
- scroll-reveal: 25 `.r-fade`, 6 `.r-rule-top`, 7 `.reveal` sections with JS; fresh full-page capture before any scroll: 19 hidden at both widths (before and after the screenshot call); no-JS context: 0 `.reveal`, 0 hidden; `reducedMotion:'reduce'`: 0 `.reveal`, 0 hidden. The committed `390-noscroll.png` visibly shows the blank bands D1 describes. `og:title/description/url/type/image` and `twitter:card` present in the HTML. D1 as Must follows the story's rule verbatim.
- mobile 390: h1 48 px, 6 lines, 282 px tall with "three" alone on a line (the crop shows it); `.mark` 205 px and `.cta` 145 px both wrap to two lines in the 390 px nav; `.arc` one column, cards 348 px and hand-off 350 px with the same `#FDFCF8` fill as card 1; `.mrow` grid `110px 164px`, Week 1 row 235 px (the report says 202 px for the text; the row is 235 px with padding — not a defect), `.offer` 1187 px tall; `.foot` three stacked lines. All six crops exist and show what the findings say.
- focus: tabbed through all 17 visible links at 1440 and all 13 at 390; every stop is an `<a>` with a computed `2px solid rgb(138,100,48)` outline, offset 3 px; no `<button>` on the page; `#book-cta` points at the Cal.com URL with `target=_blank rel=noopener` after JS. `focus-cta.png` shows the dark-section booking CTA with the bronze ring, which is the right evidence for D3.
- Dignami claims, fetched 2026-10-12: /en/proof has "In place", "In use on our own analyses · not yet in a client engagement", "Unproven", "Built and tested", "Synthetic test", "first reference run scheduled", "EXHIBIT n", the claim-support classes "verified · approved memory / plausible / unsupported", amber dashes, and `id="status-table"`; /en/about has "Transformation & Beyond advises; Dignami builds and runs; your counsel gives legal advice." and the "Shown / Not yet shown" pair (the report attributes it to /en/about correctly; the plan had it on /en/proof); /en has "some built, in demo, others not in operation; none operates with client records"; the footer "Advise → Transformation & Beyond ↗" is on all three pages. Every Dignami quote and link in the report holds.
- story acceptance criteria, all fourteen: only the two docs paths added; eight full-page PNGs with width and condition in the name plus crops and the focus shot; header names commit `2c911ac`, date, viewports, Playwright 1.58.2, contrast method and the three lenses; contrast table covers every required pair and every listed mono string; scroll-reveal section answers all four questions with screenshot evidence; mobile findings on hero, stages + hand-off, offer/price, footer, each with a crop; focus section with a focused CTA screenshot; evidence-language proposal with an ASCII sketch, comparison with /en/proof and a borrow/do-not-borrow list; hand-off critique with a sketch; sister-site section with exactly three proposals; every D-finding has ID, severity, location, evidence and proposal, Must first; closing table with one line per ID; nothing recommends palette, fonts, logo, Swedish, dignami.com, price or booking changes (D2's values are same-hue proposals, as the story permits); Team settings test passes.
- PR description: every claim (15 PNGs, 17 links, 19/25, 0 hidden under no-JS and reduced motion, links 200, commit `2c911ac`, diff limited to docs) checked against the diff and my own runs — all hold.
- rulebook: no change to `AGENTS.md`, `.team/team.md`, `REVIEW.md` or `.team/roles/`.
- tried to break: looked for a hidden AA failure the table could miss (`.stage.here p` muted on tint 4.99, `.mark span` bronze at 16.4 px, `.lead-stmt` and `.gap-stmt em` bronze at 24–38 px — all pass and are covered by the table's rows); confirmed the noscroll count is the same before and after Playwright's full-page capture, so it is not an artefact of the screenshot call; checked that the hand-off sketch's "Explore Dignami Assurance" does not claim more than dignami.com ("Dignami Assurance · Available today" on /en).
- scope vs story: report only, no page change, no scope creep. Repo grows by 8.3 MB of PNGs, within what the plan accepted; the Architect's housekeeping suggestion stands.
- Second reviewer: not run — Team settings list no Second-reviewer paths.

## For PO
- Merging adds no page change, so no production deploy to check; the Operatör trigger for merged PRs does not apply beyond Conny reading `docs/design-review-2026-10.md` and choosing from its decision list.
- The nits are documentation polish; they can ride along with whichever ORDER row builds the chosen findings.

Verdict: approve. Merging per `merge: auto` in `.team/team.md`.

— Reviewer (Fable 5.1) on behalf of Conny Wadbro
