<!-- .team/reviews/025-poster-design-sv.response.md: the Builder's answers (CLOUD.md § Builder 4). Append a section per round; never edit the Judge's or Codex's text. -->

## Build notes — 2026-11-20
Plan attack: not required (Files touch no Adversarial or Human-merge path; not a Rulebook story).

Where the build departs from the sketch, and why:
- **Top scrim in the hero** (`.hero::before`, navy fading out over the top 120–200 px). Measured over 12 frames of the film, the nav and the wordmark (15–18 px, normal text) sat at 3.5:1 against the bright sky, below AA. With the scrim they measure 15.05:1 at 1440 and ≥12.4:1 at 390. Not in the sketch; needed for the WCAG AA criterion.
- **Reduced motion stops the lines.** The sketch's `.flow svg{animation:none}` loses to `.flow .f1/.f2{animation:…}` on specificity, so the lines kept moving. Now `.flow .f1,.flow .f2{animation:none}` under `prefers-reduced-motion: reduce` (measured: `animationName` = `none`).
- **Film fallback without body classes:** the `<video>`'s `onerror` adds `no-film` to `.hero`, which hides the film and shows the lines. No new script file.
- **The figure's colours** are classes (`.dot`, `.us`, `.us-l`) instead of inline `style`/`fill`, same values.
- **Founder row:** the `h3` holds "Conny Wadbro, grundare." and the text goes on "Studier i affärsrätt (Lund) · säljledning i konsultbranschen · verksam AI-arkitekt. **Ett gränsland, en rådgivare.**" The visible sequence is today's sentence, character for character, without a paragraph that opens on a comma.
- **Hero line:** today "Transformation<span class="amp-dev own">&</span>Beyond" (spaced by CSS) → "Transformation & Beyond" in plain text, same words, as in the sketch.
- The "→" in the stage labels carries `aria-hidden="true"` (decorative).
- The cover include drops the old block's week/date line (the sketch has none); the old `_includes/latest-letter.html` is untouched for `index.html`.

