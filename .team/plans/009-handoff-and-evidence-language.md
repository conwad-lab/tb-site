---
id: 009
verdict: plan
---

# Plan 009 — D6 + D8 — hand-off as the outcome of the chain, one status-and-source pattern

Story: `.team/backlog/009-handoff-and-evidence-language.md`

## Approach
Markup and CSS in `index.html` only; no script, no new colour, host or font. Measured on master and with these exact rules and strings injected (Chromium 1440×900 and 390×844, `networkidle` + 1 s, scrolled to bottom); the Coder's run must reproduce the numbers below. Dignami wording re-verified live 2026-10-13 (`/en` qualifier, `/en/about` role sentence, `id="status-table"` on `/en/proof`).

D8 — one pattern, two classes. `.status` is already global; make `.src` global too and use it in all three places. Replace the three `.stage .src*` rules (lines 92–94) and the three `.proof .metric*` rules (112–114) with: `.src{display:block;margin-top:4px;font-family:var(--mono);font-size:11.5px;color:var(--muted)}`, `.src a{color:var(--muted);text-decoration:none;border-bottom:1px solid var(--hair)}`, `.src a:hover{color:var(--ink)}`. Delete `.stage .status{margin-bottom:4px}` (line 91; the 4 px now comes from `.src`). Keep one rule `.stage .src{margin-bottom:6px}` — that is the gap to the card's `.who` tag, not a variant of the pattern. `.metric` loses its `.06em` tracking; the Mondmodel text is unchanged. The AOS source/limit line is the same string in the card and the proof row:

`Dignami: “some built, in demo, others not in operation; none operates with client records” · <a href="https://www.dignami.com/en/proof#status-table" …>source: dignami.com/en/proof ↗</a>` — curly quotes U+201C/U+201D, link on the `source:` part only, `target="_blank" rel="noopener"` as the neighbours.

D6 — the hand-off hangs from the chain. `.handoff{margin-top:0;border:0;border-left:3px solid var(--bronze);background:none;padding:22px 30px 2px;max-width:46em}`, `.handoff .k{margin-bottom:12px}`, `.handoff p{font-size:14.5px;line-height:1.55;margin:0 0 10px}`. No fill, no box: the 3 px bronze rule starts at the arc's bottom-left corner (under the "01 · Here" column) and runs down the block, so it reads as a conclusion drawn from the cards. Content: label as today; the role sentence and the Assurance sentence in **one** `<p>`; then the link. The slogan "Dignami — Your AI got faster. Your decisions didn't." leaves the page: the hand-off link now names the next step, the footer's "Assurance & Platform → Dignami ↗" and the hero-base "Dignami ↗" already route there, and D9 (the only other candidate spot) is not taken. `grep -c "got faster"` → 0.

Mondmodel: the sentence drops "in daily operation" so the row says it once, in the status line.

Visible copy strings that change (old → new):
1. Platform card `.src`: "Status as published on dignami.com/en/proof ↗" (whole line linked to `/en/proof`) → the AOS string above (link to `/en/proof#status-table`).
2. Hand-off sentence 2: "The Review's recommendations are carried forward in Dignami Assurance." → "Review recommendations continue through Dignami Assurance."
3. Hand-off link: "Dignami — Your AI got faster. Your decisions didn't. ↗" → "Explore Dignami Assurance ↗" (`href` stays `https://www.dignami.com/en`).
4. Proof row Platform: new `.src` line after `.status`, the AOS string above (added, nothing removed).
5. Mondmodel `.d`: "Mondmodel — AI-driven editorial platform in daily operation." → "Mondmodel — AI-driven editorial platform."; new `.status` "In production · daily editorial operation"; the "9 destinations · 4 languages · source: mondmodel.com ↗" line keeps its text and `href`, class `metric` → `src`.
Unchanged: "Hand-off → Dignami", the role sentence, both "Built · In demo · Not in operation", every other card and row. Price block, booking CTA, Cal.com URL, contact address, footer, `CNAME`: untouched.

Measured: 390 — hand-off 279 → 180 px (stage cards 250 / 230 / 292, so visibly shorter than every card); Platform card 273 → 292; proof rows 170/165/144/141 → 227/164/144/141; page 7823 → 7776. 1440 — hand-off 180 → 135; stage cards 272 → 291 (all three, equal-height grid); proof rows 170/124 → 209/147; `.qs` top 3838 → 3787; page 6676 → 6687. No overflow at either width; `.price` and `.offer .cta-big` rects identical to master.

