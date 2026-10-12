---
id: 002
verdict: plan
---

# Plan 002 — Sync Dignami references and proof claims (C4, C5, C6, C7)

Story: `.team/backlog/002-dignami-sync.md`

## Approach
Copy and `href` edits in `index.html` plus one new CSS rule for a status label. Sources checked 2026-10-12: dignami.com/en (slogan), /en/products/aos (AOS capability table: WORM archive, hash chain, retention sweep, policy gate = "Built, in demo"; erasure, transcription = "Not in operation"; "Production infrastructure is not in operation"), /en/proof, /en/evidence, /en/assurance/evidence. **No public URL to the architecture decisions exists** — ADRs appear on /en/evidence only as repo file paths, and the repos are private (404 unauthenticated). C5 therefore becomes "available on request". mondmodel.com sitemap confirms the figures: 9 destination sections, hreflang de/en/es/sv = 4 languages. Operatör lines for C5/C6 were unanswered at planning time.

Touches price block: no. Booking CTA: no. Footer: `href` only (line 375). `CNAME`, hosts, fonts: unchanged.

## Files
- `index.html` — lines 188, 190, 285, 286, 288, 335–336, 341, 345, 375; one CSS rule near line 87.

## Copy changes (old → new)
1. **C4, line 190 (hero base)** `href="https://www.dignami.com"` → `https://www.dignami.com/en`. Text unchanged.
2. **C4, line 288 (arc-note)** `href` → `https://www.dignami.com/en`; link text "Dignami — AI that survives cross-examination ↗" → "Dignami — Your AI got faster. Your decisions didn't. ↗".
3. **C4, line 375 (footer)** `href` → `https://www.dignami.com/en`. Text "Build &amp; Run → Dignami ↗" unchanged.
4. **C5, line 188** `href="#grundaren"` → `https://www.dignami.com/en/proof`, add `target="_blank" rel="noopener"` like the other external links. Text unchanged.
5. **C5, line 336** metric "21 architecture decisions — open for review before you engage" → removed; see 8.
6. **C5, line 345 (Method)** "architecture decisions recorded as we build. Review them before you engage us." → "architecture decisions recorded as we build. Available on request before you engage us."
7. **C6, line 341** keep "9 destinations · 4 languages · autonomous operations"; append inside the same `.metric` span: ` · <a href="https://mondmodel.com" target="_blank" rel="noopener">source: mondmodel.com ↗</a>`. Style like `.hero-base a` (muted, no underline, 1px `--hair` bottom border, ink on hover) so it reads as a source line, not a CTA.
8. **C7, line 335 (Platform row)** "Dignami AOS — audit-proof AI platform: SHA-256 ledger, WORM retention, sovereign EU runtime." → "Dignami AOS — compliance platform for regulated advice: WORM archive, hash chain, policy gate. Architecture decisions available on request." Dropped because absent from /en/products/aos and /en/proof: "audit-proof", "SHA-256", "sovereign EU runtime". Replace the line-336 metric with `<span class="status">Built · In demo · Not in operation</span>`.
9. **C7, line 285 (03 · Run)** "The system runs on Dignami AOS — EU-only, immutable ledger, WORM retention." → "Dignami AOS — compliance platform for regulated advice, financial advisers first." Add `<span class="status">Built · In demo · Not in operation</span>` between the `<p>` and `.who`. `.who` stays "Dignami · platform".
10. **C7, line 286 (04 · Operate)** "Ongoing operations, monitoring and incident handling." → "Ongoing operations, monitoring and incident handling once a system goes live. Operation needs a separate decision." (last sentence is Dignami's own, /en/how-it-works). `.who` "Dignami · managed" → "Dignami · later stage".
11. **CSS** one rule `.status{…}` = same as `.stage .who` (mono, 10.5px, letter-spacing .12em, uppercase, `--muted`), `display:block`, `margin-top:10px`. In `.stage` it sits above `.who`; give `.who` in that card its own `display:block` if the two labels collide.

## Tests
- `python3 -m html.parser index.html` exits 0.
- `grep -c -i "cross-examination\|runs on Dignami AOS\|Dignami · managed\|SHA-256\|sovereign\|audit-proof AI\|21 architecture" index.html` → 0. `grep -c 'href="https://www.dignami.com"' index.html` → 0. `grep -c 'dignami.com/en' index.html` → 4 (3 × `/en`, 1 × `/en/proof`). `grep -c "Built · In demo · Not in operation" index.html` → 2.
- Playwright (`/Users/connywadbro/.nvm/versions/node/v22.21.1/lib/node_modules/playwright`, Chromium installed): 1440×900 and 390×844, scroll to bottom in steps, wait 1 s, full-page screenshots, attach to PR. Assert `document.compatMode === 'BackCompat'` (no doctype added). Baseline on master today: 6475 px at 1440, 7920 px at 390; expect the arc stage cards and the Platform row to grow by one or two lines, nothing else to move.
- Link check: every navigable `href` (`http(s)` + `assets/favicon.svg`) returns 200, including the three new targets (`dignami.com/en`, `/en/proof`, `mondmodel.com` — all 200 today). Exclude `mailto:`, `#` and the two `rel="preconnect"` hosts.

## Risks / watch out for
- Reviewer re-checks dignami.com/en/proof and /en/products/aos on review day; if Dignami's published status changed, the label follows Dignami, not this plan.
- Keep the `.metric` span on the Mondmodel row; only append the link. The Platform row's `.metric` is replaced by `.status`.
- `a{color:inherit}` is global; the new source link must not pick up `.arc-note a` styling (ink, 600 weight). Scope the rule to `.proof .metric a`.
- Line 185 "the architecture is open for review before you engage us" and line 272 "The architectures are open for review." stay: /en/proof ("Examine the work before you commit") backs them.
- Use the page's own characters: "—" U+2014, "·" U+00B7, "↗", ASCII apostrophe.

## Out of scope
- Step 01 and 02 text, eyebrow "four stages, two companies", hero base and footer wording (ORDER row 3 rewrites the chain).
- Any colour, layout or typography change beyond `.status` and the source-link styling.
- Doctype, Swedish copy, dignami.com or mondmodel.com.

## Suggestions for PO
- Step 02 · Build still says "audit-proof system" and "sovereign runtime" (neither on dignami.com). Covered when row 3 rewrites the chain; worth a line in that story.
- "Build-in-public" as the Method row name sits oddly next to "available on request". Rename in row 3 or when Conny supplies a public decisions URL.
- "autonomous operations" on the Mondmodel row is not verifiable on mondmodel.com (destinations and languages are). Kept per story; the open Operatör line for C6 should ask Conny whether to keep that phrase.
- Close the C5 Operatör line: no public URL found by the Architect either; the page now says "available on request".
