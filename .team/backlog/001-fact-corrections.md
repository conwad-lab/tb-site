---
id: 001
title: Correct factual claims on the page (C1, C2, C3, C8, C9)
---

## Outcome
The page makes no claim about the founder's credentials or experience that the brief does not support, says plainly that T&B does not replace legal counsel, and declares its language to browsers and assistive tech.

## Why
dignami.com now states "No certifications we don't hold" and marks every claim with a status. transformationbeyond.se (from 2026-07-19) still says the founder holds a master's degree in commercial law. The founder holds a bachelor's degree; the Lund commercial-law studies are master's-level courses, not a master's degree (hard rail in `AGENTS.md`). Two sites selling to the same board must not contradict each other, and this one must not overclaim. Source for every change: `.team/briefs/2026-10-site-refresh.md`, table "Innehållsändringar", rows C1, C2, C3, C8, C9.

## Acceptance criteria
- [ ] C1 — `02 · Law` card (`index.html` ~line 271): "A master's degree in commercial law." → "Master's-level studies in commercial law at Lund University." No wording anywhere on the page that implies a master's degree is held.
- [ ] C2 — Foundation row (~line 348): "Master's in commercial law · sales leadership in consulting · working AI architect." → "Commercial law studies (Lund) · sales leadership in consulting · working AI architect." The bold "One borderland, one advisor." stays.
- [ ] C3 — `01 · Business` card (~line 270): "Two decades in consulting" → "Two decades in IT, consulting and sales leadership". Rest of the sentence unchanged.
- [ ] C8 — one new sentence in the `02 · Law` card, after the existing text: "We read the regulation to shape the design — we don't replace your counsel."
- [ ] C9 — `<html>` gets `lang="en"`.
- [ ] A full-text search of `index.html` for "master's degree" and "Master's in" returns nothing.
- [ ] `<meta name="description">` and `<title>` unchanged (they make no credential claim).
- [ ] Price block, booking CTA and footer untouched. `CNAME` untouched.
- [ ] Team settings test passes: `python3 -m html.parser index.html` clean, Playwright screenshots at 1440×900 and 390×844 after scrolling to bottom, all `href`s return 200. Screenshots attached to the PR.

## Out of scope
- Dignami wording, links and AOS status (C4–C7) — next story.
- Restructuring "How we work" (Advise → Assurance → Platform) — later story.
- Any colour, layout or typography change.
- Swedish version.

## Log
- 2026-10-12 PO: created from ORDER row 1. Brief says C8 goes in "the Law discipline / the Advise step"; chose the Law card because the Advise step is rewritten wholesale in a later row.
