---
id: 961
verdict: request-changes
---

# Review 961 — Åtgärda P2-fynden i tillgänglighetsrevisionen

PR: #98 · 2026-11-26 · head reviewed 4cbbd04 (this file is the only later commit)

Order 961 (Astra work order, `Plan: .team/ORDER.md`; no ORDER row). Not a Human-merge path (`assets/site.css`, `sv/index.html` language spans, `docs/` templates; no price, URL, address or founder claim). The fixes themselves hold; two things block the merge.

## Must fix
- **M1** `assets/site.css:26` (`@media(max-width:860px){.top{position:relative;…}}`) and `:57` (`.hero{padding-top:72px}`) — the mobile header now sits in the normal flow above the hero (125 px tall at 390 px, was 86 px overlaid), so everything below moves down. #90 (order 035, being merged now) lowers the hero to `86svh` so that the red booking band shows on the first screen at 390×844. I built master + #90 + #98 together and measured at 390×844: band top **851 px** (viewport 844) on both pages, i.e. below the fold again (with #90 alone: 726 px; with #98 alone: 969 px; master: 844 px). The same story's criterion would silently fail the day this merges. Fix: keep the header over the hero (leave `.top` absolute) and give the hero the extra top padding for a two-row nav instead, or otherwise keep hero + header within the first screen; then re-measure with main merged in: `a.band` top < 844 at 390×844 on `/` and `/sv/`, and attach the numbers.
- **M2** Base branch. #98 is stacked on `feat/956-a11y-testtackning`, which is gone since #97 merged (the PR still lists it as base and reports `dirty`), so `pr-check` never ran on this head (it only runs for PRs to `master`). Retarget to `master` (done by the Judge, see the PR) and merge main: `docs/revision-a11y-test-2026-11-25.md` conflicts add/add (master has the #97 version, this branch has it plus the 12-line follow-up). Take this branch's file. A green `pr-check` on the new head is required before a Judge request.

## Should fix
- **S1** `docs/offert-ordforandens-fraga/README.md:2` still says "ersätt ☐ med ☑ för exakt ett valt svar", which the PR makes false (the choices are now radio buttons). One-line fix in the same PR (the Builder noted it under "För PO"; leaving a false instruction in the template's own manual is worse than touching the README).

## Nits
- N1 Mobile header: all five links now show and wrap to two rows; story 008's D7 had kept only the brand and the booking link in the mobile menu on purpose. The fix is what finding P2·1.4.10 asked for ("låt länkarna radbrytas"), so I accept it; Conny should look at the mobile header once live.
- N2 `.film` opacity .5 → .35 and `.hero-foot .sis` opacity removed are visual changes. They are the cheapest way to reach the contrast and I accept them under "inga designval" because the order's own measure demands it; the film is now somewhat dimmer.
- N3 The Builder's screenshots are "i byggets lokala bilaga" and not attached to the PR; the checks below are mine.

## Evidence
| Acceptance criterion (order 961) | Shown by | Result |
|---|---|---|
| P2 contrast over film/poster fixed | My Jekyll build + Playwright, hero-foot text hidden, sampled every 4 px over the paragraphs at 1440×900 against `#F8F6F1`: master worst **3.02:1** (both pages), this head worst **4.80:1** (both pages) | pass |
| P2 menu reflow at 320 px | At 320×568 and 390×844 all five nav links are displayed on both pages (master: 3); no horizontal scroll | pass |
| P2 `lang="en"` on the two English quotes | Diff: `sv/index.html:82` and `:152` wrap only the quote in `<span lang="en">`; link text outside | pass |
| P2 offer-field labels and the choice group | Playwright on `mall-sv`, `mall-en`, `exempel-sv`: three radios in a `radiogroup`, every `aria-labelledby` target exists, ArrowDown moves the selection, `exempel-sv` opens with the first selected, the templates with none | pass |
| P2 offer templates reflow at 320 px, print on one A4 page | 320 px: no horizontal scroll on all three; `page.pdf` (A4) → 1 page each | pass |
| Only P1/P2, no design choices, no text | Diff read: CSS, language spans, ARIA/radio markup, the report tick-offs; no copy, price or link changed (but see N1, N2, S1) | pass |
| Does not break the other open story (#90, first screen) | Combined build measured | **fail (M1)** |
| Test before commit | HTML check, `pr-check` | `pr-check` did not run (M2) |

## Codex findings
- Codex code review on 4cbbd04 completed with no findings (receipt 2026-11-25T20:24Z). Nothing to rule on. The M1 collision is between two PRs and could not show up in a one-PR review.

## What I checked
- tests run: Jekyll build of master, #90, #98 and #90+#98; Playwright at 1440×900, 390×844, 320×568; contrast sampling; template checks and A4 print.
- tried to break: the neighbouring open story's criterion (found M1); the stale base (found M2).
- scope vs story: within the order except S1.
- sync gate: not met: main is not in the branch (M2).

## Papercuts
2026-11-26 | reviewer | the stacked PR's base branch vanished when #97 merged and the PR stayed on the dead base | retargeted to master | open
