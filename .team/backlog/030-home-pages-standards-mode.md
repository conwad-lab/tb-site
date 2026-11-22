---
id: 030
title: "The home pages render in standards mode"
---

## Outcome
Both home pages start with `<!doctype html>` in the generated HTML, so browsers render them in standards mode instead of quirks mode, and the HTML check in CI fails a home page that lacks it. The pages look exactly as today.

## Why
Astra's counter-review on issue #63 (`docs/design-utforskning/granskning-063-codex.md` on `feat/063-design-review`, point 2 and question 4): `index.html` and `sv/index.html` have no doctype, and `.github/scripts/check_html.py` checks tag balance only. Quirks mode can shift layout (box model of tables and inline images, line heights) in ways the screenshots do not show today, and the later lower-hero trial should be measured in standards mode. ORDER row (Kö, "`<!doctype html>` på `index.html` och `sv/index.html`"), requested by the Coordinator 2026-11-20; after 029 because both touch the same two files.

## Signal
- After merge, live on both pages: `document.compatMode === "CSS1Compat"` (read from the Mac; the cloud cannot reach the site).
- The next PR that touches a home page runs the new check (pr-check green with the doctype present).

## Acceptance criteria
- [ ] `index.html` and `sv/index.html`: the line `<!doctype html>` directly after the closing `---` of the front matter (the front matter stays first in the source file).
- [ ] `.github/scripts/check_html.py`: a file argument whose normalized path is `index.html` or `sv/index.html` fails with `<path>: missing <!doctype html>` when its text, after a leading front matter block, does not start with `<!doctype html>` (case-insensitive); other files are checked as before.
- [ ] `bin/test-check-html.py` (stdlib) shows the check fails a home page without the doctype and passes one with it; Test before commit green.
- [ ] Builder: Jekyll build before and after, screenshots at 1440×900 and 390×844 (first screen and full page: menu, line breaks, hero, booking band, price block, footer, no horizontal scroll) match; `document.compatMode === "CSS1Compat"` on both built pages. If the layout moves, the story fixes it in `assets/site.css` so the page looks as today (that turns the order into a Claude build; the Builder says so).
- [ ] Price block, booking CTA, Cal.com URL, contact address, founder claims and all copy unchanged.

## Out of scope
- A lower hero; doctype on other pages (they come from layouts that already have one, or are checked separately).

## Vad blir publikt?
Nothing visible if the comparison holds; the pages render in standards mode.

## Log
- 2026-11-22 Coordinator: unparked, 029 merged (#70).
- 2026-11-22 Coordinator's planner (thread "Använd Codex och Astra mer i natt"): written from the Kö row, parked on 029. `.github/scripts/check_html.py` is a Human-merge path: the merge needs Conny's card.

— Coordinator (Claude) on behalf of Conny
