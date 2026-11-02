# 016 — Builder's response

## Codex round 1 — 2026-11-02
- M1 (front matter parsed line by line): fixed in 5673747. Parsed with `yaml.safe_load`; malformed YAML is refused, `status: "publicerad"` accepted, an indented continuation (`publicerad utkast`) refused. Fixtures run: quoted → 0, indent → 1, `bad: [unterminated` → 1.
- M2 (titled / reference-style images not validated): fixed in 5673747. Only plain `![alt](path)` is supported; any other `![` form, an `<img>` tag, a URL or an absolute path is refused. Fixtures: titled → 1, reference style → 1, remote URL → 1.
- M3 (sidecar alt text not checked for internal material): fixed in 5673747. Each `.alt.txt` goes through the same forbidden-material check. Fixture with `TODO internt: insikter/private.md [Connys exempel]` → 1.
- M4 (archive entry has no date): fixed in 5673747. Each entry shows week and the publication date (`<time datetime>`, Swedish month).

Process note: no separate plan attack ran before the build (story and plan ride in this PR); round 1 was asked to read the plan with the diff.