## Files
- `index.html` — CSS: lines 91–94 and 112–114 as above, `.handoff` rules at 97–100. Markup: Platform card (line 296), `.handoff` (298), proof rows Platform and Mondmodel (343–352). Nothing else.
- `docs/screenshots/009-handoff-and-evidence-language/` — `desktop.png`, `mobile.png` (full page, scrolled to bottom, as before), `390-stages.png` (element shot of `.arc`), `390-handoff.png` (element shot of `.handoff`), `390-proofs.png` (element shot of `.proofs`), for side-by-side with `docs/design-review-2026-10/390-{stages,handoff}.png`.

## Steps
1. Branch `feat/009-handoff-and-evidence-language`. CSS first, then the four markup edits.
2. Run Tests with a throwaway Playwright script (not committed); save the five PNGs.
3. PR body: the five old → new strings; before/after heights at 390 for hand-off, stage cards, proof rows and page; 1440 numbers; grep counts; link results; screenshots linked by commit SHA; "slogan removed, see plan".

## Tests
- `python3 -m html.parser index.html` exits 0; `git diff master --stat` shows `index.html` plus five PNGs.
- `grep -c "Built · In demo · Not in operation"` → 2; `grep -c "status-table"` → 2; `grep -c "autonomous operations"` → 0; `grep -c "got faster"` → 0; `grep -c "daily operation"` → 0 (only "daily editorial operation" remains, once); `grep -c 'class="metric"'` → 0; `grep -c 'class="src"'` → 3; `grep -c 'class="status"'` → 3.
- 390×844: `.handoff` height 180, computed `background-color` transparent, `border-left` 3 px `--bronze`, `border-top/right/bottom` 0, its top edge within 1 px of the `.arc` bottom edge; stage cards 250/230/292; proof rows 227/164/144/141; page 7776; `scrollWidth === innerWidth`; 0 `.r-fade` with opacity < 1, 7 `.revealed`. Every `.status` and `.src` computes to JetBrains Mono 10.5 px / 11.5 px with `--muted`, `.src` `letter-spacing: normal`, and in each of the three places the `.src` box starts 4 px below the `.status` box.
- 1440×900: `.handoff` 782×135, stage cards 291 each, proof rows 209/147/121/119, page 6687, `.price` 390×24 and `.offer .cta-big` 181×49 at the same x as master.
- Link check as in review 008 (curl with a browser `-A`; preconnect bare hosts excluded): every `http(s)` `href`, `og:image`, both band images, the PDF and the Cal.com URL return 200; `https://www.dignami.com/en/proof` body contains `id="status-table"`.

## Risks / watch out for
- `.status` and `.src` are `display:block` spans inside the inline `.proof .d` span, as `.metric` was (reviewed OK in 002). Keep them inside `.d`, after the sentence, in the order status → src.
- Do not shorten or paraphrase the Dignami quote; it is their qualifier verbatim from dignami.com/en. Reviewer re-checks /en and /en/proof on review day and follows Dignami if it moved.
- "daily editorial operation" is the story's wording. Evidence the Reviewer can open: mondmodel.com is live, and its sitemap shows 219 URLs with `lastmod` 2026-10-13. If the Reviewer wants a weaker word, that is a story change, not a Coder call.
- The two 4 px margins (`.stage .status` bottom, `.src` top) collapse, so deleting the first changes nothing; the numbers above were confirmed both ways.
- The equal-height `.arc` grid means the taller Platform card lifts all three cards to 291 at 1440; expected, not a bug.
- `.handoff` keeps `r-fade`; the `.stage:nth-child` stagger delays and the reveal script are untouched.
- Do not touch `.who`, `.k`, `.t`, section order, `CNAME`, hosts, fonts, colours.

## Out of scope
- D9. Footer, hero base, `<title>`/meta/OG/JSON-LD. The three cards' body copy beyond the Platform `.src`. The "Architecture decisions available on request." sentence. Widths other than 1440 and 390.

## Suggestions for PO
- "Explore Dignami Assurance ↗" lands on `/en` per the story; `https://www.dignami.com/en/assurance` exists (200 today) and would match the link text better. One-line change if Conny wants it.
- Review 007 N1 (comment on the `.cta-bronze` pin) is still open; a ride-along for the next CSS story.
