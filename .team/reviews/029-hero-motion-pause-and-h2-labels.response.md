## Outcome
built-by: codex-cli
model: claude-sonnet-5-5 (Builder thread: order, Test before commit, Playwright checks); the code is gpt-6-astra via the Codex CLI poller on connys-macbook-air
parts: none
missed: nothing

Run's Hinder line: `Hinder: inga` (run 20261122T221419Z-29468, 3 min, order on issue #69).

Checks on head 601ef4c (Builder thread, cloud):
- Test before commit (`check_html.py` on every page): green. Proof `python3 bin/test-hero-motion.py`: green.
- Playwright, both pages: reduced motion → no request for `sluseholmen-720.mp4`, button hidden, no `src`; JavaScript off → no film request, button hidden; motion on → film requested, button visible, click sets `.hero.paused`, `video.paused === true`, `.flow svg` `animation-play-state: paused` (with `.no-film` forced), label swaps to "Play film" / "Spela filmen", second click resumes.
- Before/after full-page screenshots at 1440×900 and 390×844 (scrolled to the bottom): page heights identical; pixel differences only inside the first screen (film frame and the button), none in the label rows. Screenshots in `.team/screenshots/029-*`.
- Button contrast: #F8F6F1 on navy at 72 % over the worst backdrop (white) 6.0:1, over black 16.6:1 (WCAG AA).
- Internal links 200 on the local copy. External links (cal.com, mailto) and the live site: not checked (the cloud network does not reach them).
