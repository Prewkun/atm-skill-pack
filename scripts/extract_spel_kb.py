"""
EPSON SPEL+ Manual → Markdown Knowledge Base Extractor
Parses Operator/Program HTML reference files into clean .md files
"""

import os
import re
import json
from pathlib import Path
from html.parser import HTMLParser

# ── Config ────────────────────────────────────────────────────────────────────
# Paths are relative to this script's location (works from any clone)
_SCRIPTS_DIR = Path(__file__).resolve().parent
_REPO_ROOT   = _SCRIPTS_DIR.parent

# Place the EPSON manual at <repo>/Manual/English/
BASE = _REPO_ROOT / "Manual" / "English"
SOURCES = {
    "Operator": BASE / "Operator" / "Content" / "html",
    "Program":  BASE / "Program"  / "Content" / "html",
}
OUT_MD   = _REPO_ROOT / "KB" / "markdown"
OUT_JSON = _REPO_ROOT / "KB" / "json"
OUT_MD.mkdir(parents=True, exist_ok=True)
OUT_JSON.mkdir(parents=True, exist_ok=True)

# ── HTML → plain text parser ──────────────────────────────────────────────────
class TextExtractor(HTMLParser):
    SKIP_TAGS = {"script", "style"}

    def __init__(self):
        super().__init__()
        self.parts: list[str] = []
        self._skip = 0
        self._cur_class = ""
        self._in_td = False
        self._td_buf: list[str] = []
        self._row: list[str] = []
        self._table_rows: list[list[str]] = []

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag in self.SKIP_TAGS:
            self._skip += 1
            return
        attrs_d = dict(attrs)
        cls = attrs_d.get("class", "")
        if cls:
            self._cur_class = cls
        if tag == "td":
            self._in_td = True
            self._td_buf = []
        elif tag == "tr":
            self._row = []
        elif tag in ("br", "p"):
            if self._in_td:
                self._td_buf.append("\n")
            else:
                self.parts.append("\n")

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in self.SKIP_TAGS:
            self._skip -= 1
            return
        if tag == "td":
            self._in_td = False
            self._row.append("".join(self._td_buf).strip())
        elif tag == "tr":
            if self._row:
                self._table_rows.append(self._row[:])
                self.parts.append("\t".join(self._row) + "\n")
            self._row = []

    def handle_data(self, data):
        if self._skip:
            return
        if self._in_td:
            self._td_buf.append(data)
        else:
            self.parts.append(data)

    def get_text(self):
        return "".join(self.parts)


# ── Section splitter ──────────────────────────────────────────────────────────
SECTION_HEADINGS = [
    "Syntax", "Parameters", "Description", "Notes", "See Also",
    "Example", "Remarks", "Return Value", "Usage", "Errors",
]

def split_sections(raw: str) -> dict:
    """Split flat text into labelled sections."""
    sections: dict[str, list[str]] = {"_body": []}
    cur = "_body"
    for line in raw.splitlines():
        stripped = line.strip()
        matched = next((h for h in SECTION_HEADINGS if stripped.lower().startswith(h.lower())), None)
        if matched and len(stripped) < len(matched) + 20:
            cur = matched
            sections.setdefault(cur, [])
        else:
            sections.setdefault(cur, []).append(line)
    return {k: "\n".join(v).strip() for k, v in sections.items() if v}


def extract_code_blocks(raw_html: str) -> list[str]:
    """Pull <p class='SourceCode'> content as code examples."""
    pattern = re.compile(
        r'class=["\']SourceCode["\'][^>]*>(.*?)</p>',
        re.DOTALL | re.IGNORECASE,
    )
    blocks = []
    for m in pattern.finditer(raw_html):
        inner = m.group(1)
        # <br> and <br /> are intentional line breaks — convert first
        inner = re.sub(r"<br\s*/?>", "\n", inner, flags=re.IGNORECASE)
        # bare \n inside the HTML source are just editor line-wraps — join them
        inner = re.sub(r"[ \t]*\n[ \t]*(?=\S)", " ", inner)
        # strip remaining tags
        code = re.sub(r"<[^>]+>", "", inner)
        # decode HTML entities
        code = (code.replace("&#160;", " ").replace("\xa0", " ")
                    .replace("&amp;", "&").replace("&quot;", '"')
                    .replace("&lt;", "<").replace("&gt;", ">")
                    .replace("&ndash;", "-").replace("&mdash;", "--"))
        # collapse runs of spaces (but keep indentation intent)
        code = re.sub(r"[ \t]{2,}", "  ", code)
        # collapse excess blank lines
        code = re.sub(r"\n{3,}", "\n\n", code)
        code = code.strip()
        if code:
            blocks.append(code)
    return blocks


