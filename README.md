# transformationbeyond.se

Static one-pager for Transformation & Beyond AB (Commercial OS Tier 1, Item 1).
Source comp: dignify-rebuild/design-comps/tb-onepager-concept-v5-en.html (v5, 2026-07-06),
promoted 2026-07-19: band images + OG on R2 (brand/tb/), Architecture Review offer block,
booking CTA (mailto now; set CALCOM_URL in index.html when the Cal.com account exists),
viewport + OG + schema.org added; proof metrics verified truthful.

Hosting: GitHub Pages — DEPLOYED 2026-07-19 (repo conwad-lab/tb-site, branch master,
build green, custom domain transformationbeyond.se configured on the GitHub side,
content verified served at the Pages edge: 27,374-byte HTML, favicon 200, sample-PDF
link present). NOTE: the conwad-lab account carries a stale user-level Pages custom
domain (mondmodel.com), so github.io project URLs redirect account-wide — harmless
for this repo (its own custom domain overrides), but worth cleaning up separately.

Operator gate G1 — registrar side only (the GitHub side is done):
  1. Buy transformationbeyond.se; DNS: A records @ -> 185.199.108.153 / 185.199.109.153 / 185.199.110.153 / 185.199.111.153, CNAME www -> conwad-lab.github.io
  2. Wait for the cert to issue, then tick "Enforce HTTPS" in the repo's Pages settings
  3. Same session: email routing for contact@transformationbeyond.se (the booking CTA mailto)
  4. G2: set CALCOM_URL in index.html when the Cal.com account exists

## & Beyond (the weekly letter, story 016)

Letters live in `_beyond/` (one Markdown file per issue) and are built by the Jekyll that GitHub Pages runs:
`/beyond/` (archive), `/beyond/<year>-v<week>/` (one letter) and `/beyond/feed.xml` (Atom). `index.html` has no
front matter, so Jekyll copies it unchanged.

Add a letter only after Conny has published it and set `status: publicerad` in conwad-lab/ai-insikter:

    python3 bin/import-beyond.py ../ai-insikter/veckor/2026-V44-publicering.md

The script copies the article section and its images, and refuses drafts, missing images, a missing source list
and internal material. Merging the PR publishes the letter. Local build (Pages versions):
`gem install github-pages -v 232`, a Gemfile with `gem "github-pages", "= 232"`, then
`LC_ALL=C.UTF-8 PAGES_REPO_NWO=conwad-lab/tb-site bundle exec jekyll build`.
