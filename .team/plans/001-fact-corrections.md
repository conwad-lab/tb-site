---
id: 001
verdict: plan
---

# Plan 001 — Correct factual claims on the page (C1, C2, C3, C8, C9)

Story: `.team/backlog/001-fact-corrections.md`

## Approach
Five copy edits in `index.html` and a `lang` attribute. Nothing else moves. The file today has no `<!doctype>`, `<html>`, `<head>` or `<body>` tags at all (the browser infers them), so C9 means adding an `<html lang="en">` wrapper. Do **not** add a doctype: the page renders in quirks mode (`document.compatMode === 'BackCompat'`) and a doctype switches it to standards mode, which I measured as a 45 px taller page at 1440 and 106 px at 390, spread across every section. That is a layout change and out of scope. The wrapper alone renders pixel-identical to master (verified with Playwright) and sets `lang` correctly.

Touches price block: no. Booking CTA: no. Footer: no. `<title>`, meta description, OG tags, JSON-LD: unchanged (none of them make a credential claim — checked).

## Files
- `index.html` — lines 1, 270, 271, 348 and a new last line. No CSS, no script changes.

## Steps
1. Line 1: insert `<html lang="en">` as the new first line. Last line of file: append `</html>` after the closing `</script>` of the JSON-LD block. No `<!doctype>`, no explicit `<head>`/`<body>`.
2. C3, line 270 (`01 · Business` card): "Two decades in consulting — sales leadership, pricing, go-to-market." → "Two decades in IT, consulting and sales leadership — sales leadership, pricing, go-to-market." Literal per the story; the repeated "sales leadership" is a known wart, see Suggestions. If the PO has amended C3 in the story by the time you branch, follow the story.
3. C1 + C8, line 271 (`02 · Law` card), one `<p>`: "A master's degree in commercial law. We read DORA, AMLR and the AI Act in the source text — not in summaries." → "Master's-level studies in commercial law at Lund University. We read DORA, AMLR and the AI Act in the source text — not in summaries. We read the regulation to shape the design — we don't replace your counsel."
4. C2, line 348 (Foundation proof row): "Master's in commercial law · sales leadership in consulting · working AI architect." → "Commercial law studies (Lund) · sales leadership in consulting · working AI architect." Keep `<b>One borderland, one advisor.</b>`.
5. Use the same characters the page already uses: literal em dash "—" (U+2014), middle dot "·", ASCII apostrophe as in "don't"/"what's" elsewhere on the page.

## Tests
- `python3 -m html.parser index.html` exits 0 (passes on master).
- `grep -n -i "master's degree\|master's in" index.html` → no output. `grep -c 'lang="en"' index.html` → 1.
- Playwright (global `npx playwright` 1.58.2 is on this machine; Chromium was installed with `npx playwright install chromium`): open `file://…/index.html` at 1440×900 and 390×844, scroll to the bottom in steps so every `.reveal` fires, wait ~1 s, full-page screenshot. Assert `document.documentElement.lang === 'en'` and `document.compatMode === 'BackCompat'` (proves no render-mode change). Attach both screenshots to the PR.
- Expected visual diff vs master: only the three text blocks. Page height 6432 px at 1440 and 7851 px at 390 on master; the Law card grows by one line, nothing else should shift.
- Link check: every `href` that is navigable — `http(s)` and the local `assets/favicon.svg` — returns 200. Exclude `mailto:`, `#` fragments and the two `rel="preconnect"` hrefs (`https://fonts.googleapis.com`, `https://fonts.gstatic.com`): bare hosts, they return 404 on master today and are not links. Also check the Cal.com URL in the booking script (200 on master).

## Risks / watch out for
- Adding `<!doctype html>` "while you're at it" changes layout on every section. Don't.
- `</html>` must come after the last `<script>`; the parser is lenient but the Reviewer will read the diff.
- The Law card becomes the longest of the three; the grid equalises heights at 1440, so the other two cards get more bottom whitespace. That is expected, not a bug.
- Keep the Dignami arc-note, stage cards and proof metrics untouched — they are C4–C7, next story.

## Out of scope
- C4–C7 (Dignami wording, /en/proof link, Mondmodel source, AOS status), the "How we work" restructure, any colour/layout/typography change, a doctype, Swedish copy.

## Suggestions for PO
- C3 as specified produces "…consulting and sales leadership — sales leadership, pricing, go-to-market." Consider amending the story to end "— pricing, go-to-market." or similar before the Coder branches. Not a factual issue, a readability one.
- Separate small story: add `<!doctype html>` so the page renders in standards mode. Measured impact: +45 px at 1440, +106 px at 390, no visible breakage in my screenshots, but it belongs with the design review, not with a fact-correction PR.
- Team settings say "every `href` returns 200"; two `rel="preconnect"` hrefs 404 by nature. Suggest the human amends the wording to "every navigable `href`" (rulebook change).
