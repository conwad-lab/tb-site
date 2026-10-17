---
id: 013
verdict: approve
---
<!-- verdict: approve | request-changes | escalate — the board reads this line from the PR branch. Keep it current on re-review.
     approve only with no Must fix open. escalate: a Must fix still disputed after the third round (add ## Escalation). -->

# Review 013 — One booking label: "Book a scoping call" on every booking button

PR: #17 · 2026-10-17 · head `9fbd68a` · base `eea6616` (= current master, mergeable: clean)

## Must fix
- None.

## Should fix
- None.

## Nits
- N1 `PR #17 body` (Screenshots section) — Nit: the two image links point at `raw.githubusercontent.com/.../feat/013-one-booking-label/...`, a branch ref. After a squash merge with `--delete-branch` the branch is gone and the PR record shows broken images. · Suggested fix (next PRs, not this one): link by commit sha (`.../tb-site/<sha>/.team/screenshots/...`), which survives the branch deletion.
- N2 `.team/screenshots/013-one-booking-label-{1440,390}.png` — Nit / For PO: `.team/screenshots/` is not in any role's lane in `TEAM.md`, and the merge adds ~2.3 MB of binaries to master history per story. Declared as a deviation in the PR body and excluded from the site via `_config.yml` (`.team`), so no production effect. · Suggested fix: PO/human decides whether `.team/screenshots/` becomes the Coder's sanctioned place for review screenshots (Team settings line), or whether screenshots go elsewhere. Not blocking.

## What I checked
- **Tests run (Team settings › Test before commit), all by me on `9fbd68a`:**
  - `python3 -m html.parser index.html` — exits 0.
  - Plan grep counts: "Book a scoping call" = 4 (L182, L195, L319, L373); "Book the review" = 0; "Book the AI value review" = 0.
  - `git diff origin/master --stat -- index.html` — 1 file, 3 insertions, 3 deletions; hunks exactly `@@ -182 +182`, `@@ -195 +195`, `@@ -373 +373`, text only. `git diff --check` clean.
  - Unchanged, verified in the diff: every `href` (incl. `#kontakt` ×2 and `mailto:contact@transformationbeyond.se?subject=AI%20Value%20Review` on L373), `CALCOM_URL` (L413) and the Cal.com script block (L410–415), the `h2` on L371, the price (`75 000 SEK ex VAT · fixed scope · two weeks`, L374), the footer, `CNAME`, `_config.yml`, `AGENTS.md`, `.team/team.md`, `.team/CLOUD.md`. No rulebook file touched.
  - Playwright Chromium (web fonts loaded: Hanken Grotesk, JetBrains Mono, Newsreader), scrolled to bottom, full-page screenshots at 1440×900 and 390×844. Mine match the Coder's committed ones in size (1440×6967, 390×8200).
  - At 390: `.nav` 122.78 px, `.nav .cta` 43.19 px tall × 189.92 px wide, one line box, right edge 209.92 px; `scrollWidth` 390 = `innerWidth` 390; no element's right edge past the viewport. **Story AC "nav CTA does not wrap or overflow at 390" holds.**
  - At runtime `#book-cta` href becomes `https://cal.com/conny-wadbro-impk9g/architecture-review`, `target=_blank` — the Cal.com override still works with the new label.
  - href check (curl, browser User-Agent, follow redirects): 200 for the Google Fonts CSS URL, `https://mondmodel.com`, the R2 sample PDF, `https://transformationbeyond.se/`, `https://www.dignami.com/en`, `/en/proof`, `/en/proof#status-table`, and the Cal.com URL. Excluded per plan: `mailto:` ×2, bare preconnect hosts `fonts.googleapis.com` / `fonts.gstatic.com` (404 as documents, as expected). Fragments `#praktiken #arbetssatt #review #grundaren #kontakt` each have exactly one matching `id`; `assets/favicon.svg` exists. **Not checked:** nothing — no URL was blocked by my network.
- **Tried to break:**
  - Other widths 320, 360, 375, 414: `.nav` 122.78 px, nav CTA 43.19 px (one line), no horizontal overflow at any of them.
  - All four CTAs one line at 1440 and 390 (hero 52.8 px, offer 49 px, `#book-cta` 54.8 px tall).
  - Leftover labels: no other visible "Book…" button text. Remaining "book" occurrences are the L371 heading (out of scope per plan), CSS class `.book`, and "booked within week 1" in the offer body copy — none are booking buttons.
  - aria-labels / meta: no CTA carries an `aria-label`, so the accessible name equals the new text. `<title>`, `meta description`, `og:*` contain no booking-button label (they name the offer "AI Value Review", which is the product name, not a CTA — out of scope).
  - PR body claims, each verified against the diff and my own runs: three replacements (yes), offer button already had the label (yes, master L319), price/footer/hrefs/CALCOM_URL/script/contact address unchanged (yes), parser pass (yes), four/zero counts (yes), 390 measurements 122.78 / 43.19 / 189.92 / scrollWidth 390 (identical to mine), all non-mailto hrefs 200 and preconnect hosts 404 (yes), screenshot links resolve (200, image/png). No unsupported claim.
  - GitHub checks on `9fbd68a`: none configured (combined status `pending` with zero statuses; Team settings: CI-only checks none).
- **Review checks (Team settings):** no new factual claims on the page (copy is a button label only); no Dignami wording changed, so no comparison against dignami.com /en/proof and /en/about needed; no colour changed, so no WCAG contrast check needed; screenshots at both widths attached to the PR (Coder's, committed) and reproduced independently by me.
- **Scope vs story:** exactly the three label edits the plan names, no CSS, no markup, no script. The only extra is the screenshot commit (N2), which is declared and has no site effect. All four acceptance criteria met.
- **Not run:** Second reviewer (Team settings: no second-reviewer paths). My own screenshots could not be uploaded to GitHub from this session (REST has no image upload); they exist locally in the reviewer session and match the Coder's committed ones.

— Reviewer (Claude) on behalf of Conny Wadbro

## 2026-10-17 — second Reviewer session concurs (independent run)

Verdict unchanged: **approve**. This local Reviewer session (`reviewer/` clone, Fable 5.1) reviewed `9fbd68a` in parallel without seeing the section above, reached the same findings, and adds its screenshots.

- Reproduced every check above on `9fbd68a`: `html.parser` exit 0; `git diff --check` clean; diff is exactly L182/L195/L373, 3+/3−; grep counts 4/0/0; rulebook, `CNAME`, price, footer, `subject=`, `CALCOM_URL` and script block untouched.
- Playwright 1.58.2 Chromium, scrolled to bottom, 1440×900 and 390×844: all four CTAs read "Book a scoping call" on one line; at 390 the nav CTA is 43.19 × 189.92 px in a 122.78 px `.nav`, `scrollWidth` 390 = `innerWidth`; `#book-cta` rewrites to the Cal.com URL with `target=_blank rel=noopener`; Cal.com URL 200.
- href check: every `http(s)` link 200, all six anchors resolve, favicon exists; bare preconnect hosts 404 as documents (expected). Opened the Coder's committed PNGs: nav/hero and `#kontakt` show the new label at both widths.
- Concur with N1 and N2. One addition for PO, out of scope for 013: in `#kontakt` the button "Book a scoping call" sits directly above "75 000 SEK ex VAT · fixed scope · two weeks"; a first-time reader can take the price as the call's. Same adjacency pre-exists in the offer block. Copy decision, not a defect.

Reviewer screenshots on branch `evidence/013-review-screenshots` (`263c8db`): [1440×900](https://github.com/conwad-lab/tb-site/blob/263c8db/1440x900.png) · [390×844](https://github.com/conwad-lab/tb-site/blob/263c8db/390x844.png).

## Merge
Not merged by the Reviewer: `.team/CLOUD.md` says the human merges every PR during the cloud test, whatever `merge:` says. Merging deploys to production; Conny checks the live page afterwards (Operatör trigger). Both Reviewer sessions stop watching PR #17.

— Reviewer (Claude) on behalf of Conny Wadbro
