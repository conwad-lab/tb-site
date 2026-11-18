---
id: 023
verdict: approve
---

# Review 023 — A not-found page that leads back to the site

PR: #56 · 2026-11-18 · reviewed head `c6a3c80610cb82e43338e04c4853035ae37df7fc`

Judged against story `.team/backlog/023-not-found-page.md`, plan `.team/plans/023-not-found-page.md` (incl. its verbatim work order), `AGENTS.md` and `CLOUD.md` § Judge at v0.8.9 (230dee6). Codex-built PR (codex-cli): whole diff read.

## Must fix
- none

## Should fix
- none

## Nits
- N1 `404.html:44` — the footer SVG keeps its inline `style="display:inline-block;vertical-align:-4px"` attribute. That is what the order said ("Keep the inline SVG as it is") and what `_layouts/beyond-base.html` does, so it does not break "no inline `<style>`" (that is about the element). Noted only so a later CSP story knows the attribute exists on this page too.
- N2 `.team/PAPERCUTS.md:18` — the Builder's papercut uses role `Builder` (capital B) while earlier lines use `builder`. Cosmetic; the retro greps lower case.

## Evidence
| Acceptance criterion | Shown by (test, command + output, screenshot) | Result |
|---|---|---|
| New static `404.html` at root, no front matter, no Liquid, `lang="en"`, robots noindex, no canonical, no OG | read `404.html` 1–49: starts `<!doctype html>`/`<html lang="en">`, `<meta name="robots" content="noindex">`, no `canonical`/`og:`/`twitter:`; `grep -c '{[{%]' 404.html` → 0 | pass |
| Only `/assets/beyond.css` + existing classes, same Fonts URL, favicon; no `<style>`, no script, no new host | `diff` of the `css2?` URL in `_layouts/beyond-base.html` vs `404.html`: identical; classes `archive wrap eyebrow lead issues mark nav-r foot mono` and `.issues .t` (`assets/beyond.css:40`) all present; no `<style>`/`<script>`; hosts: fonts.googleapis.com, fonts.gstatic.com, w3.org (SVG xmlns) only, as in the layout | pass |
| Every href/src root-relative or absolute; works at a nested path | `grep -nE '(href|src)="[^/h]' 404.html` → empty. Local server returning `404.html` with status 404 for any missing path; Playwright at `/a/b/c`: status 404, `h1` "Page not found" in Newsreader, `document.fonts` loaded Newsreader/Hanken Grotesk/JetBrains Mono, beyond.css loaded (judge screenshots, both widths) | pass |
| Copy exactly as plan's Copy strings; Swedish lines `lang="sv"` | title, description, eyebrow `404`, h1, both leads, three link texts compared line by line with plan § Copy strings and work order step 4: identical; Swedish lead and links 2–3 carry `lang="sv"` | pass |
| Header and footer match `beyond-base.html` minus the year | side-by-side read: header identical with `/` and `/beyond/` literal; footer identical with `© Transformation &amp; Beyond AB` (no year), reg. no line, RSS → `/beyond/feed.xml` | pass |
| No price block, booking CTA, Cal.com URL, contact address, founder claim; no other file except `.team/**` | `git diff --name-only origin/master...HEAD`: `404.html` + `.team/PAPERCUTS.md`, `.team/reviews/023-…response.md`, four `.team/screenshots/*.png`; no `cal.com`, `mailto:`, price or founder text in `404.html`. No Human-merge path touched | pass |
| Test before commit green; screenshots 1440×900 and 390×844 at `/404.html` and nested, attached; WCAG AA | `check_html.py` over all `*.html`: exit 0. Builder's four screenshots in `.team/screenshots/` linked from the PR body; my own Playwright run at both widths, both paths, full page after scroll: `scrollWidth == clientWidth` (1440/1440, 390/390), layout as expected (390 nested screenshot viewed). Only existing beyond.css colour pairs (no CSS added) | pass |
| Link check | local server: `/` 200, `/sv/` 200, `/beyond/` 200, `/beyond/feed.xml` 200, `/assets/favicon.svg` 200; Google Fonts URL 200 | pass |
| Required check | `pr-check` on c6a3c80: completed, success | pass |
| Sync gate | `git merge-base --is-ancestor origin/master c6a3c80` true (master 1acbc85) | pass |
| Signal: live `/finns-inte-023` returns 404 with the page | after merge; the cloud session's proxy refuses `transformationbeyond.se` (connect_rejected), so **not checked** here — the Coordinator's routine or Conny's live check (Operator trigger: every merged PR) | not yet |

## Codex findings
- Round 1 on d662f33 (the last commit outside `.team/reviews/**`; c6a3c80 only edits the response file): finished 2026-11-18 21:13Z, "Didn't find any major issues" (https://github.com/conwad-lab/tb-site/pull/56#issuecomment-6991831666). No findings to rule on, no Builder disputes. The earlier attempts on bd05e73 ended in usage-limit replies, not reviews.

## What I checked
- tests run: Test before commit (`check_html.py`, exit 0); Playwright 1440×900 and 390×844 at `/404.html` and `/a/b/c` with a status-404 fallback server; link check of all five internal targets; fonts URL.
- tried to break: nested path (relative URL breakage) — none; horizontal overflow at 390 — none; Liquid leaking into a static file — none; `.issues` list styling with 3 non-letter items — renders cleanly; Jekyll copying `.team/screenshots/*.png` to the site — `.team` is a dot-directory, which Jekyll excludes by default; `sitemap.xml` already skips `/404.html`.
- scope vs story: exactly one site file, the one in the work order's May touch; Builder files under `.team/**` only. Route: `merge: auto`, no Human-merge path, not a rulebook story → merge on the Judge's word (CLOUD.md § Judge 5 [J9]); Codex also agreed.

## Papercuts
- 2026-11-18 | reviewer | live site and the R2 image host are refused by the cloud proxy | Signal left as not checked, routine/Conny reads it | open

— Judge (Claude) on behalf of Conny
