"""Fail on unreadable HTML files, unbalanced tags, or a home page without <!doctype html>.
Usage: check_html.py FILE..."""
import os
import sys
from html.parser import HTMLParser

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}
# Elements whose end tag HTML allows to be omitted; not tracked for balance.
OPTIONAL = {"li", "p", "dt", "dd", "tr", "td", "th", "thead", "tbody", "tfoot",
            "option", "optgroup", "colgroup", "html", "head", "body"}

class Checker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.errors = [], []
    def handle_starttag(self, tag, attrs):
        if tag not in VOID and tag not in OPTIONAL:
            self.stack.append((tag, self.getpos()[0]))
    def handle_startendtag(self, tag, attrs):
        foreign = any(t in ("svg", "math") for t, _ in self.stack)
        if tag not in VOID and not foreign:
            self.errors.append(f"line {self.getpos()[0]}: <{tag}/> is not a void element")
    def handle_endtag(self, tag):
        if tag in VOID or tag in OPTIONAL:
            return
        if self.stack and self.stack[-1][0] == tag:
            self.stack.pop()
        else:
            self.errors.append(f"line {self.getpos()[0]}: unexpected </{tag}>")

def needs_doctype(path):
    return os.path.normpath(path) in ("index.html", os.path.join("sv", "index.html"))

bad = 0
for path in sys.argv[1:]:
    text = open(path, encoding="utf-8").read()
    if not text.strip():
        print(f"{path}: empty"); bad += 1; continue
    if needs_doctype(path):
        content = text
        lines = content.splitlines(keepends=True)
        if lines and lines[0].rstrip("\r\n") == "---":
            for i in range(1, len(lines)):
                if lines[i].rstrip("\r\n") == "---":
                    content = "".join(lines[i + 1:])
                    break
        if not content.lstrip().lower().startswith("<!doctype html>"):
            print(f"{path}: missing <!doctype html>")
            bad += 1
    c = Checker(); c.feed(text); c.close()
    errs = c.errors + [f"line {l}: <{t}> never closed" for t, l in c.stack]
    for e in errs:
        print(f"{path}: {e}")
    bad += bool(errs)
sys.exit(1 if bad else 0)
