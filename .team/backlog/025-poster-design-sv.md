---
id: 025
title: "The Swedish home page in the poster design"
---

## Outcome
A visitor on https://transformationbeyond.se/sv/ meets the poster design Conny chose (direction B "Affischen", "Mellanväg", palette "Marin och rött"): a navy hero with a film from Sluseholmen in Copenhagen behind the heading and a large red `&`, the gap drawn as a principle sketch, the offer as a fact sheet, the six questions in two columns with the vendor question as an "Tillval" line and the questions per role, the new section "Efter genomlysningen", and the latest *& Beyond* letter as a cover. The page no longer carries the marks of AI-made design (thin serif with coloured ending, mono labels over every section, cream with bronze, numbered cards, the same fade-in everywhere).

## Why
Conny wants the site to stop looking AI-made, because the buyers T&B wants (management teams and boards who read HBR, The Economist, Di, EFN, McKinsey, Bain, Vinge, Mannheimer Swartling) judge the advisor by the page before they book (T&B goal: a named buyer with a real AI decision says yes to a first paid engagement, vault `idetavlor/transformation-beyond/ideas.md`). The design was explored 2026-11-17 to 2026-11-20 and every choice is Conny's; the decisions and the approved text are in `/mnt/project-files/tb-site-design/story-underlag.md` (project folder) and are restated in the plan so the Builder does not need the folder for anything but the film.

Split: the English page (`index.html`) gets the same form in story 026, written when this one is merged, so that the shared stylesheet and the cover include are settled once.

## Conny's decisions (all final)
| Date | Decision |
|---|---|
| 2026-11-17 | Direction B · Affischen, "Mellanväg" after Codex's critique in issue #51: the offer as a fact sheet, the questions in two columns, fewer booking bands. Heading weight 500, price at scale 0.7. |
| 2026-11-18 | Colour and imagery from the audience's sites; a real film on the first screen, not only animation. |
| 2026-11-19 | Film: Sluseholmen. Palette: Marin och rött. `&` at size 0.8. No portrait ("Skippa porträtt"). The three new text sections approved. No JetBrains Mono. |
| 2026-11-20 | No price on the two new steps (neither a price nor "price not decided"); the questions stay six, the vendor question is a separate "Tillval" line; JSON-LD unchanged; English text approved (used in 026). |

## Signal
- After merge, read by the Coordinator's routine (from the Mac if the cloud session cannot reach the site, papercut 2026-11-14): `https://transformationbeyond.se/sv/` returns 200 and contains "Tre vägar vidare. Ingen av dem är ett krav."; `https://transformationbeyond.se/assets/film/sluseholmen-720.mp4` returns 200 with `Content-Type: video/mp4`; every `href` on `/sv/` returns 200 (mail links excluded). Logged here as seen / not seen.
- Conny opens `/sv/` on the phone and answers one card "Ser /sv/ fortfarande AI-gjord ut?" (ja/nej). Logged here.

## Acceptance criteria
- [ ] `sv/index.html` has the sketch's structure, form and visible text (`docs/design-utforskning/riktning-b-redaktionell.html` at commit `3f46a2e` on branch `design/affischen-utforskning`) with only the chosen variants: no settings panel, no body classes for unchosen variants, no "Förslag" labels, no portrait placeholder.
- [ ] Every visible text change against today's `sv/index.html` is one listed in the plan's Copy strings; all other text is unchanged character for character.
- [ ] Price ("75 000 kr", "exkl. moms · fast omfattning · två veckor"), the Cal.com URL and the script that sets it on `#book-cta`, the mailto fallback, the contact address, the founder line and the legal-advice sentence ("er jurist ger juridisk rådgivning", "Er jurist ger den juridiska rådgivningen") are unchanged. No price on "Granskning före skalning" or "Löpande beslutsstöd".
- [ ] The `<head>` is unchanged except the Google Fonts URL (Newsreader + Familjen Grotesk only; no Hanken Grotesk, no JetBrains Mono, no other family) and the stylesheet link; title, description, canonical, hreflang, OG tags and the JSON-LD block are byte-identical.
- [ ] Film: `assets/film/sluseholmen-720.mp4` and `assets/film/sluseholmen-poster.jpg` in the repo; the `<video>` is `muted autoplay loop playsinline preload="metadata"` with `poster`, `aria-hidden="true"`; text is visible before the film loads; under `prefers-reduced-motion: reduce` no film shows and the line animation stands still; when the film fails to load the line animation shows. No file from a new host.
- [ ] The latest letter is rendered by Jekyll from the `beyond` collection as the sketch's cover, and nothing is rendered while the collection is empty (as today).
- [ ] No horizontal scroll at 390 px and 1440 px; the hero heading is clear of the `&` at 1440×900; WCAG AA for every text colour pair used (red `#CF2318` on navy is not used for running text).
- [ ] Test before commit green; Playwright full-page screenshots at 1440×900 and 390×844 (plus one at 1440×900 with `reducedMotion: 'reduce'`) attached to the PR; link check of every `href` on the page.
- [ ] `index.html`, `beyond/**`, `_layouts/**`, `assets/beyond.css`, `_config.yml`, `CNAME`, `404.html` unchanged.

## Out of scope
- The English page (story 026).
- `assets/beyond.css` and `/beyond/` in the new colours; a new OG image; the *& Beyond* graphics in `ai-insikter` (separate stories, see the underlag).
- Any change to the price, the booking URL, the contact address, founder claims or the JSON-LD.

## Vad blir publikt?
The whole Swedish home page changes look: navy and red, serif headings, a muted 2.3 MB film of Sluseholmen (Copenhagen, Pixabay content licence) on the first screen, a principle sketch of the gap, and three new text blocks Conny approved: "Efter genomlysningen" (three ways forward, no prices), the optional vendor and contract line in the offer and under the questions, and the questions per role (VD, CFO, Chefsjurist, Styrelse). The English page stays as it is until 026.

## Log
- 2026-11-20 Coordinator's planner: written from Conny's decisions (thread "Planera affischdesignen för tb-site"). ORDER row split in 025 (Swedish page, shared stylesheet, cover include, film) and 026 (English page in the same form with the approved English text, removes the old include if nothing uses it); 026 is written when 025 is merged.

— Coordinator (Claude) on behalf of Conny
