---
id: 029
verdict: plan
---

# Plan 029 — A pause button for the moving hero, and two section labels as headings

Story: `.team/backlog/029-hero-motion-pause-and-h2-labels.md`

## Approach
The film's address moves from `src` to `data-src`, and one small inline script on each home page sets `src` (which starts the existing `autoplay`) only when reduced motion is off, then reveals a `hidden` button that toggles the class `paused` on `.hero`, pauses or plays the film and swaps its label. CSS pauses the `.flow` SVG animation under `.hero.paused` and styles the button in the hero's own colours. The four labels become `h2.tag` with one CSS rule that gives them back the paragraph look. A stdlib Python test in `bin/` (excluded from the site by `_config.yml`) pins the markup, CSS and script facts. Codex CLI (Astra) builds it from the work order below. Touches the price block: no. Booking CTA: no. Footer: no.

## Baseline
`master` at d332284: Test before commit exits 0; Builder screenshots of `/` and `/sv/` at 1440×900 and 390×844 (first screen and full page) for the before/after comparison of the labels.

## Estimate
size: S
risk: plain
files: 4
codex-rounds: 2
builder: codex-cli — every choice (markup, copy, CSS values, script) is settled in the work order; tb-site's Test before commit runs on the poller
codex-model: astra — Conny asked for Astra tonight; script and accessibility details reward the stronger model
model: light — Codex builds; the Builder thread posts the order, runs screenshots and the link check

## Files
- `index.html` — video `src` → `data-src`, the button, two labels `p.tag` → `h2.tag`, one new inline script.
- `sv/index.html` — the same with Swedish copy.
- `assets/site.css` — `h2.tag` reset, `.motion` button, `.hero.paused .flow svg` pause.
- `bin/test-hero-motion.py` (new) — the Proof test.
- `.team/**` — response file, papercuts (Builder only).

## Copy strings (old → new)
- New, `index.html`: button "Pause film" (playing) / "Play film" (paused).
- New, `sv/index.html`: button "Pausa filmen" (spelar) / "Spela filmen" (pausad).
- Unchanged text, new element (`p` → `h2`): "How we work — three links, two companies", "The questions we answer", "Arbetssätt — tre led, två bolag", "Frågorna vi besvarar".

## Steps (Builder thread)
1. Open issue `029: A pause button for the moving hero, and two section labels as headings` (label `codex-cli` exists).
2. Post the work order below as one comment, then add the label. Post it **without** the `Model:` line: the host default is gpt-6-astra, and the MacBook's `MODELS` (agent-team v0.8.14 reinstall) is unconfirmed, so a `Model: astra` line could bounce. Reminders at about 15 min and at the hour; fallback per `team/CODEX-CLI.md` [K6] (the Mac may sleep tonight).
3. On `done`: run the full Test before commit on the poller's head (check, screenshots of both pages at both widths before/after, the link check), plus in Playwright: with `reducedMotion: 'reduce'` no request for `sluseholmen-720.mp4` and the button stays hidden; with JavaScript disabled the same; with motion on, a click sets `.hero.paused`, `video.paused === true`, the `.flow svg` computed `animation-play-state` is `paused` (force `.no-film` to see it) and the label swaps; contrast of the button text. Attach screenshots, `@codex review`.
4. Response file with `built-by: codex-cli` in its Outcome and the run's Hinder line quoted.

