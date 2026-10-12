---
id: 005
verdict: approve
---

# Review 005 — D1 — content visible in unscrolled full-page renders (reveal fallback)

PR: #5 · 2026-10-12

## Must fix
- none

## Should fix
- none

## Nits
- N1: `index.html:162–166` — print after a scroll. The reveal CSS has no `@media print` override, so a visitor who scrolls part-way and then prints gets the not-yet-revealed sections blank (`.reveal .r-fade{opacity:0}` applies on paper). The story only requires an unscrolled render, which now passes, and on master every print after load was blank below the hero, so this is strictly better than before. Nit: a two-line `@media print{.reveal .r-fade{opacity:1;transform:none}.reveal .r-rule,.reveal[data-rule]>.r-rule-top{transform:none}}` would close it; outside this story, noted for the PO.
- N2: `index.html:390–394` — the plan's "all six sections are below the fold" holds at 1440×900 and 390×844 (hero 1280 / 1000 px). On a viewport taller than the hero (≈1280 px at 1440 wide) section 2 has `top < innerHeight` at the first scroll, gets no `.reveal`, and shows statically where master animated it on load. Not a defect, no flash; recording it so nobody files it as a regression.

## What I checked
- tests run: `python3 -m html.parser index.html` clean; `git diff master --check` clean; `git diff master --name-only` is `index.html` (+6/−2, first inline `<script>` only, no markup or CSS line) plus the four PNGs under `docs/screenshots/005-reveal-fallback/` (1440×6694 ×2, 390×8077 ×2, four distinct md5s, both no-scroll images visibly show every section). Playwright 1.58.2 Chromium, my own script, both widths: fresh page, `networkidle` + 1 s, no scroll: 25 `.r-fade`, **0 hidden, 1 `.reveal`, 1 `.revealed`**; identical after the full-page capture. `mouse.wheel(0,1)` + 100 ms: **19 hidden, 7 `.reveal`, 1 `.revealed`** (master's numbers). Stepped 400 px to bottom: 0 hidden, 7 `.revealed`, `scrollWidth === innerWidth`, heights 6694 / 8077 as on master, 6 `.r-rule-top` drawn. Fresh page + single `scrollTo(bottom)`: 0 hidden. `javaScriptEnabled:false`: 0 `.reveal`, 0 hidden. `reducedMotion:'reduce'`: 0 `.reveal`, 0 hidden, also after a 2000 px scroll. Hero settle: sampled per frame from `commit` — `.reveal` is on the hero before its first `.r-fade` reaches opacity 0, `.revealed` lands two frames later, opacity 1 at 600 ms; same sequence as master. Link check with curl: every `http(s)` `href`, `og:image` and the Cal.com URL return 200; the two `rel=preconnect` bare hosts 404 as in every earlier review and are excluded; five `#id` anchors resolve, `href="#"` is the logo (pre-existing), `assets/favicon.svg` exists. `gh pr checks 5`: no checks configured.
- tried to break: load with `#review` — only the sections below the target get `.reveal` (desktop: `kontakt`; mobile: `grundaren`, `kontakt`), the target is `.revealed` without `.reveal`, nothing above it is touched. Tab ×12 from a fresh page — the first scroll comes from the hero CTA, the six lower sections are hidden before paint, and the section holding the focused link is already `reveal revealed` when focus lands (no blank focus target). Reload with scroll restoration at y=2500: sections in view show statically, only the 3–4 below get `.reveal`. Jump to the middle then back to top: the three sections below stay hidden and observed, nothing above flashes. Viewport resize without scroll: still 0 hidden. Confirmed the handler measures `getBoundingClientRect` inside the `scroll` event (before paint) and skips `.revealed` sections, as the plan's risk list demands; `{once:true,passive:true}` means the listener detaches after the first scroll.
- Review checks: no copy string changes (the diff is script-only), so no new factual or Dignami claim to trace; no colour changes, so no contrast to measure; screenshots at both widths, scrolled and unscrolled, attached to the PR and committed. Price block, booking CTA, Cal.com script, footer, `CNAME`, `_config.yml`, `docs/design-review-2026-10.md` untouched. No new hosts.
- PR description: every count (0/1/1, 19/7/1, 0/7, 0, 0/0), the html.parser result, the link check and the four screenshot URLs (commit `8e8fcb0` = branch HEAD) checked against the diff and my own runs — all hold.
- rulebook: no change to `AGENTS.md`, `.team/team.md`, `REVIEW.md` or `.team/roles/`.
- scope vs story: all six acceptance criteria met; the change is exactly the plan's two script edits, no scope creep.
- Second reviewer: not run — Team settings list no Second-reviewer paths.

## For PO
- Merge deploys to production (Operatör trigger): Conny should open https://transformationbeyond.se/ once, confirm the hero still settles and lower sections fade in on scroll, and that a link preview / unscrolled capture now shows the whole page.
- N1 (print after scroll) is a candidate line for a later row; it is not covered by D1–D8.

Verdict: approve. Merging per `merge: auto` in `.team/team.md`.

— Reviewer (Fable 5.1) on behalf of Conny Wadbro