## Build checks — 2026-11-20
- Test before commit (`check_html.py` over every `*.html`): exit 0.
- `<head>`: lines 1–21 and 23 byte-identical to master (`diff` empty); only the Fonts URL (line 22) changes and `<link rel="stylesheet" href="/assets/site.css">` is added. The Cal.com script and the JSON-LD (last 24 lines) are byte-identical to master; `grep -c cal.com/conny-wadbro-impk9g/architecture-review sv/index.html` = 1.
- `grep -nE 'Hanken|JetBrains|Schibsted|Sofia|Source\+Serif' sv/index.html assets/site.css`: nothing. `grep -nE 'https?://' assets/site.css`: nothing.
- `grep -nE '[0-9] ?000 kr|kr/' sv/index.html`: the meta description (unchanged), the offer price and the contact line; nothing in `#efter`.
- Jekyll 4.4.1 (installed in the session): as committed, `_site/sv/index.html` has no `id="beyond"`; with one sample letter in `_beyond/` (scratch copy, not committed) the cover renders.
- Playwright (Chromium, H.264 "probably", film plays): `scrollWidth` = 1440 / 390, no horizontal scroll. Film shown and lines hidden by default; `reducedMotion: 'reduce'` → film `display:none`, lines shown, `animationName: none`; `*.mp4` aborted via `page.route` → `video.error.code` 4, `.hero.no-film`, lines shown and moving.
- h1 vs `&` at 1440×900: the boxes overlap (the `&` line box is 852 px tall) but the glyphs do not; pixel scan of the h1 rows, smallest gap between the h1's light pixels and the red glyph = 12 px, also under reduced motion. At 390 the boxes do not intersect.
- Every section the panel's switches could hide is on screen: `.roles`, `.q7`, the Tillval row, `#efter`, and (with the sample letter) `#beyond`.
- Screenshots in `.team/screenshots/025/`: `sv-1440.png`, `sv-390.png`, `sv-1440-reduced-motion.png`, `sv-1440-film-blocked.png`, plus `sv-1440-figure-in-view.png` and `sv-390-figure-in-view.png` (the figure's dots and labels fade in on a scroll-driven timeline, so a full-page shot taken at scroll 0 shows only its axes).

Contrast (AA), every text/background pair in `site.css`:
| Pair | Ratio |
|---|---|
| ink #14181B on paper #F8F6F1 | 16.53 |
| ink on salmon #F6E6DA | 14.67 |
| paper on navy #0C2233 | 15.05 |
| white on red #CF2318 (bands, button, layer Affär, tag on cover, `::selection`) | 5.38 |
| paper on red (nav links over the `&`, the `&` cover) | 4.98 |
| dark red #B01C13 on paper | 6.44 |
| dark red on salmon (question numbers, "Tillval") | 5.71 |
| grey #5B5F66 on paper (sources, caption) | 5.94 |
| paper on ink (layer Teknik, pill, hover, contact line) | 16.53 |
| footer #C6C8CC on ink | 10.66 |
| hero over the film, worst of 12 frames (95th-percentile background) | h1 3.78 (large text) at 1440, 6.28 at 390; hero text ≥11.3; nav ≥12.4 |
| red #CF2318 on navy | 3.02 — only the decorative `&`, never text |

Link check of every `href` on the built `/sv/` (with sample letter): anchors `#arbetssatt #grundaren #kontakt #praktiken #review` exist; `/`, `/assets/favicon.svg`, `/assets/site.css`, `/beyond/`, the letter, `/sv/` 200 locally; the Google Fonts CSS URL 200. **Not checked** (the session's proxy blocks the host): dignami.com (3 URLs), mondmodel.com, the R2 sample PDF, transformationbeyond.se (canonical/hreflang), cal.com. All of these URLs are unchanged from master. Mail links excluded.

Visible text, master `/sv/` → branch `/sv/` (both built by Jekyll; branch with the sample letter, so the cover lines show; `alt`/`aria-label` prefixed). Every difference is in the plan's Copy strings or listed above:
```diff
1,3c1
< Transformation
< &
< Beyond
---
> Transformation & Beyond
10,15d7
< Boka ett inledande samtal
< Rådgivning · Affär × Juridik × AI
< AI-rådgivning för ledningsgruppen —
< affär, juridik och AI
< hos en rådgivare.
< Transformation
17c9,11
< Beyond ger råd till nordiska företag som tar AI från pilot till granskningsbar drift.
---
> AI-rådgivning
> för ledningsgruppen — affär, juridik och AI hos en rådgivare.
> Transformation & Beyond ger råd till nordiska företag som tar AI från pilot till granskningsbar drift.
20,21d13
< Boka ett inledande samtal
< Granska bevisen först →
25,29c17,30
< [alt] Topografiska höjdkurvor i bronston
< Varför vi finns
< De stora konsultbolagen förstår er verksamhet men bygger inte tekniken. AI-labben bygger tekniken men förstår inte er verksamhet.
< Vi sitter i glappet
< , små med avsikt, som de främsta advokatbyråerna.
---
> Boka ett inledande samtal
> →
> Granska bevisen först
> →
> De stora konsultbolagen förstår er verksamhet men bygger inte tekniken.
> AI-labben bygger tekniken men förstår inte er verksamhet.
> Principskiss, inga mätvärden.
> [aria-label] Principskiss med två axlar: förstår er verksamhet och bygger tekniken. De stora konsultbolagen ligger högt på den första och lågt på den andra, AI-labben tvärtom, Transformation & Beyond högt på båda.
> Förstår er verksamhet →
> Bygger tekniken →
> AI-labben
> De stora konsultbolagen
> Transformation & Beyond
> Vi sitter i glappet, små med avsikt, som de främsta advokatbyråerna.
31,34c32,33
< Varje disciplin är vanlig.
< Kombinationen hos en och samma rådgivare är det inte.
< [aria-label] Three fine-lined horizontal strata representing business, legal, and AI architecture, separated by gaps, crossed by a single bronze bridging bar that overshoots past the bottom ruled line
< 01 · Affär
---
> Varje disciplin är vanlig. Kombinationen hos en och samma rådgivare är det inte.
> Affär
37c36
< 02 · Juridik
---
> Juridik
40c39
< 03 · Teknik
---
> Teknik
44c43,44
< 01 · Här
---
> T&B · projekt
> Här
47,48c47,48
< T&B · projekt
< 02 · Dignami
---
> Dignami · uppdrag
> →
51,52c51,52
< Dignami · uppdrag
< 03 · Dignami AOS
---
> Dignami · plattform
> →
58d57
< Dignami · plattform
68a68,82
> Tillval
> Vilken leverantör ska ni välja, och vad står i avtalet?
> Samma frågor, för den som ska svara på dem
> VD
> Vad ska automatiseras, och vad ska inte det?
> Vem äger förändringen?
> CFO
> Hur ser ekonomin egentligen ut?
> Hur säkrar ni kostnaden för tokens?
> Chefsjurist
> Vem äger vilket AI-beslut?
> Vad står i leverantörsavtalet, och vad behöver er jurist ta ställning till?
> Styrelse
> Var står AI-verksamheten egentligen?
> Vilka beslut behöver styrelsen fatta, och på vilket underlag?
91a106,107
> Tillval
> Leverantörsval och avtal. Vilken leverantör och modell som passar er, och vilka avtalsvillkor ni bör granska: dataanvändning, lagring, ansvar och utträde. Vi formar underlaget. Er jurist ger den juridiska rådgivningen.
93a110,124
> Efter genomlysningen
> Tre vägar vidare. Ingen av dem är ett krav.
> T&B · projekt
> Här
> Granskning före skalning
> För er som har en pilot. Tre till fyra veckor, fast omfattning: ekonomi och tokenkostnad, ägande, AI-förordningen och GDPR, avtalet och kriterierna för att ta piloten i drift.
> T&B · löpande
> Här
> Löpande beslutsstöd
> Ett månadsupplägg för ledning och styrelse. Efter varje pass får ni ett skriftligt underlag där varje påstående har en källa.
> Dignami · uppdrag
> →
> Assurance
> Om ledningen vill gå vidare kan rekommendationerna från genomlysningen fortsätta genom Dignami Assurance.
> Underlaget står på egna ben. Att avstå från att investera är ett giltigt utfall.
96d126
< Plattform
98c128,129
< — efterlevnadsplattform för reglerad rådgivning: WORM-arkiv, hashkedja, policyspärr. Arkitekturbesluten visas på begäran.
---
> Plattform
> Efterlevnadsplattform för reglerad rådgivning: WORM-arkiv, hashkedja, policyspärr. Arkitekturbesluten visas på begäran.
102d132
< I produktion
104c134,135
< — AI-driven redaktionsplattform.
---
> I produktion
> AI-driven redaktionsplattform.
108d138
< Metod
110c140,142
< — arkitekturbesluten dokumenteras medan vi bygger. Visas på begäran innan ni anlitar oss.
---
> Metod
> Arkitekturbesluten dokumenteras medan vi bygger. Visas på begäran innan ni anlitar oss.
> Conny Wadbro, grundare.
112,113c144
< Conny Wadbro
< , grundare. Studier i affärsrätt (Lund) · säljledning i konsultbranschen · verksam AI-arkitekt.
---
> Studier i affärsrätt (Lund) · säljledning i konsultbranschen · verksam AI-arkitekt.
115c146,156
< [alt] Bergskikt i lager, i bronston
---
> [aria-label] Senaste brevet: Vems namn står på utfallet?
> &
> & Beyond · 2026
> Vems namn står på utfallet?
> Arbetet går att delegera till AI. Ansvaret gör det inte.
> Transformation & Beyond
> Senaste brevet
> Vems namn står på utfallet?
> Arbetet går att delegera till AI. Ansvaret gör det inte.
> Läs brevet →
> Alla nummer
118a160
> →
```

## Codex round 1 — 2026-11-20
- No findings ("Didn't find any major issues", reviewed `027384a`, focus: copy, head/JSON-LD, hosts, hard rails, build notes).

## Outcome
built-by: claude
model: claude-opus-5-5
parts: none
missed: the sketch's hero let the film's bright sky sit behind the nav (3.5:1), and its reduced-motion rule did not stop the lines; both fixed in the build.
