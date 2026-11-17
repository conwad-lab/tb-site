#!/usr/bin/env python3
"""Import one & Beyond letter from conwad-lab/ai-insikter into this site (story 016).

Usage:
  python3 bin/import-beyond.py <ai-insikter>/veckor/2026-V44-publicering.md
  python3 bin/import-beyond.py <file> --allow-draft --out <dir>   # local test only

Takes the article section ("# Substack / LinkedIn-artikel" up to the next "# "
heading; the LinkedIn post is left out), checks it, and writes
_beyond/<year>-v<week>.md plus its images under assets/beyond/<slug>/.
The week is the ISO week of `publiceras:` (the publication Monday).
Wording is never changed: only image paths are rewritten.
Exit 1 with one line per problem if the letter must not be published.
"""
import argparse
import datetime as dt
import pathlib
import re
import shutil
import sys

SITE = pathlib.Path(__file__).resolve().parent.parent
ARTICLE_HEADING = "# Substack / LinkedIn-artikel"
FORBIDDEN = [
    ("<!--", "HTML-kommentar"),
    ("[Connys", "platshållare för Connys text"),
    ("TODO", "TODO"),
    ("veckor/", "sökväg i ai-insikter"),
    ("insikter/", "sökväg i ai-insikter"),
    ("granskning-codex", "granskningsfil"),
]
IMG = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)\)")
IMG_START = re.compile(r"!\[")
HTML_IMG = re.compile(r"<img\b", re.I)
# The body is written inside {% raw %}…{% endraw %} so Jekyll's Liquid pass leaves
# text such as {{ … }} or {% … %} exactly as written; a letter that closes the raw
# block itself cannot be kept verbatim and is refused.
ENDRAW = re.compile(r"\{%-?\s*endraw\s*-?%\}")


def front_matter(text):
    """Parse the front matter as YAML. Returns (mapping or None if malformed, body)."""
    try:
        import yaml
    except ImportError:
        sys.exit("PyYAML saknas: pip install pyyaml")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, text
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return None, text[m.end():]
    return (fm if isinstance(fm, dict) else None), text[m.end():]


def forbidden(text, where):
    return [f"internt material i {where}: {what} ('{needle}')" for needle, what in FORBIDDEN if needle in text]


# A line that opens or closes a fenced code block; "# " inside one is not a heading.
FENCE_LINE = re.compile(r"^[ ]{0,3}(```|~~~)")


def outside_fences(lines):
    """Indexes of lines that are not inside a fenced code block."""
    keep, fence = [], None
    for i, line in enumerate(lines):
        m = FENCE_LINE.match(line)
        if m:
            fence = None if fence == m.group(1) else (fence or m.group(1))
            continue
        if fence is None:
            keep.append(i)
    return keep


def article(body):
    lines = body.splitlines()
    try:
        start = lines.index(ARTICLE_HEADING) + 1
    except ValueError:
        return None
    out, fence = [], None
    for line in lines[start:]:
        if fence is None and line.startswith("# "):
            break
        out.append(line)
        m = FENCE_LINE.match(line)
        if m:
            fence = None if fence == m.group(1) else (fence or m.group(1))
    while out and out[-1].strip() in ("", "---"):
        out.pop()
    return "\n".join(out).strip("\n")


