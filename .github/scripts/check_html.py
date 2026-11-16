"""Fail on unreadable HTML files or unbalanced tags. Usage: check_html.py FILE..."""
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

bad = 0
for path in sys.argv[1:]:
    text = open(path, encoding="utf-8").read()
    if not text.strip():
        print(f"{path}: empty"); bad += 1; continue
    c = Checker(); c.feed(text); c.close()
    errs = c.errors + [f"line {l}: <{t}> never closed" for t, l in c.stack]
    for e in errs:
        print(f"{path}: {e}")
    bad += bool(errs)
sys.exit(1 if bad else 0)
