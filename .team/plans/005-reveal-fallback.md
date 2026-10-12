---
id: 005
verdict: plan
---

# Plan 005 — D1 — content visible in unscrolled full-page renders (reveal fallback)

Story: `.team/backlog/005-reveal-fallback.md`

## Approach
Invert when the hidden state is applied. Today the script adds `.reveal` to all seven `main section`s at load and the IntersectionObserver clears it per section; a render that never scrolls keeps 19 of 25 `.r-fade` at opacity 0. New rule: the page is fully visible by default; the hero keeps its load settle exactly as today (`.reveal` at script run, `.revealed` on the double `requestAnimationFrame`); the other six sections get `.reveal` only in a one-shot `scroll` listener on `window` (`{once:true,passive:true}`), and only if they have no `.revealed` and `getBoundingClientRect().top >= window.innerHeight`. The observer is unchanged (same threshold, rootMargin, `observe` on all sections at load) and reveals them as today.

Why this and not the report's load timer: a timer that clears hidden state after N seconds also removes the reveal for any visitor who reads the hero longer than N seconds, which breaks criterion 2. Hide-on-first-scroll satisfies both: nothing is hidden until the visitor scrolls, and at that moment every section below the fold is hidden before the frame paints (the `scroll` event runs before paint), so the visitor's experience is byte-for-byte today's. Measured on master: the hero is 1280 px tall at 1440×900 and 1000 px at 390×844, so all six sections are entirely below the fold at load at both widths. Prototype in a scratch copy today: unscrolled 0 hidden; after a 1 px wheel 19 hidden, 7 `.reveal`, 1 `.revealed` (= today); stepped to bottom 0 hidden; one-jump `scrollTo` bottom 0 hidden; load with `#review` hides only the sections below the target; no-JS and reduced-motion 0 `.reveal`, 0 hidden.

Bounded wait for the acceptance check: 1 s after `networkidle` (two frames plus the hero's 450 ms transition).

Copy strings changed: none. Price block, booking CTA, Cal.com script, footer, `CNAME`: untouched. No new hosts.

## Files
- `index.html` — only the first inline `<script>` (reveal IIFE, lines 385–401): replace the `forEach … add('reveal')` line with the scroll listener; add `hero.classList.add('reveal')` before the hero's rAF chain. No CSS change (lines 161–171 stay).
- `docs/screenshots/005-reveal-fallback/` — `desktop.png`, `mobile.png` (scrolled, as in PRs 1–3) plus `desktop-noscroll.png`, `mobile-noscroll.png` (fresh page, networkidle + 1 s, no scroll).

## Steps
1. Branch `feat/005-reveal-fallback`. Edit the script as above; keep the early returns for reduced motion and missing IntersectionObserver.
2. Run the checks under Tests with a throwaway Playwright script (do not commit it); drop the four PNGs in the screenshots folder.
3. PR body: the four counts below, the screenshots, and the sentence "no copy change".

## Tests
- `python3 -m html.parser index.html` exits 0; `git diff master --stat` shows `index.html` plus four PNGs.
- Chromium 1440×900 and 390×844, fresh page, `networkidle` + 1 s, no scroll: 0 `.r-fade` with computed opacity < 1; `.reveal` count 1 (hero), `.revealed` count 1. Take the full-page screenshot, then assert the same counts again (capture must not change them).
- Same page, `mouse.wheel(0,1)`, wait 100 ms: 19 hidden, 7 `.reveal`, 1 `.revealed` (today's numbers). Then scroll to the bottom in ≈400 px steps: 0 hidden, 7 `.revealed`, `scrollWidth === innerWidth`, heights 6694 / 8077 as on master. Scrolled screenshots from this state.
- Fresh page, single `scrollTo(0, scrollHeight)`: 0 hidden.
- `javaScriptEnabled:false` and `emulateMedia({reducedMotion:'reduce'})`: 0 `.reveal`, 0 hidden, as today.
- Link check: every `http(s)` `href`, `og:image` and the Cal.com URL return 200 (the two `rel=preconnect` bare hosts 404 as in every earlier review; excluded).

## Risks / watch out for
- Do not use `wheel` or `touchstart` as the trigger; only `scroll` fires with the final position in the same frame, before paint. Measure `top` inside the handler, not before it.
- Skip sections that already have `.revealed`: with the observer registered at load, a section in view when the first scroll happens may already be revealed, and re-adding `.reveal` would flash it.
- The hero must get `.reveal` synchronously in the script (it no longer comes from the forEach), or its settle is lost and the hero shows without animation.
- `.r-rule` / `.r-rule-top` are driven by the same two classes; nothing extra to do, but include the 6 `.r-rule-top` in the scrolled visual check.
- `docs/design-review-2026-10.md` is not edited (story criterion).

## Out of scope
- D2–D8, reveal timing/easing, which elements fade, a timer fallback for the hero in background tabs (rAF pauses there; the settle plays when the tab is shown, which is fine).

## Suggestions for PO
- Review 004 nits N1–N3 (line references and wording in the report) still wait for a row; the story forbids touching the report here.
- `docs/screenshots/` grows by four more PNGs; the housekeeping row from plan 004 still stands.