# Only the source list ("### Källor" up to the next heading) gets autolinks; the rest
# of the letter is left exactly as written. Inside it, these spans are copied as is:
# fenced and inline code, Markdown links and images (inline, reference, shortcut, and
# definition lines), any [bracketed] text, HTML elements
# whose content is raw or a link (<a>, <pre>, <code>, <script>, <style>) and any other tag.
KEEP = re.compile(
    r"```.*?```|~~~.*?~~~|(`+).*?\1"
    r"|^[ ]{0,3}\[[^\]\n]+\]:[^\n]*"
    r"|!?\[(?:[^\[\]\n]|\[[^\[\]\n]*\])*\]"
    r"(?:\((?:[^()\s]|\([^()\s]*\))*(?:\s+\"[^\"\n]*\")?\)|\[[^\[\]\n]*\])?"
    r"|<(a|pre|code|script|style)\b[^>]*>.*?</\2\s*>|<[^>\n]+>",
    re.S | re.I | re.M,
)
# A URL may hold balanced parentheses (…/wiki/AI_(disambiguation)); trailing
# sentence punctuation (an apostrophe inside a URL stays, a closing one does not) and an unbalanced ")" stay outside the link. A "(" right
# before a URL is plain text here: Markdown link targets are already in KEEP.
BARE_URL = re.compile(r"(?<![<\[\"'=])https?://(?:[^\s<>()\[\]\"`]|\([^\s<>()\[\]\"`]*\))+")
SOURCES = re.compile(r"^### Källor[ \t]*$.*?(?=^#{1,6} |\Z)", re.M | re.S)


def _link_urls(text):
    def wrap(m):
        url = m.group(0)
        tail = ""
        while url[-1] in ".,;:!?'":
            url, tail = url[:-1], url[-1] + tail
        return f"<{url}>{tail}"
    return BARE_URL.sub(wrap, text)


def _autolink_span(text):
    out, pos = [], 0
    for m in KEEP.finditer(text):
        out.append(_link_urls(text[pos:m.start()]))
        out.append(m.group(0))
        pos = m.end()
    out.append(_link_urls(text[pos:]))
    return "".join(out)


FENCE = re.compile(r"^[ ]{0,3}(```|~~~).*?^[ ]{0,3}\1[^\n]*$", re.M | re.S)


def autolink(text):
    """Wrap bare URLs in <…> in the source list only, outside code, links and HTML.

    A "### Källor" line inside a fenced code block is not a heading, so fenced
    blocks are set aside before the section is looked up and put back unchanged."""
    fences = []

    def hide(m):
        fences.append(m.group(0))
        return f"\0FENCE{len(fences) - 1}\0"

    hidden = FENCE.sub(hide, text)
    linked = SOURCES.sub(lambda m: _autolink_span(m.group(0)), hidden)
    return re.sub(r"\0FENCE(\d+)\0", lambda m: fences[int(m.group(1))], linked)


