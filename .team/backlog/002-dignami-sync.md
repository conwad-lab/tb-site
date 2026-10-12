---
id: 002
title: Sync Dignami references and proof claims (C4, C5, C6, C7)
---

## Outcome
Every Dignami reference on the page carries Dignami's current message and links to https://www.dignami.com/en, every figure in "Who you get" has an openable source, and the page says nothing about Dignami AOS being in operation that dignami.com does not say itself.

## Why
dignami.com was redone: Dignami Assurance is the flagship, every claim carries a status, and the site states "Current product status — no client data". transformationbeyond.se still quotes the old slogan ("AI that survives cross-examination"), says the system "runs on Dignami AOS" with "Dignami · managed" operations, and lists "21 architecture decisions — open for review" and Mondmodel figures with no link a reviewer can open. Two sites selling to the same board must not contradict each other, and this one must never claim more about Dignami than dignami.com does (`AGENTS.md`, Project conventions and hard rails). Source for every change: `.team/briefs/2026-10-site-refresh.md`, table "Innehållsändringar", rows C4–C7.

## Acceptance criteria
- [ ] C4 — every `href` to dignami.com on the page (hero base line ~190, arc-note ~288, footer ~375) points to `https://www.dignami.com/en`. The arc-note link text "Dignami — AI that survives cross-examination ↗" becomes "Dignami — Your AI got faster. Your decisions didn't. ↗" (verified live on dignami.com/en 2026-10-12). The old slogan appears nowhere on the page.
- [ ] C5 — "Read the architecture decisions first →" (~line 188) links to `https://www.dignami.com/en/proof` instead of `#grundaren`.
- [ ] C5 — the metric "21 architecture decisions — open for review before you engage" (~line 336) and the Method row "Review them before you engage us." (~line 345) keep the figure only if the Architect finds a public URL to the decisions and links it. No URL found: both become "available on request" wording and the Architect's plan says so. PO found none on dignami.com/en/proof on 2026-10-12 and has asked Conny under Operatör; assume "available on request" unless Conny answers before the plan.
- [ ] C6 — the Mondmodel metric "9 destinations · 4 languages · autonomous operations" (~line 341) keeps its figures and gains a link to `https://mondmodel.com` as source (the only Mondmodel URL in the repo, `README.md`). The link opens (200) and is visually a source line, not a CTA.
- [ ] C7 — step `03 · Run` (~line 285): no present-tense claim that anything runs on AOS. Text describes AOS as Dignami's compliance platform for regulated advice and carries the status label `Built · In demo · Not in operation` in T&B style (mono, small caps, like `.k`/`.who`). Suggested: "Dignami AOS — compliance platform for regulated advice. Built · In demo · Not in operation."
- [ ] C7 — step `04 · Operate` (~line 286): "Ongoing operations, monitoring and incident handling." and "Dignami · managed" must not read as a service in operation today. Future or conditional phrasing, `who` label without "managed".
- [ ] C7 — "Platform" row in Who you get (~line 335): every technical attribute kept ("SHA-256 ledger", "WORM retention", "sovereign EU runtime", "audit-proof") must appear on dignami.com/en/products/aos or /en/proof; drop any that do not. Row gets the same status label `Built · In demo · Not in operation`.
- [ ] Reviewer compares all Dignami wording against https://www.dignami.com/en/proof and /en/about on review day; if Dignami's published status has changed, the label follows Dignami, not the brief.
- [ ] A full-text search of `index.html` for "cross-examination", "runs on Dignami AOS", "Dignami · managed" and `href="https://www.dignami.com"` (without `/en`) returns nothing.
- [ ] Price block and booking CTA untouched. Footer changes only in the Dignami `href`. `CNAME` untouched. No new hosts.
- [ ] Team settings test passes: `python3 -m html.parser index.html` clean, Playwright screenshots at 1440×900 and 390×844 after scrolling to bottom, all `href`s return 200. Screenshots attached to the PR.

## Out of scope
- Replacing the four-stage Advise/Build/Run/Operate chain with Advise → Assurance → Platform, and the Dignami hand-off block (ORDER row 3, after this story). Step 01, step 02 text, the hero base line and the footer wording stay as they are apart from `href`s.
- Any colour, layout or typography change beyond the status label.
- Changes on dignami.com or mondmodel.com.
- Swedish version.

## Log
- 2026-10-12 PO: created from ORDER row 2. C7 is done as minimal claim fixes in steps 03–04 and the Platform row, because row 3 rewrites the chain wholesale. Dignami slogan verified live; dignami.com/en/proof shows "Built and tested" and "no client data" but no public decisions URL — Operatör line added. Mondmodel source taken from `README.md` (mondmodel.com); Operatör line asks Conny to confirm.
