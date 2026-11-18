---
id: 023
title: "A not-found page that leads back to the site"
parked-until: 022
---

## Outcome
A visitor who follows a broken or old link to transformationbeyond.se (for example a shared letter URL with a typo, or an address from before the site refresh) gets a page in the site's own look with a way back: the English home page, the Swedish home page and *& Beyond*, instead of GitHub's generic "404 — File not found" page that has no link to the site.

## Why
The T&B goal (`idetavlor/transformation-beyond/ideas.md` in the vault: a named buyer with a real AI decision says yes to a first paid engagement) depends on a buyer reaching the site and staying on it. The site now has three entry points that get shared as links (`/`, `/sv/`, `/beyond/` with one URL per letter), and nothing catches a mistyped or retired path: the repo has no `404.html`, so GitHub Pages serves its own page. `sitemap.xml` already skips `/404.html`, so the page was expected. No copy decision for Conny: the page makes no claim and uses only existing link texts and styles.

This is also the first story built by `builder: codex-cli` (Astra on the host Mac, agent-team v0.8.9): small, one new file, no design choice left to Codex.

## Signal
- After merge: `https://transformationbeyond.se/finns-inte-023` returns HTTP 404 and its body contains "Page not found" and links to `/`, `/sv/` and `/beyond/` that return 200. Read by the Coordinator's routine (or from the Mac if the cloud session's network blocks the site, papercut 2026-11-14); logged here as seen / not seen.
- The first codex-cli run ends `done` with `Hinder: inga` (or the Hinder list says what the order lacked).

## Acceptance criteria
- [ ] A new `404.html` at the repo root, a static file with no front matter and no Liquid, `lang="en"`, `<meta name="robots" content="noindex">`, no canonical and no Open Graph tags.
- [ ] It uses only `/assets/beyond.css` and its existing classes, the same Google Fonts URL as `_layouts/beyond-base.html` and `/assets/favicon.svg`; no inline `<style>`, no script, no new host.
- [ ] Every `href` and `src` is root-relative (`/…`) or absolute, because GitHub Pages serves this file at any depth (`/a/b/c` too); shown by a screenshot of the page served at a nested path.
- [ ] Copy exactly as in the plan's Copy strings; the Swedish lines carry `lang="sv"`.
- [ ] Header and footer match `_layouts/beyond-base.html` (mark link to `/`, nav link "& Beyond" to `/beyond/`, footer company line, org. no. line, RSS link), except the footer year, which is left out (static file).
- [ ] Price block, booking CTA, Cal.com URL, contact address and founder claims: not on this page and unchanged elsewhere; no other file changes except `.team/**`.
- [ ] Test before commit green; Playwright screenshots at 1440×900 and 390×844 (the file served at `/404.html` and at a nested path) attached to the PR; WCAG AA holds because only existing colour pairs from `beyond.css` are used.

## Out of scope
- A Swedish-first or separate Swedish 404 page; redirects for old paths (`redirect_from` needs a plugin and `_config.yml`, a Human-merge path).
- Any change to `index.html`, `sv/index.html`, `beyond/**`, `_layouts/**`, `_config.yml`, `sitemap.xml`.

## Vad blir publikt?
A page shown only for addresses that do not exist on transformationbeyond.se: the heading "Page not found" with a Swedish line under it and three links back into the site. Not indexed by search engines.

## Log
- 2026-11-18 Coordinator's planner: written as the first `builder: codex-cli` story in tb-site (thread "Planera första Astra-bygget i tb-site"). Parked on 022, which makes Test before commit runnable by the poller and pins v0.8.9; unpark (rename to `023-not-found-page.md`, drop `parked-until`) when 022 is merged.

— Coordinator (Claude) on behalf of Conny
