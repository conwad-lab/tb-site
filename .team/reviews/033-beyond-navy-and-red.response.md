<!-- .team/reviews/033-beyond-navy-and-red.response.md: the Builder's answers (CLOUD.md § Builder 4). -->

## Builder checks on the built head — 2026-11-23
Jekyll 4.4.1 build of the PR head and of master d72113b, both with an uncommitted fixture letter in `_beyond/` (never committed). Playwright, Chromium.
- `python3 bin/test-beyond-palette.py`: ok. Test before commit (`check_html.py`, every page): exit 0.
- `getComputedStyle(document.body).fontFamily` on `/beyond/`, the letter and `/404.html` starts with "Familjen Grotesk". Header and footer background rgb(12, 34, 51) on all three.
- Requests to other hosts: fonts.googleapis.com (the css2 URL), fonts.gstatic.com Newsreader and Familjen Grotesk woff2 only. No Hanken Grotesk, no JetBrains Mono.
- Focus ring (Tab): header and footer links paper rgb(248, 246, 241) 2px solid; letter body links and "Alla nummer" red rgb(207, 35, 24) 2px solid.
- Link check (17 internal hrefs on the three pages, local server): all 200. External links and mailto not fetched.
- Screenshots before/after at 1440×900 and 390×844 of `/beyond/`, the fixture letter and `/404.html`, plus the header focus ring: `.team/screenshots/033-beyond-{before,after}-{archive,letter,404}-{1440,390}.png` and `033-beyond-after-focus-header.png`, committed on the branch as in earlier stories (`.team/` is excluded from the published site).

Contrast, measured (WCAG relative luminance):
| Pair | Measured | Need |
|---|---|---|
| navy #0C2233 on paper | 15.05 | 4.5 |
| black #14181B on paper | 16.53 | 4.5 |
| red #CF2318 on paper | 4.98 | 4.5 |
| deep red #B01C13 on paper | 6.44 | 4.5 |
| grey #5B5F66 on paper | 5.94 | 4.5 |
| paper on navy | 15.05 | 4.5 |
| red on navy (non-text, wordmark) | 3.02 | 3 |
| focus ring paper on navy / red on paper | 15.05 / 4.98 | 3 |

## Outcome
built-by: codex (via @codex on GitHub after the codex-cli poller took no order within 17 minutes; Codex had no remote, so its `git format-patch` was applied here with `git am` unchanged and pushed by the Builder)
model: claude-sonnet-5-5
parts: none
missed: nothing; the plan's steps applied cleanly. Codex's environment could not run Jekyll (no Gemfile), so the Builder ran the build and screenshots.
Codex CLI Hinder: none, the order was never picked up (no `codex-cli: started` on issue #83).
Codex @codex Hinder: "ingen Git-remote och ingen lokal Jekyll/Gemfile; full patch följer".

## Codex round 1 — 2026-11-23
- M1 `.team/reviews/033-beyond-navy-and-red.response.md:10` screenshots not attached to the PR — fixed: the 13 PNGs are committed under `.team/screenshots/033-beyond-*.png` (the repo's convention) and the line above names them.
