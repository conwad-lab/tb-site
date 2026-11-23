## Outcome
built-by: codex-cli
model: claude-sonnet-5-5 (Builder thread: order, Test before commit, Playwright checks); the code is gpt-6-astra via the Codex CLI poller on connys-macbook-air
parts: none
missed: nothing

Run's Hinder line: `Hinder: inga` (run 20261123T083613Z-81124, 2 min, order on issue #76).

Checks on head 50cb4e5 (Builder thread, cloud, local Jekyll-free copy with the front matter stripped):
- Test before commit (`check_html.py` on every page): green. Proof `python3 bin/test-hero-motion.py`: green.
- Playwright, both pages: reduced motion and JavaScript off → no request for `sluseholmen-720.mp4`, button `display: none`. Motion on, 1440×900 and 390×844: button 40×40, no text, only `.i-pause` shown; click → `.hero.paused`, `video.paused` true, only `.i-play`, `aria-label` "Play film" / "Spela filmen"; second click restores everything. Accessibility tree name matches the label. No horizontal scroll.
- Icon contrast (#F8F6F1 against the 50 % navy backing): over the brightest pixel of the poster/film frame under the button 11.1:1, over `.no-film` navy 15.0:1; worst case over pure white 3.0:1 (≥ 3:1 for a UI component).
- Before/after first-screen screenshots at both widths in `.team/screenshots/031-*`.
- Not checked: external links, the live site (cloud network). Internal asset paths unchanged by this diff.
