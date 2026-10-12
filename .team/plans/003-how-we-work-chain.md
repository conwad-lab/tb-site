---
id: 003
verdict: plan
---

# Plan 003 — Replace "How we work" with Advise → Assurance → Platform and add a Dignami hand-off block

Story: `.team/backlog/003-how-we-work-chain.md`

## Approach
Rewrite the `#arbetssatt` section of `index.html` (lines 283–293): four `.stage` cards become three, the `.arc-note` paragraph becomes a bordered hand-off block, and the `.arc` grid goes from four columns to three. Two one-line copy edits outside the section (hero base line 194, footer line 379). Every Dignami string below was re-fetched 2026-10-12 and is verbatim on dignami.com/en (slogan, "evidence pack", "Every claim has a status", AOS sentence), /en/about (roles sentence) and /en/products/aos ("Built, in demo", "No client records in operation").

Touches price block: no. Booking CTA: no. Footer: link text only, `href` unchanged. `CNAME`, hosts, fonts: unchanged.

## Files
- `index.html` — lines 86–94 and 165–168 (CSS), 194, 283–293, 379.

## Copy changes (old → new)
1. **Eyebrow, line 286** "How we work — four stages, two companies" → "How we work — three links, two companies".
2. **Card 1 (keeps `here`), line 287** `.k` "01 · Here" and `h4` "Advise" unchanged. `p` "Strategy, AI governance, regulatory gap analysis, project scoping." → "The Architecture Review — a board-standard answer on where your AI operation stands and what to do next. Strategy, AI governance, regulatory gap analysis, project scoping." `.who` "T&B · project" unchanged.
3. **Card 2, line 288** `.k` "02 · Build" → "02 · Dignami"; `h4` "Build" → "Assurance"; `p` "The audit-proof system is built with you: ledger, verification gate, sovereign runtime." → "Understand · Rethink · Rebuild. Every recommendation travels with an evidence pack; every claim has a status."; `.who` "Dignami · project" → "Dignami · engagement".
4. **Card 3, line 289** `.k` "03 · Run" → "03 · Dignami AOS"; `h4` "Run" → "Platform"; `p` "Dignami AOS — compliance platform for regulated advice, financial advisers first." and `.status` "Built · In demo · Not in operation" unchanged. New line between `.status` and `.who`: `<span class="src"><a href="https://www.dignami.com/en/proof" target="_blank" rel="noopener">Status as published on dignami.com/en/proof ↗</a></span>`. `.who` "Dignami · platform" unchanged.
5. **Card 4, line 290** removed entirely ("04 · Operate", "Operate", "Ongoing operations, monitoring and incident handling once a system goes live. Operation needs a separate decision.", "Dignami · later stage").
6. **arc-note, line 292** "Stage 1 lives here. Stages 2–4 are delivered by our sister company Dignami — Your AI got faster. Your decisions didn't. ↗" → removed. In its place, before `.qs`, a `<div class="handoff r-fade">` containing in order: `<span class="k">Hand-off → Dignami</span>`; `<p>Transformation &amp; Beyond advises; Dignami builds and runs; your counsel gives legal advice.</p>`; `<p>The Review's recommendations are carried forward in Dignami Assurance.</p>`; `<a href="https://www.dignami.com/en" target="_blank" rel="noopener">Dignami — Your AI got faster. Your decisions didn't. ↗</a>`. The slogan then appears once in the section.
7. **Hero base, line 194** "Build &amp; Run are delivered by our sister company <a …><b>Dignami</b> ↗</a>" → "Assurance and the platform are delivered by our sister company <a …><b>Dignami</b> ↗</a>". `href` unchanged.
8. **Footer, line 379** "Build &amp; Run → Dignami ↗" → "Assurance &amp; Platform → Dignami ↗". `href` unchanged.

