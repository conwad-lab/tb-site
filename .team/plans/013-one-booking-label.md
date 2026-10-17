---
id: 013
verdict: plan
---

# Plan 013 — One booking label: "Book a scoping call" on every booking button

Story: `.team/backlog/013-one-booking-label.md`

## Approach
Copy-only change in `index.html`: three button texts become "Book a scoping call". No CSS, no markup, no script, no URL change. Measured on master (`2d85a28`) with the new strings injected at 1440×900 and 390×844: the nav CTA stays one line at 390 (43 px tall, 159 → 190 px wide, `.nav` 123 px, no horizontal overflow), so the D5 stack from plan 008 needs no change.

Strings (old → new), line numbers on master `2d85a28`:
1. L182 nav `<a class="cta" href="#kontakt">`: "Book the review" → "Book a scoping call"
2. L195 hero `<a class="cta-big" href="#kontakt">`: "Book the AI value review" → "Book a scoping call"
3. L373 `<a class="cta-bronze" id="book-cta" href="mailto:…?subject=AI%20Value%20Review">`: "Book the AI value review" → "Book a scoping call"

L319 offer button already reads "Book a scoping call" — unchanged. L371 `<h2>` "Review the build before you book the call." is a heading, not a button — unchanged.

Touches: booking CTA — text only, every `href`, `CALCOM_URL` (L413) and the `mailto:` incl. `subject=` unchanged. Price block: no. Footer: no.

## Files
- `index.html` — the three edits above.

## Steps
1. Branch `feat/013-one-booking-label`, make the three edits.
2. Run Tests; PR body lists the three old → new strings and the 390 px nav measurement.

## Tests
- `python3 -m html.parser index.html` exits 0.
- `grep -c "Book a scoping call" index.html` → 4; `grep -c "Book the review" index.html` → 0; `grep -c "Book the AI value review" index.html` → 0.
- `git diff master -- index.html` changes exactly lines 182, 195, 373 and nothing else (`--stat`: 3 insertions, 3 deletions).
- Playwright 1440×900 and 390×844, scrolled to bottom, full-page screenshots attached. At 390: `.nav` height 123, `.nav .cta` height 43 (one line), `document.documentElement.scrollWidth === innerWidth`.
- `href` check: every `http(s)` href 200 (the two bare `preconnect` hosts excluded, `mondmodel.com` needs a browser User-Agent).

## Risks / watch out for
- Do not touch `subject=AI%20Value%20Review`, the Cal.com script block (L411–414) or the `h2` on L371.
- The `.cta` rule has no `white-space:nowrap`; the measurement shows it is not needed at 390. Do not add CSS.

## Out of scope
- Cal.com event title (Operatör line, already in ORDER).
- Sample-PDF link, any other copy, CSS.

## Suggestions for PO
- None.
