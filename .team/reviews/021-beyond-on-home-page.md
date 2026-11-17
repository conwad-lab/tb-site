---
id: 021
verdict: approve
---

# Review 021 — & Beyond on the home page — menu link and latest letter

PR: #50 · 2026-11-17 · reviewed head `6ae2483cfb285cba3165197b4930ab9dd4b5ccfa`

Route: `merge: auto` (`.team/team.md`); the diff touches `index.html`, `sv/index.html`, `_includes/latest-letter.html` and `.team/**`, none on a Human-merge path, no price, booking URL, contact address or founder claim changed, not a rulebook story. Merges on my word (CLOUD.md § Judge 5 [J9]).

## Must fix
- none

## Should fix
- none

## Nits
- N1 `index.html:195`, `sv/index.html:197`, `sv/index.html:413` — `/beyond/` is hard-coded while the include uses `relative_url`. Fine for a root-hosted site with `CNAME`; use `{{ '/beyond/' | relative_url }}` if the site ever gets a `baseurl`.
- N2 Screenshots are in the project files folder `tb-site-021/`, not on the PR (the cloud session cannot upload images to a PR). The review check says "attached to the PR"; same gap as earlier stories, worth a papercut-driven rule change rather than a block here.

## Evidence
| Acceptance criterion | Shown by | Result |
|---|---|---|
| Nav link "& Beyond" → `/beyond/` before the booking button on `/` and `/sv/`; visible at 390 px without horizontal scroll | Jekyll 3.10.0 build + Playwright: `a.nav-beyond` rendered at 390 and 1440 on both pages, left of `.cta`; `scrollWidth` 390 at 390 px, 1440 at 1440 px. `.nav-r a.nav-beyond` (0,2,1) beats `.nav-r a:not(.cta)` (0,2,1) by source order (line 187 after 51). Header wraps to two rows at 390 px exactly as on master (master already does) | pass |
| sv footer link "& Beyond — veckobrev" | diff `sv/index.html:413`, `lang="sv"` | pass |
| Latest-letter block from `site.beyond`, newest by `date`; week, title (`lang="sv"`), date, link; en "(in Swedish)"; nothing with no letters | Build without letters: 0 `latest-letter` sections on both pages, no stray `{{`/`{%`. Build with fixture `_beyond/2026-w48.md` (title with `<`, `&`): en "Week 48 · 24 November 2026", sv "Vecka 48 · 24 november 2026", title escaped (`&lt;om&gt; &amp;`), links `/beyond/2026-w48/` and `/beyond/` both 200 on the local server | pass |
| Fixture shown, not committed | `_beyond/` absent from the PR tree | pass |
| Price block, booking CTA, Cal.com URL, contact, founder claims unchanged; no other copy | full diff read: only additions listed above plus empty front matter on `index.html`; built `_site/index.html` equals the source minus the front matter and the include line (one blank line differs) | pass |
| No script, tracker or font host; WCAG AA | no `<script>`/`<link>` added; `--bronze-deep` #5C421E on `--paper` #F7F5F0 ≈ 9.3:1, `--muted` #5B5E62 on #F7F5F0 ≈ 6.2:1 | pass |
| Team settings tests, screenshots both widths | `python3 -m html.parser index.html` exit 0; `check_html.py index.html sv/index.html _includes/latest-letter.html` exit 0; `pr-check` success on 6ae2483; own screenshots at 390 px, Builder's 8 in `tb-site-021/` | pass (N2) |

## Codex findings
- Codex review on 6ae2483 finished: "Didn't find any major issues" (code_review status completed, no findings). No Builder disputes.

## What I checked
- tests run: as in Evidence; Jekyll 3.10.0 builds in temp copies with and without a fixture letter.
- tried to break: Liquid in the newly front-mattered `index.html` (only the include, no other `{{`/`{%`); HTML in a letter title (escaped); empty collection (block absent, no empty heading); `id="beyond"` collision (none on either page); nav at 390 px.
- scope vs story: matches; out-of-scope items (sign-up, UTM, import) untouched. External links not re-checked (no external href changed).

## Papercuts
- 2026-11-17 | reviewer | no Jekyll in the cloud image | `gem install jekyll -v 3.10.0 kramdown-parser-gfm webrick` | open

— Judge (Claude) on behalf of Conny
