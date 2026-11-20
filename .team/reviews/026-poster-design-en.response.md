<!-- .team/reviews/026-poster-design-en.response.md: the Builder's answers (CLOUD.md § Builder 4). Append a section per round; never edit the Judge's or Codex's text. -->

## Build notes — 2026-11-20
Plan attack: not required (Files touch no Adversarial or Human-merge path; not a Rulebook story).

- `index.html`: body rebuilt from `sv/index.html` (2edf70e) with today's English text and the plan's Copy strings; no Skåne section. The 025 departures carry over as they are in `sv/index.html` (top scrim, reduced-motion rule, `no-film` on `.hero`, figure classes, founder row in the `h3`).
- **`assets/site.css`, one rule** (allowed by the story's last criterion): `.hero h1:lang(en){font-size:clamp(40px,5.4vw,96px)}`. At the shared size (7vw, 101 px at 1440) the English `h1` ran 1000 px wide and "AI" and "not" sat on the `&` glyph (screenshot checked). With the rule the `h1` box ends at x=835 and the `&` box starts at x=880 at 1440×900 (also clear at 1024 and 800 px wide); at 390 the clamp's 40 px floor applies as before, so the phone size is unchanged. `:lang(en)` only, the Swedish page is untouched (`_site/sv/index.html` byte-identical, see checks).
- **Mark link** `href="#"` → `href="/"` (as `/sv/` points to `/sv/`); text unchanged.
- **Footer**: the inline SVG mark before "© 2026" is gone (025's footer has none); the five texts are unchanged.
- **Cover include**: `lang="en"` gives the English tag, link texts and `aria-label` prefix; the lead also gets `lang="sv"` on `/` (on `/sv/` it has none, byte-identical). The old include's "Week NN · date" line is not in the cover (as in 025). The `<p>` with or without `lang` is written as two whole start tags in an `if`, because `check_html.py` reads `<p{{ … }}>` as an unclosed tag.
- Removed with the inline `<style>`: the reveal script, the two `mat-band` images, the strata SVG (all in the plan).

## Build checks — 2026-11-20
- Test before commit (`check_html.py` over every `*.html`): exit 0.
- `<head>`: lines 1–19 byte-identical to master; line 20 is the Fonts URL from `sv/index.html`; line 21 (favicon) unchanged; line 22 the stylesheet link. Cal.com script + JSON-LD + `</html>` (last 23 lines) byte-identical to master (`diff` empty). `grep -c cal.com/conny-wadbro-impk9g/architecture-review index.html` = 1.
- `grep -n SEK index.html`: the meta description, the offer price and the contact line, as on master; none in `#efter`, none on the Optional row.
- `grep -rn 'latest-letter.html' --include=*.html .`: nothing.
- Jekyll 4.4.1: `_site/sv/index.html` from master and from this branch are byte-identical (`cmp`), without letters and with one scratch sample letter (not committed). `_site/index.html` has no `id="beyond"` without letters and the English cover with one.
- Playwright (Chromium, sample letter in the build): `scrollWidth` = 1440 / 390. Film shown, lines hidden by default; `reducedMotion: 'reduce'` → film `display:none`, lines shown; `*.mp4` aborted → `video.error.code` 4, `.hero.no-film`, lines shown. All five figure labels inside the SVG box at both widths.
- Contrast: CSS colours unchanged from 025 (table in its response file). The hero `h1` over the film, measured as in 025 (12 frames, 95th-percentile background behind the `h1` box with text and `&` hidden): 3.27 at 1440 (large text, 75 px; AA 3.0), 4.05 at 390.
- Screenshots in `.team/screenshots/026/`: `en-1440.png`, `en-390.png`, `en-1440-reduced-motion.png`, `en-1440-film-blocked.png`, `en-1440-figure-in-view.png`, `en-390-figure-in-view.png`, `sv-1440.png`, `sv-390.png`.
- Link check of every `href`/`src` on the built `/` (with sample letter): anchors `#arbetssatt #grundaren #kontakt #praktiken #review` exist; `/`, `/sv/`, `/beyond/`, the letter, `/assets/site.css`, `assets/favicon.svg`, the film and its poster 200 locally; the Google Fonts CSS URL 200. **Not checked** (the session's proxy blocks the host): dignami.com (3 URLs), mondmodel.com, the R2 sample PDF, transformationbeyond.se (canonical/hreflang), cal.com. All unchanged from master. Mail links excluded.

Visible text, master `/` → branch `/` (both built by Jekyll with the sample letter; `alt`/`aria-label` prefixed). Every difference is in the plan's Copy strings or listed above:
```diff
1,3c1
< Transformation
< &
< Beyond
---
> Transformation & Beyond
10,15d7
< Book a scoping call
< Advisory · Commercial excellence × Law × AI
< Commercial excellence, law and AI —
< in one advisor
< , not three consultancies.
< Transformation
17c9,10
< Beyond advises Nordic companies taking AI from pilot to auditable operations.
---
> Commercial excellence, law and AI — in one advisor, not three consultancies.
> Transformation & Beyond advises Nordic companies taking AI from pilot to auditable operations.
20,21d12
< Book a scoping call
< Examine the proof first →
25,29c16,29
< [alt] Topographic contour layers in bronze duotone
< Why we exist
< The consulting giants understand your business but don't build the technology. The AI labs build the technology but don't understand your business.
< We sit in the gap
< — small by design, like the elite law firms.
---
> Book a scoping call
> →
> Examine the proof first
> →
> The consulting giants understand your business but don't build the technology.
> The AI labs build the technology but don't understand your business.
> Illustrative sketch, no measured data.
> [aria-label] Illustrative sketch with two axes: understands your business and builds the technology. The consulting giants sit high on the first and low on the second, the AI labs the other way round, Transformation & Beyond high on both.
> Understands your business →
> Builds the technology →
> The AI labs
> The consulting giants
> Transformation & Beyond
> We sit in the gap — small by design, like the elite law firms.
31,34c31,32
< Each discipline is common.
< The combination in a single advisor is not.
< [aria-label] Three fine-lined horizontal strata representing business, legal, and AI architecture, separated by gaps, crossed by a single bronze bridging bar that overshoots past the bottom ruled line
< 01 · Business
---
> Each discipline is common. The combination in a single advisor is not.
> Business
37c35
< 02 · Law
---
> Law
40c38
< 03 · Technology
---
> Technology
44c42,43
< 01 · Here
---
> T&B · project
> Here
47,48c46,47
< T&B · project
< 02 · Dignami
---
> Dignami · engagement
> →
51,52c50,51
< Dignami · engagement
< 03 · Dignami AOS
---
> Dignami · platform
> →
58d56
< Dignami · platform
68a67,81
> Optional
> Which vendor should you choose, and what does the contract say?
> The same questions, for the person who has to answer them
> CEO
> What should be automated, and what should not?
> Who owns the change?
> CFO
> What do the economics actually look like?
> How do you secure the cost of tokens?
> General Counsel
> Who owns which AI decision?
> What does the vendor contract say, and what does your lawyer need to take a position on?
> Board
> Where does the AI operation actually stand?
> Which decisions does the board need to make, and on what basis?
85a99,100
> Optional
> Vendor selection and contract. Which vendor and model fit you, and which contract terms you should examine: data use, storage, liability and exit. We shape the memo. Your lawyer gives the legal advice.
87a103,117
> After the review
> Three ways forward. None of them is required.
> T&B · project
> Here
> Review before scaling
> For teams with a pilot. Three to four weeks, fixed scope: economics and token cost, ownership, the EU AI Act and GDPR, the contract, and the criteria for taking the pilot into operation.
> T&B · ongoing
> Here
> Ongoing decision support
> A monthly arrangement for management and board. After each session you receive a written memo in which every claim has a source.
> Dignami · engagement
> →
> Assurance
> If management decides to go further, review recommendations can continue through Dignami Assurance.
> The memo stands on its own. Deciding not to invest is a valid outcome.
90d119
< Platform
92c121,122
< — compliance platform for regulated advice: WORM archive, hash chain, policy gate. Architecture decisions available on request.
---
> Platform
> Compliance platform for regulated advice: WORM archive, hash chain, policy gate. Architecture decisions available on request.
96d125
< In production
98c127,128
< — AI-driven editorial platform.
---
> In production
> AI-driven editorial platform.
102d131
< Method
104c133,135
< — architecture decisions recorded as we build. Available on request before you engage us.
---
> Method
> Architecture decisions recorded as we build. Available on request before you engage us.
> Conny Wadbro, founder.
106,107c137
< Conny Wadbro
< , founder. Commercial law studies (Lund) · sales leadership in consulting · working AI architect.
---
> Commercial law studies (Lund) · sales leadership in consulting · working AI architect.
108a139,144
> [aria-label] Latest letter: Vems namn står på utfallet?
> &
> & Beyond · 2026
> Vems namn står på utfallet?
> Arbetet går att delegera till AI. Ansvaret gör det inte.
> Transformation & Beyond
110,111d145
< Week 47 ·
< 16 November 2026
112a147
> Arbetet går att delegera till AI. Ansvaret gör det inte.
115d149
< [alt] Layered rock strata in bronze duotone
118a153
> →
```

## Outcome
built-by: claude
model: claude-opus-5-5
parts: none
missed: the plan expected the longer English h1 might need a rule; it did (a `:lang(en)` size).
