---
id: 008
verdict: approve
---

# Review 008 — D4 + D5 + D7 — mobile hero, navigation and offer rows at 390 px

PR: #8 · 2026-10-13

## Must fix
- none

## Should fix
- none

## Nits
- N1: `index.html:55` — at 320 px the h1 formula gives 30.4 px and the lines become `in one advisor, not three` / `consultancies.`, a single word on the last line. Outside the story (390, spot-checked 375 and 430, all four-line) and no current device is 320 wide; noted so nobody is surprised. No action on this PR.

## What I checked
- tests run: `python3 -m html.parser index.html` clean; `git diff master...HEAD --check` clean; diff is exactly three CSS lines in `index.html` (`index.html:47`, `:55`, `:156`) plus five PNGs under `docs/screenshots/008-mobile-hero-nav-offer/` (1440×6676, 390×7823, 390×520 hero clip, 390×124 header, 350×1029 `.offer`). `grep -n '@media'`: six on master, eight on the branch; `max-width:480px` ×2 (plan said one block for h1 + `.nav`, the Coder wrote two blocks next to the rules they override, which the plan's Files line allows), `max-width:520px` ×1. No markup, script or copy diff.
- Playwright 1.58.2 Chromium, my own script, `networkidle` + 1 s, scrolled to bottom in 400 px steps, branch and `master` at 1440×900, 390×844, 375×844, 430×932. Every number in the PR table reproduced: 390 h1 38 px / 350×149 / four lines `Commercial excellence,` · `law and AI —` · `in one advisor, not` · `three consultancies.` (master 48 px, 282 px, six lines, `three` alone); `.nav` 123 (74), padding `16px 20px 18px` so the horizontal `.wrap` padding survives; `.mark` 226×34 at x 20, one line (was 205×67, two); `.cta` 159×43 at x 20, one line, padding `12px 22px` unchanged (was 145×62, two); four `.nav-r a:not(.cta)` `display:none` on both; `.mrow` columns `292px` (was `110px 164px`), heights 168/145/123/123 (235/213/145/123), hairline `border-top` colours identical row by row, `.mk` padding-top 0 and full width 292; `.offer-mech` 558 (716); `.offer` 1028 (1187); `.price` 292×43 and `.offer .cta-big` 181×49 → `#kontakt` identical to master; sample-PDF href identical; page 7823 (8077); `scrollWidth === innerWidth`; 0 of 25 `.r-fade` hidden, 7 `.revealed`. 375 and 430: same four h1 lines, no overflow. `document.body.innerText` and the ordered href list are equal to master at every width (AC "no visible copy changes").
- 1440: page 6676, h1 112 px / 1008×549 at x 206 / five lines, `.nav` 74, `.mrow` `110px 340px`, `.offer` 500, all rects identical to master to the hundredth of a pixel; my branch and master full-page PNGs are byte-identical, and the Coder's `desktop.png` is byte-identical to my branch shot. (It is not byte-identical to the PNG committed in 007 — different run, same pixels as far as the rects show — so the PR's "byte-identical to the master baseline" refers to the Coder's own baseline run; the substance holds.)
- Breakpoint edges (tried to break): 480 → h1 47.8 px, five lines in the 481 form, `.nav` still stacked; 481 → 48 px, `.nav` back to 74 and one row, mark and CTA one line each; 520/521 → `.mrow` flips `420px` ↔ `110px 293px`; 360 → four lines; 760/761 → the existing nav-link rule flips. No overflow at any width tried. At 761–~800 the mark, four links and CTA wrap to two lines on master as well — pre-existing, out of scope.
- Keyboard at 390: Tab → `.mark` → `.cta` → `.cta-big`, all visible, `:focus-visible` true, outline `rgb(122,87,41)` (the 007 ring). DOM order unchanged, so the stacked layout changes nothing in tab order. Viewed the focus crop: ring visible around the stacked CTA.
- Screenshots: viewed the Coder's three 390 crops against `docs/design-review-2026-10/390-{hero,nav,offer}.png`. Hero four lines with `in one advisor` on one line in bronze; mark above CTA with the header rule below; offer labels above full-width text with hairlines between rows. All five PR links return 200.
- Link check with curl (browser UA): fonts CSS, `mondmodel.com`, both band images, OG image, sample PDF, `transformationbeyond.se`, both dignami URLs and `CALCOM_URL` → 200; the two `rel=preconnect` bare hosts 404 as in every earlier review (excluded); five `#id` anchors resolve; two `mailto:` unchanged. `gh pr checks 8`: no checks configured. PR `MERGEABLE / CLEAN` against `master`.
- Review checks: no copy change, so no claim to source and no Dignami wording to compare; no colour changes, so no contrast to recompute (`.mk` stays `--bronze` on paper, 5.98 from 007). Screenshots at both widths attached.
- Hard rails / rulebook: price text, `CALCOM_URL`, contact address, `CNAME`, `_config.yml`, `README.md`, hosts: untouched. `AGENTS.md`, `.team/team.md`, `REVIEW.md`, `.team/roles/`: untouched. No new fonts, colours or third-party hosts.
- scope vs story: all six acceptance criteria met; D5 chosen as the stack option the plan picked; D7 breakpoint 520 as the plan picked. No scope creep.
- Second reviewer: not run — Team settings list no Second-reviewer paths.

## For PO
- Merge deploys to production (Operatör trigger): Conny should open https://transformationbeyond.se/ on a phone and confirm the four-line headline, the stacked header and the offer labels above their text.
- The offer still reads "The Architecture Review"; the brief says it was renamed to "The AI Value Review" on 2026-10-13 via ORDER. Not this story's scope (no copy), just making sure the rename has its own row.
- 761–~800 px (small tablet portrait): mark, four links and CTA wrap to two rows on master and on this branch. Out of scope here; a candidate for the tablet pass the plan mentions.

## For Architect
- Plan's Story line points at `008-mobile-hero-nav-offer.md`; the file is `.team/backlog/008-mobile-layout.md` (the Coder flagged it too).

Verdict: approve.

— Reviewer (Fable 5.1) on behalf of Conny Wadbro
