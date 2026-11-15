# 016 — Builder's response

## Codex round 1 — 2026-11-02
- M1 (front matter parsed line by line): fixed in 5673747. Parsed with `yaml.safe_load`; malformed YAML is refused, `status: "publicerad"` accepted, an indented continuation (`publicerad utkast`) refused. Fixtures run: quoted → 0, indent → 1, `bad: [unterminated` → 1.
- M2 (titled / reference-style images not validated): fixed in 5673747. Only plain `![alt](path)` is supported; any other `![` form, an `<img>` tag, a URL or an absolute path is refused. Fixtures: titled → 1, reference style → 1, remote URL → 1.
- M3 (sidecar alt text not checked for internal material): fixed in 5673747. Each `.alt.txt` goes through the same forbidden-material check. Fixture with `TODO internt: insikter/private.md [Connys exempel]` → 1.
- M4 (archive entry has no date): fixed in 5673747. Each entry shows week and the publication date (`<time datetime>`, Swedish month).

Process note: no separate plan attack ran before the build (story and plan ride in this PR); round 1 was asked to read the plan with the diff.

## Codex round 2 — 2026-11-02
- No findings on 27c4bc5 (Codex: "Didn't find any major issues").

## Codex round 3 — 2026-11-15 (rebase on master)
- The branch was rebased on master (488620b, no conflicts) and the screenshots retaken (e581733). Outside the screenshots the diff against master is the same as the diff 27c4bc5 had against its base; only the context lines of `.team/ORDER.md` moved.
- `@codex review` on e581733 failed twice: Codex usage limit for code reviews reached (requests 2026-11-15 15:52, comments 6897168087 and 6897171538). No code changed since the last clean Codex round on 27c4bc5.
- Test before commit on e581733: `python3 -m html.parser index.html` ok; Jekyll (github-pages 232) builds `index.html` (byte-identical to the source), `beyond/index.html` and `beyond/feed.xml` (well-formed XML), and no team file, `docs/` or `bin/` reaches `_site`. Screenshots at 1440 and 390 for `/` and `/beyond/` in `docs/screenshots/016-and-beyond-archive/`. Links: all local links 200; the external links (dignami.com, cal.com, mondmodel.com, the R2 PDF) are **not checked**, the session's network blocks them, and none of them changed in this PR.
