<!-- Builder's answers for story 030. -->

## Visual comparison — 2026-11-22
Jekyll 4.4.1 build of master (before) and this head (after); Playwright, reduced motion, scrolled to the bottom. Screenshots: `.team/screenshots/030/` (`before-*` / `after-*`, `en|sv` × `1440|390`, full page).
- `document.compatMode`: before `BackCompat`, after `CSS1Compat` on `/` and `/sv/`.
- Standards mode moved one thing: the offer block's line `<a class="btn-in">…</a><br><a class="sample">…`. The `<br>` after the inline-block button now makes a 22px line box and the sample link sits 2px lower (page +9px at 390). Fixed in `assets/site.css` (`built-by: claude`, commit after Codex CLI's): `.btn-in{vertical-align:top}`, `.btn-in+br{display:none}`, `.sample{display:block;margin-top:2px;line-height:22.67px}`.
- After the fix: full-page height identical at 1440 (9718 / 10580); 2px shorter at 390 (the 3-line sample link wraps at 22.67px vs the quirks line height); the only pixel differences are inside that one link's text rows (sub-pixel). No horizontal scroll (`scrollWidth == innerWidth`) at 1440, 390 and 360.
- Not checked: the link check against the live site (the cloud cannot reach it); nothing changed any href.

## Codex round 1 — pending

## Outcome
built-by: codex-cli->claude
model: claude-sonnet-5-5
parts: none
missed: standards mode shifts the line boxes around the `<br>` in the offer block; the plan guessed "if anything moves" and it did
