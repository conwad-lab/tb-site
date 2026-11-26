---
id: 038
verdict: plan
---

# Plan 038 — The core words on the first screen

Story: `.team/backlog/038-core-words-first-screen.md`

## Approach
One `<p class="tag">` line goes in directly before the hero `<h1>` on each home page, and two CSS rules in `assets/site.css` make it sit above the absolutely positioned `.amp` glyph and give its square marker the text colour, as `.end .tag::before` already does on the dark contact band. Colour of the dots: the row says red if it holds WCAG AA against the film, else the text colour. Red `#CF2318` against the navy `#0C2233` under the film is 3.0:1 (relative luminance 0.145 vs 0.015), under 4.5:1 for 15 px text, and the film only lightens the background, so the dots stay plain characters in the text colour (`--on-blue`); no `span`. Touches the price block: no. Booking CTA: no. Footer: no.

## Baseline
`master` at 744af50 (035 merged as #90, 036 as #95, 037 as #93): Test before commit exits 0, `bin/test-hero-first-screen.py` and `bin/test-hero-motion.py` print `ok`. Screenshots could not be taken at planning time (no browser in the planning run); the Builder's before-shots of `/` and `/sv/` at 1440×900 and 390×844 are the baseline. If in an "after" shot the booking band drops below the first screen or the `h1` collides with the `&`, the Builder stops with `blocked` and the measured heights instead of widening the order; the Coordinator plans the next step as a new story.

## Estimate
size: S
risk: plain
files: 4
codex-rounds: 1
builder: codex-cli — markup, CSS and the test are settled in the work order
codex-model: sol — S plain story
model: light — Codex builds; the Builder thread posts the order, runs screenshots and the link check

## Files
- `index.html` — one new line before the hero `<h1>`.
- `sv/index.html` — one new line before the hero `<h1>`.
- `assets/site.css` — two new rules after the `.hero h1:lang(en)` rule.
- `bin/test-hero-core-words.py` — new Proof test.
- `.team/**` — response file, papercuts (Builder only).

## Copy strings (old → new)
- `index.html` hero: (none) → "Understand · Rethink · Rebuild"
- `sv/index.html` hero: (none) → "Förstå · Ompröva · Bygg om"

## Work order
```
Goal: Add the core-words label line directly above the hero h1 on both home pages, in the existing .tag style, changing nothing else.
May touch:
index.html
sv/index.html
assets/site.css
bin/test-hero-core-words.py
Steps:
1. index.html: directly before the line '    <h1>Commercial excellence, law and&nbsp;AI — in one advisor, not three consultancies.</h1>' insert the line '    <p class="tag">Understand · Rethink · Rebuild</p>' (four spaces indent; each dot is U+00B7 MIDDLE DOT with one space on each side). Nothing else in the file changes.
2. sv/index.html: directly before the line that starts '    <h1><span class="nb">AI-rådgivning</span>' insert the line '    <p class="tag">Förstå · Ompröva · Bygg om</p>' (same indent and U+00B7 dots). Nothing else in the file changes.
3. assets/site.css: directly after the line starting '.hero h1:lang(en){' insert these two lines, nothing else in the file changes:
.hero .tag{position:relative}
.hero .tag::before{background:var(--on-blue)}
4. New file bin/test-hero-core-words.py, python3 stdlib only, executable, one line per failure on stdout and exit 1, print "ok" and exit 0 otherwise. Checks:
   a. For (index.html, "Understand · Rethink · Rebuild") and (sv/index.html, "Förstå · Ompröva · Bygg om"), parsing with html.parser: inside the element with class "hero", the first start tag after the label's </p> that is not whitespace is <h1>, the label is a <p> with class exactly "tag" and text exactly the string (U+00B7 dots), and the string occurs exactly once inside the hero.
   b. Each page still has exactly one <h1>, and the number of h2–h6 start tags is the same as in the page with the label line removed (that is, the label adds no heading).
   c. assets/site.css contains the lines ".hero .tag{position:relative}" and ".hero .tag::before{background:var(--on-blue)}", and the rules starting ".tag{", ".tag::before{" and ".hero{" are byte-identical to: ".tag{font-size:15px;font-weight:700;margin:0 0 clamp(22px,3vw,40px);display:flex;align-items:center;gap:10px}", ".tag::before{content:\"\";width:14px;height:14px;background:var(--red);flex:none}" and the .hero line as it stands in the file before your change (copy it into the test).
Proof: bin/test-hero-core-words.py — python3 bin/test-hero-core-words.py
Must not: commit or push; touch any file not under May touch; add dependencies; weaken a check to make it pass; change any other text, link, price, colour, class, element, the film, the diagram, bin/test-hero-first-screen.py or bin/test-hero-motion.py; add text-transform or letter-spacing.
```

## Steps (Builder thread)
1. Open issue `038: The core words on the first screen`.
2. Post the CLI work order from `templates/codex.md` with `Branch: feat/038-core-words`, `Plan: .team/plans/038-core-words-first-screen.md`, `PR title: 038: The core words on the first screen`, `Model: sol`, then the work order above unchanged; add the label `codex-cli`. Reminders at about 15 min and at the hour; fallback per `team/CODEX-CLI.md` [K6].
3. On `done`: Test before commit on the poller's head, `python3 bin/test-hero-core-words.py`, `python3 bin/test-hero-first-screen.py`, `python3 bin/test-hero-motion.py`; on the Jekyll build, first-screen screenshots before/after at 1440×900 and 390×844 of `/` and `/sv/` (band in view, `h1` clear of the `&`), and with the film off (reduced motion) once per page. Link check. `@codex review`.
4. Response file with `built-by: codex-cli` in its Outcome and the run's Hinder line quoted.

## Tests
- `bin/test-hero-core-words.py` (Proof) and Test before commit (`check_html.py` on every page).
- `bin/test-hero-first-screen.py`, `bin/test-hero-motion.py` unchanged and green.
- Builder: Step 3 (screenshots, link check).

## Risks / watch out for
- The label adds about 40–60 px above the `h1`; at 390×844 that may push the booking band under the fold (035 lowered the hero to 86svh). The screenshots decide; the Builder reports `blocked` rather than shrinking anything.
- Without `position:relative` the static label would paint under the positioned `.amp` glyph; step 3 covers it.
- The `.tag` bottom margin (22–40 px) sets the gap to the `h1`; kept as is.

## Out of scope
- Uppercase or letter-spacing, any new colour, the headline, the film, the hero height.

## Suggestions for PO
- The Kö row describes `.tag` as "versaler, spärrad", but the site's `.tag` is bold 15 px in normal case with a square marker; nothing on the site uses uppercase. This plan follows the row's operative instruction ("samma stil som befintliga `.tag`-etiketter") and adds no new style. If Conny wants the line in spaced capitals, that is a new row (and a new style on the site).
- The marker square on the hero takes the text colour, as on the contact band, for the same contrast reason as the dots.
