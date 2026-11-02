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


def front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.split("#", 1)[0].strip()
    return fm, text[m.end():]


def article(body):
    lines = body.splitlines()
    try:
        start = lines.index(ARTICLE_HEADING) + 1
    except ValueError:
        return None
    out = []
    for line in lines[start:]:
        if line.startswith("# "):
            break
        out.append(line)
    while out and out[-1].strip() in ("", "---"):
        out.pop()
    return "\n".join(out).strip("\n")


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
    status = fm.get("status", "")
    if status != "publicerad" and not a.allow_draft:
        problems.append(f"status är '{status or 'saknas'}', inte 'publicerad'")
    try:
        pub = dt.date.fromisoformat(fm.get("publiceras", ""))
    except ValueError:
        pub = None
        problems.append("publiceras: saknas eller är inget datum (ÅÅÅÅ-MM-DD)")

    text = article(body)
    if text is None:
        problems.append(f"avsnittet '{ARTICLE_HEADING}' saknas")
        text = ""

    lines = text.splitlines()
    title_i = next((i for i, l in enumerate(lines) if l.startswith("## ")), None)
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

    src_section = re.search(r"^### Källor\s*$(.*)", text, re.M | re.S)
    if not src_section or not re.search(r"https?://", src_section.group(1)):
        problems.append("'### Källor' med minst en länk saknas")

    for needle, what in FORBIDDEN:
        if needle in text:
            problems.append(f"internt material i texten: {what} ('{needle}')")

    slug = f"{pub.isocalendar()[0]}-v{pub.isocalendar()[1]:02d}" if pub else "okand"
    images = []
    for alt, path in IMG.findall(text):
        if re.match(r"https?://", path):
            continue
        f = (src.parent / path).resolve()
        if not f.is_file():
            problems.append(f"bilden finns inte: {path}")
            continue
        alt_file = f.with_suffix(".alt.txt")
        long_alt = alt_file.read_text(encoding="utf-8").strip() if alt_file.is_file() else alt
        long_alt = " ".join(long_alt.replace("[", "(").replace("]", ")").split())
        images.append((alt, path, f, long_alt))

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
    # Bare URLs (the source list) become autolinks; the text itself is unchanged.
    body_text = re.sub(r"(?<![(<\[])(https?://[^\s<>)]+[^\s<>).,;:])", r"<\1>", body_text)
    body_text = re.sub(r"\n{3,}", "\n\n", body_text).strip() + "\n"

    year, week = pub.isocalendar()[0], pub.isocalendar()[1]
    head = [
        "---",
        f"title: {yaml_str(title)}",
        f"lead: {yaml_str(lead)}" if lead else None,
        f"date: {pub.isoformat()}",
        f"year: {year}",
        f"week: {week}",
        f"source: {yaml_str(fm.get('vecka', src.stem))}",
        f"image: {cover}" if cover else None,
        "---",
        "",
    ]
    out = out_root / "_beyond" / f"{slug}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(h for h in head if h is not None) + body_text, encoding="utf-8")
    print(f"skrev {out.relative_to(out_root)} och {len(images)} bilder i {img_dir.relative_to(out_root)}")


if __name__ == "__main__":
    main()
