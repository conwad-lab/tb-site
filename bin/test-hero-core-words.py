#!/usr/bin/env python3
"""Check the bilingual hero label and its position in the heading structure."""
from html.parser import HTMLParser
from pathlib import Path


class HeroParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hero_div_depth = 0
        self.events = []
        self.h1_count = 0

    def handle_starttag(self, tag, attrs):
        classes = dict(attrs).get("class", "")
        if tag == "div" and (self.hero_div_depth or "hero" in classes.split()):
            self.hero_div_depth += 1
        self.h1_count += tag == "h1"
        if self.hero_div_depth:
            self.events.append(("start", tag, classes))

    def handle_endtag(self, tag):
        if self.hero_div_depth:
            self.events.append(("end", tag))
            if tag == "div":
                self.hero_div_depth -= 1

    def handle_data(self, data):
        if self.hero_div_depth and data.strip():
            self.events.append(("text", data))


errors = []
for file, label in (("index.html", "Understand · Rethink · Rebuild"),
                    ("sv/index.html", "Förstå · Ompröva · Bygg om")):
    page = HeroParser()
    page.feed(Path(file).read_text())
    label_text = ("text", label)
    if page.events.count(label_text) != 1:
        errors.append(f"{file}: expected one core-words label inside the hero")
    else:
        i = page.events.index(label_text)
        if page.events[i-1:i+3] != [("start", "p", "tag"), label_text,
                                     ("end", "p"), ("start", "h1", "")]:
            errors.append(f"{file}: expected a tag paragraph immediately before h1")
    if page.h1_count != 1:
        errors.append(f"{file}: expected one h1")

css = Path("assets/site.css").read_text().splitlines()
for rule in (
    '.hero .tag{position:relative}',
    '.hero .tag::before{background:var(--on-blue)}',
    '.tag{font-size:15px;font-weight:700;margin:0 0 clamp(22px,3vw,40px);display:flex;align-items:center;gap:10px}',
    '.tag::before{content:"";width:14px;height:14px;background:var(--red);flex:none}',
    '.hero{position:relative;isolation:isolate;background:var(--blue);color:var(--on-blue);min-height:86svh;display:flex;flex-direction:column;justify-content:flex-end;padding-top:96px;padding-bottom:clamp(24px,4vh,48px);overflow:hidden}',
):
    if rule not in css:
        errors.append(f"assets/site.css: missing {rule}")

print("\n".join(errors) if errors else "ok")
raise SystemExit(bool(errors))
