---
id: 033
verdict: plan
---

# Plan 033 — The & Beyond archive in navy and red

Story: `.team/backlog/033-beyond-navy-and-red.md`

## Approach
Only the look changes. `assets/beyond.css` gets the home pages' tokens (copied from `assets/site.css` `:root`, no new colour), the bronze and mono tokens go, and header and footer become navy bands. The two pages that load fonts for this stylesheet (`_layouts/beyond-base.html`, `404.html`) load the home pages' exact Google Fonts URL, so Familjen Grotesk replaces Hanken Grotesk and JetBrains Mono, and Newsreader's light 300 (not in that URL) gives way to 500 as on the home pages. The footer mark and the favicon are recoloured. A new dependency-free `bin/test-beyond-palette.py` pins it. Codex CLI (Astra) builds from the work order; every value is settled below. Touches the price block: no. Booking CTA: no. Footer: colours and the mark's fills only, its text and links unchanged.

## Baseline
`master` at 01841c2 (031 merged as #77): Test before commit exits 0. The Builder builds the site with Jekyll and takes screenshots at 1440×900 and 390×844 of `/beyond/`, `/404.html`, and a letter page from a local fixture letter in `_beyond/` (never committed), for before/after.

## Estimate
size: S
risk: plain
files: 5
codex-rounds: 2
builder: codex-cli — every token, rule and file line is settled in the work order
codex-model: astra — host default, as in plans 029–031
model: light — Codex builds; the Builder thread posts the order, runs screenshots, contrast and the link check

## Files
- `assets/beyond.css` — tokens and the rules named in the work order.
- `_layouts/beyond-base.html` — font link, footer mark fills.
- `404.html` — font link, footer mark fills.
- `assets/favicon.svg` — fills and its label text.
- `bin/test-beyond-palette.py` — new Proof test.
- `.team/**` — response file, papercuts (Builder only).

## Copy strings (old → new)
- None visible. `assets/favicon.svg` label (read by screen readers only where the icon is shown as an image): "weighted plus with bronze overshoot block" → "weighted plus with red overshoot block".

## Steps (Builder thread)
1. Open issue `033: The & Beyond archive in navy and red`.
2. Post the work order below unchanged as one comment with the header lines the poller reads (`templates/codex.md`), `Branch: feat/033-beyond-navy-red`, without a `Model:` line, then add the label `codex-cli`. Reminders at about 15 min and at the hour; fallback per `team/CODEX-CLI.md` [K6].
3. On `done`: Test before commit on the poller's head, `python3 bin/test-beyond-palette.py`, and on the Jekyll build (with the uncommitted fixture letter): screenshots before/after at both widths of `/beyond/`, the letter and `/404.html`; `getComputedStyle(document.body).fontFamily` starts with "Familjen Grotesk"; no network request to a font family other than Familjen Grotesk and Newsreader; Tab through header and footer links and see the focus ring on navy and on paper. Measure contrast for every pair in the work order's table and put the values in the response file. Link check. `@codex review`.
4. Response file with `built-by: codex-cli` in its Outcome and the run's Hinder line quoted.

## Work order
```
Goal: Restyle the & Beyond pages (assets/beyond.css and the pages that load it) from bronze to the home pages' navy and red, with Familjen Grotesk and Newsreader, changing no text.
May touch:
assets/beyond.css
_layouts/beyond-base.html
404.html
assets/favicon.svg
bin/test-beyond-palette.py
Steps:
1. assets/beyond.css: replace the first comment line and the whole :root block (lines 1-8) with exactly:
/* & Beyond (stories 016, 033): letter and archive pages in the home pages' navy and red. Colours copied from assets/site.css :root, no new colours. */
:root{
  --paper:#F8F6F1; --ink:#0C2233; --body:#14181B; --muted:#5B5F66;
  --navy:#0C2233; --on-navy:#F8F6F1; --red:#CF2318; --red-deep:#B01C13; --rule:#0C2233; --hair:#F6E6DA;
  --serif:"Newsreader",Georgia,"Times New Roman",serif;
  --sans:"Familjen Grotesk","Helvetica Neue",Arial,sans-serif;
}
2. assets/beyond.css, in all remaining rules: replace every var(--bronze-deep) with var(--red-deep), then every var(--bronze) with var(--red), and every var(--mono) with var(--sans).
3. assets/beyond.css, replace these whole lines (each starts as shown) with exactly:
::selection{background:var(--red);color:#FFFFFF}
body > header{background:var(--navy);color:var(--on-navy)}
.mark span{font-family:var(--serif);font-weight:500;font-size:1em;color:var(--red)}
.nav-r a{text-decoration:none;color:var(--on-navy);border-bottom:2px solid transparent;padding-bottom:2px}
.nav-r a:hover{color:var(--on-navy);border-color:var(--red)}
.eyebrow{font-family:var(--sans);font-size:12px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--red);margin:0 0 22px;display:flex;gap:14px;align-items:center;line-height:1.4}
.archive h1,.letter h1{font-family:var(--serif);font-weight:500;letter-spacing:-.02em;line-height:1.04;margin:.2em 0 .5em;text-wrap:balance;color:var(--ink)}
.follow{font-family:var(--sans);font-size:14px;font-weight:500;letter-spacing:.02em;margin:0 0 48px}
.issues .wk{display:block;font-family:var(--sans);font-size:12px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--red);margin-bottom:8px}
.meta{font-family:var(--sans);font-size:13px;letter-spacing:.02em;color:var(--muted);margin:0 0 40px;padding-bottom:28px;border-bottom:1px solid var(--rule)}
.back{margin-top:48px;padding-top:24px;border-top:1px solid var(--rule);font-family:var(--sans);font-size:14px;font-weight:500;letter-spacing:.02em}
footer{background:var(--navy);color:var(--on-navy);padding:38px 0 56px;font-size:13px}
.foot .mono{font-family:var(--sans);font-size:13px;letter-spacing:.02em}
.foot a{color:var(--on-navy);text-decoration:none;border-bottom:1px solid var(--red)}
.foot a:hover{color:var(--on-navy);border-color:var(--on-navy)}
   The lines to replace are the ones starting "::selection{", "body > header{", ".mark span{", ".nav-r a{", ".nav-r a:hover{", ".eyebrow{", ".archive h1,.letter h1{", ".follow{", ".issues .wk{", ".meta{", ".back{" (the rule, not ".back a"), "footer{", ".foot .mono{", ".foot a{", ".foot a:hover{".
4. assets/beyond.css: directly after the line starting "a:focus-visible{" add exactly:
body > header a:focus-visible,footer a:focus-visible{outline-color:var(--on-navy)}
5. _layouts/beyond-base.html and 404.html: replace the line that starts '<link href="https://fonts.googleapis.com/css2?' with line 21 of index.html, copied byte for byte. Keep both preconnect lines.
6. _layouts/beyond-base.html and 404.html, footer SVG: change fill="#1C2022" to fill="#F8F6F1" and fill="#8A6430" to fill="#CF2318". Nothing else in those lines.
7. assets/favicon.svg: fill="#F7F5F0" → fill="#F8F6F1", fill="#1C2022" → fill="#0C2233", fill="#8A6430" → fill="#CF2318", and in aria-label "with bronze overshoot block" → "with red overshoot block". Nothing else.
8. New file bin/test-beyond-palette.py, python3 stdlib only, executable, exit 1 with one line per failure, print "ok" and exit 0 otherwise. Checks:
   a. None of assets/beyond.css, _layouts/beyond-base.html, _layouts/beyond-letter.html, beyond/index.html, 404.html, assets/favicon.svg contains (case-insensitive) any of: #7A5729 #5C421E #8A6430 #E8D9BE #F7F5F0 #1C2022 #E3DFD5 #3B3E42 #5B5E62 Hanken JetBrains --mono --bronze.
   b. Every hex colour (#RGB or #RRGGBB) in assets/beyond.css is, upper-cased, one of the hex values in the :root block of assets/site.css or #FFFFFF.
   c. The Google Fonts stylesheet href in _layouts/beyond-base.html and in 404.html equals the one in index.html, and each of the three files has exactly one link to fonts.googleapis.com/css2.
   d. Every fill="#..." in assets/favicon.svg and in the footer SVG of _layouts/beyond-base.html and 404.html is one of #F8F6F1 #0C2233 #CF2318.
   e. assets/beyond.css contains each line from step 3 and the line from step 4 exactly.
Proof: bin/test-beyond-palette.py — python3 bin/test-beyond-palette.py
Must not: commit or push; touch any file not under May touch; add dependencies; weaken a check to make it pass; change any text, link, element, class name, the RSS feed, _config.yml, index.html, sv/index.html, assets/site.css, CNAME, .github/**, beyond/**, _includes/**; add a colour not in assets/site.css :root, a style attribute, a script, or a font or host. If a quoted line does not match the file, or a step needs a choice this order does not make, stop and list it under Hinder.
```

## Contrast pairs (Builder measures, all must hold)
| Pair | Expected | Need |
|---|---|---|
| navy #0C2233 headings / black #14181B body on paper #F8F6F1 | 15.1 / 16.5 | 4.5 |
| red #CF2318 eyebrow, week label, links on paper | 4.98 | 4.5 |
| deep red #B01C13 hover on paper | 6.44 | 4.5 |
| grey #5B5F66 meta on paper | 5.94 | 4.5 |
| paper on navy (header, footer text) | 15.1 | 4.5 |
| red border/`&` on navy (non-text, wordmark) | 3.02 | 3 (logotype exempt) |
| focus ring paper on navy / red on paper | 15.1 / 4.98 | 3 |

## Tests
- `bin/test-beyond-palette.py` (Proof) and Test before commit (`check_html.py` on every page).
- Builder: Steps 3 (screenshots, font family, font requests, focus, contrast, link check).

## Risks / watch out for
- Newsreader 300 is not in the home pages' font URL; the plan moves the two h1 to 500 so the browser does not synthesise a light face.
- `.foot .mono` keeps its class name (markup unchanged) while it no longer is monospace; harmless, a later clean-up if wanted.
- No letter exists yet, so the letter layout is only seen through the fixture; the Builder must not commit `_beyond/`.
- The favicon also shows on the home pages; that is intended (the story's Vad blir publikt).

## Out of scope
- `beyond_linkedin_url` (034), positioning on `/sv/` (032), layout changes, an email signup.
