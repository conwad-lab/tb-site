---
id: 010
verdict: plan
---

# Plan 010 — Rename the entry offer "The Architecture Review" → "The AI Value Review"

Story: `.team/backlog/010-rename-ai-value-review.md`

## Approach
Nine string replacements in `index.html`, nothing else. No CSS, no script, no URL, no new host. Casing follows each line as it stands today (Title Case in headings, meta and JSON-LD `name`; sentence case in the two button labels and the JSON-LD `description`). Dry-run measured 2026-10-13 on master with exactly these strings injected (Chromium, 1440×900 and 390×844, `networkidle` + 1 s, scrolled to bottom); the Coder's run must reproduce the numbers below.

Strings that change (old → new), by line on master:
1. L5 `meta description` (not visible): "Fixed-price Architecture Review: 75 000 SEK, two weeks." → "Fixed-price AI Value Review: 75 000 SEK, two weeks."
2. L8 `og:description` (not visible): "Fixed-price Architecture Review, two weeks." → "Fixed-price AI Value Review, two weeks."
3. L195 hero `.cta-big`, visible: "Book the architecture review" → "Book the AI value review". `href="#kontakt"` unchanged.
4. L291 stage 01 · Advise, visible: "The Architecture Review — a board-standard answer …" → "The AI Value Review — a board-standard answer …" (rest of the sentence unchanged).
5. L316 offer `h2`, visible: "The Architecture Review" → "The AI Value Review".
6. L320 sample link, visible: "Read the sample first — a genuine review of our own orchestrator, gaps included →" → "Read a sample review of our own orchestrator first — gaps included →". `href` (the `architecture-review-sample.pdf` URL), `target`, `rel` unchanged.
7. L372 `#book-cta`, visible: "Book the architecture review" → "Book the AI value review"; `subject=Architecture%20Review` → `subject=AI%20Value%20Review`; the `mailto:` address unchanged.
8. L427 JSON-LD `makesOffer.name` (not visible): "Architecture Review" → "AI Value Review".
9. L427 JSON-LD `makesOffer.description` (not visible): "Fixed-scope two-week AI architecture review: …" → "Fixed-scope two-week AI value review: …" (rest unchanged).

Stated for the Reviewer: price block text unchanged ("75 000 SEK ex VAT · fixed scope · two weeks", L317 and L373); booking CTA text changed (3 and 7 above); every CTA `href` unchanged (`#kontakt` ×3, the `mailto:` address, `CALCOM_URL` at L412, the Cal.com script); footer unchanged. Also unchanged: `<title>`, `og:title`, nav ("The review", "Book the review"), offer-block `.cta-big` "Book the review" (L319), `CNAME`, `_config.yml`.

`README.md`: unchanged. Its only old-name mention (L5, "promoted 2026-07-19: … Architecture Review offer block") is a dated history note; there is no present-tense description of the offer in the file.

## Files
- `index.html` — the nine replacements above, no other diff.
- `docs/screenshots/010-rename-ai-value-review/` — `desktop.png`, `mobile.png` (full page, scrolled to bottom, as the earlier stories).

## Steps
1. Branch `feat/010-rename-ai-value-review`. Apply the nine replacements; `git diff master --stat` must show `index.html` plus two PNGs only.
2. Run Tests with a throwaway Playwright script (not committed); save the two PNGs.
3. PR body: the nine old → new strings; grep counts; the measurements below (before/after); link results; screenshots linked by commit SHA. Note the Cal.com event title is an Operatör row for Conny, not part of the PR.

## Tests
- `python3 -m html.parser index.html` exits 0.
- Greps: `grep -c -i "architecture review"` → 0; `grep -c "architecture-review"` → 2 (Cal.com URL, PDF URL); `grep -c "Architecture%20Review"` → 0; `grep -c "AI%20Value%20Review"` → 1; `grep -c "AI Value Review"` → 5; `grep -c "AI value review"` → 3; `grep -c "decision review"` → 0 (same as master); `grep -c "75 000 SEK"` → 3 (same as master); `grep -c "conny-wadbro-impk9g/architecture-review"` → 1.
- 390×844 (master → branch): page 7776 → 7744; offer `h2` 292×63.59 → 292×31.80 (two lines → one; the only layout change); hero `.cta-big` width 288.97 → 255.69 at x 20; `#book-cta` width 296.97 → 263.69 at x 20; `.price` 292×43.19 at x 49 unchanged; stage 01 card 250.38 unchanged; `scrollWidth === innerWidth`; 0 `.r-fade` with opacity < 1.
- 1440×900: page 6687 unchanged; `h2` 390×97.5 at x 255 unchanged; hero `.cta-big` width 288.97 → 255.69 at x 206; `#book-cta` width 296.97 → 263.69; `.price` 390×24 at x 255 unchanged; stage cards 290.5 unchanged.
- `document.body.innerText` diff vs master at both widths is exactly strings 3–7 above; `#book-cta.href` resolves to the unchanged Cal.com URL after the script runs; the two `mailto:` addresses unchanged.
- Link check as in review 009 (curl, browser UA, `-L`; preconnect bare hosts excluded): every `http(s)` `href`, `og:image`, both band images, the sample PDF and the Cal.com URL return 200 (all 200 on master today).

## Risks / watch out for
- Line 427 holds two replacements (8 and 9) with different casing; do both, keep the JSON valid.
- Do not touch L319 "Book the review", the nav, `<title>`/`og:title`: the story lists them as "verify unchanged", and they contain no old name.
- String 6 is the story's wording; do not improve it. It must not call the PDF an Architecture Review and must say "a sample review of our own orchestrator".
- The sample PDF's own first page is titled "Architecture Review — Arnold OS" (checked 2026-10-13). That is Conny's Operatör row, not this PR; the new link text is what covers it on the page.
- `docs/design-review-2026-10.md` mentions the old name once; it is a dated report and stays.

## Out of scope
- Cal.com event title, OG image, sample PDF contents (Operatör rows). Dignami wording. Price, scope, duration, URLs, layout, CSS, script. `README.md`.

## Suggestions for PO
- The sample PDF does show the old name (title "Architecture Review — Arnold OS", review date 2026-07-19), so the Operatör question has its answer: Conny needs a re-exported PDF at the same URL, or the link keeps pointing at a document with the old title.
- `README.md` L6 still says "booking CTA (mailto now; set CALCOM_URL in index.html when the Cal.com account exists)" although `CALCOM_URL` has been set since 2026-07-19 (G2 closed). One-line docs fix for a future ride-along.
- Open from 009: S1 (AOS source line links `/en/proof#status-table`, the quote lives on `/en`), the `/en/assurance` link target, and 007 N1.
