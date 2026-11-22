---
id: 030
verdict: approve
---

# Review 030 — The home pages render in standards mode

PR: #73 · 2026-11-22 · reviewed head ea135ae (code last changed in 991d9dd)

## Must fix
- none

## Should fix
- none

## Nits
- N1 `assets/site.css:149` — `.sample{display:block}` makes the link a full-width block: at 1440 on `/sv/` its box grows from 490 to 571px, so the empty space to the right of the text is now clickable. Invisible, harmless; `display:inline-block` or `width:fit-content` would keep the old hit area if anyone cares.
- N2 `assets/site.css:149` — `line-height:22.67px` is a measured quirks-mode value tied to the 16px font size; if `.sample`'s font size changes, the number silently stops meaning anything. A unitless `1.417` says the same thing and scales.
- N3 `.github/scripts/check_html.py:1-2` — the work order said "change nothing else"; the docstring's `Usage:` part moved to a second line. Harmless.
- N4 process (for the Coordinator, not this PR): the Builder's papercut notes that plan 030 touches a Human-merge path, so CLOUD.md [F5] asked for a plan attack that the plan's Steps skipped.

## Evidence
| Acceptance criterion | Shown by (test, command + output, screenshot) | Result |
|---|---|---|
| `<!doctype html>` directly after the front matter in `index.html` and `sv/index.html` | diff; Jekyll 4.4.1 build of the head: first line of `_site/index.html` and `_site/sv/index.html` is `<!doctype html>` | pass |
| `check_html.py` fails a home page without it with `<path>: missing <!doctype html>`, others as before | diff read (front matter strip, case-insensitive, `os.path.normpath` so `./index.html` from pr-check's `find .` matches); `python3 .github/scripts/check_html.py ./index.html` → 0; `bin/test-check-html.py` covers en/sv with and without, and `other.html` | pass |
| `bin/test-check-html.py` (stdlib) + Test before commit green | `python3 bin/test-check-html.py` → exit 0; Test before commit `find … \| xargs -0 python3 .github/scripts/check_html.py` → exit 0; `pr-check` green on ea135ae | pass |
| Jekyll before/after at 1440×900 and 390×844 match; `compatMode` `CSS1Compat` | my own Playwright run on master vs head builds (reduced motion, scrolled to bottom, external requests blocked): `BackCompat` → `CSS1Compat` on both pages; page height identical at 1440 (9793 / 10513), −2px at 390 and −2/−3px at 360; button, price block and footer at identical positions; pixel diff at 1440 confined to the sample link's text rows (y 5922–5942 en, 6557–6578 sv); `scrollWidth == innerWidth` at 1440, 390, 360. Builder's screenshots in `.team/screenshots/030/` | pass |
| Price block, booking CTA, Cal.com URL, contact address, founder claims, copy unchanged | text-only diff of built pages master vs head: only the added doctype line; every `href` identical | pass |

## Codex findings
- Codex review on 991d9dd (last commit outside `.team/reviews/**`): "Didn't find any major issues". No findings to rule on; the Builder disputed nothing.

## What I checked
- tests run: `bin/test-check-html.py`, Test before commit, Jekyll build of master and head, Playwright at 1440/390/360 with geometry and pixel diff.
- tried to break: `./`-prefixed paths (pr-check passes `./index.html`); front matter without closing `---` (falls through to the full text → fails, correct); uppercase `<!DOCTYPE html>` (accepted); whether `.btn-in`/`.sample` are used on any other page (only the two home pages); the `+br` selector hides only the `<br>` after the button.
- scope vs story: CSS fix is the one the story allows ("fixes it in `assets/site.css`"), Builder says so (`built-by: codex-cli->claude`). No rulebook files touched.
- Link check: hrefs unchanged from master; live targets (transformationbeyond.se, dignami.com, mondmodel.com, the R2 sample PDF) **not checked** — the cloud's network blocks them. Conny checks the live page after merge (Operator trigger).

## Merge
Human-merge path (`.github/scripts/check_html.py`), no [H1] exception: approve with no M/S open, no Codex finding ruled not valid, Codex finished on the last code commit with no findings, checks green, head contains master → merge on agreement [J10].

## Papercuts
2026-11-22 | reviewer | `gh pr view/checkout` refused (GraphQL blocked in the cloud) | REST `gh api` + `git fetch origin pull/73/head` | open

— Judge (Claude) on behalf of Conny