def extract_title(raw_html: str) -> str:
    m = re.search(r"<title>(.*?)</title>", raw_html, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(r'class=["\']MainTopic["\'][^>]*>(.*?)</p>', raw_html, re.IGNORECASE | re.DOTALL)
    if m:
        return re.sub(r"<[^>]+>", "", m.group(1)).strip()
    return ""


# ── Main conversion ───────────────────────────────────────────────────────────
def html_to_record(path: Path, section: str) -> dict | None:
    try:
        raw = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return None

    title = extract_title(raw)
    if not title:
        return None

    # plain text
    parser = TextExtractor()
    parser.feed(raw)
    plain = parser.get_text()

    # clean noise
    plain = re.sub(r"\n{3,}", "\n\n", plain)
    plain = plain.replace("\xa0", " ").strip()

    sections = split_sections(plain)
    code_blocks = extract_code_blocks(raw)

    # determine command type from filename
    fname = path.stem
    cmd_type = "statement" if fname.endswith("_stmt") or fname.endswith("_Statement") else \
               "function"  if fname.endswith("_func") or fname.endswith("_Function") else \
               "property"  if fname.endswith("_Property") else \
               "result"    if fname.endswith("_Result") else \
               "reference"

    return {
        "title":       title,
        "file":        fname,
        "section":     section,
        "type":        cmd_type,
        "syntax":      sections.get("Syntax", ""),
        "parameters":  sections.get("Parameters", ""),
        "description": sections.get("Description", sections.get("_body", "")),
        "notes":       sections.get("Notes", sections.get("Remarks", "")),
        "see_also":    sections.get("See Also", ""),
        "examples":    code_blocks,
    }


def record_to_markdown(rec: dict) -> str:
    lines = [f"# {rec['title']}", f"**Type:** {rec['type']} | **Section:** {rec['section']}", ""]

    if rec["syntax"]:
        lines += ["## Syntax", "```", rec["syntax"], "```", ""]

    if rec["parameters"]:
        lines += ["## Parameters", rec["parameters"], ""]

    if rec["description"]:
        lines += ["## Description", rec["description"], ""]

    if rec["notes"]:
        lines += ["## Notes", rec["notes"], ""]

    if rec["examples"]:
        lines.append("## Examples")
        for ex in rec["examples"]:
            lines += ["```spel", ex, "```", ""]

    if rec["see_also"]:
        lines += ["## See Also", rec["see_also"], ""]

    return "\n".join(lines)


# ── Run ───────────────────────────────────────────────────────────────────────
def main():
    all_records = []
    total = 0
    skipped = 0

    for section, html_dir in SOURCES.items():
        if not html_dir.exists():
            print(f"[WARN] Not found: {html_dir}")
            continue

        htm_files = list(html_dir.glob("*.htm")) + list(html_dir.glob("*.html"))
        print(f"\n[{section}] Processing {len(htm_files)} files...")

        for path in htm_files:
            rec = html_to_record(path, section)
            if not rec:
                skipped += 1
                continue

            # write markdown
            md_path = OUT_MD / section / f"{path.stem}.md"
            md_path.parent.mkdir(parents=True, exist_ok=True)
            md_path.write_text(record_to_markdown(rec), encoding="utf-8")

            # write json
            json_path = OUT_JSON / section / f"{path.stem}.json"
            json_path.parent.mkdir(parents=True, exist_ok=True)
            json_path.write_text(json.dumps(rec, ensure_ascii=False, indent=2), encoding="utf-8")

            all_records.append(rec)
            total += 1

        print(f"  -> {total} converted, {skipped} skipped so far")

    # write combined index JSON
    index_path = Path(r"E:\Claude\Epson e-manual project\KB") / "spel_kb_index.json"
    index = [{"title": r["title"], "file": r["file"], "section": r["section"], "type": r["type"]} for r in all_records]
    index_path.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")

    # write combined single-file KB (Operator only — fits in context window)
    operator_records = [r for r in all_records if r["section"] == "Operator"]
    combined_path = Path(r"E:\Claude\Epson e-manual project\KB") / "spel_operator_kb.md"
    with combined_path.open("w", encoding="utf-8") as f:
        f.write("# EPSON SPEL+ Operator Command Reference\n\n")
        for rec in sorted(operator_records, key=lambda r: r["title"]):
            f.write(record_to_markdown(rec))
            f.write("\n\n---\n\n")

    print(f"\nDone: {total} files -> KB/markdown + KB/json")
    print(f"Combined operator reference -> KB/spel_operator_kb.md")
    print(f"Index -> KB/spel_kb_index.json")


if __name__ == "__main__":
    main()
