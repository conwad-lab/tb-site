#!/usr/bin/env node
// One-shot: extract base64 data-URI images from the v5 comp into assets/,
// rewrite references, write index.html. Run once, then delete or keep for provenance.
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';

const SRC = '/Users/connywadbro/WebProjects/dignify-rebuild/design-comps/tb-onepager-concept-v5-en.html';
const OUT = new URL('.', import.meta.url).pathname;

let html = readFileSync(SRC, 'utf8');
mkdirSync(OUT + 'assets', { recursive: true });

const names = ['contours-duotone.jpg', 'strata-duotone.jpg'];
let i = 0;
html = html.replace(/data:image\/jpeg;base64,([A-Za-z0-9+/=]+)/g, (_, b64) => {
  const name = names[i] ?? `img-${i}.jpg`;
  writeFileSync(OUT + 'assets/' + name, Buffer.from(b64, 'base64'));
  i += 1;
  return '/assets/' + name;
});

writeFileSync(OUT + 'index.html', html);
console.log(`extracted ${i} images; index.html ${Buffer.byteLength(html)} bytes`);
