# transformationbeyond.se

Static one-pager for Transformation & Beyond AB (Commercial OS Tier 1, Item 1).
Source comp: dignify-rebuild/design-comps/tb-onepager-concept-v5-en.html (v5, 2026-07-06),
promoted 2026-07-19: band images + OG on R2 (brand/tb/), Architecture Review offer block,
booking CTA (mailto now; set CALCOM_URL in index.html when the Cal.com account exists),
viewport + OG + schema.org added; proof metrics verified truthful.

Hosting: GitHub Pages (headless Vercel/CF paths were credential-blocked 2026-07-19).
Operator gate G1 — when buying transformationbeyond.se:
  1. DNS: A records @ -> 185.199.108.153 / 185.199.109.153 / 185.199.110.153 / 185.199.111.153, CNAME www -> conwad-lab.github.io
  2. Set the custom domain on the repo Pages settings (or: gh api repos/conwad-lab/tb-site/pages -X PUT -f cname=transformationbeyond.se)
  3. Enforce HTTPS once the cert issues; www redirects automatically
  4. Same session: set up email routing for contact@transformationbeyond.se (the booking CTA mailto)
