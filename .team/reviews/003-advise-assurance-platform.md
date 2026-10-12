---
id: 003
verdict: approve
---
<!-- verdict: approve | request-changes | escalate — the board reads this line from the PR branch. Keep it current on re-review.
     approve only with no Must fix open. escalate: a Must fix still disputed after the third round (add ## Escalation). -->

# Review 003 — Replace "How we work" with Advise → Assurance → Platform and add a Dignami hand-off block

PR: #3 · 2026-10-12

## Must fix
- none

## Should fix
- none

## Nits
- N1 `index.html:292` — Nit: the source line links `https://www.dignami.com/en/proof`, whose status table sits below the fold under the id `status-table`. dignami.com/en itself links "See product status and its source →" to `/en/proof#status-table`. Appending that anchor would land the reader on the table instead of the page top. Story 003 fixed the URL as `/en/proof`, so this is optional and not a correctness point; if taken, same `href` host, nothing else changes.

## What I checked
- tests run: `python3 -m html.parser index.html` clean; `git diff --check` clean. Playwright 1.58 Chromium at 1440×900 and 390×844 (plus 900 and 700 px for the plan's squeeze risk), scrolled to the bottom in 400 px steps, 1 s wait: 0 unrevealed `.reveal`/`.r-fade`, `compatMode === 'BackCompat'`, `lang === 'en'`, `scrollWidth === innerWidth` at every width. `.arc` computed `gridTemplateColumns` has three values at 1440 (342 px each) and 900, one value at 700 and 390; the three cards share one top edge at 1440 and stack with a `border-top` at 390. Page heights 6694 px (1440) and 8077 px (390), identical to the committed PNGs (1440×6694, 390×8077), which the PR body links and raw.githubusercontent.com serves with 200. Versus master (6553 / 7990) that is +141 / +87 px: the plan expected 390 to shrink, but the longer Advise paragraph and the hand-off block outweigh the removed card. Nothing above the section moved. Not a defect; noted so the numbers are explained.
- links: every navigable `href` returned 200 with curl: site root, Google Fonts CSS, dignami.com/en, /en/proof, the R2 sample PDF, mondmodel.com, the Cal.com URL in the script; `assets/favicon.svg` exists; all five `#` anchors resolve. The two `rel="preconnect"` bare hosts return 404 as before and are excluded per the earlier reviews. No new host: the host list is unchanged from master.
- plan greps: "four stages", `>Build<`, `>Run<`, `>Operate<`, "audit-proof", "sovereign", "verification gate", "later stage", "separate decision", "Stage 1 lives", "Build &amp; Run", "arc-note" → 0. `class="stage` → 3; "Your AI got faster" → 1; "Built · In demo · Not in operation" → 2; `dignami.com/en"` → 3. `dignami.com/en/proof` → 3, not the plan's 2: the visible link text "Status as published on dignami.com/en/proof" contains the string, so the count is right and the plan's estimate was off by the text node. The `.qs` block is byte-identical to master.
- copy vs plan: all eight copy changes match the plan's old → new strings exactly, including the hero base line (194) and the footer link text (381), both on their unchanged `href`. The Assurance card's `.who` reads "Dignami · engagement" as the plan says; the story only asked for Dignami. Cards 2 and 3 carry no "In operation" claim.
- Dignami wording vs source, fetched 2026-10-12: /en has "Your AI got faster. Your decisions didn't." as title and H1, "Understand. Rethink. Rebuild.", "Every claim has a status.", "The evidence pack travels with every recommendation.", "Dignami AOS is a compliance platform for regulated advice, with financial advisers first", and in the footer "Advise → Transformation & Beyond ↗". /en/about has "Transformation & Beyond advises; Dignami builds and runs; your counsel gives legal advice." verbatim. Status re-checked for the Platform card: /en still says "some built, in demo, others not in operation; none operates with client records"; /en/products/aos still says "Built, in demo" for the capabilities, "Production infrastructure is not in operation" and "No client records in operation"; /en/proof says "Current product status — no client data", "Built and tested", "Synthetic test", "first reference run scheduled". The label `Built · In demo · Not in operation` therefore follows Dignami's published status today. "Understand · Rethink · Rebuild" with middle dots is the story's label form of Dignami's "Understand. Rethink. Rebuild." (plan Risks). "The Review's recommendations are carried forward in Dignami Assurance" is T&B's own sentence, sourced to the brief (Fasta beslut 2: next step after the Review is Dignami Assurance) and consistent with Dignami's "The evidence pack travels with every recommendation".
- contrast: computed the WCAG ratios on the hand-off tint `#FDFCF8` myself: `--body` 10.47:1, `--bronze` 5.18:1, `--muted` 4.99:1, `--ink` 15.99:1. The PR's three figures match. All pairs already exist on the page (`.stage.here` uses the same tint), so no new colour pair. Hand-off paragraphs render in `--body` at 15 px, label in `--bronze` JetBrains Mono, link in `--ink` 600 with a bronze underline; the source line renders muted, 11.5 px mono, `--hair` underline, no uppercase — a source line, not a CTA.
- layout details: Platform card stacks status / source / owner with 4 px and 7 px gaps at both widths, three distinct lines. At 1440 the source line wraps once after "on"; at 900 the status label wraps to two lines; both read cleanly in the renders. Hand-off block sits 24 px under the cards and 40 px above `.qs` at every width, `max-width:46em` holds at 1440 (782 px wide), full width at 390 with no overflow. `a:focus-visible` is a global rule (line 31) and applies to the new links.
- PR description: every claim checked against the diff and my runs (tests, widths, columns, overflow, 900 px, link check, contrast figures, screenshot links, "Plan differences: None") — all hold.
- rulebook: diff touches only `index.html` and two PNGs under `docs/screenshots/003-advise-assurance-platform/`; `_config.yml` excludes `docs/`. No `AGENTS.md`, `.team/team.md`, `REVIEW.md` or `.team/roles/` change.
- scope vs story: all thirteen acceptance criteria met (eyebrow, three cards in order with owners and `here` on card 1, old stage words and phrases gone, hand-off block with label / roles sentence / Assurance sentence / one slogan link with `target="_blank" rel="noopener"`, `.arc-note` removed, slogan once, footer and hero base text on unchanged `href`, no in-operation claim, `.qs` unchanged, three columns at 1440 and one at 390 with no overflow, no new palette or font). Price block (75 000 SEK at lines 5/316/370), booking CTA, Cal.com URL, contact address and `CNAME` untouched. CSS additions limited to `.stage .src`, `.handoff` and the one 860 px media rule the plan names; `.arc-note`, the 520 px rule and the `nth-child(4)` delay are gone with nothing left referencing them.
- tried to break: the removed 520 px rule previously carried the `.stage + .stage` border-top; it now lives in the 860 px rule and the 390 render shows the dividers. `.src` and `.handoff` class names are used nowhere else on the page. Title, meta description, OG tags and JSON-LD carry none of the removed chain words. "build" survives only in T&B-voice copy outside the section (contact `h2`, hero line), as the plan notes.
- `gh pr checks 3`: no checks configured (Pages build only), nothing pending or failing.
- Second reviewer: not run — Team settings list no Second-reviewer paths.

## For PO
- The merge deploys to production: Operatör line for Conny to check the live "How we work" section at both widths.
- /en/proof is the page Dignami itself designates as the status source, but the words "in demo" and "not in operation" are on /en and /en/products/aos, not on /en/proof. If a later story tightens source lines, consider "Status as published by Dignami" or the `#status-table` anchor (N1).

Verdict: approve. Merging per `merge: auto` in `.team/team.md`.

— Reviewer (Fable 5.1) on behalf of Conny Wadbro
