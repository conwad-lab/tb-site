---
id: 003
title: Replace "How we work" with Advise → Assurance → Platform and add a Dignami hand-off block
---

## Outcome
The "How we work" section shows the three-link chain Advise (T&B) → Assurance (Dignami) → Platform (Dignami AOS), mirroring dignami.com, and ends in a clearly marked hand-off block that tells the reader what Dignami takes over and where to go — the mirror image of Dignami's footer line "Advise → Transformation & Beyond ↗".

## Why
The current four-stage chain (Advise / Build / Run / Operate) is T&B's old picture of the work. dignami.com now sells Dignami Assurance (Understand · Rethink · Rebuild, with an evidence pack) as the flagship and Dignami AOS as the platform, and names T&B as the advisor in its footer and on /en/about. Two sites selling to the same board must show the same chain. Story 002 only patched the claims inside the old four cards; this story replaces the structure. Source: `.team/briefs/2026-10-site-refresh.md`, section "Strukturändring: How we work", and "Fasta beslut" 1–2. All Dignami wording below was verified live on dignami.com/en, /en/about and /en/proof on 2026-10-12.

## Acceptance criteria
- [ ] Section `#arbetssatt` (lines ~283–293) shows exactly three stage cards, in this order, with these headings and owners:
  1. **Advise — Transformation & Beyond.** Body: The Architecture Review — a board-standard answer on where your AI operation stands and what to do next. Keep the existing scope words (strategy, AI governance, regulatory gap analysis, project scoping) if they fit in one short paragraph. `who`: T&B. This card keeps the `here` highlight.
  2. **Assurance — Dignami.** Body: Understand · Rethink · Rebuild. Every recommendation travels with an evidence pack; every claim has a status. `who`: Dignami.
  3. **Platform — Dignami AOS.** Body: Compliance platform for regulated advice, financial advisers first. Status label `Built · In demo · Not in operation` (the existing `.status` style), and a visible source line "Status as published on dignami.com/en/proof" linking to `https://www.dignami.com/en/proof`. `who`: Dignami.
- [ ] The eyebrow "How we work — four stages, two companies" is replaced by wording that matches three links and two companies (e.g. "How we work — three links, two companies"). The nav label "How we work" (line ~177) stays.
- [ ] The words "Build", "Run" and "Operate" no longer appear as stage headings. The phrases "audit-proof system", "sovereign runtime", "verification gate", "Dignami · later stage" and "Operation needs a separate decision" are gone from this section (none is on dignami.com; they belonged to the old cards).
- [ ] A **hand-off block** follows the three cards, visually distinct from the `.arc-note` paragraph (a bordered or tinted block in the page's paper/bronze style, not a new colour or font). It contains, in this order: a mono label in the style of `.eyebrow`/`.k` reading "Hand-off → Dignami"; one sentence stating the division of roles in Dignami's own words — "Transformation & Beyond advises; Dignami builds and runs; your counsel gives legal advice." (dignami.com/en/about); one sentence saying the Review's recommendations are carried forward in Dignami Assurance; and one link to `https://www.dignami.com/en` with the text "Dignami — Your AI got faster. Your decisions didn't. ↗" (`target="_blank" rel="noopener"`, like the other external links).
- [ ] The old `.arc-note` paragraph ("Stage 1 lives here. Stages 2–4 are delivered by …") is removed or folded into the hand-off block; the Dignami slogan appears once in this section, not twice.
- [ ] Footer link text "Build & Run → Dignami ↗" (line ~379) becomes "Assurance & Platform → Dignami ↗"; its `href` stays `https://www.dignami.com/en`. Hero base line (line ~194) "Build & Run are delivered by our sister company Dignami ↗" becomes "Assurance and the platform are delivered by our sister company Dignami ↗"; `href` unchanged.
- [ ] Nothing in the section claims that Assurance or AOS is in operation with client records. The Reviewer re-checks dignami.com/en/proof and /en/products/aos on review day; if Dignami's published status changed, the label follows Dignami, not this story.
- [ ] "The questions we answer" block (`.qs`, after the cards) stays unchanged in content and position.
- [ ] Layout: three cards side by side at 1440 px, stacked at 390 px, no horizontal scroll at either width. The existing `.arc` grid and breakpoints are adjusted from four columns to three; no new palette colours or fonts; WCAG AA contrast for any colour that changes.
- [ ] Price block, booking CTA, Cal.com URL, contact address and `CNAME` untouched. No new hosts.
- [ ] Team settings test passes: `python3 -m html.parser index.html` clean, Playwright screenshots at 1440×900 and 390×844 after scrolling to bottom, all `href`s return 200. Screenshots attached to the PR.
- [ ] The plan names every visible copy string that changes (old → new) and states that the footer changes (link text only) and that the price block and booking CTA do not.

## Out of scope
- Design review (ORDER row 4) — this story does not fix contrast, focus or reveal findings beyond what the new block itself needs.
- Any change to the "Who you get" section, the Platform/Mondmodel/Method rows, or the hero `lede` lines (done in 001/002).
- New palette, fonts or logo; Swedish version; dignami.com.
- Renaming the "Build-in-public" Method row (Architect's suggestion from plan 002) — separate ORDER row if Conny wants it.

## Log
- 2026-10-12 PO: created from ORDER row 3, after story 002 merged (PR #2). Brief's chain wording checked live on dignami.com/en (Understand. Rethink. Rebuild.; evidence pack; AOS "compliance platform for regulated advice, with financial advisers first"), /en/about (roles sentence) and footer ("Advise → Transformation & Beyond ↗"). Hero base line and footer link text included because they name the old "Build & Run" chain; both stay on the same `href`. Hand-off block: one block, three sentences and one link, kept small so it fits one PR with the card rewrite.