def yaml_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("--allow-draft", action="store_true", help="accept status other than publicerad (requires --out)")
    ap.add_argument("--out", help="site root to write into (default: this repo)")
    a = ap.parse_args()

    src = pathlib.Path(a.source).resolve()
    if a.allow_draft and not a.out:
        sys.exit("--allow-draft kräver --out: ett utkast skrivs aldrig in i repot")
    out_root = pathlib.Path(a.out).resolve() if a.out else SITE

    problems = []
    fm, body = front_matter(src.read_text(encoding="utf-8"))
    if fm is None:
        problems.append("front matter saknas eller är inte giltig YAML")
        fm = {}
    status = fm.get("status")
    if status != "publicerad" and not a.allow_draft:
        problems.append(f"status är '{status if status is not None else 'saknas'}', inte 'publicerad'")
    pub = fm.get("publiceras")
    if isinstance(pub, str):
        try:
            pub = dt.date.fromisoformat(pub)
        except ValueError:
            pub = None
    if not isinstance(pub, dt.date) or isinstance(pub, dt.datetime):
        pub = None
        problems.append("publiceras: saknas eller är inget datum (ÅÅÅÅ-MM-DD)")

    text = article(body)
    if text is None:
        problems.append(f"avsnittet '{ARTICLE_HEADING}' saknas")
        text = ""

    lines = text.splitlines()
    title_i = next((i for i in outside_fences(lines) if lines[i].startswith("## ")), None)
    title = lines[title_i][3:].strip() if title_i is not None else ""
    if not title:
        problems.append("rubrik (## …) saknas")
    lead = ""
    if title_i is not None:
        for l in lines[title_i + 1:]:
            if l.strip():
                m = re.fullmatch(r"\*(.+)\*", l.strip())
                if m:
                    lead = m.group(1).strip()
                break

    # A "### Källor" or a URL inside fenced code (an example) does not count.
    unfenced = FENCE.sub("", text)
    src_section = SOURCES.search(unfenced)
    if not src_section or not re.search(r"https?://", src_section.group(0)):
        problems.append("'### Källor' med minst en länk saknas")

    problems += forbidden(text, "texten")
    if ENDRAW.search(text):
        problems.append("texten innehåller '{% endraw %}', som inte kan publiceras ordagrant")

    # Only plain inline images ![alt](path) are supported; refuse every other form
    # (titles, reference style, HTML) instead of publishing a broken or unchecked path.
    if len(IMG_START.findall(text)) != len(IMG.findall(text)) or HTML_IMG.search(text):
        problems.append("bild i form som inte stöds: använd bara ![alt](grafik/…) utan titel")

    slug = f"{pub.isocalendar()[0]}-v{pub.isocalendar()[1]:02d}" if pub else "okand"
    images = []
    for alt, path in IMG.findall(text):
        if re.match(r"[a-z]+:", path, re.I) or path.startswith("/"):
            problems.append(f"bilden ligger inte bredvid brevet: {path}")
            continue
        f = (src.parent / path).resolve()
        if not f.is_file():
            problems.append(f"bilden finns inte: {path}")
            continue
        alt_file = f.with_suffix(".alt.txt")
        long_alt = alt_file.read_text(encoding="utf-8").strip() if alt_file.is_file() else alt
        problems += forbidden(long_alt, f"alt-texten för {f.name}")
        # The sidecar text is put inside the raw block too, so it gets the same check.
        if ENDRAW.search(long_alt):
            problems.append(f"alt-texten för {f.name} innehåller '{{% endraw %}}', som inte kan publiceras ordagrant")
        long_alt = " ".join(long_alt.replace("[", "(").replace("]", ")").split())
        images.append((alt, path, f, long_alt))
    # Images are published flat under assets/beyond/<slug>/: two different files with
    # the same name would overwrite each other.
    by_name = {}
    for _, path, f, _ in images:
        if by_name.setdefault(f.name, f) != f:
            problems.append(f"två olika bilder heter {f.name}: byt namn på den ena")

    if problems:
        print(f"{src.name}: publiceras inte.", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        sys.exit(1)

    # Body: drop the title and lead lines (the layout prints them), rewrite image paths.
    body_lines = lines[:title_i] + lines[title_i + 1:]
    body_text = "\n".join(body_lines)
    if lead:
        body_text = body_text.replace(f"*{lead}*", "", 1)
    img_dir = out_root / "assets" / "beyond" / slug
    img_dir.mkdir(parents=True, exist_ok=True)
    cover = None
    for alt, path, f, long_alt in images:
        shutil.copyfile(f, img_dir / f.name)
        web = f"/assets/beyond/{slug}/{f.name}"
        cover = cover or web
        body_text = body_text.replace(f"![{alt}]({path})", f"![{long_alt}]({web})", 1)
    # Bare URLs in the source list become autolinks; the text itself is unchanged.
    body_text = autolink(body_text)
    # No whitespace normalisation: blank lines inside code or HTML are part of the text.
    body_text = body_text.strip("\n") + "\n"
    body_text = "{% raw %}\n" + body_text + "{% endraw %}\n"

    year, week = pub.isocalendar()[0], pub.isocalendar()[1]
    head = [
        "---",
        f"title: {yaml_str(title)}",
        f"lead: {yaml_str(lead)}" if lead else None,
        f"date: {pub.isoformat()}",
        f"year: {year}",
        f"week: {week}",
        f"source: {yaml_str(str(fm.get('vecka', src.stem)))}",
        f"image: {cover}" if cover else None,
        'excerpt_separator: ""',  # no excerpt: it would cut the raw block open
        "---",
        "",
    ]
    out = out_root / "_beyond" / f"{slug}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(h for h in head if h is not None) + body_text, encoding="utf-8")
    print(f"skrev {out.relative_to(out_root)} och {len(images)} bilder i {img_dir.relative_to(out_root)}")


if __name__ == "__main__":
    main()