## CSS (existing colours and fonts only)
- `.arc` → `grid-template-columns:repeat(3,1fr)`. Replace the two arc media rules (lines 94–95) with one: at `max-width:860px` stack to one column with `border-top` between cards, same pattern as `.layers` at 760. Drop the `.stage:nth-child(3)/(4)` border hacks and the `.revealed .stage:nth-child(4)` delay (line 168).
- Remove `.arc-note` and `.arc-note a` (lines 92–93); nothing else uses them.
- `.stage .src` — mono 11.5px, `--muted`, `display:block`, `margin-bottom:6px`, link styled like `.proof .metric a` (no underline, 1px `--hair` bottom border, ink on hover). Not uppercase: it is a sentence, not a label.
- `.handoff` — `margin-top:24px`, `border:1px solid var(--rule)`, `border-left:3px solid var(--bronze)`, `background:#FDFCF8` (the `.stage.here` tint), `padding:26px 30px`, `max-width:46em`. `.handoff .k` as `.qs-k`. `.handoff p` 15px `--body`, margin 0 0 8px. `.handoff a` as the old `.arc-note a` (ink, 600, bronze underline). Keep `.qs` `margin-top:40px` so the block sits between the cards and the questions.

## Tests
- `python3 -m html.parser index.html` exits 0.
- Greps → 0: "four stages", ">Build<", ">Run<", ">Operate<", "audit-proof", "sovereign", "verification gate", "later stage", "separate decision", "Stage 1 lives", "Build &amp; Run", "arc-note". Counts: `class="stage` → 3; "Your AI got faster" → 1; "Built · In demo · Not in operation" → 2; `dignami.com/en/proof` → 2; `dignami.com/en"` → 3.
- Playwright (`/Users/connywadbro/.nvm/versions/node/v22.21.1/lib/node_modules/playwright`, Chromium) at 1440×900 and 390×844: scroll to bottom in steps, wait 1 s, full-page screenshots attached to PR; `.arc` computed `gridTemplateColumns` has three values at 1440 and one at 390; `document.documentElement.scrollWidth === innerWidth` at both; 0 unrevealed `.reveal`; `compatMode === 'BackCompat'`. Baseline on master today: 6553 px at 1440, 7990 px at 390, both widths 0 overflow. Expect 1440 to grow by the hand-off block minus the note (+40–90 px) and 390 to shrink (one card gone), nothing above the section to move.
- Link check: every navigable `href` 200 (`mailto:`, `#` anchors and the two `rel="preconnect"` hosts excluded). No new targets; all three Dignami URLs returned 200 today.

## Risks / watch out for
- At 760–860 px the old grid showed two columns; three cards in two columns leaves an orphan, hence one column from 860 down. Check the 860–1000 px range does not squeeze card 1's longer paragraph into an ugly column; if it does, lower `.stage` padding at that width rather than change the font.
- Card 3 now stacks `.status`, `.src`, `.who` — three mono lines. Keep the 4–6 px gaps so they read as separate lines (Reviewer N1 in 002).
- No new colour pairs: `#FDFCF8`, `--bronze`, `--muted`, `--body` all already sit on `--paper`/`#FDFCF8` elsewhere on the page, so no new WCAG check beyond confirming the hand-off text uses `--body`, not `--muted`, at 15 px.
- Use the page's own characters: "—" U+2014, "·" U+00B7, "→", "↗", ASCII apostrophe in "didn't", `&amp;` in markup.
- "Understand · Rethink · Rebuild" with middle dots is the story's label form of Dignami's "Understand, Rethink and Rebuild"; keep it, the Reviewer knows the source.
- Reviewer re-checks dignami.com/en/proof and /en/products/aos on review day; the status label follows Dignami, not this plan.

## Out of scope
- "Who you get" rows, hero `lede` lines, nav label, `<title>`, meta and JSON-LD (none carry the old chain).
- Contrast, focus and reveal findings beyond the new block (ORDER row 4).
- Renaming "Build-in-public"; Swedish copy; dignami.com; doctype.

## Suggestions for PO
- Contact `h2` "Review the build before you book the call." and hero line 189 "someone who builds the systems" still use "build" in the T&B voice; consistent with /en/about ("Dignami builds"), so no change proposed, just noting it survives the grep.
- "Build-in-public" Method row (plan 002) remains the odd one out next to "available on request".
