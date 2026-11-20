# Review brief 063: counter-critique of the design follow-up

Analysis only. Nothing is built from this brief, and no PR is opened.

Read on this branch (same as `master` at 596d669): `index.html`, `sv/index.html`, `assets/site.css`, `robots.txt`, `.github/scripts/check_html.py`.

## Background

The start pages were rebuilt in #60 and #62 (navy `#0C2233`, red `#CF2318`, paper `#F8F6F1`, salmon `#F6E6DA`, film on the first screen). A research note on web design for humans and agents gives this checklist: film needs a poster, a pause control and a reduced-motion path and must not be the LCP element; the hero should be a real full-width image with a literal headline and the next section peeking in; palettes dominated by dark blue read as generated; pages need semantic HTML and one clear heading tree; search and user bots must be let in by robots.txt and by any firewall; JSON-LD must match visible text; a Markdown version and llms.txt come last.

## Findings to challenge

1. The film autoplays and loops with no pause control. WCAG 2.2.2 asks for one.
2. Neither page has `<!doctype html>`, so browsers use quirks mode. `check_html.py` does not check for it.
3. Colour share on a full-page screenshot at 1440 px: paper about 50 %, navy 11 %, red 8 %, salmon 7 %. Navy dominates only the first screen, because `.hero` has `min-height:100svh` and nothing of the next section shows.
4. The sections "Arbetssätt" and "Frågorna vi besvarar" have a `p.tag` label and no `h2`. Their `h3`s hang under the `h1`.
5. Title and description on `/sv/` say Malmö, Lund, Skåne and Lomma. The owner's position since 2026-11-19 is Nordic with a base in Greater Copenhagen. The JSON-LD offer description on the Swedish page is in English.
6. `robots.txt` allows everything. The site is on GitHub Pages, so there is no firewall of our own. The live domain was not reachable for a check.
7. No Markdown version and no `llms.txt`.

## Intended recommendation, in order

1. One small story: pause button on the film, doctype on both pages plus a check in `check_html.py`, `h2` for the two section labels with the same look.
2. One small design story: lower the hero to about 86svh so the red booking band shows on the first screen, and put one more section on salmon. No palette change.
3. Owner's decision: move title and description from Skåne to Nordic / Greater Copenhagen, or not.
4. Leave robots.txt, verify bot access once from a machine that reaches the domain.
5. Skip Markdown and llms.txt for now.

## Questions

- Is any finding wrong, or is something more important missing (performance, accessibility, agent readability)?
- Is the order right? What would you drop or merge?
- Is a lower hero plus one salmon section the right answer to "navy dominates", or the wrong fix?
- Does adding the doctype risk changing the approved layout, and how would you guard against it?

Answer briefly, with file and line where you disagree.
