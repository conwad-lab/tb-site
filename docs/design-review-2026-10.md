# Design review — October 2026

**Reviewed:** `master` at `2c911ac6f456c30853a5c9dbffd1e72a13fc9a8e` (page content from the merged 003 changes). **Date:** 2026-10-12. **Viewports:** Chromium 1440 × 900 and 390 × 844, device scale 1. **Tools:** Playwright 1.58.2; WCAG 2.1 relative-luminance contrast calculation from Chromium `getComputedStyle()` values; Python HTML parser; HTTP GET with curl. Screenshots use loaded web fonts and images. “Full” means scrolled through to the bottom and allowed reveal transitions to finish; “noscroll” is a fresh page captured immediately after network idle. [Desktop full](design-review-2026-10/1440-full.png) · [mobile full](design-review-2026-10/390-full.png).

**Lenses:** T&B's own paper/bronze, Newsreader/Hanken Grotesk and topographic identity; readability and hierarchy; movement between T&B and [Dignami](https://www.dignami.com/en) as sister sites. This is a review of the merged page, with proposals for a later decision, not a redesign. No visible copy changes, and no change to the price block, booking CTA or footer is made here.

## Findings

### D1 · Must — offscreen content disappears in unscrolled full-page captures

**Location:** `index.html:161–174`, `main section.reveal .r-fade`, IntersectionObserver setup at the end of the file. **Evidence:** 19/25 fade elements have computed `opacity: 0` in a fresh 1440 and 390 full-page capture: [1440 noscroll](design-review-2026-10/1440-noscroll.png), [390 noscroll](design-review-2026-10/390-noscroll.png). After scrolling, 0/25 remain hidden: [1440 full](design-review-2026-10/1440-full.png), [390 full](design-review-2026-10/390-full.png). **Proposal:** keep the content visible by default and ensure a bounded load fallback clears any JS-added hidden state even if the observer never reports an intersection. Preserve the visual reveal for normal scrolling. Verify this specifically with a fresh full-page capture that never scrolls.

### D2 · Should — small mono labels have narrow AA margins

**Location:** `index.html:34, 83–91, 110–111, 126, 149, 157` and analogous 10.5–13 px labels. **Evidence:** bronze on paper is 4.88:1, muted on paper 4.70:1, and `.book-sub` on dark 4.66:1; all pass 4.5:1 but leave only 0.38, 0.20 and 0.16 respectively. See the complete table below and [mobile full](design-review-2026-10/390-full.png). **Proposal:** if labels need more resilience, darken only the existing hue families: muted `#5B5E62` (5.98:1 on paper), bronze `#7A5729` (5.98:1 on paper), and lighten `.book-sub` to `#A39C8F` (6.01:1 on dark). Recheck against both paper and tinted card backgrounds before selecting values. This is a contrast margin improvement, not an AA failure or a new palette.

### D3 · Should — bronze focus ring is only just distinguishable on dark

**Location:** `index.html:31, 121–122, 362–370`, `.dark a:focus-visible`. **Evidence:** the 2 px bronze ring at 3 px offset has 3.08:1 contrast against `#231F1A`; it passes the 3:1 non-text threshold by 0.08. [Focused booking CTA](design-review-2026-10/focus-cta.png). **Proposal:** use the site's existing light bronze `#B69463` for focus outlines inside `.dark` (5.77:1 on dark), keeping the current outline size and offset. Check its appearance around both the booking CTA and the email link.

### D4 · Should — mobile hero opens with a dense headline

**Location:** `index.html:50–52, 190`, `h1` and forced `<br>`. **Evidence:** at 390 px the 48 px headline occupies six lines and 282 px in height; the forced break follows “AI —”, leaving “three” on a short line before “consultancies.” [Hero crop](design-review-2026-10/390-hero.png). **Proposal:** test a mobile-only heading measure and line-break rule that keeps the emphasized “in one advisor” intact while avoiding the isolated “three”; retain the same words, typefaces and hierarchy.

### D5 · Should — mobile navigation makes two competing two-line units

**Location:** `index.html:39–46, 178–181`, `.nav`, `.mark`, `.cta`. **Evidence:** within a 350 px row, the mark measures 205 px wide and the CTA 145 px; both wrap to two lines. [Navigation crop](design-review-2026-10/390-nav.png). **Proposal:** tune mobile spacing and CTA padding, or let the mark and CTA take deliberate separate rows; keep both visible and keyboard reachable.

