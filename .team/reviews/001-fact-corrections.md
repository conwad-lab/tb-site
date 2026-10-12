---
id: 001
verdict: approve
---

# Review 001 — Correct factual claims on the page (C1, C2, C3, C8, C9)

PR: #1 · 2026-10-12

## Must fix
- none

## Should fix
- none

## Nits
- N1 `index.html:271` — C3 now reads "Two decades in IT, consulting and sales leadership — sales leadership, pricing, go-to-market." The repeated "sales leadership" is what the story specifies verbatim, so this is not on the Coder. For the PO: fold into the next copy story, e.g. end the sentence "— pricing, go-to-market." No factual issue.

## What I checked
- tests run: `python3 -m html.parser index.html` exit 0. `grep -i master` → only line 272 ("Master's-level studies"); no "master's degree", no "Master's in"; `lang="en"` count 1. `git diff --check` clean. Playwright 1.58.2 Chromium at 1440×900 and 390×844, scrolled to bottom in steps, 0 unrevealed `.reveal`/`.r-fade` elements at either width. `document.documentElement.lang === 'en'`, `compatMode === 'BackCompat'` on both (no render-mode change). Page height 6432→6475 at 1440 and 7851→7920 at 390 versus master, i.e. the Law card grew by one line and nothing else moved. My screenshots match the two the Coder committed under `docs/screenshots/001-fact-corrections/`.
- links: every navigable `href` 200 (site root, Google Fonts CSS, dignami.com, R2 sample PDF, Cal.com booking URL in the script, local `assets/favicon.svg` exists). The two `rel="preconnect"` bare hosts 404 as on master; they are not links. Team settings should say "navigable `href`" — Architect has already suggested this to the PO.
- facts vs source: C1, C2, C3, C8, C9 each traced to `.team/briefs/2026-10-site-refresh.md` table "Innehållsändringar", word for word. "Master's-level studies … Lund" matches the `AGENTS.md` hard rail (bachelor's held; Lund commercial-law studies are master's-level courses). C8 mirrors dignami.com/en ("shaping the design, not replacing your counsel") and /en/about ("your counsel gives legal advice"). dignami.com/en/about publishes no credentials ("Work roles, not biographies or certifications"), so nothing on this page now claims more than the sister site. No credential claim in `<title>`, meta description, OG tags or JSON-LD (grepped for degree/certif/LL.M/jur).
- PR description: every claim checked against the diff and my own runs; all hold.
- rulebook: the PR diff does not touch `AGENTS.md`, `.team/team.md`, `REVIEW.md` or `.team/roles/`.
- scope vs story: only `index.html` lines 1, 271, 272, 349, last line, plus the two PNGs. No CSS, script, price block, booking CTA, footer or `CNAME` change. No doctype added (plan's reason verified: would change layout). `_config.yml` excludes `docs/`, so the screenshots do not publish.
- tried to break: `<html lang>` start tag before `<meta charset>` with no doctype parses to the same tree in Chromium (charset still within first 1024 bytes); `</html>` sits after the last `<script>`. Mobile wrapping of the longer Law card is clean at 390.
- `gh pr checks 1`: no checks configured (Pages build only), nothing pending.
- Second reviewer: not run — Team settings list no Second-reviewer paths.

## Merge
Not merged by me. `.team/team.md` says `merge: auto`, but that line was changed from `merge: human` in commit 769b7e3 by the Product Owner, with no row in `.team/ORDER.md` ordering it. The rulebook changes only on the human's order, and a merge here is a production deploy, so I am leaving the merge to Conny. If `merge: auto` was intended, say so in ORDER.md (or confirm to the PO) and I will merge on the next pass, or merge it yourself: `gh pr merge 1 --squash --delete-branch`.

— Reviewer (Fable 5.1) on behalf of Conny Wadbro
