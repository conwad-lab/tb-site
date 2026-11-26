---
id: 967
verdict: approve
---

# Review 967 — Granska SEO och strukturerad data per språkversion

PR: #99 · 2026-11-26 · code head 1cd864b; main merged in (956 had merged), this file is the only other change

Order 967 (Astra work order, `Plan: .team/ORDER.md`, no ORDER row or story file; the order text is the story). Merge route: `merge: auto`, no Human-merge path touched: one new file under `docs/`, excluded from the site. Judge merges on its word (CLOUD.md § Judge 5, J9).

## Must fix
- none

## Should fix
- none

## Nits
- N1 `docs/seo-revision-2026-11-25.md` ("Prioritera bolagets JSON-LD"): "`ProfessionalService`, som Schema.org har fasat ut". I could not open schema.org from the cloud (proxy, curl 000) and I do not know of such a deprecation; as far as I know the type is current. The other reasons given (no shared `@id`, different `url` on the two pages) hold, so the recommendation stands; the PO should check schema.org before acting on the "fasat ut" part.
- N2 Reported title/"Sweden" wording is the state at `28dedbf`; #95 (order 036) changes the English title once it merges. The report says which master it describes, so no fix needed.
- N3 No ORDER row names 967 (see review 956 N1).

## Evidence
| Acceptance criterion (order 967) | Shown by | Result |
|---|---|---|
| One report per language version in one file, `docs/seo-revision-2026-11-25.md`, no content touched | Files: one added file, 38 lines | pass |
| Canonical/hreflang/sitemap claims | My Jekyll 4.4 build of master: sitemap lists exactly `/`, `/beyond/`, `/sv/`; `index.html` and `sv/index.html` have mutual `hreflang` en/sv and `x-default` → `/`; `robots.txt` `Allow: /` + sitemap line | pass |
| JSON-LD claims | Both blocks are `ProfessionalService`, no `@id`, `url` differs (`/` vs `/sv/`); the Swedish block has `inLanguage: "sv"` and an English `makesOffer.description` | pass |
| Letter-template claims (empty `description`, future `lastmod`) | Code read, not re-run: `_layouts/beyond-base.html:7` takes `page.lead \| default: page.description`, so a letter without a lead gets `content=""`; `sitemap.xml:16` writes `d.date` as `lastmod` and `_config.yml` has `future: true` | pass (read, not run) |
| 33 local references resolve | Script: every `../path#L…` target exists in the branch and no line number is past EOF | pass |
| Test before commit | `pr-check` success on the new head | pass |

## Codex findings
- A first Codex run on 1cd864b ended "Something went wrong" (Unknown error); the Builder re-requested and the second run finished clean on the same commit with a 👍 receipt (2026-11-25T21:17Z). Nothing to rule on.

## What I checked
- tests run: my own Jekyll build + reading of the built sitemap, hreflang and JSON-LD; link/line check of the report.
- tried to break: looked for a claim that the built output contradicts; found only the unverifiable schema.org deprecation (N1).
- scope vs story: one docs file, content untouched.
- sync gate: main merged into the branch by me (the only file in common is none; no conflict).

## Papercuts
2026-11-26 | reviewer | schema.org unreachable from the cloud (curl 000), so the "fasat ut" claim could not be checked | flagged as N1 | open
