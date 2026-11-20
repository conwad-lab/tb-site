---
id: 026
title: "The English home page in the poster design"
---

## Outcome
A visitor on https://transformationbeyond.se/ meets the same poster design as `/sv/` (story 025): navy hero with the Sluseholmen film and the red `&`, the gap as a principle sketch, the offer as a fact sheet, the six questions in two columns with the vendor question as an "Optional" line and the questions per role, the section "After the review", and the latest *& Beyond* letter as a cover. The English and Swedish pages share one stylesheet and one cover include, and the old include and inline styles are gone.

## Why
Story 025 put the Swedish page in the design Conny chose; the English page is the site's default (`x-default`) and what an international or Copenhagen-based reader lands on, which matters for the goal "Nordic with a base in Greater Copenhagen" (Conny 2026-11-19). Until it changes, the two languages look like two companies. Same decisions as 025 (see its table); the English text for the new sections was approved by Conny 2026-11-20 and the figure's English labels on 2026-11-20 (card in thread "Planera affischdesignen för tb-site").

## Signal
- After merge, read by the Coordinator's routine (from the Mac if the cloud session cannot reach the site): `https://transformationbeyond.se/` returns 200 and contains "Three ways forward. None of them is required."; every `href` on `/` returns 200 (mail links excluded). Logged here as seen / not seen.
- Conny opens `/` on the phone and answers one card "Ser engelska sidan ut som den svenska?" (ja/nej). Logged here.

## Acceptance criteria
- [ ] `index.html` has the same structure and form as `sv/index.html` after 025 (same sections in the same order, same classes, `/assets/site.css`, the same film and fallback), except that the English page keeps having no Skåne section.
- [ ] Every visible text change against today's `index.html` is one listed in the plan's Copy strings; all other text is unchanged character for character.
- [ ] Price ("75 000 SEK", "ex VAT · fixed scope · two weeks"), the Cal.com URL and its script, the mailto fallback, the contact address, the founder line ("Conny Wadbro, founder. Commercial law studies (Lund) · sales leadership in consulting · working AI architect. One borderland, one advisor.") and the legal-advice sentences ("your counsel gives legal advice", "Your lawyer gives the legal advice") unchanged. No price on "Review before scaling" or "Ongoing decision support".
- [ ] `<head>`: only the Google Fonts URL (the one `sv/index.html` uses) and the stylesheet link change; title, description, canonical, hreflang, OG tags and JSON-LD byte-identical.
- [ ] `_includes/latest-letter-cover.html` takes `lang` ("sv" default, "en") and renders the English labels on `/`; `_includes/latest-letter.html` is deleted; nothing renders while the collection is empty.
- [ ] No horizontal scroll at 390 px and 1440 px; the English `h1` (longer than the Swedish) is clear of the `&` glyph at 1440×900; WCAG AA as in 025.
- [ ] Test before commit green; Playwright full-page screenshots of `/` at 1440×900 and 390×844, reduced motion and film-blocked shots, and `/sv/` at both widths (unchanged by the include edit) attached to the PR; link check of every `href` on `/`.
- [ ] `sv/index.html` and `assets/site.css` unchanged, except a rule in `site.css` the English text needs (named in the response file).

## Out of scope
- `assets/beyond.css`, `/beyond/`, a new OG image, JSON-LD, `_config.yml`, `404.html`.
- A Skåne section in English.

## Vad blir publikt?
The English home page gets the same look as the Swedish one, with the English text Conny approved 2026-11-20 ("After the review", the Optional vendor line, the questions per role) and the figure's English labels. The Swedish page looks the same as after 025.

## Log
- 2026-11-20 Coordinator's planner: second story of the ORDER row "Ny design på startsidan", written after 025 merged (#60, 2edf70e).

— Coordinator (Claude) on behalf of Conny
