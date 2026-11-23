---
id: 031
verdict: plan
---

# Plan 031 — The film's pause button shows only a pause or play symbol

Story: `.team/backlog/031-pause-button-icon-only.md`

## Approach
The button from 029 keeps its place, its script and its labels; only what it shows changes. Its text is replaced by two small inline SVG icons (pause bars, play triangle), and its accessible name moves to `aria-label`, which the script swaps instead of `textContent`. CSS shows one icon or the other from the existing `.hero.paused` class, and restyles the button as a 40 px circle with a thin half-opacity border on a 50 % navy backing. Because `display:grid` beats the browser's `[hidden]` rule, `.motion[hidden]{display:none}` keeps the button hidden for reduced motion and no JavaScript. `bin/test-hero-motion.py` is updated to pin the new facts. Codex CLI (Astra) builds it from the work order below. Touches the price block: no. Booking CTA: no. Footer: no.

## Baseline
`master` at ff70bc4 (029 merged as #70, 030 merged): `python3 bin/test-hero-motion.py` and Test before commit exit 0; the Builder takes screenshots of `/` and `/sv/` first screen at 1440×900 and 390×844, playing and paused, for before/after.

## Estimate
size: S
risk: plain
files: 4
codex-rounds: 2
builder: codex-cli — markup, icons, CSS values and script line are all settled in the work order
codex-model: astra — accessibility details (hidden override, accessible name) reward the stronger model
model: light — Codex builds; the Builder thread posts the order, runs screenshots, contrast and the link check

## Files
- `index.html` — the button's content and attributes, one script line.
- `sv/index.html` — the same with Swedish labels.
- `assets/site.css` — the `.motion` rule replaced, three lines added.
- `bin/test-hero-motion.py` — the Proof test, updated.
- `.team/**` — response file, papercuts (Builder only).

## Copy strings (old → new)
- `index.html`: visible "Pause film" / "Play film" → no visible text; the same strings stay as `aria-label` (screen readers only).
- `sv/index.html`: visible "Pausa filmen" / "Spela filmen" → no visible text; the same strings stay as `aria-label`.
- No other copy changes.

## Steps (Builder thread)
1. Open issue `031: The film's pause button shows only a pause or play symbol`.
2. Post the work order below unchanged as one comment with the header lines the poller reads (`templates/codex.md`), `Branch: feat/031-pause-icon`, **without** a `Model:` line (host default gpt-6-astra, as in plans 029/030), then add the label `codex-cli`. Reminders at about 15 min and at the hour; fallback per `team/CODEX-CLI.md` [K6].
3. On `done`: Test before commit on the poller's head, `python3 bin/test-hero-motion.py`, and in Playwright on the Jekyll build: with `reducedMotion: 'reduce'` and with JavaScript off, no request for `sluseholmen-720.mp4` and the button not displayed (`getComputedStyle(btn).display === 'none'`); with motion on, the button is 40×40, shows only `.i-pause`, a click sets `.hero.paused`, `video.paused === true`, shows only `.i-play`, `aria-label` is "Play film" / "Spela filmen", a second click restores both; the accessibility tree name of the button matches the label. Measure the icon colour against the button's backing over the poster frame and over `.no-film` (≥ 3:1). Screenshots at both widths, playing and paused, before/after; link check. `@codex review`.
4. Response file with `built-by: codex-cli` in its Outcome and the run's Hinder line quoted.

## Work order
```
Goal: Make the hero's pause button on both home pages show only a pause or play icon, with its name in aria-label, keeping all of story 029's behaviour.
May touch:
index.html
sv/index.html
assets/site.css
bin/test-hero-motion.py
Steps:
1. index.html line 34 is exactly
    <button class="motion" type="button" hidden data-pause="Pause film" data-play="Play film">Pause film</button>
   Replace that line with (same indentation, one line):
    <button class="motion" type="button" hidden aria-label="Pause film" data-pause="Pause film" data-play="Play film"><svg class="i-pause" viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M3 2h3.5v12H3zM9.5 2H13v12H9.5z"/></svg><svg class="i-play" viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M4 2l10 6-10 6z"/></svg></button>
2. sv/index.html line 36 is exactly
    <button class="motion" type="button" hidden data-pause="Pausa filmen" data-play="Spela filmen">Pausa filmen</button>
   Replace it with the same line as in step 1 but aria-label="Pausa filmen" data-pause="Pausa filmen" data-play="Spela filmen".
3. In both files (index.html line 176, sv/index.html line 189) replace the line
    btn.textContent = btn.getAttribute(paused ? 'data-play' : 'data-pause');
   with (same indentation)
    btn.setAttribute('aria-label', btn.getAttribute(paused ? 'data-play' : 'data-pause'));
   Change nothing else in the script.
4. assets/site.css: replace the line that starts with ".motion{position:absolute;" with exactly
.motion{position:absolute;top:calc(96px + env(safe-area-inset-top,0px));right:max(var(--pad),env(safe-area-inset-right,0px));z-index:2;display:grid;place-items:center;width:40px;height:40px;padding:0;color:var(--on-blue);background:rgba(12,34,51,.5);border:1px solid rgba(248,246,241,.5);border-radius:50%;cursor:pointer}
   Keep the next line (".motion:focus-visible{...}") unchanged, and directly after it add these three lines exactly:
.motion[hidden],.motion .i-play,.hero.paused .motion .i-pause{display:none}
.hero.paused .motion .i-play{display:block}
.motion svg{width:14px;height:14px;fill:currentColor}
5. bin/test-hero-motion.py: in CSS_LINES replace the old ".motion{position:absolute;...}" string with the new line from step 4 and add the three new lines; keep the other lines. In the button checks: replace the check that the button text equals the pause label with two checks, the button's text stripped of whitespace is empty, and attrs aria-label equals the pause label; keep the type, hidden, in-hero, data-pause and data-play checks. Track each element's button ancestor the way in_hero is tracked, and check that each page has exactly one svg with class i-pause and one with class i-play, both inside button.motion, both with aria-hidden="true" and focusable="false" and no style attribute. Add "setAttribute('aria-label'" to the script hooks, and check that "btn.textContent" does not occur in either page. Keep every other check.
Proof: bin/test-hero-motion.py — python3 bin/test-hero-motion.py
Must not: commit or push; touch any file not under May touch; add dependencies; weaken a check to make it pass; change any other line, text, link, price, Cal.com URL, contact address, JSON-LD, the footer, the video element or the h2.tag labels; add a style attribute, another script, stylesheet, font or host; touch _config.yml, CNAME, .github/**, beyond/**, _layouts/**. If a line number or a quoted line does not match the file, or a step needs a choice this order does not make, stop and list it under Hinder.
```

## Tests
- `bin/test-hero-motion.py` (Proof) and Test before commit (`check_html.py` on every page).
- Builder: the Playwright checks in Steps 3, contrast, screenshots before/after at both widths, link check.

## Risks / watch out for
- `hidden` vs `display:grid`: without `.motion[hidden]{display:none}` the button would show under reduced motion and without JavaScript, and do nothing. The Playwright check in Steps 3 catches it.
- Over a bright film frame the 50 % backing may not hold 3:1 for the icon; the Builder measures over the poster, and if it fails the fix is the backing's alpha (a value choice for a fix order, not for Codex).
- `check_html.py` balances tags; the self-closing `<path/>` inside `<svg>` is foreign content it already handles (`handle_startendtag`).

## Out of scope
- The film's length or loop (waits on Conny's answer in the 029 thread).
- Button position, tooltip, `aria-pressed`.
