---
id: 016
verdict: plan
---

# Plan 016 — & Beyond archive

Story: `.team/backlog/016-and-beyond-archive.md`

## Approach
Use the Jekyll that GitHub Pages already runs for this repo (`_config.yml` exists; `index.html` has no front matter, so Jekyll copies it unchanged). Add a Jekyll collection `beyond` with one Markdown file per letter, two layouts, one stylesheet and a hand-written Liquid Atom feed (`beyond/feed.xml`). No plugin, no Actions workflow, no Node, no new dependency.

Letters come from the private repo conwad-lab/ai-insikter. Only letters marked `status: publicerad` are copied in, by `bin/import-beyond.py`, which also validates them; drafts and review files never reach this public repo.

URL: the publication week, which is what the cover and the LinkedIn title use (`publiceras: 2026-11-02` → ISO week 45 → `/beyond/2026-v45/`). The source file keeps its Saturday week (`2026-V44`) in front matter as `source`.

## Files
- `_config.yml` (Human-merge path): add `url`, `title`, `description`, `author`, `beyond_linkedin_url` (empty), `collections.beyond` (`output: true`, `permalink: /beyond/:name/`), `defaults` (layout `beyond-letter` for the collection), and `bin` + `Gemfile*` to `exclude`. `description` is set so the github-metadata plugin Pages runs does not need the API for it. The existing exclude list stays.
- `_layouts/beyond-base.html` — HTML shell for the two `/beyond/` pages: `lang="sv"`, title, description, canonical, OG tags (cover image when the letter has one), the same Google Fonts link and favicon as `index.html`, `assets/beyond.css`, `<link rel="alternate" type="application/atom+xml">`, header with the mark linking to `/` and a link to the archive, footer as on the home page.
- `_layouts/beyond-letter.html` — week label, title, lead, publication date, body (`{{ content }}`), "Alla nummer" link back.
- `beyond/feed.xml` — Atom feed of the collection, newest 20, full content, `xml:lang="sv"`. (Built in place of `jekyll-feed`, whose collection feed is titled "Transformation & Beyond | Beyond" and which also writes an empty `/feed.xml`.)
- `_data/beyond_months.yml` — Swedish month names for the letter date.
- `beyond/index.html` — the archive (front matter, layout `beyond-base`): short intro in Swedish, list of `site.beyond | sort: 'date' | reverse`, RSS link. A LinkedIn follow link only when `site.beyond_linkedin_url` is set (no URL is known yet; Operatör line).
- `assets/beyond.css` — tokens copied from `index.html` `:root` (no new colours), reading-width typography for long Swedish text, images full width, mobile rules.
- `_beyond/2026-v45.md` — the first letter, produced by the script, **only once V44 is `status: publicerad` in ai-insikter**. Until then the PR carries no letter and the archive shows an empty state.
- `assets/beyond/2026-v45/*.png` — the letter's images, copied by the script.
- `bin/import-beyond.py` — reads a `-publicering.md`, takes the section between `# Substack / LinkedIn-artikel` and the next `# ` heading (drops the LinkedIn post), takes the title from the first `## `, the lead from the italic line under it, rewrites `grafik/…` image paths to `/assets/beyond/<slug>/…` with alt text from `<image>.alt.txt` when present, writes front matter (`title`, `lead`, `date`, `week`, `year`, `source`, `image`), and copies the images. Refuses (exit 1, message per problem): status not `publicerad` (unless `--allow-draft`, for local tests only, which writes nowhere but a given `--out`), no title, no `### Källor` with at least one link, a missing image, an HTML comment, `veckor/` or `insikter/` paths, `[Connys`, `TODO`, `<!--`.
- `index.html` — one footer link: `<span><a href="/beyond/">&amp; Beyond — weekly letter (in Swedish)</a></span>`. Touches the footer: yes. Price block, booking CTA: no. Copy strings: only this new one.
- `README.md` — a short "& Beyond" section: how to import a letter, that a merge publishes it.

## Steps
1. Branch `feat/016-and-beyond-archive` from master.
2. `_config.yml`, layouts, archive, stylesheet, footer link.
3. `bin/import-beyond.py`; run it on `2026-V44-publicering.md` with `--allow-draft --out` into a scratch copy to build and screenshot; commit the real letter only when V44 is `publicerad`.
4. Build locally with the github-pages gem (`jekyll build`), run Tests on `_site/`.

## Tests
- `python3 -m html.parser index.html` exits 0, and the same on `_site/beyond/index.html` and each `_site/beyond/*/index.html`.
- `jekyll build` with the github-pages gem (the Pages versions) exits 0 with no warnings about the collection or the feed.
- `_site/index.html` is byte-identical to `index.html`.
- `_site/beyond/feed.xml` parses as XML with `feed` root (Atom); one `entry` per letter.
- `_site/` contains none of `AGENTS.md`, `CLAUDE.md`, `README.md`, `docs/`, `.team/`, `.claude/`, `bin/`.
- Script: refuses the V44 file while it says `status: utkast` (exit 1); with `--allow-draft` produces a page with three images and a source list; refuses a fixture with `<!--` and one with a missing image.
- Playwright on `_site/` served locally: home, `/beyond/` and the letter at 1440×900 and 390×844, scrolled to the bottom, full-page screenshots; `scrollWidth === innerWidth` at 390.
- Every `href` on the new pages returns 200 (`mailto:` excluded; a URL the session's network blocks is listed as not checked).
- Contrast: text colours reuse existing tokens (`--ink`, `--body`, `--muted`, `--bronze` on `--paper`), all AA on the home page already; note the ratios in the PR.

## Risks / watch out for
- Pages runs Jekyll 3.x via the github-pages gem; test with that gem, not a newer Jekyll.
- A local build with the github-pages gem also writes `assets/css/style.css` (the default Primer theme). Nothing links it; same for master, which already has `_config.yml`.
- The letter text is Conny's published text; the script must not change wording. Only image paths change.
- Do not touch `CNAME`, the price, Cal.com URL or contact address.

## Out of scope
- E-mail form (step 2), automation of the import, English versions.

## Suggestions for PO
- Operatör: Conny supplies the LinkedIn newsletter URL for `beyond_linkedin_url`, and marks V44 `status: publicerad` in ai-insikter.
