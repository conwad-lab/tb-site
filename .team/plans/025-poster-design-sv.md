---
id: 025
verdict: plan
---

# Plan 025 — The Swedish home page in the poster design

Story: `.team/backlog/025-poster-design-sv.md`

## Approach
Port the sketch `docs/design-utforskning/riktning-b-redaktionell.html` at commit `3f46a2e` (branch `design/affischen-utforskning`; read it with `git fetch --depth 1 origin design/affischen-utforskning && git show 3f46a2e:docs/design-utforskning/riktning-b-redaktionell.html`; the film in it is a 3 MB data URI, strip it before reading) into `sv/index.html`, keeping today's `<head>`, front matter, JSON-LD and booking script. The sketch's `<style>` becomes `assets/site.css` with every CSS variable fixed at the value the sketch's `:root` resolves to and only the rules for the chosen body classes (`few-bands offer-sheet q-matrix gap-fig show-letter has-video p-after p-law p-roles`) kept, written as plain rules without the body-class switches; the rules for the panel, unchosen palettes, the portrait and the `.plab` labels are dropped. 026 reuses the same stylesheet for the English page. The latest letter becomes a new include `_includes/latest-letter-cover.html` (the sketch's `.brev` block built from the `beyond` collection); the old include stays for `index.html` until 026. The film and its poster go into `assets/film/` from the project folder.

Touches the price block: yes, form only (the fact sheet), the text and figure are unchanged. Booking CTA: form only (bands instead of buttons, the nav button removed per "fewer booking bands"); the Cal.com URL, the script and the mailto fallback are unchanged. Footer: form only, text unchanged.

## Baseline
`master` at `11d5623`: `find . -name '*.html' -not -path './.claude/*' -not -path './.git/*' -print0 | xargs -0 python3 .github/scripts/check_html.py` exits 0; Playwright full-page screenshots of `/sv/` (Jekyll build or `python3 -m http.server` on a `jekyll build` output) at 1440×900 and 390×844, and the link check of every `href` on `/sv/` (a URL the session blocks is "not checked").

## Estimate
size: M
risk: plain
files: 5
codex-rounds: 2
builder: claude — a design port with binary assets from the project folder that Codex's environment cannot reach, and visual judgement at two widths
model: standard — M plain; every design choice is made in the sketch and this plan

## Files
- `sv/index.html` — body rebuilt from the sketch; `<head>`: Google Fonts URL changed, inline `<style>` replaced by `<link rel="stylesheet" href="/assets/site.css">` (root-relative, since the page lives at `/sv/`); front matter, title, meta, canonical, hreflang, OG and JSON-LD byte-identical; the reveal-animation `<script>` removed; the Cal.com `<script>` kept byte-identical.
- `assets/site.css` — new, from the sketch's `<style>` as described in Approach.
- `_includes/latest-letter-cover.html` — new: the cover block from the `beyond` collection.
- `assets/film/sluseholmen-720.mp4` — new, copied from `/mnt/project-files/tb-site-design/film/sluseholmen-720.mp4` (2 298 159 bytes, 1280×720, no audio).
- `assets/film/sluseholmen-poster.jpg` — new, copied from `/mnt/project-files/tb-site-design/film/sluseholmen-poster.jpg`.
- `.team/**` — response file, papercuts (Builder only).

