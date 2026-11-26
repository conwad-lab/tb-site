---
id: 036
verdict: approve
---

# Review 036 — Geografi på den engelska sidan

PR: #95 · 2026-11-26 · code head 8974e95; main merged in twice (#97 and #99 had merged), the review file is the only other change

Story: ORDER row 036 (no story file; the row and the Astra work order on #94 are the spec). Merge route: `merge: auto`. The diff changes copy but touches no Human-merge path: no price, Cal.com URL, contact address, founder claim, `CNAME`, `_config.yml` or workflow. The Judge merges on its word (CLOUD.md § Judge 5, J9).

## Must fix
- none

## Should fix
- none

## Nits
- N1 "from a base in Greater Copenhagen" is Conny's wording from the row (decision 2026-11-23 "Dela efter språk"); the footer still says "Lomma, Sweden" and `addressLocality` is `Lomma`, as the row requires. Lomma lies in the Öresund region, so the two do not contradict, but Conny may want to reread the sentence live.

## Evidence
| Acceptance criterion (ORDER row 036) | Shown by | Result |
|---|---|---|
| `<title>` = "AI advisory for Nordic leadership teams — Transformation & Beyond, Greater Copenhagen" | Exact-string check of the row's text against `index.html` → present | pass |
| Meta description = the row's sentence | Exact-string check → present | pass |
| JSON-LD `areaServed` = `["Greater Copenhagen", "Nordics"]`, `addressLocality` "Lomma" | JSON parsed with `json.loads`: `areaServed` as required, `addressLocality` Lomma, price 75000 | pass |
| Ingress sentence changed to the row's text | Exact-string check of `Transformation &amp; Beyond advises Nordic companies, from a base in Greater Copenhagen, taking AI from pilot to auditable operations.` → present | pass |
| Nothing else changes: footer, price, Cal.com URL, contact address, `sv/index.html` | `git diff origin/master...HEAD --stat` → `index.html` only, 4 insertions, 4 deletions; "Lomma, Sweden" ×1, one cal.com URL, mailto address unchanged | pass |
| Test before commit | `check_html.py index.html` ok; `pr-check` on the head (see checks) | pass |
| Screenshots 1440×900 and 390×844, links | My Jekyll build + Playwright, full page after scrolling at both widths: title and ingress render, no horizontal scroll, ingress inside the viewport; the 14 distinct hrefs were collected, the local ones answer 200. External hosts (dignami.com, cal.com, R2, Google Fonts) are **not checked** (the cloud network blocks them) | pass (external links not checked) |

## Codex findings
- Codex code review on 8974e95 completed with no findings (receipt 2026-11-25T08:36Z). Nothing to rule on.

## What I checked
- tests run: exact-string comparison against the ORDER row, JSON-LD parse, check_html.py, Playwright at both widths.
- tried to break: looked for a second `areaServed`, a changed `addressLocality`, a touched Swedish page: none.
- scope vs story: the four strings in the row and nothing else.
- sync gate: `git merge-base --is-ancestor origin/master HEAD` → yes right before posting.

## Papercuts
2026-11-26 | reviewer | the PR needed main merged twice because other PRs merged while I worked | merged main again before posting | open
