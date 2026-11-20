---
id: 026
verdict: plan
---

# Plan 026 — The English home page in the poster design

Story: `.team/backlog/026-poster-design-en.md`

## Approach
Rebuild the body of `index.html` from `sv/index.html` as merged in 025 (2edf70e): same sections, classes, film, fallback, stylesheet and Cal.com script, with the English text from today's `index.html` and the approved new English text below. Keep today's English `<head>` except the fonts URL and the stylesheet link, and drop the inline `<style>` and the reveal script. Generalise `_includes/latest-letter-cover.html` with a `lang` parameter (Swedish default, so `/sv/` renders the same) and delete the old `_includes/latest-letter.html`. Read `.team/reviews/025-poster-design-sv.response.md` first: its departures from the sketch (top scrim, reduced-motion fix, `no-film` fallback on `.hero`, figure classes, founder row in the `h3`) apply here too.

Touches the price block: form only, text unchanged. Booking CTA: form only (bands; the nav button "Book a scoping call" removed as on `/sv/`); Cal.com URL, script and mailto fallback unchanged. Footer: form only, text unchanged.

## Baseline
`master` at 2edf70e: Test before commit exits 0; Playwright full-page screenshots of `/` and `/sv/` from a `jekyll build` at 1440×900 and 390×844; link check of every `href` on `/`.

## Estimate
size: M
risk: plain
files: 3
codex-rounds: 2
builder: claude — a port of 025's markup with exact strings and visual checks at two widths
model: standard — M plain; every choice is made in 025 and this plan

## Files
- `index.html` — body rebuilt as `sv/index.html`; `<head>` fonts URL as in `sv/index.html`, inline `<style>` replaced by `<link rel="stylesheet" href="/assets/site.css">`; front matter, title, meta, canonical, hreflang, OG and JSON-LD byte-identical; reveal script removed; Cal.com script byte-identical.
- `_includes/latest-letter-cover.html` — `lang` parameter: `include.lang == "en"` → English labels; anything else → today's Swedish output, byte-identical.
- `_includes/latest-letter.html` — deleted (only `index.html` used it).
- `assets/site.css` — only if the English text needs a rule (e.g. the longer `h1`); name it in the response file.
- `.team/**` — response file, screenshots, papercuts (Builder only).