## Form (fixed values; the sketch's `:root` already has them)
- Colours: navy `#0C2233` (hero and dark fields), red `#CF2318` (the `&`, accent, button), paper `#F8F6F1` (page), ink `#14181B` (text), salmon `#F6E6DA` (soft surface), darker red `#B01C13` (red text on light). Red text on navy only at heading size, never running text (3.02:1).
- Type: Newsreader 500 for headings, bands, questions, price; Familjen Grotesk for everything else. Fonts URL: `https://fonts.googleapis.com/css2?family=Familjen+Grotesk:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400;1,6..72,500&display=swap` (the sketch's URL without Schibsted Grotesk, Sofia Sans, Sofia Sans Extra Condensed and Source Serif 4). Keep the two `preconnect` links.
- `&` at `--as: .8`; price at `--ps: .7`; heading weight 500.
- Hero: the film at opacity .5 with `grayscale(.55) contrast(1.05)`; the two-line flow SVG (`.flow`) as fallback.

## Copy strings (old → new, `sv/index.html`)
Every other visible string, `alt` and `aria-label` stays character for character.
- Nav: the button "Boka ett inledande samtal" in the menu → removed (Mellanväg, fewer booking bands; the hero band right under it carries the same text and link). The mark: "Transformation **&** Beyond" with link `/sv/` → same text, same link (the sketch's `href="#"` is a sketch artefact; keep `/sv/`).
- Hero eyebrow "Rådgivning · Affär × Juridik × AI" → removed.
- `h1` "AI-rådgivning för ledningsgruppen —<br><em>affär, juridik och AI</em> hos en rådgivare." → `<span class="nb">AI-rådgivning</span> för ledningsgruppen — affär, juridik och AI hos en rådgivare.` (same words, no line break, no italic).
- Hero CTA "Boka ett inledande samtal" (button) → band with the same text, `href="#kontakt"`; "Granska bevisen först →" (link) → thin band "Granska bevisen först" with the arrow as a separate `aria-hidden` span, same URL.
- The two `mat-band` images (R2 `contours-duotone.jpg`, `strata-duotone.jpg`) and their alt texts → removed.
- Section "Varför vi finns": the eyebrow → removed; the gap sentence is split as in the sketch: the figure's caption column holds "De stora konsultbolagen förstår er verksamhet men bygger inte tekniken." and "AI-labben bygger tekniken men förstår inte er verksamhet.", and the line under it is "Vi sitter i glappet, små med avsikt, som de främsta advokatbyråerna." (same words, no italic).
- New figure (the sketch's inline SVG, approved 2026-11-17/19): axis texts "Förstår er verksamhet →" and "Bygger tekniken →", dot labels "AI-labben", "De stora konsultbolagen", "Transformation & Beyond", caption "Principskiss, inga mätvärden.", `aria-label` as in the sketch. Replaces the strata SVG and its English `aria-label`.
- "Vad vi gör": lead "Varje disciplin är vanlig. **Kombinationen hos en och samma rådgivare är det inte.**" → `h2` with the same sentence, no bold. Layer keys "01 · Affär", "02 · Juridik", "03 · Teknik" → `h3` "Affär", "Juridik", "Teknik"; the sub-headings "Affärsutveckling & strategi", "Affärsjuridik", "AI-arkitektur" and the paragraphs unchanged.
- "Arbetssätt": stage keys "01 · Här", "02 · Dignami", "03 · Dignami AOS" → removed; each stage shows its existing `who` label ("T&B · projekt", "Dignami · uppdrag", "Dignami · plattform") with "Här" on the first and "→" on the others, as in the sketch. Texts, status pill, source line and hand-off text unchanged.
- "Frågorna vi besvarar": the six questions unchanged, as a numbered list in two columns. New, approved 2026-11-19/20: the line "**Tillval** Vilken leverantör ska ni välja, och vad står i avtalet?"; the block "Samma frågor, för den som ska svara på dem" with **VD** "Vad ska automatiseras, och vad ska inte det?" / "Vem äger förändringen?"; **CFO** "Hur ser ekonomin egentligen ut?" / "Hur säkrar ni kostnaden för tokens?"; **Chefsjurist** "Vem äger vilket AI-beslut?" / "Vad står i leverantörsavtalet, och vad behöver er jurist ta ställning till?"; **Styrelse** "Var står AI-verksamheten egentligen?" / "Vilka beslut behöver styrelsen fatta, och på vilket underlag?". No "Förslag" label.
- "Skåne": lead with bold "besluta" → `h2` with `<em>besluta</em>`, same words.
- Offer: same text; the new row before "Efteråt", approved: "**Tillval** Leverantörsval och avtal. Vilken leverantör och modell som passar er, och vilka avtalsvillkor ni bör granska: dataanvändning, lagring, ansvar och utträde. Vi formar underlaget. Er jurist ger den juridiska rådgivningen." No price on the row, no "Förslag" label. "Avgränsad till de sex frågorna ovan." unchanged.
- New section `#efter` before "Vem du får", approved: tag "Efter genomlysningen"; `h2` "Tre vägar vidare. Ingen av dem är ett krav."; three stages: "T&B · projekt / Här" **Granskning före skalning** "För er som har en pilot. Tre till fyra veckor, fast omfattning: ekonomi och tokenkostnad, ägande, AI-förordningen och GDPR, avtalet och kriterierna för att ta piloten i drift."; "T&B · löpande / Här" **Löpande beslutsstöd** "Ett månadsupplägg för ledning och styrelse. Efter varje pass får ni ett skriftligt underlag där varje påstående har en källa."; "Dignami · uppdrag / →" **Assurance** "Om ledningen vill gå vidare kan rekommendationerna från genomlysningen fortsätta genom Dignami Assurance."; note "Underlaget står på egna ben. Att avstå från att investera är ett giltigt utfall." No price anywhere in the section.
- "Vem du får": the proof rows take the sketch's form (`h3` name, key, text); "— efterlevnadsplattform …", "— AI-driven redaktionsplattform.", "— arkitekturbesluten …" lose the dash and start with a capital ("Efterlevnadsplattform …", "AI-driven …", "Arkitekturbesluten …"). **The founder row keeps today's sentence exactly**: "Conny Wadbro, grundare. Studier i affärsrätt (Lund) · säljledning i konsultbranschen · verksam AI-arkitekt. **Ett gränsland, en rådgivare.**" (name may sit in the `h3`, but the text after it reads ", grundare. …" unchanged). No portrait placeholder.
- Latest letter: `{% include latest-letter.html lang="sv" %}` → `{% include latest-letter-cover.html %}` (see Steps 4).
- Contact: same `h2`, same text in the CTA (now a band, `id="book-cta"`, same mailto `href`), same price line and address.
- Footer: same five items and texts; the mono class goes.

## Steps
1. Branch `feat/025-poster-design-sv`. Read the sketch (strip the data URI: `sed -E 's/data:[a-z]+\/[a-z0-9.+-]+;base64,[A-Za-z0-9+\/=]{100,}/DATAURI/g'`) and today's `sv/index.html`.
2. `assets/site.css`: the sketch's `<style>` with the variables resolved as above; drop every rule for `.panel`, palettes other than Marin och rött, `amp-off/amp-front/amp-line/no-amp-anim`, `no-film`, `no-figanim`, `.portrait`, `show-portrait`, `.plab`, and the unchosen states of each body class; turn the chosen `body.<class> …` rules into plain rules. Keep the reduced-motion rules. No `@import`, no URL to another host.
3. `sv/index.html`: keep lines 1–(end of JSON-LD and meta) of the head as they are, swap the fonts URL and the `<style>` block for the stylesheet link; body from the sketch with the Copy strings above; video `src="/assets/film/sluseholmen-720.mp4" poster="/assets/film/sluseholmen-poster.jpg"`, the sketch's attributes, and a fallback to `.flow` when the video errors (a `<source>` with an `onerror` on it, or `error` listener in the existing inline script; no new script file). Add `<!-- film: Sluseholmen, Copenhagen — Pixabay video 262412, Pixabay content licence -->` next to the video, as the old images carried their credit. Keep the Cal.com script last, byte-identical; drop the reveal script.
4. `_includes/latest-letter-cover.html`: `{%- assign latest = site.beyond | sort: "date" | last -%}`; nothing when empty; otherwise the sketch's `section.brev#beyond`: the cover link to `latest.url | relative_url` with `aria-label="Senaste brevet: {{ latest.title | escape }}"`, `&`, "& Beyond · {{ latest.date | date: '%Y' }}", title, `latest.lead` when present (omit the span when absent), "Transformation & Beyond"; beside it tag "Senaste brevet", `h2` title, lead, links "Läs brevet →" (`latest.url`) and "Alla nummer" (`/beyond/`). Swedish only (026 decides the English variant). `lang="sv"` on the title.
5. Copy the two film files from the project folder. Check their size and type (`file`, `ls -l`).
6. Test before commit; screenshots; link check; PR as draft, `@codex review` with the focus "copy unchanged except the plan's list; head and JSON-LD byte-identical; no new host".

## Tests
- Test before commit (`check_html.py` over every `*.html`).
- `git diff master -- sv/index.html` shows the JSON-LD block and every `<meta>`/`<link rel="canonical|alternate">` line unchanged; `grep -c 'cal.com/conny-wadbro-impk9g/architecture-review' sv/index.html` is 1 and the script is byte-identical to master's.
- `grep -niE 'fonts\.(googleapis|gstatic)\.com' sv/index.html` lists only those hosts; `grep -nE 'Hanken|JetBrains|Schibsted|Sofia|Source\+Serif' sv/index.html assets/site.css` prints nothing; `grep -nE 'https?://' assets/site.css` prints nothing.
- Visible-text diff: extract text from master's and the branch's `/sv/` (a small HTMLParser script, the one used for planning is fine) and check every difference is in Copy strings; paste the diff in the response file.
- `grep -nE '[0-9] ?000 kr|kr/' sv/index.html` shows only the existing "75 000 kr" occurrences (offer and contact), none in `#efter`.
- Jekyll build (`jekyll build`, installed in the session if missing) twice: as committed (no letters: no `#beyond` section in `_site/sv/index.html`), and in a scratch copy with one sample letter in `_beyond/` (never committed) to screenshot the cover. If Jekyll cannot run in the session, say "not checked" in the response file.
- Playwright at 1440×900 and 390×844, full page after scrolling to the bottom; one more at 1440×900 with `reducedMotion: 'reduce'` (no film, lines still); one with the film URL blocked (`page.route`) showing the lines. `document.documentElement.scrollWidth <= innerWidth` at both widths. The `h1` box does not intersect the `.amp` glyph box at 1440×900 (compare `getBoundingClientRect`, or say why the overlap is the sketch's intended layering).
- Contrast: every text/background pair in `site.css` passes AA (list them in the response file).
- Link check of every `href` on `/sv/` (200, mail links excluded; blocked hosts "not checked").

## Risks / watch out for
- The sketch has the settings panel's switches all through its CSS; leaving a `body.x` rule without its class on `<body>` silently hides a block (`.brev`, `.prop`, `.mrow.prop`, `.q7`, `.roles` are `display:none` by default). The full-page screenshot must show the roles block, the Tillval rows, `#efter` and (with a sample letter) the cover.
- The founder line is a hard rail: same words, same order, as today.
- 2.3 MB film on the first screen: `preload="metadata"` and the poster keep the text first; do not add `preload="auto"`.
- `assets/site.css` is published; no comments in it that name people or decisions beyond what the page shows.
- `index.html` must keep working with its own inline styles and the old include; do not touch it or `_includes/latest-letter.html`.

## Out of scope
- `index.html` (026), `assets/beyond.css`, `/beyond/`, OG image, `_config.yml`, `404.html`, JSON-LD.

## Suggestions for PO
- 026: the English page with the approved English text from the underlag; the figure's axis and dot labels in English are not in the approved text, so 026 needs Conny's ok on them (proposal from the existing English gap sentence) before it is written; it also removes `_includes/latest-letter.html` and the `.latest-letter` CSS when nothing uses them.
