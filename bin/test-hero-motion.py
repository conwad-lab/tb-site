#!/usr/bin/env python3
"""Check story 029's hero markup, script hooks and CSS without dependencies."""

from html.parser import HTMLParser
from pathlib import Path
import sys


FILM = "/assets/film/sluseholmen-720.mp4"
CSS_LINES = (
    ".hero.paused .flow svg{animation-play-state:paused}",
    ".motion{position:absolute;top:calc(96px + env(safe-area-inset-top,0px));right:max(var(--pad),env(safe-area-inset-right,0px));z-index:2;display:grid;place-items:center;width:40px;height:40px;padding:0;color:var(--on-blue);background:rgba(12,34,51,.5);border:1px solid rgba(248,246,241,.5);border-radius:50%;cursor:pointer}",
    ".motion:focus-visible{outline:3px solid var(--white);outline-offset:2px;box-shadow:0 0 0 8px var(--black)}",
    ".motion[hidden],.motion .i-play,.hero.paused .motion .i-pause{display:none}",
    ".hero.paused .motion .i-play{display:block}",
    ".motion svg{width:14px;height:14px;fill:currentColor}",
    "h2.tag{font-family:var(--f);letter-spacing:normal;line-height:1.5;text-wrap:wrap}",
)
VOID = set("area base br col embed hr img input link meta param source track wbr".split())


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = []
        self.stack = []

    def handle_starttag(self, tag, attrs):
        element = {
            "tag": tag, "attrs": dict(attrs), "text": "",
            "in_hero": any(has_class(parent, "hero") for parent in self.stack),
            "in_motion_button": any(parent["tag"] == "button" and has_class(parent, "motion")
                                    for parent in self.stack),
        }
        self.elements.append(element)
        if tag not in VOID:
            self.stack.append(element)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index]["tag"] == tag:
                del self.stack[index:]
                break

    def handle_data(self, data):
        for element in self.stack:
            element["text"] += data


def has_class(element, name):
    return name in (element["attrs"].get("class") or "").split()


def main():
    failures = []

    def check(condition, path, message):
        if not condition:
            failures.append(f"{path}: {message}")

    for name, pause, play, labels in (
        ("index.html", "Pause film", "Play film", (
            "How we work — three links, two companies", "The questions we answer")),
        ("sv/index.html", "Pausa filmen", "Spela filmen", (
            "Arbetssätt — tre led, två bolag", "Frågorna vi besvarar")),
    ):
        try:
            source = Path(name).read_text(encoding="utf-8")
        except OSError as error:
            check(False, name, str(error))
            continue
        page = Page()
        page.feed(source)
        page.close()
        films = [e for e in page.elements if e["tag"] == "video" and has_class(e, "film")]
        check(len(films) == 1, name, "expected exactly one video.film")
        for film in films:
            attrs = film["attrs"]
            check(attrs.get("data-src") == FILM, name, "video.film data-src must be the film URL")
            check("src" not in attrs, name, "video.film must not have src")
            for attr in ("autoplay", "muted", "loop", "playsinline", "poster", "onerror"):
                check(attr in attrs, name, f"video.film must retain {attr}")
        check(not any(FILM in (e["attrs"].get("src") or "") for e in page.elements),
              name, "film URL must not appear in any src attribute")
        buttons = [e for e in page.elements if e["tag"] == "button" and has_class(e, "motion")]
        check(len(buttons) == 1, name, "expected exactly one button.motion")
        for button in buttons:
            attrs = button["attrs"]
            check(attrs.get("type") == "button", name, "button.motion type must be button")
            check("hidden" in attrs, name, "button.motion must be hidden initially")
            check(button["in_hero"], name, "button.motion must be inside .hero")
            check(attrs.get("data-pause") == pause, name, "incorrect data-pause label")
            check(attrs.get("data-play") == play, name, "incorrect data-play label")
            check(button["text"].strip() == "", name, "button.motion must have no text")
            check(attrs.get("aria-label") == pause, name, "incorrect initial aria-label")
        for icon_class in ("i-pause", "i-play"):
            icons = [e for e in page.elements if e["tag"] == "svg" and has_class(e, icon_class)]
            check(len(icons) == 1, name, f"expected exactly one svg.{icon_class}")
            for icon in icons:
                attrs = icon["attrs"]
                check(icon["in_motion_button"], name, f"svg.{icon_class} must be inside button.motion")
                check(attrs.get("aria-hidden") == "true", name, f"svg.{icon_class} must be aria-hidden")
                check(attrs.get("focusable") == "false", name, f"svg.{icon_class} must not be focusable")
                check("style" not in attrs, name, f"svg.{icon_class} must not have a style attribute")
        for label in labels:
            matches = [e for e in page.elements if has_class(e, "tag") and e["text"] == label]
            check(sum(e["tag"] == "h2" for e in matches) == 1,
                  name, f"expected one h2.tag for {label!r}")
            check(not any(e["tag"] == "p" for e in matches),
                  name, f"label must not remain a p.tag: {label!r}")
        for hook in ("prefers-reduced-motion: reduce", "getAttribute('data-src')", "classList.toggle('paused')", "setAttribute('aria-label'"):
            check(hook in source, name, f"missing script hook: {hook}")
        check("btn.textContent" not in source, name, "button script must not replace icon content")

    css_path = "assets/site.css"
    try:
        css_lines = Path(css_path).read_text(encoding="utf-8").splitlines()
        for line in CSS_LINES:
            check(line in css_lines, css_path, f"missing verbatim CSS line: {line}")
    except OSError as error:
        check(False, css_path, str(error))
    for failure in failures:
        print(failure)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
