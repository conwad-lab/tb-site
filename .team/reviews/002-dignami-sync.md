---
id: 002
verdict: approve
---
<!-- verdict: approve | request-changes | escalate — the board reads this line from the PR branch. Keep it current on re-review.
     approve only with no Must fix open. escalate: a Must fix still disputed after the third round (add ## Escalation). -->

# Review 002 — Sync Dignami references and proof claims (C4, C5, C6, C7)

PR: #2 · 2026-10-12

## Must fix
- M1 `index.html:191` — the hero CTA still reads "Read the architecture decisions first →" and now opens https://www.dignami.com/en/proof, which contains no architecture decisions (it shows "What you can check before you buy": built safeguards, reference-run plan, evidence pack). dignami.com/en/evidence lists the ADRs by file path and marks them "Not published", and this PR itself changes the Platform row and the Method row to "available on request" for exactly that reason. The result is one page that promises readable decisions in the hero and says they are available on request two screens down, and the hero promise claims more than dignami.com claims (`AGENTS.md`, Project conventions; hard rail on product-status claims without an openable source). Suggested fix: keep the `href`, change the text to something /en/proof actually delivers, e.g. "See what you can check before you engage →" or "Examine the proof first →" (dignami.com/en/proof: "Examine the work before you commit."). The C5 row in the brief fixes the destination, not the text; if the Coder would rather have the PO choose the wording, say so in the response file and I will keep M1 open until the text is settled.

## Should fix
- none

## Nits
- N1 `index.html:88` — Nit: at 1440 px the status label in the Run card wraps to two lines ("BUILT · IN DEMO · NOT IN / OPERATION") and the `.who` line follows with no gap, so three mono lines read as one block. The plan foresaw this ("give `.who` in that card its own `display:block` if the two labels collide"). Suggested: `.stage .status{margin-bottom:4px}` or `.stage .who{display:block}`; not blocking, the mobile rendering is clean.

## What I checked
- tests run: `python3 -m html.parser index.html` clean; `git diff --check` clean. Playwright 1.58 Chromium at 1440×900 and 390×844, scrolled to the bottom in steps, 1 s wait: 0 unrevealed `.reveal`/`.r-fade`, `compatMode === 'BackCompat'`, `lang === 'en'`. Page heights 6549 px and 7986 px, identical to the Coder's committed PNGs (1440×6549, 390×7986) and +74/+66 px over master as the plan predicted (stage cards and Platform row grew, nothing else moved). Every navigable `href` returned 200 with curl: site root, Google Fonts CSS, dignami.com/en, /en/proof, the R2 sample PDF, mondmodel.com, the Cal.com URL in the script; `assets/favicon.svg` exists; all five `#` anchors have a matching `id`. Preconnect bare hosts excluded as before.
- grep assertions from the plan: "cross-examination", "runs on Dignami AOS", "Dignami · managed", "SHA-256", "21 architecture" → 0; bare `href="https://www.dignami.com"` → 0; `dignami.com/en` → 4 (3 × `/en`, 1 × `/en/proof`); "Built · In demo · Not in operation" → 2. "audit-proof" and "sovereign" survive only in step 02 (line 287), which the story puts out of scope.
- Dignami wording vs source, fetched 2026-10-12: slogan "Your AI got faster. Your decisions didn't." is the `<title>` and H1 of dignami.com/en. "compliance platform for regulated advice, [with] financial advisers first" and "WORM archive, hash chain, policy gate" are on /en and /en/products/aos; all three capabilities are "Built, in demo" there, and the page says "Production infrastructure is not in operation" and "No capability is in operation with client records", so the label `Built · In demo · Not in operation` follows Dignami's published status today. "Operation needs a separate decision." is verbatim on /en/how-it-works. Dropped terms "SHA-256", "sovereign EU runtime", "audit-proof", "EU-only" appear on none of /en, /en/proof, /en/about, /en/products/aos, /en/how-it-works, /en/evidence. /en/about says "Dignami … operates it as a managed service", so the old "Dignami · managed" was not wrong, but the new "later stage" claims less and the story ordered it. Status label renders as the `.who` style (JetBrains Mono 10.5 px, uppercase, `--muted`) at both widths.
- Mondmodel: mondmodel.com 200; its sitemap has nine destination sections (barcelona, basque-country, copenhagen, costa-brava, costa-del-sol, costa-dorada, ibiza, mallorca, menorca) and hreflang de/en/es/sv, so "9 destinations · 4 languages" is sourced. "autonomous operations" and "in daily operation" are not verifiable on mondmodel.com; pre-existing, Operatör line for C6 is open. The source link renders muted, 400 weight, no underline, 1 px `--hair` border, 11.5 px mono — a source line, not a CTA; it does not pick up the `.arc-note a` ink/600 style.
- PR description: every claim checked against the diff and my own runs; all hold. "Plan differences: None" is true — the diff matches plan items 1–11 line for line, including the `.proof .metric a` scoping from the Risks section.
- rulebook: diff touches only `index.html` and two PNGs under `docs/screenshots/002-dignami-sync/`; `_config.yml` excludes `docs/`. No `AGENTS.md`, `.team/team.md`, `REVIEW.md`, `.team/roles/` change.
- scope vs story: no price block, booking CTA, `CNAME`, host or font change; footer and hero base change `href` only. CSS additions limited to `.status` and `.proof .metric a` as the plan allows. `.status` is used only at lines 288 and 339.
- tried to break: `display:block` span inside the inline `.proof .d` span follows the existing `.metric` pattern and renders correctly; no other `.status` class on the page; `<title>`, meta description, OG tags and the JSON-LD block carry none of the removed claims; external hero link has `target="_blank" rel="noopener"` like the others.
- `gh pr checks 2`: no checks configured (Pages build only), nothing pending.
- Second reviewer: not run — Team settings list no Second-reviewer paths.

## For PO
- Step 02 · Build still says "audit-proof system" and "sovereign runtime", neither on dignami.com. Out of scope here (ORDER row 3 rewrites the chain) but it is the last Dignami claim on the page without a source.
- "Build-in-public" as the Method row name next to "available on request" — already flagged by Architect and Coder.

## Round 2 — 2026-10-12

Re-review of 73b5606 (code) and 38d5d13 (response). Diff since round 1: one `<a>` text, one CSS rule, two PNGs, the response file. Nothing else moved.

### Round-1 answers
- M1 — fixed in 73b5606, accepted. Hero link now reads "Examine the proof first →" and keeps `href="https://www.dignami.com/en/proof"` with `target="_blank" rel="noopener"`. dignami.com/en/proof opens on "Examine the work before you commit." today, so the text now promises what the destination delivers and no more. "Read the architecture decisions" appears nowhere on the page.
- N1 — fixed in 73b5606, accepted. `.stage .status{margin-bottom:4px}`; measured gap between the Run status label and `.who` is 5 px at both widths, and the two labels read as separate lines in the 1440 px render.

### Must fix
- none open.

### Should fix
- none.

### What I checked (round 2)
- tests run: `python3 -m html.parser index.html` clean; `git diff --check` clean. Playwright 1.58 Chromium at 1440×900 and 390×844, scrolled to the bottom in steps, 1 s wait: 0 unrevealed `.reveal`/`.r-fade`, `compatMode === 'BackCompat'`, `lang === 'en'`. Page heights 6553 px and 7990 px — exactly the PR description's figures and the committed PNGs (1440×6553, 390×7990), +4 px over round 1 from the new margin, as expected.
- links: every navigable `href` 200 with curl (site root, Google Fonts CSS, dignami.com/en, /en/proof, R2 sample PDF, mondmodel.com, the Cal.com URL in the script); `assets/favicon.svg` present; all five `#` anchors resolve. Both raw.githubusercontent.com screenshot URLs in the PR body return 200 and point at 73b5606, the final code commit. Preconnect bare hosts excluded as before.
- grep assertions from the plan unchanged: "cross-examination", "runs on Dignami AOS", "Dignami · managed", "SHA-256", "21 architecture", "Read the architecture decisions" → 0; bare `href="https://www.dignami.com"` → 0; `dignami.com/en` → 4; "Built · In demo · Not in operation" → 2. "audit-proof"/"sovereign" survive only in step 02 (line 288), out of scope per story.
- Dignami status re-fetched 2026-10-12 (round 2): /en still titles "Your AI got faster. Your decisions didn't." and says "some built, in demo, others not in operation; none operates with client records"; /en/products/aos still "Production infrastructure is not in operation", WORM archive / hash chain / policy gate "Built, in demo"; /en/proof "Current product status — no client data"; /en/how-it-works "Operation needs a separate decision." verbatim. Label follows Dignami's published status today. "SHA-256", "sovereign", "audit-proof", "EU-only" absent from /en, /en/proof, /en/about, /en/products/aos, /en/how-it-works (the string "SHA-256" on /en/evidence refers to private-source hashes, not a ledger). No public ADR URL: /en/evidence lists ADRs by file path marked "Not published".
- PR description: every claim re-checked against the diff and my runs (heights, tests, link check, pages compared, screenshot links, plan differences, For PO) — all hold.
- rulebook: no `AGENTS.md`, `.team/team.md`, `REVIEW.md` or `.team/roles/` change in the PR.
- scope vs story: price block, booking CTA, `CNAME`, hosts and fonts untouched; footer and hero base change `href` only; CSS additions limited to `.status`, `.stage .status`, `.proof .metric a`.
- `gh pr checks 2`: no checks configured (Pages build only), nothing pending or failing.
- Second reviewer: not run — Team settings list no Second-reviewer paths.

Verdict: approve. Merging per `merge: auto` in `.team/team.md`.

— Reviewer (Fable 5.1) on behalf of Conny Wadbro
