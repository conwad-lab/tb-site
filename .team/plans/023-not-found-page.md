---
id: 023
verdict: plan
---

# Plan 023 — A not-found page that leads back to the site

Story: `.team/backlog/023-not-found-page.md` (parked as `_023-not-found-page.md` until 022 is merged)

## Approach
One new static file, `404.html`, built from the head, header and footer of `_layouts/beyond-base.html` and the `.archive` section pattern of `beyond/index.html`, with Liquid replaced by literal values. GitHub Pages serves `/404.html` with status 404 for any missing path, so every URL in it is root-relative. Codex CLI (Astra) builds it from the work order below; the Builder thread posts the order, drives the PR, runs the full Test before commit and attaches the screenshots. Touches the price block: no. Booking CTA: no. Footer: a copy of the `& Beyond` layout's footer on a new page only.

## Baseline
`master` after 022: `find . -name '*.html' -not -path './.claude/*' -not -path './.git/*' -print0 | xargs -0 python3 .github/scripts/check_html.py` exits 0; one screenshot of GitHub's own 404 page for a missing path on the live site (or "not checked" if the session cannot reach it).

## Estimate
size: S
risk: plain
files: 1
codex-rounds: 1
builder: codex-cli — S plain, one new file, every choice made in this plan; first run of the host-Mac poller (installed 2026-11-18, dry run OK)
model: strongest — Conny's model principle (2026-11-18): Fable writes and adjusts the narrow order and checks Astra's outcome; first codex-cli run, so the Builder must judge a `blocked`/`bounced` outcome well

## Files
- `404.html` (new).
- `.team/**` — response file, papercuts (Builder only).

## Copy strings (old → new; all new, on `404.html` only)
- `<title>`: "Page not found — Transformation & Beyond"
- `<meta name="description">`: "This address does not exist on transformationbeyond.se."
- Eyebrow (`p.eyebrow`): "404"
- `h1`: "Page not found"
- Lead 1 (`p.lead`): "The address may be mistyped, or the page may have moved."
- Lead 2 (`p.lead`, `lang="sv"`): "Sidan finns inte. Adressen kan vara felskriven, eller så har sidan flyttats."
- Links (`ol.issues`, each `li > a > span.t`):
  1. "Home" → `/`
  2. "Startsidan på svenska" (`lang="sv"`) → `/sv/`
  3. "& Beyond — veckobrev" (`lang="sv"`) → `/beyond/`
- Header and footer: as in `_layouts/beyond-base.html` (mark "Transformation & Beyond" → `/`; nav "& Beyond" → `/beyond/`; footer "© Transformation & Beyond AB" without year; "reg. no 559411-1634 · Lomma, Sweden"; "RSS" → `/beyond/feed.xml`).

## Steps (Builder thread)
1. Unpark: `git mv .team/backlog/_023-not-found-page.md .team/backlog/023-not-found-page.md`, drop the `parked-until` line (board PR or the first commit of the story branch; say which).
2. Open issue `023: A not-found page that leads back to the site`. Create the label once if missing: `gh label create codex-cli --repo conwad-lab/tb-site --color 5319e7 --description "Work order for the Codex CLI poller on the host Mac"`.
3. Post the work order below as one comment, then add the label. Reminders at about 15 min and at the hour; fallback per `team/CODEX-CLI.md` [K6] (remove the label, post the `@codex` build task, or build yourself).
4. On `done`: fetch the branch, run the full Test before commit (check, screenshots at both widths for `/404.html` and a nested path, link check of the three links against a local server), attach screenshots, `@codex review`. On `blocked`: read the Hinder list; fix the plan or the order (not the code), post a new order. On `bounced`: read the reason; a second bounce → fallback.
5. Response file with `built-by: codex-cli` in its Outcome and the run's Hinder line quoted.

## Work order (post verbatim, one comment)

