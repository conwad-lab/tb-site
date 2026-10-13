---
id: 010
title: Rename the entry offer "The Architecture Review" → "The AI Value Review"
---

## Outcome
The entry offer is called "The AI Value Review" everywhere a visitor, a link preview or a search engine reads it, while price, scope, duration, the Cal.com URL and the sample-PDF URL stay exactly as they are.

## Why
Conny's decision (ORDER row 7, 2026-10-13): the offer is renamed. The page, its metadata and its structured data must all say the same name so previews, search snippets and the page never disagree. Dignami's own offer is a "decision review" and is a different product; it keeps its name.

## Acceptance criteria
- [ ] Every occurrence of the old name in `index.html` becomes the new one, in the same casing pattern as today:
  - line 5 `meta description`: "Fixed-price Architecture Review: 75 000 SEK, two weeks." → "Fixed-price AI Value Review: 75 000 SEK, two weeks."
  - line 8 `og:description`: "Fixed-price Architecture Review, two weeks." → "Fixed-price AI Value Review, two weeks."
  - line 195 `.cta-big`: "Book the architecture review" → "Book the AI value review"
  - line 291 stage 01 · Advise: "The Architecture Review — a board-standard answer …" → "The AI Value Review — a board-standard answer …"
  - line 316 `h2`: "The Architecture Review" → "The AI Value Review"
  - line 372 `#book-cta` text: "Book the architecture review" → "Book the AI value review"; the `mailto:` fallback keeps the address `contact@transformationbeyond.se` and its `subject=` becomes `AI%20Value%20Review`
  - line 427 JSON-LD `makesOffer.name`: "Architecture Review" → "AI Value Review"; its `description` "Fixed-scope two-week AI architecture review: …" → "Fixed-scope two-week AI value review: …" (rest unchanged)
- [ ] Line 320 sample-PDF link text becomes "Read a sample review of our own orchestrator first — gaps included →" (or close; it must describe the PDF as "a sample review of our own orchestrator" and must not call it an Architecture Review). Its `href` (`…/brand/tb/architecture-review-sample.pdf`) is unchanged.
- [ ] Unchanged, verified by diff: `<title>` and `og:title` (they do not contain the old name today), the nav ("The review", "Book the review"), the price line "75 000 SEK ex VAT · fixed scope · two weeks", `CALCOM_URL` (`https://cal.com/conny-wadbro-impk9g/architecture-review`), the Cal.com script, the `#kontakt` targets, `CNAME`, footer.
- [ ] `grep -c -i "architecture review" index.html` returns 0; `grep -c "architecture-review" index.html` returns exactly 2 (the Cal.com URL and the PDF URL). `grep -c "decision review" index.html` is the same before and after.
- [ ] `README.md`: the history note on line 5 ("promoted 2026-07-19: … Architecture Review offer block") may stay as history; any present-tense description of the offer in `README.md` uses the new name. The plan says which.
- [ ] The plan lists every visible copy string that changes (old → new) and states: price block text unchanged, booking CTA text changed, CTA `href`s unchanged, footer unchanged.
- [ ] Team settings test passes (HTML parse, screenshots at both widths, all `href`s 200, including the unchanged PDF and Cal.com URLs). Screenshots attached.

## Out of scope
- The Cal.com event title (Conny changes it; Operatör line).
- The OG image on R2 and the sample PDF's own contents (not in this repo; Operatör line asks whether they show the old name).
- Dignami's "decision review" wording anywhere on the page or on dignami.com.
- Any change to price, scope, duration, URLs or layout.

## Log
- 2026-10-13 PO: created from ORDER row 7, after 009 merged (PR #9). Nine occurrences found by case-insensitive grep; `<title>`/`og:title` and nav contain no old name, listed as "verify unchanged". JSON-LD `description` phrase "AI architecture review" included in the rename so structured data matches the page. The mailto subject is changed with the name; the address is not touched.
