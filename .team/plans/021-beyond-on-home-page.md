---
id: 021
verdict: plan
---

# Plan 021 — & Beyond on the home page

Story: `.team/backlog/021-beyond-on-home-page.md`

## Approach
`sv/index.html` already has front matter, so Jekyll runs Liquid on it; `index.html` has none and is copied as is. Give `index.html` an empty front matter block (`---` / `---`) so both pages can render the block from `site.beyond`, then add the menu link, the Swedish footer link and the block on both pages. The block is a small Liquid snippet in `_includes/latest-letter.html` taking the language as a parameter, styled with the pages' existing tokens. No new dependency, plugin or workflow.

## Baseline
`master` at `b662559`: Team settings tests (html.parser, Playwright screenshots at both widths, link check) before any change; a URL the session cannot reach is listed as not checked.

## Estimate
size: S
risk: plain
files: 4
codex-rounds: 2
builder: codex — S plain; tb-site has a working Codex environment (issue #23)
model: light — S plain, markup and one Liquid include

## Files
- `index.html` — empty front matter at the top; nav link; the block (placement: after the founder section `#grundaren`, before `#kontakt`).
- `sv/index.html` — nav link; footer link; the block in the same place.
- `_includes/latest-letter.html` (new) — `{%- assign l = site.beyond | sort: "date" | last -%}{%- if l -%}…{%- endif -%}`; week, title (`lang="sv"`), date with `site.data.beyond_months` on sv and an English month name on en, link `l.url | relative_url`.
- CSS for the block inside each page's existing `<style>` (no new stylesheet), using existing `:root` tokens.

## Copy strings (old → new)
- Nav, en: (none) → "& Beyond"; nav, sv: (none) → "& Beyond".
- Footer, sv: (none) → "& Beyond — veckobrev".
- Block heading, en: (none) → "Latest letter (in Swedish)"; sv: (none) → "Senaste brevet".
- Block link, en: (none) → "Read the letter"; sv: (none) → "Läs brevet". "All letters" / "Alla nummer" → `/beyond/`.
Touches the price block: no. Booking CTA: no (the nav link goes before it; the CTA's text and href are unchanged). Footer: yes (sv only, one new link).

## Steps
1. Front matter on `index.html`; build locally (`jekyll build` if the environment has it, else GitHub Pages' build on the PR preview is the evidence; say which) and diff `_site/index.html` against the source to show Liquid changed nothing else (no `{{`/`{%` in the page today: check with `grep`).
2. Include, nav, footer, CSS.
3. Fixture letter in a temp `_beyond/` (not committed) for the with-letter screenshots.
4. Team settings tests on both pages; screenshots attached.

## Tests
- `python3 .github/scripts/check_html.py index.html sv/index.html _includes/latest-letter.html`.
- Playwright screenshots, 4 cases (2 pages × with/without letter) at both widths; link check (`/beyond/` 200 in the built site).

## Risks / watch out for
- Front matter on `index.html` makes Jekyll run Liquid on the whole page: any `{{` or `{%` in the inline CSS, JSON-LD or SVG would break it. Check before and after.
- The nav on 390 px is tight; a fifth link must not wrap the booking button off screen.
- `_config.yml` is a Human-merge path: do not touch it (not needed).

## Out of scope
- E-mail sign-up, UTM parameters, letter import.

## Suggestions for PO
- When the first letter is imported, log the Signal in this story.
