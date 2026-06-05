"""
KB Cleanup — fixes HTML entities and junk characters in existing KB files.
Rewrites KB/json/ and KB/markdown/ in-place, then rebuilds the search index.

Run:  python kb_cleanup.py
"""

import re
import json
import html
import pickle
import unicodedata
from pathlib import Path

# Paths are relative to this script's location (works from any clone)
_SCRIPTS_DIR = Path(__file__).resolve().parent
_REPO_ROOT   = _SCRIPTS_DIR.parent
KB   = _REPO_ROOT / "KB"
JSON = KB / "json"
MD   = KB / "markdown"

# ── Character normalisation map ───────────────────────────────────────────────
CHAR_MAP = str.maketrans({
    "’": "'",   # right single quote
    "‘": "'",   # left single quote
    "“": '"',   # left double quote
    "”": '"',   # right double quote
    "–": "-",   # en-dash
    "—": "--",  # em-dash
    "•": "*",   # bullet
    "·": ".",   # middle dot
    " ": " ",   # non-breaking space
    "…": "...", # ellipsis
    "×": "x",   # multiplication sign
    "°": " deg",# degree sign
    "�": "",    # replacement char (the ? boxes)
    "​": "",    # zero-width space
})


def clean(text: str) -> str:
    if not text:
        return text
    # decode HTML entities: &ndash; &#8211; &amp; etc.
    text = html.unescape(text)
    # apply char map
    text = text.translate(CHAR_MAP)
    # collapse multiple blank lines (incl. lines that are all whitespace)
    text = re.sub(r"(\n\s*){3,}", "\n\n", text)
    # strip trailing spaces per line
    text = "\n".join(line.rstrip() for line in text.splitlines())
    return text.strip()


def clean_code(code: str) -> str:
    """Fix source-level line-wraps inside code blocks.

    The HTML source sometimes wraps long lines with a bare newline inside
    <p class='SourceCode'>. E.g.:
        Jump \\n pick
    The <br> tag is the real line break; the bare \\n is just editor wrapping.
    Pattern: a line that follows \\n and starts with exactly one space then
    a non-space character is a continuation of the previous line.
    """
    if not code:
        return code
    # join continuation lines: bare \n followed by one space then non-space
    # e.g.  "Jump\n pick"  ->  "Jump pick"
    code = re.sub(r"\n (\S)", r" \1", code)
    # also handle trailing-space wrap: "Jump \n pick" -> "Jump pick"
    code = re.sub(r" \n ([^ \t])", r" \1", code)
    return code


def clean_record(rec: dict) -> dict:
    str_fields = ["title", "syntax", "parameters", "description", "notes", "see_also"]
    for f in str_fields:
        if f in rec:
            rec[f] = clean(clean_code(rec[f]))
    if "examples" in rec:
        rec["examples"] = [clean(clean_code(ex)) for ex in rec["examples"]]
    return rec


def record_to_markdown(rec: dict) -> str:
    lines = [f"# {rec['title']}", f"**Type:** {rec['type']} | **Section:** {rec['section']}", ""]
    if rec.get("syntax"):
        lines += ["## Syntax", "```", rec["syntax"], "```", ""]
    if rec.get("parameters"):
        lines += ["## Parameters", rec["parameters"], ""]
    if rec.get("description"):
        lines += ["## Description", rec["description"], ""]
    if rec.get("notes"):
        lines += ["## Notes", rec["notes"], ""]
    if rec.get("examples"):
        lines.append("## Examples")
        for ex in rec["examples"]:
            lines += ["```spel", ex, "```", ""]
    if rec.get("see_also"):
        lines += ["## See Also", rec["see_also"], ""]
    return "\n".join(lines)


def main():
    json_files = list(JSON.rglob("*.json"))
    print(f"Cleaning {len(json_files)} JSON records...")

    all_records = []
    for jf in json_files:
        rec = json.loads(jf.read_text(encoding="utf-8"))
        rec = clean_record(rec)
        jf.write_text(json.dumps(rec, ensure_ascii=False, indent=2), encoding="utf-8")

        # rewrite matching markdown
        # json path:     KB/json/Section/name.json
        # markdown path: KB/markdown/Section/name.md
        rel = jf.relative_to(JSON)
        md_path = MD / rel.with_suffix(".md")
        if md_path.exists():
            md_path.write_text(record_to_markdown(rec), encoding="utf-8")

        all_records.append(rec)

    print(f"  Done. Rewriting combined operator KB...")

    # rewrite combined single-file KB
    operator_records = sorted(
        [r for r in all_records if r["section"] == "Operator"],
        key=lambda r: r["title"]
    )
    combined = KB / "spel_operator_kb.md"
    with combined.open("w", encoding="utf-8") as f:
        f.write("# EPSON SPEL+ Operator Command Reference\n\n")
        for rec in operator_records:
            f.write(record_to_markdown(rec))
            f.write("\n\n---\n\n")

    # rewrite index
    index = [{"title": r["title"], "file": r["file"], "section": r["section"], "type": r["type"]}
             for r in all_records]
    (KB / "spel_kb_index.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # rebuild BM25 search index
    print("  Rebuilding search index...")

    TOKEN_RE = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]*")
    import math
    from collections import Counter

    def tokenize(text):
        return [t.lower() for t in TOKEN_RE.findall(text or "")]

    def searchable(rec):
        t = rec.get("title", "")
        return " ".join([t, t, t,
                         rec.get("syntax", ""),
                         rec.get("parameters", ""),
                         rec.get("description", ""),
                         rec.get("notes", ""),
                         " ".join(rec.get("examples", []) or [])])

    docs_tokens = [tokenize(searchable(r)) for r in all_records]
    df = Counter()
    for toks in docs_tokens:
        for t in set(toks):
            df[t] += 1

    N = len(all_records)
    avgdl = sum(len(t) for t in docs_tokens) / max(N, 1)
    idf = {t: math.log(1 + (N - n + 0.5) / (n + 0.5)) for t, n in df.items()}

    pkl_index = {
        "records": all_records,
        "doc_tf":  [Counter(t) for t in docs_tokens],
        "doc_len": [len(t) for t in docs_tokens],
        "idf":     idf,
        "avgdl":   avgdl,
        "N":       N,
    }
    (KB / "spel_search_index.pkl").write_bytes(pickle.dumps(pkl_index))

    print(f"All done.")
    print(f"  JSON/MD files cleaned: {len(json_files)}")
    print(f"  Combined KB:           {combined.stat().st_size // 1024} KB")
    print(f"  Search index:          {(KB / 'spel_search_index.pkl').stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
