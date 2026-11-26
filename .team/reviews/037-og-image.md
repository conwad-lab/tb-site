---
id: 037
verdict: approve
---

# Review 037 — Ny delningsbild (OG)

PR: #93 · 2026-11-26 · code head 99b1291; main merged in (it was one commit behind, then #95, #97 and #99 merged), the review file is the only other change

Story: ORDER row 037 (no story file; the row is the spec), "efter 036": #95 (036) is merged. Merge route: `merge: auto`, no Human-merge path touched (no price, Cal.com URL, contact address, founder claim, `CNAME`, `_config.yml` or workflow). The Judge merges on its word (CLOUD.md § Judge 5, J9).

## Must fix
- none

## Should fix
- none

## Nits
- N1 The sample-report PDF and the Cal.com link stay on `r2.dev` as the row requires; only `og:image` moves. Link previews cache images, so LinkedIn may show the old image until its cache is refreshed (Post Inspector). That is an Operatör step for Conny, not a defect of the PR.
- N2 No `og:image:width`/`height`/`alt` tags and no `twitter:image` line exist on either page before or after; not in the row, so out of scope.

## Evidence
| Acceptance criterion (ORDER row 037) | Shown by | Result |
|---|---|---|
| `assets/og-1200x630.png`, 1200×630 | PIL: size (1200, 630), RGB, 33 242 bytes | pass |
| Marint `#0C2233`, rött `#CF2318`, papper `#F8F6F1` | Pixel histogram: `#0C2233` 721 041 px, `#F8F6F1` 25 355 px, `#CF2318` 1 715 px (and no other brand colour) | pass |
| Ordmärket "Transformation & Beyond" with a red `&` and the line "The AI Value Review", Newsreader + Familjen Grotesk | I opened the PNG: serif wordmark in paper on navy with the `&` in red, the line "The AI Value Review" in a grotesk below, nothing else on the image | pass |
| `og:image` on `index.html` and `sv/index.html` = `https://transformationbeyond.se/assets/og-1200x630.png` | `grep`: `index.html:17`, `sv/index.html:19`; no other `og:image`; diff is exactly one line per page | pass |
| The file is published | My Jekyll build puts `assets/og-1200x630.png` in the output, byte-identical to the committed file (`cmp`) | pass |
| Sample-report PDF on r2.dev untouched; no other text | The `architecture-review-sample.pdf` links on both pages unchanged; diff stat: 3 files, 2 insertions, 2 deletions plus the PNG | pass |
| Test before commit | `check_html.py` ok on both pages; `pr-check` on the head | pass |
| Screenshots of the changed pages | Only `<head>` changes; the visible page is untouched, so I took none. The PR body embeds the image. | n/a |

## Codex findings
- Codex code review on 99b1291 completed with no findings (receipt 2026-11-25T20:24Z). Nothing to rule on.

## What I checked
- tests run: PNG size and colours, Jekyll build output identity, check_html.py.
- tried to break: looked for a third page or a layout that sets another `og:image` (`404.html`, `_layouts/beyond-base.html`): not touched by the row and not touched here.
- scope vs story: the image plus the two lines, nothing else.
- sync gate: `git merge-base --is-ancestor origin/master HEAD` → yes right before posting.

## Papercuts
2026-11-26 | reviewer | main moved four times during the session, so each PR needed a fresh merge of main before its merge line | merged main per PR just before posting | open
