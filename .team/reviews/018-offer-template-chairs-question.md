---
id: 018
verdict: request-changes
---

# Review 018 — Offer template "Ordförandens fråga"

PR: #32 · 2026-11-11 · head `08d4fd3`

The branch was cut at `dbdb9d9`, before `fbb9919` ("018: no prices on the offer page", Conny 2026-11-07) changed the story and the plan. The build follows the old plan. Everything else on the pages is right and prints to one A4 page; the fix is small.

## Must fix
- `docs/offert-ordforandens-fraga/mall-sv.html:58-60`, `mall-en.html:58-60`, `exempel-sv.html:60-62` — **M1** The three `<span class="price">` elements put "25 000 kr ex moms" / "75 000 kr ex moms" (SEK ex VAT in English) on every page. The story's acceptance criterion says "No price figure anywhere on the pages" and "the only figures are the dates"; the plan's § Decision says neither "kr", "SEK", "moms" nor "VAT" appears. Conny's decision 2026-11-07. Fix: delete the three price spans on each page and the `.price` CSS rule; the plan's grep `grep -E -i -w "kr|SEK|moms|VAT|[0-9]{2} ?000" docs/offert-ordforandens-fraga/*.html` must return no match. Also `README.md:5` carries the same price mapping; replace with the plan's wording (attach your own agreement; price and terms are in it). Merge or rebase `master` into the branch first so the plan you build from is the current one.
- PR #32 body — **M2** Claims the diff does not support: "Price mapping follows the plan's specified implementation" (the plan on `master` says the opposite), the visible-copy list includes the price strings, and Tests says "only the two price figures". After M1, rewrite the body: visible copy without prices, Tests line "no price figure on any page", and drop the "For PO" paragraph on the mapping (decided).

## Should fix
- PR #32 — **S1** Review checks in Team settings: screenshots at both widths attached to the PR, plus the plan's step 3 PNG of each offer page as A4. None is attached (no comments, no files). Builder: attach `index.html` at 1440×900 and 390×844 and the three offer pages.
- PR #32 — **S2** Cloud mode, CLOUD.md § Builder 3–5: no `@codex review` has been requested on this PR, there is no `.team/reviews/018-offer-template-chairs-question.response.md`, and the PR is still a draft. Before the next Judge round: one Codex round on the fixed head, every M/S answered in the response file (also M1–S2 from this round, by number), and the PR marked ready.

## Nits
- Nit: `.box` is `contenteditable` with `cursor:text`; the README explains "ersätt ☐ med ☑", which works, but a plain `☐`/`☑` toggle on click would save Conny a keystroke. Not required.
- Nit: the example is marked `exempel-sv.html` (lowercase) rather than `EXEMPEL`; matches the plan's file name, acceptable.

## Evidence
| Acceptance criterion | Shown by (test, command + output, screenshot) | Result |
|---|---|---|
| Folder holds SV template, EN template, filled SV example, short README; each prints to one A4 | `git diff --name-only master...HEAD` = the four files; Playwright `page.pdf({format:'A4'})` + `pdfinfo`: mall-sv 1 page, mall-en 1 page, exempel-sv 1 page (595.92×842.88 pt); same with fonts.googleapis.com/gstatic.com blocked: 1 page each | pass |
| Fields: question word for word; board meeting date; delivery date with the one-week rule next to it; checkboxes (a)(b)(c) | Rendered PDFs `/tmp/rev018/*-pdf-1.png`: question block, Styrelsemöte/Board meeting, Leverans/Delivery with "en vecka före mötet" / "one week before the meeting", three ☐ rows with the (a)(b)(c) wording from the story | pass |
| No price figure anywhere on the pages | `grep -E -i -w "kr\|SEK\|moms\|VAT\|[0-9]{2} ?000" docs/offert-ordforandens-fraga/*` → 10 matches (3 per page + README) | **fail → M1** |
| Sender is Transformation & Beyond on every page; "Dignami" absent from the folder | masthead + footer on all three pages; `grep -ri dignami docs/offert-ordforandens-fraga/` → no match | pass |
| Terms one line only | `grep -c "Villkor enligt bifogat avtal"` → 1 in mall-sv and exempel-sv; `grep -c "Terms as per the attached agreement"` → 1 in mall-en; no other contract/legal text on the pages | pass |
| Yes line: authorised signatory, printed name, date | signature grid "Behörig firmatecknare (underskrift) · Namnförtydligande · Datum" / EN equivalents, seen in the PDFs | pass |
| No claims about customers, credentials or numbers; only figures are dates | Read all three pages: no customer, credential or result claim. Figures present besides dates: the prices (M1) | **fail → M1** |
| Example uses a made-up company, marked "EXEMPEL" on the page and in the file name | bronze band "EXEMPEL — påhittat bolag" at the top of `exempel-sv.html`, present in the PDF; company "Exempelbolaget Fjällsta AB"; `document.body.innerText` contains EXEMPEL; file `exempel-sv.html` | pass |
| `index.html`, `CNAME`, `_config.yml` unchanged; `docs` stays excluded | `git diff master...HEAD -- index.html CNAME _config.yml` → empty; `_config.yml` exclude list contains `docs` | pass |

## Codex findings
- None: no Codex review has been requested on #32 (→ S2). Nothing to rule on this round.

## What I checked
- tests run: `python3 -m html.parser` on `index.html` and the three offer pages (all OK). Playwright 1.58 (chromium): A4 PDF per offer page, page count via `pdfinfo` (1 each, with and without web fonts); `index.html` full-page screenshots at 1440×900 and 390×844 after scrolling to the bottom, scrollWidth = innerWidth at both widths; link check on every `href` in `index.html`: transformationbeyond.se, dignami.com/en, /en/proof, /en/proof#status-table, r2.dev sample PDF, mondmodel.com, cal.com booking URL all 200; local favicon and section anchors resolve. Pre-existing, not from this PR: the two `preconnect` bare hosts return 404 and the logo `href="#"` has no target. Nothing on `index.html` changed.
- tried to break: fallback fonts (page count unchanged), fixed `height:260mm` vs A4 minus 18 mm margins (261 mm, fits), `contenteditable` focus style not printed, example band inside the page flow so it prints. Fonts come from the same Google Fonts URL as `index.html`, no new host.
- scope vs story: diff is the four planned files only. Scope creep is the price column, which the current story forbids.

— Reviewer (Fable 5.1) on behalf of Conny Wadbro
