#!/usr/bin/env python3
"""Guard the colours and fonts shared by the & Beyond pages."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parent.parent
failures = []


def fail(message):
    failures.append(message)


checked_files = (
    "assets/beyond.css",
    "_layouts/beyond-base.html",
    "_layouts/beyond-letter.html",
    "beyond/index.html",
    "404.html",
    "assets/favicon.svg",
)
forbidden = (
    "#7A5729", "#5C421E", "#8A6430", "#E8D9BE", "#F7F5F0",
    "#1C2022", "#E3DFD5", "#3B3E42", "#5B5E62", "Hanken",
    "JetBrains", "--mono", "--bronze",
)
for filename in checked_files:
    text = (ROOT / filename).read_text(encoding="utf-8")
    for value in forbidden:
        if value.casefold() in text.casefold():
            fail(f"{filename}: forbidden value {value}")

site_css = (ROOT / "assets/site.css").read_text(encoding="utf-8")
root_match = re.search(r":root\s*\{([^}]*)\}", site_css, re.DOTALL)
if root_match is None:
    fail("assets/site.css: missing :root block")
    allowed_colours = set()
else:
    allowed_colours = {
        colour.upper()
        for colour in re.findall(r"#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?\b", root_match.group(1))
    }
allowed_colours.add("#FFFFFF")
beyond_css = (ROOT / "assets/beyond.css").read_text(encoding="utf-8")
for colour in re.findall(r"#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?\b", beyond_css):
    if colour.upper() not in allowed_colours:
        fail(f"assets/beyond.css: colour {colour} is not allowed")

font_pattern = re.compile(r'<link\s+href="([^"]*fonts\.googleapis\.com/css2\?[^"]+)"')
font_hrefs = {}
for filename in ("index.html", "_layouts/beyond-base.html", "404.html"):
    font_hrefs[filename] = font_pattern.findall((ROOT / filename).read_text(encoding="utf-8"))
    if len(font_hrefs[filename]) != 1:
        fail(f"{filename}: expected exactly one Google Fonts stylesheet link")
if all(len(hrefs) == 1 for hrefs in font_hrefs.values()):
    expected_href = font_hrefs["index.html"][0]
    for filename in ("_layouts/beyond-base.html", "404.html"):
        if font_hrefs[filename][0] != expected_href:
            fail(f"{filename}: Google Fonts stylesheet href differs from index.html")

allowed_fills = {"#F8F6F1", "#0C2233", "#CF2318"}
fill_sources = {"assets/favicon.svg": (ROOT / "assets/favicon.svg").read_text(encoding="utf-8")}
for filename in ("_layouts/beyond-base.html", "404.html"):
    text = (ROOT / filename).read_text(encoding="utf-8")
    footer_match = re.search(r"<footer\b.*?</footer>", text, re.DOTALL)
    if footer_match is None:
        fail(f"{filename}: missing footer")
    else:
        fill_sources[f"{filename} footer"] = footer_match.group(0)
for source, text in fill_sources.items():
    for fill in re.findall(r'fill="(#[0-9a-fA-F]+)"', text):
        if fill.upper() not in allowed_fills:
            fail(f"{source}: fill {fill} is not allowed")

required_lines = (
    "::selection{background:var(--red);color:#FFFFFF}",
    "body > header{background:var(--navy);color:var(--on-navy)}",
    ".mark span{font-family:var(--serif);font-weight:500;font-size:1em;color:var(--red)}",
    ".nav-r a{text-decoration:none;color:var(--on-navy);border-bottom:2px solid transparent;padding-bottom:2px}",
    ".nav-r a:hover{color:var(--on-navy);border-color:var(--red)}",
    ".eyebrow{font-family:var(--sans);font-size:12px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--red);margin:0 0 22px;display:flex;gap:14px;align-items:center;line-height:1.4}",
    ".archive h1,.letter h1{font-family:var(--serif);font-weight:500;letter-spacing:-.02em;line-height:1.04;margin:.2em 0 .5em;text-wrap:balance;color:var(--ink)}",
    ".follow{font-family:var(--sans);font-size:14px;font-weight:500;letter-spacing:.02em;margin:0 0 48px}",
    ".issues .wk{display:block;font-family:var(--sans);font-size:12px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--red);margin-bottom:8px}",
    ".meta{font-family:var(--sans);font-size:13px;letter-spacing:.02em;color:var(--muted);margin:0 0 40px;padding-bottom:28px;border-bottom:1px solid var(--rule)}",
    ".back{margin-top:48px;padding-top:24px;border-top:1px solid var(--rule);font-family:var(--sans);font-size:14px;font-weight:500;letter-spacing:.02em}",
    "footer{background:var(--navy);color:var(--on-navy);padding:38px 0 56px;font-size:13px}",
    ".foot .mono{font-family:var(--sans);font-size:13px;letter-spacing:.02em}",
    ".foot a{color:var(--on-navy);text-decoration:none;border-bottom:1px solid var(--red)}",
    ".foot a:hover{color:var(--on-navy);border-color:var(--on-navy)}",
    "body > header a:focus-visible,footer a:focus-visible{outline-color:var(--on-navy)}",
)
css_lines = beyond_css.splitlines()
for line in required_lines:
    if line not in css_lines:
        fail(f"assets/beyond.css: missing required line {line}")

if failures:
    print(*failures, sep="\n")
    sys.exit(1)
print("ok")