## Copy strings (old → new, `index.html`)
Every other visible string, `alt` and `aria-label` stays character for character.
- Nav: the button "Book a scoping call" → removed (as on `/sv/`). Mark and the four section links and "& Beyond" unchanged.
- Hero eyebrow "Advisory · Commercial excellence × Law × AI" → removed.
- `h1` "Commercial excellence, law and&nbsp;AI —<br><em>in one advisor</em>, not three consultancies." → "Commercial excellence, law and&nbsp;AI — in one advisor, not three consultancies." (same words, no line break, no italic).
- Lede "Transformation<span class="amp-dev own">&amp;</span>Beyond advises Nordic companies …" → "Transformation &amp; Beyond advises Nordic companies …" (same words, as 025 did).
- Hero CTA "Book a scoping call" (button) → band, same text, `href="#kontakt"`; "Examine the proof first →" → thin band "Examine the proof first", arrow as an `aria-hidden` span, same URL.
- The two `mat-band` images and their alt texts → removed.
- "Why we exist": eyebrow → removed; the figure's text column holds "The consulting giants understand your business but don't build the technology." and "The AI labs build the technology but don't understand your business."; the line under it "We sit in the gap — small by design, like the elite law firms." (same words, no italic).
- New figure (approved by Conny 2026-11-20): axis texts "Understands your business →" and "Builds the technology →"; dot labels "The AI labs", "The consulting giants", "Transformation & Beyond"; caption "Illustrative sketch, no measured data."; `aria-label` "Illustrative sketch with two axes: understands your business and builds the technology. The consulting giants sit high on the first and low on the second, the AI labs the other way round, Transformation & Beyond high on both." Replaces the strata SVG and its `aria-label`.
- "What we do": "Each discipline is common. **The combination in a single advisor is not.**" → `h2`, same sentence, no bold. Keys "01 · Business", "02 · Law", "03 · Technology" → `h3` "Business", "Law", "Technology"; sub-headings and paragraphs unchanged.
- "How we work": keys "01 · Here", "02 · Dignami", "03 · Dignami AOS" → removed; each stage shows its existing `who` label with "Here" on the first and "→" (`aria-hidden`) on the others, as on `/sv/`.
- "The questions we answer": six unchanged. New (approved 2026-11-20): "**Optional** Which vendor should you choose, and what does the contract say?"; block "The same questions, for the person who has to answer them" with **CEO** "What should be automated, and what should not?" / "Who owns the change?"; **CFO** "What do the economics actually look like?" / "How do you secure the cost of tokens?"; **General Counsel** "Who owns which AI decision?" / "What does the vendor contract say, and what does your lawyer need to take a position on?"; **Board** "Where does the AI operation actually stand?" / "Which decisions does the board need to make, and on what basis?".
- Offer: same text; new row before "After" (approved): "**Optional** Vendor selection and contract. Which vendor and model fit you, and which contract terms you should examine: data use, storage, liability and exit. We shape the memo. Your lawyer gives the legal advice." No price on it.
- New section `#efter` before "Who you get" (approved): tag "After the review"; `h2` "Three ways forward. None of them is required."; stages "T&B · project / Here" **Review before scaling** "For teams with a pilot. Three to four weeks, fixed scope: economics and token cost, ownership, the EU AI Act and GDPR, the contract, and the criteria for taking the pilot into operation."; "T&B · ongoing / Here" **Ongoing decision support** "A monthly arrangement for management and board. After each session you receive a written memo in which every claim has a source."; "Dignami · engagement / →" **Assurance** "If management decides to go further, review recommendations can continue through Dignami Assurance."; note "The memo stands on its own. Deciding not to invest is a valid outcome." No price in the section.
- "Who you get": proof rows in 025's form; "— compliance platform …", "— AI-driven editorial platform.", "— architecture decisions …" lose the dash and start with a capital. **Founder row**: as 025 did, `h3` "Conny Wadbro, founder." and the text "Commercial law studies (Lund) · sales leadership in consulting · working AI architect. **One borderland, one advisor.**" — the visible sequence is today's sentence, character for character.
- Latest letter: `{% include latest-letter.html lang="en" %}` → `{% include latest-letter-cover.html lang="en" %}` with today's English labels: tag "Latest letter (in Swedish)", links "Read the letter →" and "All letters", cover `aria-label` "Latest letter: <title>"; the title and lead keep `lang="sv"` (the letters are Swedish).
- Contact: same `h2`, CTA text, price line and address, in 025's form.
- Footer: same five items and texts (with today's English year line, reg. no line, "& Beyond — weekly letter (in Swedish)", Dignami link, "På svenska" with `lang="sv"`), in 025's form.

## Steps
1. Branch `feat/026-poster-design-en`. Read the 025 response file, `sv/index.html`, `assets/site.css` and today's `index.html`.
2. `_includes/latest-letter-cover.html`: assign the four labels by `include.lang`; Swedish output unchanged byte for byte (check with a `jekyll build` diff of `_site/sv/index.html` before and after, with a scratch sample letter).
3. `index.html` per Copy strings; `sv/index.html` is the template for markup, today's `index.html` for text.
4. `git rm _includes/latest-letter.html`; `grep -rn 'latest-letter.html' --include=*.html .` prints nothing.
5. Test before commit; screenshots; link check; PR as draft; `@codex review` with the focus "copy unchanged except the plan's list; head and JSON-LD byte-identical; /sv/ output unchanged".

## Tests
- Test before commit.
- `<head>` and JSON-LD diff against master as in 025; `grep -c 'cal.com/conny-wadbro-impk9g/architecture-review' index.html` is 1, script byte-identical.
- Visible-text diff of `/` (master vs branch) matches Copy strings; pasted in the response file.
- `jekyll build`: `_site/sv/index.html` identical to master's build (with and without a scratch letter); `_site/index.html` has no `id="beyond"` without letters and the English cover with one.
- Playwright as in 025 for `/` (1440, 390, reduced motion, film blocked), plus `/sv/` at both widths; `scrollWidth <= innerWidth`; the `h1` glyphs clear of the `&` at 1440×900 (025's pixel method).
- `grep -nE 'SEK' index.html` shows only today's occurrences; none in `#efter`.
- Link check of every `href` on `/`.

## Risks / watch out for
- The English `h1` is about twice as long as the Swedish; check it at 1440 and 390 against the `&` before touching `site.css`. A size change for English only goes as a `:lang(en)` rule, never a change to the Swedish look.
- The include edit must not change `/sv/`.
- Founder row and legal sentences are hard rails: same words, same order.

## Out of scope
- `sv/index.html`, `assets/beyond.css`, `/beyond/`, OG image, `_config.yml`, `404.html`, JSON-LD.

## Suggestions for PO
- After 026: `assets/beyond.css` and `/beyond/` in the new colours, and a new OG image (both named in the underlag as their own stories).
