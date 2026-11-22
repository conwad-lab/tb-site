---
id: 030
verdict: plan
---

# Plan 030 — The home pages render in standards mode

Story: `.team/backlog/030-home-pages-standards-mode.md`

## Approach
One line in each home page and a small rule in the HTML check, plus a stdlib test that runs the check on two temporary home pages. Codex CLI (Astra) builds from the work order; the Builder thread does the visual before/after on the Jekyll build, which the poller cannot. `.github/scripts/check_html.py` is a Human-merge path: Conny gets a "Merga #N?" card. Touches the price block: no. Booking CTA: no. Footer: no.

## Baseline
`master` after 029: Test before commit green; Jekyll build (`gem install jekyll` in the cloud, no Gemfile) and screenshots of `/` and `/sv/` at both widths; `document.compatMode` is `BackCompat` on both.

## Estimate
size: S
risk: human-merge
files: 4
codex-rounds: 2
builder: codex-cli — the three edits are fully specified; the layout comparison stays with the Builder thread
codex-model: astra — human-merge risk (the required check changes)
model: light — Codex builds; strongest is not needed for the screenshot comparison

## Files
- `index.html`, `sv/index.html` — `<!doctype html>` after the front matter.
- `.github/scripts/check_html.py` — the home-page doctype rule (Human-merge path; listed here so the poller's push guard allows it).
- `bin/test-check-html.py` (new) — the Proof test.
- `.team/**` — response file (Builder only).

## Steps (Builder thread)
1. (Unparked on board PR 2026-11-22 after 029 merged as #70.)
2. Issue `030: The home pages render in standards mode`, post the work order without the `Model:` line (as in plan 029), add the label `codex-cli`; reminders and fallback per `team/CODEX-CLI.md` [K6].
3. On `done`: Jekyll build before/after, screenshots at both widths, `document.compatMode`, link check. If anything moves, fix it in `assets/site.css` yourself (`built-by: claude` for that commit) and attach the before/after.
4. Ask for a Judge; the merge needs Conny's card naming the PR and head.

## Work order
```
Goal: Put <!doctype html> first in the generated HTML of both home pages and make check_html.py fail a home page without it.
May touch:
index.html
sv/index.html
.github/scripts/check_html.py
bin/test-check-html.py
Steps:
1. index.html: insert the line <!doctype html> between the second line (---) and the line <html lang="en">. sv/index.html: insert the line <!doctype html> between the line --- that closes the front matter (line 3) and the line <html lang="sv">.
2. .github/scripts/check_html.py: add a function needs_doctype(path) that returns True when os.path.normpath(path) equals "index.html" or os.path.join("sv", "index.html"). In the main loop, after the empty-file check, for such a path strip a leading front matter block (the text starts with a line "---", and runs to and including the next line "---") and leading whitespace; if the rest does not start with "<!doctype html>" compared case-insensitively, print f"{path}: missing <!doctype html>" and count the file as bad. Update the module docstring's first line to "Fail on unreadable HTML files, unbalanced tags, or a home page without <!doctype html>." Change nothing else in the file.
3. Create bin/test-check-html.py: Python 3 standard library only, run from the repo root as python3 bin/test-check-html.py. In a tempfile.TemporaryDirectory it writes index.html with the text "---\n---\n<html lang=\"en\">\n<title>t</title>\n</html>\n" and runs [sys.executable, <absolute path of .github/scripts/check_html.py>, "index.html"] with cwd set to the temp dir: it must exit 1 and print "missing <!doctype html>". Then it rewrites the file with "<!doctype html>\n" inserted after the second "---" line: the run must exit 0. Then the same two cases for sv/index.html (with a front matter line "permalink: /sv/"). Then a file other.html without doctype must exit 0. Print one line per failed case; exit 1 on any failure, else 0.
Proof: bin/test-check-html.py — python3 bin/test-check-html.py
Must not: commit or push; touch any file not under May touch; add dependencies; change tests to make them pass; change any other line of index.html or sv/index.html; change how tag balance is checked; touch .github/workflows/**, _config.yml, CNAME, assets/**. If a quoted line does not match the file, stop and list it under Hinder.
```

## Tests
- `bin/test-check-html.py` (Proof), Test before commit.
- Builder: before/after screenshots on the Jekyll build, `document.compatMode`.

## Risks / watch out for
- Standards mode can change line heights around inline images and SVG; the screenshot comparison decides.

## Out of scope
- A lower hero (tried after this story).
