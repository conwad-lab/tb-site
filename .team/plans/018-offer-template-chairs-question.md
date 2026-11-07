---
id: 018
verdict: plan
---

# Plan 018 — Offer template "Ordförandens fråga"

Story: `.team/backlog/018-offer-template-chairs-question.md`

## Approach
Four new files in `docs/offert-ordforandens-fraga/`, nothing else. The offer is a self-contained HTML page with a print stylesheet (`@page { size: A4; margin: 18mm }`) so Conny opens it in a browser, fills the fields (`contenteditable` spans, or edits the file) and saves as PDF. It borrows the site's identity from `index.html` L19–24 (tokens `--paper #F7F5F0`, `--ink #1C2022`, `--bronze #7A5729`, `--hair #E3DFD5`; Newsreader / Hanken Grotesk / JetBrains Mono via the same Google Fonts URL as `index.html` L15, with the same fallbacks). No script. `docs` is already in `_config.yml` `exclude` (L7), so nothing reaches the site.

Baseline on master `0d35002`: `python3 -m html.parser index.html` OK; Playwright 1440×900 and 390×844 full-page, no horizontal overflow (scrollWidth = innerWidth). Link check: every external `href` **not checked** from the planning session (proxy blocks dignami.com, r2.dev, mondmodel.com, cal.com). This story does not touch `index.html`.

## Decision
Decided by Conny 2026-11-07: **no prices on the page.** Everything is ex moms and the price sits in Conny's attached agreement. The checkboxes (a)–(c) carry no price, and neither "kr", "SEK", "moms" nor "VAT" appears on the pages.

## Files
- `docs/offert-ordforandens-fraga/mall-sv.html` — Swedish template.
- `docs/offert-ordforandens-fraga/mall-en.html` — English template, same structure.
- `docs/offert-ordforandens-fraga/exempel-sv.html` — filled-in Swedish example.
- `docs/offert-ordforandens-fraga/README.md` — Swedish, five lines at most: fill in, delivery = meeting minus 7 days, save as PDF (A4, no headers/footers), attach your own agreement (price and terms are in it).

## Page structure (both languages, top to bottom)
1. Header: "Transformation & Beyond" (mark as on the site) and `contact@transformationbeyond.se`. Eyebrow "Offert" / "Offer".
2. Title: "Ordförandens fråga" / "The chair's question".
3. "Er fråga, ordagrant" / "Your question, word for word": a large quoted field `[Kundens fråga ordagrant]`.
4. Dates: "Styrelsemöte" `[ÅÅÅÅ-MM-DD]`; "Leverans" `[ÅÅÅÅ-MM-DD]` with the note "en vecka före mötet" / "one week before the meeting". Customer: `[Bolag]`, `[Mottagare, roll]`.
5. "Vilket svar köps" / "Which answer you are buying", three checkboxes (☐), no prices:
   - (a) "Kostnad per utfall för en namngiven process, mätt före ett AI-köp" / "Cost per outcome for a named process, measured before an AI purchase"
   - (b) "Granskning av ett AI-framtaget underlag som står på styrelsemötets dagordning" / "Review of an AI-produced document on the board meeting's agenda"
   - (c) "Hela The AI Value Review" / "The whole AI Value Review"
   - No price next to any box (§ Decision).
6. "Villkor enligt bifogat avtal." / "Terms as per the attached agreement." — nothing more.
7. Yes line: "Ja. Vi beställer det kryssade svaret." / "Yes. We order the answer ticked above." then three lines: "Behörig firmatecknare (underskrift)", "Namnförtydligande", "Datum" / "Authorised signatory (signature)", "Name in print", "Date".
8. Footer: "Transformation & Beyond · contact@transformationbeyond.se". No Dignami, no founder bio, no customer names, no prices, no figures.

Example (`exempel-sv.html`): same as `mall-sv.html` with a visible bronze band "EXEMPEL — påhittat bolag" at the top; company "Exempelbolaget Fjällsta AB" (made up), a made-up question (e.g. "Vad har våra Copilot-licenser gett i kronor, och ska vi förnya dem i mars?"), meeting 2027-02-18, delivery 2027-02-11, box (a) ticked, signature lines empty.

## Steps
1. Branch `feat/018-offer-template-chairs-question`.
2. Write `mall-sv.html`, copy to `mall-en.html` and translate the strings above, write `exempel-sv.html`, write `README.md`.
3. Run Tests; PR body lists every visible string (new files only, no old → new) and attaches a PNG of each page rendered as A4.

## Tests
- `python3 -m html.parser` on each of the three HTML files and on `index.html` exits 0.
- Playwright: open each HTML file, `page.pdf({format:'A4', printBackground:true})`; the PDF has exactly one page (count `/Type /Page` objects, or `pdfinfo` Pages: 1). Screenshot at 794×1123 for the PR.
- `grep -ri dignami docs/offert-ordforandens-fraga/` → no match.
- `grep -c "Villkor enligt bifogat avtal" mall-sv.html exempel-sv.html` → 1 each; `grep -c "Terms as per the attached agreement" mall-en.html` → 1.
- `grep -E -i -w "kr|SEK|moms|VAT|[0-9]{2} ?000" docs/offert-ordforandens-fraga/*.html` → no match (no prices on the pages).
- `git diff --stat master` lists only `docs/offert-ordforandens-fraga/*` (four files). `_config.yml` still excludes `docs`.
- Team settings Test before commit on `index.html` (screenshots at both widths, link check) — unchanged page; a URL the network blocks is listed as **not checked**.

## Risks / watch out for
- Do not write any term, liability, payment or cancellation text: only the one Villkor line.
- No claim about customers, results, years of experience or percentages, not even in the example.
- The example company must not be a real company; keep the "EXEMPEL" band in print (it is in the page, not a screen-only element).
- One A4 page: if the Swedish text overflows, shrink spacing, not font below 10 pt.
- Human-merge paths: the diff does not touch `CNAME`, `_config.yml` or the site's price, Cal.com URL, contact address or founder claims, so the Judge merges. No price appears in the diff.

## Out of scope
- The agreement, any change to `index.html`, an English example, a PDF committed to the repo.

## Suggestions for PO
- Once the template has been used, a later story could move it to a form Conny fills from the phone; not now.
