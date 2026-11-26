#!/usr/bin/env python3
"""Check the shared hero height and both home page diagrams."""

from html.parser import HTMLParser
from pathlib import Path
import re
import sys


class Diagram(HTMLParser):
    def __init__(self):
        super().__init__()
        self.label = None
        self.svg_depth = 0
        self.in_text = False
        self.texts = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "svg":
            if self.svg_depth:
                self.svg_depth += 1
            elif attrs.get("viewbox") == "0 0 520 360":
                self.svg_depth = 1
                self.label = attrs.get("aria-label") or ""
                self.texts = []
        elif self.svg_depth == 1 and tag == "text":
            self.in_text = True
            self.texts.append("")

    def handle_endtag(self, tag):
        if self.svg_depth and tag == "svg":
            self.svg_depth -= 1
        elif tag == "text":
            self.in_text = False

    def handle_data(self, data):
        if self.svg_depth == 1 and self.in_text:
            self.texts[-1] += data


def check_diagram(source, first, second):
    diagram = Diagram()
    diagram.feed(source)
    diagram.close()
    if diagram.label is None:
        yield "missing diagram with viewBox 0 0 520 360"
        return
    label = diagram.label.casefold()
    if not 0 <= label.find(first.casefold()) < label.find(second.casefold()):
        yield f"diagram aria-label must name {first!r} before {second!r}"
    for axis in (first, second):
        if not any(axis in text for text in diagram.texts):
            yield f"missing diagram axis text {axis!r}"


def check_css(source):
    css = re.sub(r"/\*.*?\*/", "", source, flags=re.S)
    if not re.search(r"^\.hero\{(?:[^}\n]*;)?\s*min-height:86svh(?=[;}])", css, re.M):
        yield ".hero must set min-height:86svh"
    for selector, body in re.findall(r"([^{}]+)\{([^{}]*)\}", css):
        if selector.lstrip().startswith(".hero") and re.search(
            r"(?:^|;)\s*min-height\s*:\s*100svh\b", body
        ):
            yield f"{' '.join(selector.split())} still sets min-height:100svh"


def main():
    checks = (
        ("assets/site.css", check_css, ()),
        ("index.html", check_diagram, ("Understands your business", "Builds the technology")),
        ("sv/index.html", check_diagram, ("Förstår er verksamhet", "Bygger tekniken")),
    )
    failures = []
    for path, check, args in checks:
        try:
            source = Path(path).read_text(encoding="utf-8")
            failures.extend(f"{path}: {message}" for message in check(source, *args))
        except (OSError, UnicodeError) as error:
            failures.append(f"{path}: {error}")
    if failures:
        print("\n".join(failures))
        return 1
    print("ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
