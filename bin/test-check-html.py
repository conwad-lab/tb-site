"""Check home-page doctype enforcement using temporary HTML files."""
from pathlib import Path
import subprocess
import sys
import tempfile


checker = Path(__file__).resolve().parents[1] / ".github/scripts/check_html.py"
failed = 0
with tempfile.TemporaryDirectory() as temp_dir:
    root = Path(temp_dir)
    for path, front_matter, language in (
        ("index.html", "---\n---\n", "en"),
        ("sv/index.html", "---\npermalink: /sv/\n---\n", "sv"),
    ):
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        html = f'<html lang="{language}">\n<title>t</title>\n</html>\n'
        for doctype, expected in (("", 1), ("<!doctype html>\n", 0)):
            target.write_text(front_matter + doctype + html, encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(checker), path],
                cwd=temp_dir, capture_output=True, text=True,
            )
            if result.returncode != expected or (
                expected == 1 and "missing <!doctype html>" not in result.stdout
            ):
                state = "with" if doctype else "without"
                print(f"{path} {state} doctype: expected exit {expected}"
                      f" and the required diagnostic; got {result.returncode},"
                      f" stdout={result.stdout!r}, stderr={result.stderr!r}")
                failed += 1

    (root / "other.html").write_text(
        '<html lang="en">\n<title>t</title>\n</html>\n', encoding="utf-8",
    )
    result = subprocess.run(
        [sys.executable, str(checker), "other.html"],
        cwd=temp_dir, capture_output=True, text=True,
    )
    if result.returncode != 0:
        print(f"other.html without doctype: expected exit 0; got {result.returncode},"
              f" stdout={result.stdout!r}, stderr={result.stderr!r}")
        failed += 1

sys.exit(1 if failed else 0)
