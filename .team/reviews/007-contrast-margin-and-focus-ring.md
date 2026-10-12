---
id: 007
verdict: approve
---

# Review 007 — D2 + D3 — more contrast margin for small mono text and a visible focus ring on dark

PR: #7 · 2026-10-12

## Must fix
- none

## Should fix
- none

## Nits
- N1: `index.html:122` — `.cta-bronze` now carries the literal `#8A6430` with nothing saying why. A future edit will "tidy" it back to `var(--bronze)` and darken the booking CTA, which this story forbids. Nit: a short CSS comment (`/* pinned: token darkened in 007, CTA stays */`). No action on this PR.

## What I checked
- tests run: `python3 -m html.parser index.html` clean; `git diff master...HEAD --check` clean; diff is `index.html` (4 CSS lines: two `:root` tokens, `.book-sub` colour, the `.cta-bronze` pin, one new `.dark a:focus-visible` rule) plus four PNGs under `docs/screenshots/007-…/` (1440×6676, 390×8077, two 1440×519 element shots). Greps: `#7A5729`, `#5B5E62`, `#A39C8F` → 1 each; `#6B6E72`, `#8F887C` → 0; `#B69463` → 2 (`.dark .eyebrow` + new focus rule); `#5C421E` → 1; `#8A6430` → 7 (CSS pin + 5 in the inline hero SVG + 1 in the footer mark SVG, all unchanged from master — the plan's "→ 1" was wrong and the Coder said so in the PR). Playwright 1.58.2 Chromium, my own script, `networkidle` + 1 s, scrolled to bottom in 400 px steps, run on the branch and on `master`: 1440×900 → height **6676** both, 0 hidden `.r-fade` of 25, 7 `.revealed`, no overflow; 390×844 → **8077** both, 0 hidden, 7 `.revealed`, no overflow. Link check with curl: every `http(s)` `href`, both band images, `og:image`, the sample PDF and the Cal.com URL (`CALCOM_URL` in the script) return 200; the two `rel=preconnect` bare hosts 404 as in every earlier review (excluded); five `#id` anchors resolve; two `mailto:` unchanged. `gh pr checks 7`: no checks configured. PR `MERGEABLE / CLEAN` against `master`. All four screenshot links in the PR body (by commit SHA, as review 006 N1 asked) return 200.
- WCAG AA contrast (Review checks): computed `color` vs nearest non-transparent ancestor background at 1440, WCAG 2.1 luminance, master → branch. Bronze on paper (`.eyebrow`, `.layer .k`, `.mk`, `.proof .t`, `h1 em`, `.lead-stmt`, `.gap-stmt em`, `.qs-k`, `.mark span`, `.amp-dev.own`) 4.88 → **5.98**. Bronze on tint (`.stage.here .k`, `.stage.here .who`, `.handoff .k`) 5.18 → **6.35**. Muted on paper (`.status`, `.src`, `.src a`, `.proof .metric a`, `.price span`, `.foot .mono`, `.foot a`, `footer`, `.nav-r a`, `.proof-link`, `.hero-base`, non-here `.stage .k/.who/.status/p`) 4.70 → **5.98**. Muted on tint (`.stage.here p`) 4.99 → **6.35**. `.book-sub`, `.book-sub a` on dark 4.66 → **6.01**. Unchanged: `.cta`/`.cta-big` 15.07, `.cta-bronze` white on `rgb(138,100,48)` 5.32, `.dark .eyebrow` 5.77, `.dark h2` 13.76, `.handoff a` 15.99, body/lede 9.87–10.47. Every changed pair ≥ 5.5 (AC1). Same values on 390 (same CSS, no media-query colours). Static hex math gives the same numbers to two decimals; hue stays in family (bronze 35°→34°, muted 214°, book-sub 38°→39°, lightness only).
- Focus (D3): `page.focus` on `#book-cta` and `.book-sub a` → `outlineColor rgb(182,148,99)`, `2px solid`, offset `3px`, `:focus-visible` true (master: `rgb(138,100,48)`, 3.08 on dark; branch 5.77). On paper, `.cta-big`, `.proof-link`, `.cta`, `.foot a`, `.handoff a`, `.nav-r a` → `rgb(122,87,41)` (5.98). The `.dark` rule beats the global one on specificity, nothing else inside `section.dark` is focusable. Viewed the Coder's `focus-cta.png` and `focus-email.png`: the ring is clearly visible around both.
- Side-by-side (AC4): element shots of `.hero`, `.stage.here`, `.proof` and `section.dark` on master and on the branch, same script. Identical layout; bronze reads a shade deeper, same hue; stage/proof labels darker but unmistakably the same page. Still paper/bronze, no new hue. Decorative bronze (handoff edge, underlines, tick marks, `&`, the 1 px `.r-rule-top` on the dark band at 2.51) darkens with the token as the plan said; none is text or a control boundary.
- PR description: every claim checked — heights, 0/7/no-overflow, all contrast figures, both focus outline colours, `.cta-bronze` background `rgb(138,100,48)`, link results, the grep note on `#8A6430`, "no copy/layout/typography/price/URL/address/footer change" (markup diff is empty). All hold.
- Hard rails / rulebook: no copy change, so no claim to source and no Dignami wording to compare. Price block text, `CALCOM_URL`, contact address, `CNAME`, `_config.yml`, `README.md`, hosts: untouched. `AGENTS.md`, `.team/team.md`, `REVIEW.md`, `.team/roles/`: untouched. No new third-party host.
- tried to break: checked `--bronze-deep`, `::selection`, `#4A4238`, `--dark`, `--dark-ink` unchanged; checked `.cta-bronze:hover` still resolves to `#5C421E`; checked no second `a:focus-visible` rule could re-override the dark one; confirmed the inline SVG `#8A6430` uses are fills/strokes on paper (decorative), not text.
- scope vs story: all six acceptance criteria met. AC2's "not per-element overrides" is satisfied for text: bronze and muted are one value each page-wide; the single `.cta-bronze` pin is a background and the plan called it. No scope creep.
- Second reviewer: not run — Team settings list no Second-reviewer paths.

## For PO
- Merge deploys to production (Operatör trigger): Conny should open https://transformationbeyond.se/ once and confirm the small labels read slightly darker and Tab onto the booking button shows a light-bronze ring.
- The report's contrast table in `docs/design-review-2026-10.md` is now historical (plan's suggestion of a one-line pointer still stands).
- `.cta-bronze` white on `#8A6430` (5.32) is the thinnest text pair left; an identity decision if ever wanted.

## For Architect
- Plan test `grep -c '#8A6430' index.html → 1` missed the six SVG uses already on master. Count-based greps on this file need a `grep -n` first.

## Merge
- Not merged. `gh pr merge 7 --squash --delete-branch` was blocked by the Reviewer session's permission layer (auto-mode classifier: "Merge Without Review"), not by GitHub — the PR is `MERGEABLE / CLEAN`, no checks configured. Verdict stays `approve`; the board shows `approved` and Conny merges, or re-runs the Reviewer with merge allowed.

Verdict: approve (`merge: auto` requested, merge left to the human — see ## Merge).

— Reviewer (Fable 5.1) on behalf of Conny Wadbro
