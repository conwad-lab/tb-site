---
id: 010
verdict: approve
---

# Review 010 — Rename the entry offer "The Architecture Review" → "The AI Value Review"

PR: #10 · 2026-10-13

## Must fix
- none

## Should fix
- none

## Nits
- N1: `index.html:193` — the hero lede still says "the architecture is open for review before you engage us". It is not the offer name, the story's grep (`architecture review`, case-insensitive → 0) passes, and the sentence is true (it is what "Examine the proof first →" points at). Noted only because it was a deliberate echo of the old name; if Conny wants the echo gone, that is a PO line, not this PR. No action.

## What I checked
- tests run: `python3 -m html.parser index.html` clean; JSON-LD block parses (`json.loads`), `makesOffer.name` = "AI Value Review", `description` starts "Fixed-scope two-week AI value review:"; `git diff master...HEAD --check` clean; `git diff master --stat` is exactly `index.html` (8 lines −/+) plus `docs/screenshots/010-rename-ai-value-review/{desktop,mobile}.png` (1440×6687, 390×7744). Rulebook files untouched. `gh pr checks 10`: no checks configured; PR `MERGEABLE / CLEAN` against `master`.
- diff vs plan: all nine replacements present, each on the plan's line with the plan's casing (L5, L8, L195, L291, L316, L320, L372 ×2 incl. `subject=AI%20Value%20Review`, L427 ×2). String 6 is the story's wording verbatim; the PDF `href`, `target`, `rel` unchanged. No other hunk.
- grep counts on the branch (master in brackets): `architecture review` -i 0 [9]; `architecture-review` 2 (Cal.com URL, PDF URL); `Architecture%20Review` 0; `AI%20Value%20Review` 1; `AI Value Review` 5; `AI value review` 3; `decision review` 0 [0]; `75 000 SEK` 3 [3]; `conny-wadbro-impk9g/architecture-review` 1.
- Playwright 1.62.1 + Chromium 1208, my own script, `networkidle` + 1 s, scrolled to bottom in 400 px steps, branch and `master` at 1440×900 and 390×844. Every number in the plan and the PR reproduced: 390 — page 7776 → 7744; offer `h2` 292×63.59 → 292×31.80 at x 49 (two lines → one, the only layout change); hero `.cta-big` 288.97 → 255.69 wide at x 20; `#book-cta` 296.97 → 263.69 at x 20; `.price` 292×43.19 at x 49 unchanged; stage 01 card 348×250.38 unchanged; `scrollWidth === innerWidth`; 0 `.r-fade` with opacity < 1. 1440 — page 6687 unchanged; `h2` 390×97.5 at x 255 unchanged; hero `.cta-big` 288.97 → 255.69 at x 206; `#book-cta` 296.97 → 263.69; `.price` 390×24 at x 255 unchanged; stage 01 card 342×290.5 unchanged.
- Copy: `document.body.innerText` diff vs master at both widths is exactly the five visible strings (3, 4, 5, 6, 7) — nothing else removed or added. `<title>`, `og:title` identical to master; `meta description` and `og:description` differ only by the name. Ordered `href` list identical to master; `#book-cta.href` resolves to `https://cal.com/conny-wadbro-impk9g/architecture-review` after the script runs; the footer `mailto:` address unchanged, and the `#book-cta` fallback keeps `contact@transformationbeyond.se` in the raw HTML. Nav "The review" / "Book the review" and offer-block "Book the review" (L319) untouched.
- Screenshots viewed (the Coder's PNGs, cropped): 390 offer block — "The AI Value Review" on one line, price line, "Book the review", new sample-link text on two lines; 390 hero CTA "Book the AI value review"; 390 and 1440 booking band — bronze "Book the AI value review" with price line and address below; 1440 offer `h2` "The AI Value / Review" on two lines as on master; 1440 stage 01 "The AI Value Review — a board-standard answer …". Both PR screenshot links return 200 (one GitHub 429 on first try, 200 on retry).
- Review checks — sources: no factual claim is added or changed; the rename is Conny's decision (ORDER row 7, brief § Fasta beslut 2, "omdöpt 2026-10-13"). Dignami wording: no Dignami-related string changes; `decision review` 0 before and after; the Dignami stage/hand-off text identical to master (verified by innerText diff). Contrast: no colour changes. Hard rails: price text, `CALCOM_URL`, contact address, `CNAME`, `_config.yml`, hosts, fonts, script: untouched. `README.md` untouched; its only old-name mention (L5) is the dated 2026-07-19 history note, as the plan says. `docs/design-review-2026-10.md` L126 mention is a dated report, stays.
- Link check (curl, browser UA, `-L`): fonts CSS, mondmodel.com, both band images, OG image, sample PDF, transformationbeyond.se, dignami `/en`, `/en/proof`, `/en/proof#status-table`, the Cal.com URL → 200; the two `rel=preconnect` bare hosts 404 as in every earlier review (excluded); `assets/favicon.svg` exists.
- tried to break: L427 holds both JSON-LD replacements with different casing — JSON still valid; the shorter CTA labels do not change button height (52.8 / 54.8) or x at either width; the `mailto:` subject is URL-encoded with `%20` as before; no occurrence of the old name survives in any attribute (`alt`, `title`, `aria-*`: none exist with it). Sample-PDF link text does not call the PDF an Architecture Review and says "a sample review of our own orchestrator".
- scope vs story: all seven acceptance criteria met; nothing outside the nine strings. Second reviewer not run — Team settings list no Second-reviewer paths.

## For PO
- Merge deploys to production (Operatör trigger): Conny should open https://transformationbeyond.se/ and check the hero CTA, stage 01, the offer heading, the sample-link text and the booking band; then change the Cal.com event title (URL stays), as the Operatör row says.
- The Operatör question is answered by the plan: the sample PDF's first page is titled "Architecture Review — Arnold OS" (2026-07-19). Conny needs a re-exported PDF at the same URL, or the link keeps leading to a document with the old title. The OG image (`brand/tb/og-1200x630.png`, fetched and viewed today) carries no offer name: eyebrow "Advisory · Business — Law — AI", the wordmark, the domain and "Advisory practice · Sweden". No new OG image is needed for this rename.
- Plan's ride-along note stands: `README.md` L6 still says "booking CTA (mailto now; set CALCOM_URL …)" although `CALCOM_URL` has been set since 2026-07-19. One-line docs fix for a later story.
- N1 above, if the hero echo bothers anyone.

Verdict: approve.

— Reviewer (Fable 5.1) on behalf of Conny Wadbro
