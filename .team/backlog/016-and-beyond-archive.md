---
id: 016
title: "& Beyond archive — the weekly letter on transformationbeyond.se/beyond/ with RSS"
---

## Outcome
Every published issue of the weekly letter *& Beyond* has its own page under https://transformationbeyond.se/beyond/, listed newest first on an archive page with an RSS feed, built by the Jekyll that GitHub Pages already runs.

## Why
Conny publishes *& Beyond* every Monday as a LinkedIn newsletter. LinkedIn stays the main channel, but the letters should also live on T&B's own site: an archive T&B owns, links that do not depend on LinkedIn, and RSS. This is step 1 of the proposal of 2026-11-02 (Claude Doc "& Beyond på transformationbeyond.se: förslag"); step 2, an e-mail form so T&B owns its subscriber list, is a later story. Conny chose "Jekyll på nuvarande Pages" on a decision card on 2026-11-02, including the archive in Swedish under `/beyond/`.

## Signal
After merge: https://transformationbeyond.se/beyond/ and https://transformationbeyond.se/beyond/feed.xml return 200, the feed validates as Atom, and each letter marked `status: publicerad` in conwad-lab/ai-insikter has a page within a week of publication.

## Acceptance criteria
- [ ] `/beyond/` lists every letter in `_beyond/`, newest first, with week, title, lead and date; `lang="sv"`.
- [ ] Each letter has a page at `/beyond/<year>-v<week>/` (publication week), with the cover, diagrams (alt text from the `.alt.txt` files), body and source list as in the published text.
- [ ] `/beyond/feed.xml` is an Atom feed of the collection, linked from the archive and letter pages with `<link rel="alternate">`.
- [ ] Letter and archive pages use the site's identity (paper/bronze, Newsreader + Hanken Grotesk + JetBrains Mono from the Google Fonts host already used), work at 390 px with no horizontal scroll, and meet WCAG AA contrast.
- [ ] A script `bin/import-beyond.py` turns an ai-insikter `veckor/ÅÅÅÅ-Vvv-publicering.md` into a `_beyond/` file plus images, and refuses a file that is not `status: publicerad`, lacks a title or a source list, references a missing image, or contains internal material (HTML comments, repo paths, placeholders such as `[Connys exempel`).
- [ ] The home page gets exactly one new link to `/beyond/`, in the footer; no other copy on `index.html` changes.
- [ ] No third-party script, tracker or new font host. Team files and `bin/` stay excluded from the published site.
- [ ] Team settings tests pass on the Jekyll build output (`_site/`), screenshots of home, archive and a letter at both widths attached.

## Out of scope
- E-mail form and subscriber list (step 2, own story).
- Automating the import (Monday routine or GitHub Action): the script is run by hand or by the routine; wiring it up is its own story.
- An English translation of the letters; any change to the home page beyond the footer link.

## Log
- 2026-11-02 PO (written by the project thread on Conny's decision card answer, Coordinator informed): created.
