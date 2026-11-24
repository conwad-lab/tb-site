---
id: 035
verdict: plan
---

# Plan 035 — A lower first screen on the home pages

Story: `.team/backlog/035-first-screen-lower-hero.md`

## Approach
One CSS value changes: `.hero{... min-height:100svh ...}` becomes `min-height:86svh` in `assets/site.css`, so the booking band under the hero enters the first screen. The diagram's `aria-label` was checked against the visible axis texts (x: "Understands your business", y: "Builds the technology"; labs low on x and high on y, giants the other way, Transformation & Beyond high on both) and matches on both pages, so it is not touched; the new test pins that. Touches the price block: no. Booking CTA: no. Footer: no.

## Baseline
`master` at 17aae53 (034 merged as #81): Test before commit exits 0. The Builder takes screenshots of `/` and `/sv/` first screen at 1440×900 and 390×844 for before/after. Screenshots could not be taken at planning time (no browser in the routine's planning run); the Builder's before-shots are therefore the baseline that decides whether the one-value order can meet the acceptance criteria. If at 390×844 or 125 % zoom the band stays below the fold because the hero's content is taller than 86svh, the Builder stops with `blocked` and the measured heights instead of widening the order; the Coordinator then plans the next step (a smaller `padding-top` or headline size) as a new story.

## Estimate
size: S
risk: plain
files: 2
codex-rounds: 1
builder: codex-cli — the value and the test are settled in the work order
codex-model: astra — host default, as in plans 029–033
model: light — Codex builds; the Builder thread posts the order, runs screenshots and the link check

## Files
- `assets/site.css` — the `.hero` rule, one value.
- `bin/test-hero-first-screen.py` — new Proof test.
- `.team/**` — response file, papercuts (Builder only).

## Copy strings (old → new)
- None.

## Steps (Builder thread)
1. Open issue `035: A lower first screen on the home pages`.
2. Post the work order below unchanged as one comment with the header lines the poller reads, `Branch: feat/035-lower-hero`, without a `Model:` line, then add the label `codex-cli`. Reminders at about 15 min and at the hour; fallback per `team/CODEX-CLI.md` [K6].
3. On `done`: Test before commit on the poller's head, `python3 bin/test-hero-first-screen.py`, `python3 bin/test-hero-motion.py`, and on the Jekyll build screenshots before/after at 1440×900 and 390×844 of `/` and `/sv/` (also 125 % zoom on `/`), the red booking band in view. Link check. `@codex review`.
4. Response file with `built-by: codex-cli` in its Outcome and the run's Hinder line quoted.

## Work order
```
Goal: Lower the hero on both home pages from 100svh to 86svh so the booking band shows on the first screen, changing nothing else.
May touch:
assets/site.css
bin/test-hero-first-screen.py
Steps:
1. assets/site.css line 29 starts with ".hero{position:relative;isolation:isolate;" and contains "min-height:100svh". Replace only "min-height:100svh" with "min-height:86svh" in that line. Nothing else in the file changes.
2. New file bin/test-hero-first-screen.py, python3 stdlib only, executable, one line per failure on stdout and exit 1, print "ok" and exit 0 otherwise. Checks:
   a. In assets/site.css the line starting ".hero{" contains "min-height:86svh" and the file contains no "min-height:100svh" in any rule starting ".hero".
   b. In index.html the <svg viewBox="0 0 520 360" ...> aria-label contains "understands your business" before "builds the technology" (case-insensitive), and the visible <text> elements inside that svg contain "Understands your business" and "Builds the technology".
   c. The same for sv/index.html with "förstår er verksamhet" before "bygger tekniken" and the visible texts "Förstår er verksamhet" and "Bygger tekniken" (read the visible texts from the file; if their spelling differs, use the file's spelling and say so in the Hinder line).
Proof: bin/test-hero-first-screen.py — python3 bin/test-hero-first-screen.py
Must not: commit or push; touch any file not under May touch; add dependencies; weaken a check to make it pass; change any text, link, price, colour, element, class name, index.html, sv/index.html, the film or the diagram.
```

## Tests
- `bin/test-hero-first-screen.py` (Proof) and Test before commit (`check_html.py` on every page).
- Builder: Step 3 (screenshots, link check).

## Risks / watch out for
- `min-height` in svh with a longer English headline: the hero grows past 86svh if its content needs it; that is fine, the screenshots at 125 % zoom show whether the band still shows.
- Swedish axis texts may be spelled differently from the aria-label's; check c lets the Codex adapt and report it.

## Out of scope
- Headline size, film length, any new section.