```
codex-cli: build
Branch: feat/023-not-found-page
Plan: .team/plans/023-not-found-page.md
PR title: 023: A not-found page that leads back to the site

Goal: Add a static 404.html at the repo root that shows "Page not found" in the site's & Beyond style and links back to /, /sv/ and /beyond/.
May touch:
404.html
Steps:
1. Create 404.html. Start with <!doctype html> and <html lang="en">. No front matter, no Liquid ({{ or {% must not appear anywhere in the file).
2. Head, in this order: <meta charset="utf-8">; <meta name="viewport" content="width=device-width,initial-scale=1">; <title>Page not found — Transformation &amp; Beyond</title>; <meta name="description" content="This address does not exist on transformationbeyond.se.">; <meta name="robots" content="noindex">; then the two preconnect links, the Google Fonts stylesheet link (copy the URL character for character from _layouts/beyond-base.html), <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">, <link rel="stylesheet" href="/assets/beyond.css">. No canonical, no og: or twitter: tags, no feed link, no <style>, no <script>.
3. Header: copy the <header> block of _layouts/beyond-base.html and replace each {{ '/x/' | relative_url }} with the literal root-relative path ("/" and "/beyond/").
4. <main> with exactly this structure, using only these classes:
   <section class="archive"><div class="wrap">
     <p class="eyebrow">404</p>
     <h1>Page not found</h1>
     <p class="lead">The address may be mistyped, or the page may have moved.</p>
     <p class="lead" lang="sv">Sidan finns inte. Adressen kan vara felskriven, eller så har sidan flyttats.</p>
     <ol class="issues">
       <li><a href="/"><span class="t">Home</span></a></li>
       <li><a href="/sv/" lang="sv"><span class="t">Startsidan på svenska</span></a></li>
       <li><a href="/beyond/" lang="sv"><span class="t">&amp; Beyond — veckobrev</span></a></li>
     </ol>
   </div></section>
5. Footer: copy the <footer> block of _layouts/beyond-base.html, replace "© {{ site.time | date: "%Y" }} Transformation &amp; Beyond AB" with "© Transformation &amp; Beyond AB", and the RSS href with "/beyond/feed.xml". Keep the inline SVG as it is.
6. Every href and src in the file starts with "/" or "https://". Check with: grep -nE '(href|src)="[^/h]' 404.html (must print nothing).
Test before commit: find . -name '*.html' -not -path './.claude/*' -not -path './.git/*' -print0 | xargs -0 python3 .github/scripts/check_html.py; it must be green
Done when: 404.html exists with the head, header, main and footer above; the grep in step 6 prints nothing; grep -c '{[{%]' 404.html prints 0; Test before commit is green.
Must not: commit or push; touch any file not under May touch; add dependencies; change tests to make them pass; add CSS, scripts, front matter or Liquid; change any copy string from this order; touch index.html, sv/index.html, beyond/**, _layouts/**, _config.yml, sitemap.xml, CNAME, .github/**. If a step needs a choice this order does not make (a class missing from assets/beyond.css, a block that differs from the description), stop and list it under Hinder.
Answer with: one line per Done-when item (`- [x] <item>: <how shown>`), then as the very last line `Hinder: inga` or `Hinder: <short list>`.
```

## Tests
- Test before commit (the poller runs it; the Builder runs it again on the head).
- `grep -nE '(href|src)="[^/h]' 404.html` empty; `grep -c '{[{%]' 404.html` is 0; `git diff master --stat` lists `404.html` and `.team/**` only.
- Local server from the repo root (`python3 -m http.server`) or a Jekyll build: Playwright screenshots of `/404.html` and of the same file fetched as `/a/b/` (e.g. a small handler that serves `404.html` for any missing path, or `jekyll serve`, which does this) at 1440×900 and 390×844, styles and fonts loaded at both paths.
- Link check: `/`, `/sv/`, `/beyond/` return 200 from the local server or Jekyll build; the Google Fonts URL 200 or "not checked".

## Risks / watch out for
- Relative URLs work at `/404.html` and break at `/a/b/`: the nested-path screenshot is the proof.
- `jekyll build` treats a file without front matter as a static file and copies it as is: correct here. Do not add front matter "to be safe": the footer year would then tempt Liquid.
- `.issues` was made for the letter list; on this page it carries three links. Fine at both widths in the existing CSS; if the screenshot shows otherwise, that is a `blocked` for the plan, not a CSS change.

## Out of scope
- Redirects for old paths, a Swedish-first 404 page, any other file.

## Suggestions for PO
- After the first run, log in this story how long the poller took (order → `started` → outcome) and the Hinder line, for the retro and for the mini-1 decision.
