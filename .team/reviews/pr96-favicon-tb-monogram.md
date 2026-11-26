---
id: pr96
verdict: approve
---

# Review pr96 — favicon: the T&B monogram as the site icon

PR: #96 · 2026-11-25 · head reviewed 1a69e74 (this file is the only later commit)

Built straight from the queued row in #86 (no story number). Merge route: `merge: auto`, no Human-merge path touched (no `CNAME`, `_config.yml`, workflow, check script, settings, price, Cal.com URL, contact address or founder claim), so the Judge merges on its word (CLOUD.md § Judge 5, J9).

## Must fix
- none

## Should fix
- none

## Nits
- N1 `assets/icon-192.png`, `assets/icon-512.png` are added but nothing links them (no web manifest). Harmless; a later row can add a manifest if Conny wants an installable icon.
- N2 `prenumerera/index.html` (meta-refresh page) links no icon at all; unchanged by this PR, out of scope.

## Evidence
| Acceptance criterion (row in #86) | Shown by (test, command + output, screenshot) | Result |
|---|---|---|
| New `assets/favicon.svg` with letters as paths, T&B paper/red on navy | File read: `<rect fill="#0C2233">`, paper `#F8F6F1` and red `#CF2318` paths, no `<text>`/font load; rendered at 128 px in Chromium: "T&B" with red `&` on navy | pass |
| `favicon-32.png`, `apple-touch-icon.png` 180×180, `icon-192.png`, `icon-512.png` | `file assets/*.png` → 32×32, 180×180, 192×192, 512×512; `icon-512.png` pixel-identical to the master in the project folder `webbikon/icon-512.png` (PIL difference bbox None) | pass |
| Four pages keep the SVG link and add the 32 px PNG + apple-touch-icon in the page's own path style | Diff read: `index.html` relative, `sv/index.html` and `404.html` root-absolute, `_layouts/beyond-base.html` `relative_url`; +2 lines each, nothing removed | pass |
| No copy, price, booking button or contact address change | `git diff origin/master...1a69e74 -- '*.html'` touches only `<head>` icon links | pass |
| Test before commit | `check_html.py` on every page → exit 0; `pr-check` success on 1a69e74 | pass |
| Screenshots 1440×900 and 390×844, links 200 | My Playwright on a local server: `index.html` and `404.html` at both widths, full page after scrolling; every `link[rel*=icon]` on them → 200. Not attached: the diff touches only `<head>`, nothing visible on the page changes | pass |
| WCAG | Icon is a graphic, not text: red on navy 3.02:1 meets the 3:1 non-text minimum; paper on navy 15.05:1 | pass |

## Codex findings
- Codex code review on 1a69e74 completed with no findings, plus 👍. Nothing to rule on.

## What I checked
- tests run: check_html.py (all pages), Playwright screenshots + icon link status at both widths, PNG sizes, pixel compare with the master.
- tried to break: path style per page (relative vs root vs Jekyll filter) so `/sv/` and `/beyond/` resolve; sync gate: `git merge-base --is-ancestor origin/master 1a69e74` → yes.
- scope vs story: exactly the row in #86, nothing else.

## Papercuts