## Work order
```
Goal: Give both home pages a pause button for the hero film and the fallback line animation, stop the film from loading under reduced motion, and make four section labels h2 headings that look exactly as before.
May touch:
index.html
sv/index.html
assets/site.css
bin/test-hero-motion.py
Steps:
1. index.html line 32 and sv/index.html line 34 (the <video class="film" ...> element): rename the attribute src="/assets/film/sluseholmen-720.mp4" to data-src="/assets/film/sluseholmen-720.mp4". Change nothing else on that element.
2. Directly after that </video>, on its own line with the same indentation, add in index.html:
   <button class="motion" type="button" hidden data-pause="Pause film" data-play="Play film">Pause film</button>
   and in sv/index.html:
   <button class="motion" type="button" hidden data-pause="Pausa filmen" data-play="Spela filmen">Pausa filmen</button>
3. Change these four elements from <p class="tag">…</p> to <h2 class="tag">…</h2>, text unchanged: index.html "How we work — three links, two companies" and "The questions we answer"; sv/index.html "Arbetssätt — tre led, två bolag" and "Frågorna vi besvarar". No other p.tag changes.
4. In both files, directly after the existing </script> that closes the CALCOM_URL script (index.html line 162, sv/index.html line 175), add this block exactly:
<script>
// Story 029: the film loads only without reduced motion; one button pauses all hero motion (WCAG 2.2.2).
(function () {
  var hero = document.querySelector('.hero'), film = hero && hero.querySelector('.film'), btn = hero && hero.querySelector('.motion');
  if (!hero || !film || !btn) return;
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  film.src = film.getAttribute('data-src');
  btn.hidden = false;
  btn.addEventListener('click', function () {
    var paused = hero.classList.toggle('paused');
    if (paused) { film.pause(); } else { var p = film.play(); if (p && p.catch) p.catch(function () {}); }
    btn.textContent = btn.getAttribute(paused ? 'data-play' : 'data-pause');
  });
})();
</script>
5. assets/site.css: directly after the line that starts with "@media(prefers-reduced-motion:reduce){.film{display:none}" add these three lines exactly:
.hero.paused .flow svg{animation-play-state:paused}
.motion{position:absolute;top:calc(96px + env(safe-area-inset-top,0px));right:max(var(--pad),env(safe-area-inset-right,0px));z-index:2;font:500 14px/1 var(--f);color:var(--on-blue);background:rgba(12,34,51,.72);border:2px solid var(--on-blue);padding:9px 14px;cursor:pointer}
.motion:focus-visible{outline:3px solid var(--white);outline-offset:2px;box-shadow:0 0 0 8px var(--black)}
   and directly after the line that starts with ".tag::before{" add this line exactly:
h2.tag{font-family:var(--f);letter-spacing:normal;line-height:1.5;text-wrap:wrap}
6. Create bin/test-hero-motion.py: Python 3 standard library only (html.parser, re, sys, pathlib), runnable from the repo root as python3 bin/test-hero-motion.py, printing one line per failed check and exiting 1 on any failure, 0 otherwise. For each of index.html and sv/index.html it checks: exactly one <video class="film">, which has data-src="/assets/film/sluseholmen-720.mp4", no src attribute, and keeps autoplay, muted, loop, playsinline, poster and onerror; exactly one <button class="motion"> with type="button", the hidden attribute, and data-pause/data-play and text equal to "Pause film"/"Play film"/"Pause film" (index.html) or "Pausa filmen"/"Spela filmen"/"Pausa filmen" (sv/index.html), placed inside the element with class "hero"; the two labels from step 3 are h2 elements with class "tag" and no p.tag has those texts; the page source contains "prefers-reduced-motion: reduce", "getAttribute('data-src')" and "classList.toggle('paused')". For assets/site.css it checks the four lines from step 5 are present verbatim. It also checks that "/assets/film/sluseholmen-720.mp4" appears in no src= attribute in either page.
Proof: bin/test-hero-motion.py — python3 bin/test-hero-motion.py
Must not: commit or push; touch any file not under May touch; add dependencies; change tests to make them pass; change any text, link, price, Cal.com URL, contact address, JSON-LD, the CALCOM_URL script, the footer or any other element than those named; add another script, stylesheet or host; touch _config.yml, CNAME, .github/**, beyond/**, _layouts/**. If a line number or a quoted line does not match the file, or a step needs a choice this order does not make, stop and list it under Hinder.
```

## Tests
- `bin/test-hero-motion.py` (Proof) and Test before commit (`check_html.py` on every page).
- Builder: Playwright checks in Steps 3, screenshots before/after at both widths, link check.

## Risks / watch out for
- Moving `src` to `data-src` means a visitor without JavaScript sees the poster, not the film; intended (story Outcome).
- `h2.tag` must not move anything: compare the label rows in the before/after screenshots; `.tag` is `display:flex` with its red square, which the reset keeps.
- The button sits over the large red "&" on wide screens; the 72 % navy background keeps the text readable, the Builder measures it.

## Out of scope
- Story 030 (doctype), the diagram's aria-label, a lower hero, colours.

## Suggestions for PO
- Astra's S2 (the diagram's aria-label names the axes in reverse) as its own small Kö row after 030.
