---
id: 004
title: Design review report with screenshots (no code change)
---

## Outcome
`docs/design-review-2026-10.md` exists on master with a numbered list of findings (Must / Should / Nice, each with location and proposal) and full-page screenshots of the merged page in `docs/design-review-2026-10/`, so that Conny can pick which findings become the next ORDER row.

## Why
The page has had three rounds of copy and structure changes (stories 001–003, PRs #1–#3) and no design pass since 2026-07. Conny wants a written review before deciding what to build, not a redesign. The brief fixes the scope: T&B keeps its own identity (paper/bronze, Newsreader + Hanken Grotesk, topographic bands) and coordinates with dignami.com in evidence language and in the hand-off, not in palette or typography. Source: `.team/briefs/2026-10-site-refresh.md`, section "Design review". Row 3 is merged, so the review is done against the merged page (master at or after `0015908`).

## Acceptance criteria
- [ ] The PR adds only `docs/design-review-2026-10.md` and files under `docs/design-review-2026-10/`. `index.html`, `assets/`, `CNAME`, `_config.yml` and `README.md` are untouched (`docs` is already excluded from Pages in `_config.yml`).
- [ ] Screenshots: full-page PNGs at 1440×900 and 390×844 taken after scrolling to the bottom (reveal animations complete), plus one full-page shot per width with JavaScript disabled, and one per width with `prefers-reduced-motion: reduce` emulated. File names say width and condition (e.g. `1440-full.png`, `390-nojs.png`, `390-reduced-motion.png`). The report states the master commit the screenshots were taken from.
- [ ] Report header: commit reviewed, date, viewports, tools used (Playwright version, contrast calculator), and the three review lenses from the brief: T&B's own identity, readability and hierarchy, interplay with dignami.com as sister site.
- [ ] **Contrast (WCAG AA):** a table with every text colour/background pair on the page and its computed ratio, pass/fail against 4.5:1 (normal text) or 3:1 (large text ≥ 24 px or ≥ 19 px bold). Must include at least: `--bronze #8A6430`, `--muted #6B6E72`, `--body #3B3E42`, `--ink #1C2022` on `--paper #F7F5F0` and on `#FDFCF8` (`.stage.here`, `.handoff`); `.book-sub #8F887C`; `--paper` on `--ink` (`.cta`, `.cta-big`); and every 10.5–13 px mono string (`.eyebrow`, `.k`, `.who`, `.status`, `.cta`, `.foot .mono`, `.price span`, `.book-sub`, `.proof .metric a`). Each failing pair gets a finding with a proposed replacement value in the same hue family (no new palette).
- [ ] **Scroll-reveal:** the report counts the `.reveal`/`.r-fade` elements (25 on the merged page) and answers, with the screenshots as evidence: is all content visible without JavaScript; is it visible with reduced motion; does a full-page screenshot without scrolling show hidden content; what does a crawler or link preview get (`og:` tags present, content in HTML, initial opacity). Any content hidden in any of these cases is a Must finding with a proposed fix described in words (e.g. "render visible by default, add the hidden class via JS").
- [ ] **Mobile 390 px:** findings on the hero h1 line breaks, the three stage cards and the hand-off block, the price block, the footer. Each with a crop of the screenshot.
- [ ] **Focus / keyboard:** tab through every link and CTA; confirm a visible focus ring on each (the page sets `a:focus-visible` with a bronze outline). Report any element where the ring is clipped, invisible against its background, or missing (buttons, non-`a` controls). Include one screenshot of a focused CTA.
- [ ] **Evidence language:** a proposal, with a sketch or mock in words or ASCII, for how status labels (`Built · In demo · Not in operation`) and source lines ("source: mondmodel.com ↗", "Status as published on dignami.com/en/proof") should look in T&B style, consistent across the stage cards, the Platform row and the Mondmodel row. Compare with how dignami.com/en/proof marks status, and say what to borrow and what not to.
- [ ] **Hand-off block:** a critique of the merged `.handoff` block (line ~294): hierarchy against the three cards, the bronze left border, the two sentences plus link, how it reads next to Dignami's footer line "Advise → Transformation & Beyond ↗". Proposal with a sketch.
- [ ] **Sister-site interplay:** one short section on what a reader moving between the two sites experiences (voice, status labels, hand-off in both directions), with at most three proposals. No proposal may change the palette, fonts, logo or the Dignami site.
- [ ] Every finding has an ID (D1, D2 …), a severity (Must / Should / Nice), a location (selector or line in `index.html`), evidence (screenshot file or measured value) and a proposal. Findings are ordered Must first. A closing table lists all IDs with severity in one line each so Conny can tick them.
- [ ] No finding recommends anything in the brief's "Utanför scope": new palette, new fonts, new logo, Swedish version, changes to dignami.com, price or booking flow.
- [ ] Team settings test still passes on the branch (`python3 -m html.parser index.html` clean, Playwright screenshots at both widths, all `href`s 200) — trivially, since the page does not change; the Coder states this in the PR.

## Out of scope
- Any change to `index.html` or `assets/`. Fixes come as a later ORDER row once Conny has read the report (ORDER, "Väntar på människan").
- Performance, SEO beyond the link-preview check, analytics.
- Reviewing dignami.com itself.

## Log
- 2026-10-12 PO: created from ORDER row 4, after story 003 merged (PR #3), so the review is against the merged page. The brief's `.reveal` count (28) is 25 on the merged page; the story uses the current count. Added the three extra screenshot conditions (no JS, reduced motion) because the brief asks for them to be verified and a screenshot is the evidence the Reviewer can open. Deliverable paths taken verbatim from the brief.
