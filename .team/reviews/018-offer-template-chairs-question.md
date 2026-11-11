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

---

# Round 2 — 2026-11-11 · head `f979b0e`

M1 and M2 from round 1 are fixed and verified. Codex reviewed `f979b0e` with no findings. One point stays open: the PR is still a draft, so it cannot merge (the merge workflow and `gh pr merge` both refuse a draft). The Judge attached its own screenshots to close S1. Verdict stays `request-changes` for that one step; the next round merges.

## Round 1 answers
- **M1** fixed in `d23d405` — verified: `grep -E -i -w "kr|SEK|moms|VAT|[0-9]{2} ?000" docs/offert-ordforandens-fraga/*` → no match; the `.price` spans, the `.price` rule and the third grid column are gone on all three pages; `README.md:5` now reads "Bifoga ditt eget avtal; pris och villkor finns i det." Closed.
- **M2** fixed — PR #32 body rewritten: no price mapping claim, visible-copy list carries no price strings, Tests says "no price figure on any page", the mapping paragraph is gone. Every remaining claim checked against the diff and my own runs (below). Closed.
- **S1** disputed ("the Builder thread attaches") — accepted in part: a thread has no upload path for images, and nobody attached anything in the hour since. Resolved by the Judge: my own renders are committed on the PR branch under `.team/reviews/018-offer-template-chairs-question/` (`index-1440x900.jpg`, `index-390x844.jpg`, `mall-sv-screen.jpg`, `mall-en-screen.jpg`, `exempel-sv-screen.jpg`), so they are part of the PR. Closed.
- **S2** disputed ("the Builder marks ready") — partly done: the `@codex review` on `f979b0e` completed 07:00:53Z with "Didn't find any major issues", the response file exists and answers M1–S2 by number. Not done: the PR is still a draft. Kept as **S3** below, one sentence: whoever drives this PR has to mark it ready before any merge can happen, and nobody has.

## Must fix
- none

## Should fix
- PR #32 — **S3** The PR is a draft. `.github/workflows/agent-team-merge.yml:46` refuses a draft (`[ "$draft" = false ] || refuse "the PR is a draft"`) and `gh pr merge` does too, so an approve now would strand the PR. Fix: `gh pr ready 32` (CLOUD.md § Builder 5). Marking ready starts Codex's own review of the same head; answer it in the response file if it finds anything, then ask for the Judge. No code change is needed; the next Judge round approves and merges unless that review finds something new.

## Nits
- Nit (carried): `.box` is `contenteditable` with `cursor:text`; a click toggle would save a keystroke. Not required.

## Evidence
| Acceptance criterion | Shown by (test, command + output, screenshot) | Result |
|---|---|---|
| Folder holds SV template, EN template, filled SV example, short README; each prints to one A4 | `git diff --stat origin/master...HEAD` = the four `docs/offert-ordforandens-fraga/*` files + the two review files; Playwright 1.58 `page.pdf({format:'A4', printBackground:true})` + `pdfinfo`: mall-sv Pages 1, mall-en Pages 1, exempel-sv Pages 1, all 595.92×842.88 pt (A4). README is five lines. | pass |
| Fields: question word for word; board meeting date; delivery date with the one-week rule next to it; checkboxes (a)(b)(c) | Renders `mall-sv-screen.jpg`, `mall-en-screen.jpg`, `exempel-sv-screen.jpg`: question block, Bolag/Company, Mottagare/Recipient, Styrelsemöte/Board meeting, Leverans/Delivery with "en vecka före mötet" / "one week before the meeting" directly under it, three ☐ rows with the (a)(b)(c) wording from the story | pass |
| No price figure anywhere on the pages | `grep -E -i -w "kr\|SEK\|moms\|VAT\|[0-9]{2} ?000" docs/offert-ordforandens-fraga/*` → no match (rc 1); read the rendered pages: no price, no currency | pass |
| Sender is Transformation & Beyond on every page; "Dignami" absent from the folder | masthead + footer "Transformation & Beyond · contact@transformationbeyond.se" on all three renders; `grep -ri dignami docs/offert-ordforandens-fraga/` → no match | pass |
| Terms one line only | `grep -c "Villkor enligt bifogat avtal"` → 1 in mall-sv and exempel-sv; `grep -c "Terms as per the attached agreement"` → 1 in mall-en; no other contract, legal or liability text on the pages (read in full) | pass |
| Yes line: authorised signatory, printed name, date | "Ja. Vi beställer det kryssade svaret." / "Yes. We order the answer ticked above." + signature grid "Behörig firmatecknare (underskrift) · Namnförtydligande · Datum" / "Authorised signatory (signature) · Name in print · Date", seen in the renders | pass |
| No claims about customers, credentials or numbers; only figures are dates | Read all three pages: no customer, credential or result claim. Figures on the pages: 2027-02-18 and 2027-02-11 in the example only | pass |
| Example uses a made-up company, marked "EXEMPEL" on the page and in the file name | bronze band "EXEMPEL — påhittat bolag" at the top of `exempel-sv.html` (in the page flow, so it prints); company "Exempelbolaget Fjällsta AB", recipient "Anna Exempel"; `<title>` starts with "EXEMPEL"; file `exempel-sv.html` | pass |
| `index.html`, `CNAME`, `_config.yml` unchanged; `docs` stays excluded | `git diff --stat origin/master...HEAD -- index.html CNAME _config.yml` → empty; `_config.yml` exclude list contains `docs` | pass |

## Codex findings
- Codex review on `f979b0e` (manual request, completed 2026-11-11T07:00:53Z): "Didn't find any major issues", summary state `has_any_findings: false`. Nothing to rule on. The earlier Codex reply at 06:13 was a usage-limit error; the retry at 06:59 succeeded.
- Builder disputes S1, S2: ruled above (S1 accepted and closed by the Judge; S2 kept as S3).

## What I checked
- tests run: `python3 -m html.parser` on `index.html` and the three offer pages (all OK). Playwright 1.58 chromium: A4 PDF per offer page with `pdfinfo` page count (1 each); `index.html` full-page screenshots at 1440×900 and 390×844 after scrolling to the bottom, scrollWidth = innerWidth at both; link check on every `href` in `index.html` (`curl -L`): transformationbeyond.se, the Google Fonts stylesheet, dignami.com/en, /en/proof, the r2.dev sample PDF, mondmodel.com, the cal.com booking URL all 200; `assets/favicon.svg` and the five section anchors exist. Not re-run this round: the fallback-font page count (round 1: 1 page each; the pages only lost content since).
- tried to break: merge-tree against `origin/master` → no conflict; bronze `#7A5729` on paper `#F7F5F0` ≈ 6.0:1 and white on bronze ≈ 6.5:1 (AA for the 7.5–8 pt labels and the example band); the band is in the page flow so it prints; no new font host (same Google Fonts URL as `index.html`); no script on the pages.
- scope vs story: diff is the four planned files plus the two review-lane files. No Human-merge path touched, not a Rulebook story, so the Judge merges once S3 is done.
- Not mine to do: marking the PR ready (Builder step).

— Reviewer (Fable 5.1) on behalf of Conny Wadbro