### D6 · Should — stage and hand-off hierarchy blurs on mobile

**Location:** `index.html:80–99, 285–295`, `.arc`, `.stage`, `.handoff`. **Evidence:** all three stage cards stack at 348 px and the 350 px hand-off follows with almost the same tint as the first card, but its 3 px bronze edge and 46 em width cap make it look like another card. [Stages](design-review-2026-10/390-stages.png) · [hand-off](design-review-2026-10/390-handoff.png). **Proposal:** present the hand-off as the outcome of the chain: keep the bronze edge, give its label a clearer relation to the three cards, and set one concise role sentence above a distinct Dignami destination link. A sketch appears below.

### D7 · Should — narrow offer text column makes the process scan slowly

**Location:** `index.html:149–153, 309–325`, `.offer`, `.mrow`. **Evidence:** at 390 px each row reserves 110 px for its label and leaves 164 px for the description; “Week 1” alone takes a 202 px high row. The full offer is 1187 px high. [Offer crop](design-review-2026-10/390-offer.png). **Proposal:** on narrow screens, place the existing label above its description inside each row; retain the ruled separation and the current price and booking flow.

### D8 · Should — evidence labels use different registers and source positions

**Location:** `index.html:88–92, 110–112, 292, 340–347`, `.status`, `.src`, `.metric`. **Evidence:** the Platform stage pairs a status with a separate source line; the Platform proof row has the status but no adjacent source; Mondmodel puts its source at the end of a metric line. [Stages](design-review-2026-10/390-stages.png) · [mobile full](design-review-2026-10/390-full.png). Dignami's [proof page](https://www.dignami.com/en/proof) uses status words with explicit qualifiers and adjacent evidence; its [home page](https://www.dignami.com/en) says AOS capabilities are “some built, in demo, others not in operation” and none operates with client records. **Proposal:** use one T&B mono status register above one source/limit line below, in the stage card and both proof rows. Attribute AOS's operational qualifier to the [Dignami status statement](https://www.dignami.com/en); link evidence to the [proof status table](https://www.dignami.com/en/proof#status-table). A sketch appears below.

### D9 · Nice — the footer hand-off is quiet after the strong booking band

**Location:** `index.html:125–128, 377–383`, `.foot`. **Evidence:** on 390 px the copyright, registration and Dignami link form three separate lines, with the Dignami route given the same muted treatment as administrative text. [Footer crop](design-review-2026-10/390-footer.png). **Proposal:** preserve the compact footer but distinguish the Dignami route by spacing or a clearer text hierarchy, using the existing palette and typefaces; keep copyright and registration subordinate.

## Contrast · WCAG AA

Ratios below use the rendered sRGB foreground and effective solid background from Chromium, then the WCAG 2.1 linearized-channel relative-luminance formula `(Llighter + .05)/(Ldarker + .05)`. Normal text needs 4.5:1. Large text (at least 24 px, or 19 px bold) needs 3:1. The table applies 4.5:1 throughout, including large text, so every pass also clears its applicable threshold. No measured text pair fails AA. “Tint” is `#FDFCF8` on `.stage.here` and `.handoff`; other stage cards are on paper.

| Text / selectors represented | Foreground | Background | Ratio | AA |
|---|---|---|---:|---|
| Bronze: `.eyebrow`, `.layer .k`, `.mk`, `.proof .t`, hero emphasis | `#8A6430` | paper `#F7F5F0` | 4.88 | Pass |
| Muted: `.nav-r a`, `.proof-link`, `.hero-base`, `.stage p`, `.stage .who/.status/.src`, `.proof .metric a`, `.price span`, `footer`, `.foot .mono` | `#6B6E72` | paper | 4.70 | Pass |
| Body: `.lede`, `.layer p`, `.offer-lede`, `.mrow`, `.proof .d`, `.qs-grid span` | `#3B3E42` | paper | 9.87 | Pass |
| Ink: body, heading, `.price`, `.proof .name` | `#1C2022` | paper | 15.07 | Pass |
| Bronze: `.stage.here .k/.who`, `.handoff .k` | `#8A6430` | tint `#FDFCF8` | 5.18 | Pass |
| Muted: stage/card labels when on tint | `#6B6E72` | tint | 4.99 | Pass |
| Body: `.handoff p` | `#3B3E42` | tint | 10.47 | Pass |
| Ink: `.handoff a` | `#1C2022` | tint | 15.99 | Pass |
| `.book-sub`, `.book-sub a` (11 px mono) | `#8F887C` | dark `#231F1A` | 4.66 | Pass |
| `.cta` (12 px mono), `.cta-big` (13 px mono) | paper `#F7F5F0` | ink `#1C2022` | 15.07 | Pass |
| `.cta-bronze` (13 px mono) | `#FFFFFF` | bronze `#8A6430` | 5.32 | Pass |
| `.cta-bronze:hover` | `#FFFFFF` | deep bronze `#5C421E` | 9.32 | Pass |
| `.dark .eyebrow` (10.5 px mono) | `#B69463` | dark | 5.77 | Pass |
| `.dark` main text | `#EFEBE2` | dark | 13.76 | Pass |

This covers the distinct text-colour/background combinations and the small mono instances, including `.eyebrow` (10.5), `.k` (10.5), `.who` (10.5), `.status` (10.5), `.src` (11.5), `.proof .metric a` (11.5), `.mk` (10.5), `.cta` (12), `.price span` (12), `.foot .mono` (11), and `.book-sub` (11). The mobile and desktop renders use the same colour values. Browser-computed style confirms the white-on-bronze CTA and light-on-ink CTA pairs.

## Scroll reveal and preview

There are **25 `.r-fade` elements**, **6 `.r-rule-top` rules** and **7 sections receiving `.reveal`** when normal-motion JavaScript runs. These numbers differ from the brief's earlier count of 28 because this report reviews the merged page. Results:

| Condition | 1440 | 390 | Observation |
|---|---|---|---|
| Scrolled to bottom, animation settled | [PNG](design-review-2026-10/1440-full.png) | [PNG](design-review-2026-10/390-full.png) | 0 hidden; content visible |
| JavaScript disabled | [PNG](design-review-2026-10/1440-nojs.png) | [PNG](design-review-2026-10/390-nojs.png) | 0 hidden; `.reveal` is never added |
| Reduced motion | [PNG](design-review-2026-10/1440-reduced-motion.png) | [PNG](design-review-2026-10/390-reduced-motion.png) | 0 hidden; script exits before adding `.reveal` |
| Fresh full-page capture, no scroll | [PNG](design-review-2026-10/1440-noscroll.png) | [PNG](design-review-2026-10/390-noscroll.png) | 19 hidden; offscreen sections remain transparent |

The copy is present in HTML, so an HTML-reading crawler can read it. The page has `og:title`, `og:description`, `og:url`, `og:type`, `og:image` and `twitter:card`; the OG image returned HTTP 200. A link preview that uses those metadata fields gets text and an image. A screenshot-based preview that renders the full page without scrolling gets the D1 gaps. This is a rendering risk, not a claim that search engines have deindexed the page.

## Mobile 390 px

The six-line hero gives the title weight but places the final phrase in a ragged stack ([hero](design-review-2026-10/390-hero.png), D4). The navigation mark and CTA each wrap ([nav](design-review-2026-10/390-nav.png), D5). The three stage cards stack clearly and retain their rules, while the hand-off resembles a fourth card ([stages](design-review-2026-10/390-stages.png), [hand-off](design-review-2026-10/390-handoff.png), D6). The price reads clearly, but the process rows are long because of the 164 px description column ([offer](design-review-2026-10/390-offer.png), D7). The footer has three readable but equally quiet lines ([footer](design-review-2026-10/390-footer.png), D9). No horizontal overflow was measured (`scrollWidth = innerWidth = 390`); page height was 8077 px. Desktop height was 6694 px with no horizontal overflow.

## Focus and keyboard

Tab traversal reached all **17 rendered links and CTAs** on desktop in document order, including the navigation, proof links, sample PDF, Mondmodel source, booking CTA, email link and footer link. Each received `a:focus-visible` with a computed **2 px solid bronze outline and 3 px offset**. No focus ring was absent or clipped in the tested 1440 and 390 viewports; the CTA ring is shown in [focus-cta.png](design-review-2026-10/focus-cta.png). No `<button>` or other keyboard control is present. Bronze-on-paper is 4.88:1; bronze-on-dark is 3.08:1, the reason for D3. The booking link resolved to the existing Cal.com URL after script execution; no booking behaviour is proposed for change.

## Evidence language

Dignami's [proof page](https://www.dignami.com/en/proof) uses status plus qualifier: “In place”, “In use on our own analyses · not yet in a client engagement”, “Unproven”, “Built and tested”, and “Synthetic test”, with explicit scheduled or missing artefacts. Its [about page](https://www.dignami.com/en/about) distinguishes “Shown” from “Not yet shown.” T&B should borrow the grammar of **status + limit + source**, and the proximity of that source to the claim. It should keep its own restrained mono register. Dignami's exhibit sheets, amber missing-artefact marks and petrol palette belong to Dignami.

A shared T&B pattern, repeated in the Platform card, Platform proof row and Mondmodel proof row:

```text
PLATFORM · DIGNAMI AOS
Built · In demo · Not in operation
Status and limits: Dignami ↗  [source line directly below]

IN PRODUCTION · MONDMODEL
In production · daily editorial operation
9 destinations · 4 languages · source: mondmodel.com ↗
```

The status phrase is descriptive, not a new certification. The first line remains the current `.k`/`.t` register; the second uses `.status` (10.5 px mono); the third uses `.src`/`.metric` (11.5 px mono). For AOS, source the exact operating limit from [Dignami's home statement](https://www.dignami.com/en), then link to the [proof table](https://www.dignami.com/en/proof#status-table) for evidence. For Mondmodel, leave its existing public source visible. This pattern clarifies the differing evidence levels without implying that the Mondmodel source verifies every internal operating detail.

## Hand-off block

The merged `.handoff` at `index.html:294` has a useful bronze left border and a limited 46 em reading width. Its `#FDFCF8` fill repeats the first stage card, however, while the two explanatory sentences and slogan link form a fourth text-heavy unit after the three cards. On mobile it is nearly as tall as a stage card ([crop](design-review-2026-10/390-handoff.png)). Dignami's [footer](https://www.dignami.com/en/about) returns the reader with “Advise → Transformation & Beyond ↗”; T&B's current footer returns toward Dignami, so the two-way route exists, but the hand-off itself does not read as the result of the chain.

Proposed structure in T&B's existing visual language:

```text
01 ADVISE · T&B  →  02 ASSURANCE · DIGNAMI  →  03 PLATFORM · DIGNAMI AOS
                                  │ bronze rule
                                  HAND-OFF → DIGNAMI
                                  T&B advises; Dignami builds and runs.
                                  Review recommendations continue through Dignami Assurance.
                                  Explore Dignami Assurance ↗
```

Keep counsel's legal-advice boundary visible in the role sentence or adjacent text. The destination link should name the next step directly; the existing slogan can remain elsewhere if wanted. This is a hierarchy and wording proposal for a later story, not a change to this page now.

## Sister-site interplay

A reader moves from T&B's paper/bronze advisory voice to Dignami's evidence and operating-status voice, then can return through Dignami's “Advise” footer link. Three proposals stay within T&B: **(1)** use the same status-plus-qualifier grammar near every product claim; **(2)** place a source/limit line directly below each claim and link AOS to the relevant proof table; **(3)** make the T&B-to-Dignami hand-off read as the next step after the Architecture Review, matching the reverse route in Dignami's footer. No palette, font, logo, Dignami-site, price or booking-flow change is proposed.

## Decision list

| ID | Severity | One-line choice |
|---|---|---|
| D1 | Must | Make unscrolled full-page render show all content. |
| D2 | Should | Give small mono labels more contrast margin within current hues. |
| D3 | Should | Use the existing light bronze focus outline on dark. |
| D4 | Should | Improve the 390 px hero line breaks. |
| D5 | Should | Give mobile mark and navigation CTA deliberate space. |
| D6 | Should | Differentiate the hand-off from a fourth stage card. |
| D7 | Should | Stack offer row labels above descriptions on narrow screens. |
| D8 | Should | Standardize status and source placement. |
| D9 | Nice | Distinguish the footer's Dignami route from administrative text. |
