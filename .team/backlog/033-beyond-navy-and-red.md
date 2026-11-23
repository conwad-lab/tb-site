---
id: 033
title: "The & Beyond archive in navy and red"
---

## Outcome
The & Beyond pages (`/beyond/`, every letter page under `/beyond/<name>/`, and the 404 page that shares their stylesheet) look like the same site as the home pages: navy (#0C2233) and red (#CF2318) on paper (#F8F6F1), Newsreader headings and Familjen Grotesk text. No bronze, no Hanken Grotesk, no JetBrains Mono is left on them. The favicon, which every page uses, gets the same colours.

## Why
Conny decided the new profile 2026-11-17–20 (Marin och rött, Newsreader + Familjen Grotesk without JetBrains Mono; stories 025 and 026 built it on `/` and `/sv/`), and 2026-11-23 made the new profile a condition for publishing & Beyond #1: the letter goes out from Conny's LinkedIn, and its link leads here. Today `/beyond/` still uses the old bronze identity (`assets/beyond.css`, story 016), so a reader who comes from the navy-and-red letter lands on a page that looks like another company. Underlag: `tb-omprofilering/plan.md` in the project folder (step 2 of the order: "Redan beslutat, auto-merge vid enighet"). No copy changes, so no copy decision for Conny.

## Signal
- After merge, from a connection that reaches the site (the Mac): `https://transformationbeyond.se/beyond/` has a navy header and footer, red eyebrow and links, `getComputedStyle(document.body).fontFamily` starts with "Familjen Grotesk", and the page requests no Hanken Grotesk or JetBrains Mono font. The same holds for the first letter page once #1 is imported.
- Conny says the archive reads as the same site as the home page. The Coordinator logs seen / not seen here.

## Acceptance criteria
- [ ] `assets/beyond.css` uses only colours from `assets/site.css` `:root` (plus `#FFFFFF`): paper #F8F6F1, navy #0C2233, red #CF2318, deep red #B01C13, black #14181B, grey #5B5F66, fog #F6E6DA. No bronze token or hex remains; no `--mono`.
- [ ] Header and footer of the archive, letter and 404 pages are navy bands with paper text; the `&` in the wordmark, the eyebrow, week labels, links and the blockquote rule are red; headings are navy.
- [ ] `_layouts/beyond-base.html` and `404.html` load exactly the Google Fonts URL that `index.html` loads (Familjen Grotesk + Newsreader), and nothing else from a font host.
- [ ] The footer mark (inline SVG in `_layouts/beyond-base.html` and `404.html`) and `assets/favicon.svg` are drawn in paper, navy and red only.
- [ ] WCAG AA: every text/background pair that changes meets 4.5:1 (normal text) or 3:1 (large text, focus ring, non-text); measured values in the response file. Focus rings stay visible on the navy bands and on paper.
- [ ] `bin/test-beyond-palette.py` (new) green; Test before commit green.
- [ ] Screenshots at 1440×900 and 390×844, before and after: `/beyond/`, a letter page (built from a local fixture letter that is not committed) and `/404.html`; attached to the PR.
- [ ] No text, link, price, Cal.com URL, contact address, founder claim, RSS feed, `_config.yml` or home page markup changes. The home pages change only by the favicon.

## Out of scope
- `beyond_linkedin_url` (story 034, when Conny has created the newsletter on LinkedIn).
- Positioning text on `/sv/` (story 032).
- Layout changes beyond colours, type and the header/footer bands; an email signup.

## Vad blir publikt?
The & Beyond archive, its letter pages and the 404 page switch from bronze to the home pages' navy and red, with the same typefaces. The favicon (also on the home pages) turns navy and red. No words change.

## Log
- 2026-11-23 Coordinator's planner (thread "Planera story 033 i tb-site"): written from Conny's decision 2026-11-19 and the T&B rebrand plan 2026-11-23; builder codex-cli.

— Coordinator (Claude) on behalf of Conny
