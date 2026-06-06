"""
SPEL+ KB Search — zero-dependency BM25 retrieval over the extracted KB.

Usage:
    python spel_search.py "pick and place jump motion"           # search
    python spel_search.py "set speed before motion" -n 10       # top 10 results
    python spel_search.py "palletizing" --context               # full AI context pack
    python spel_search.py "jump" --section Operator             # Operator section only
    python spel_search.py "jump" --section all                  # all sections (shows dupes)
    python spel_search.py --build                               # (re)build the index

The --context flag prints a ready-to-paste block you can feed to any AI
("here is the relevant SPEL+ reference, now write me ...").

Default --section is Program, which filters out the ~309 exact duplicate records
that also exist in the Operator section.
"""

import os
import re
import sys
import json
import math
import pickle
import argparse
from pathlib import Path
from collections import Counter, defaultdict

# Force UTF-8 output on Windows terminals
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Paths are relative to this script's location (works from any clone)
_SCRIPTS_DIR = Path(__file__).resolve().parent
_REPO_ROOT   = _SCRIPTS_DIR.parent
KB_ROOT   = _REPO_ROOT / "KB"
JSON_DIR  = KB_ROOT / "json"
INDEX_PKL = KB_ROOT / "spel_search_index.pkl"

TOKEN_RE = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]*")


def tokenize(text: str) -> list[str]:
    return [t.lower() for t in TOKEN_RE.findall(text or "")]


def _trunc(text: str, limit: int) -> str:
    """Truncate to limit chars, appending … when cut."""
    if not text:
        return ""
    return text[:limit] + ("…" if len(text) > limit else "")


# ── Folder-index metadata cache (for category/toc_chapter inheritance) ─────────
_folder_meta_cache: dict[Path, dict] = {}

def _folder_meta(dirpath: Path) -> dict:
    """Return the _folder.json metadata for a directory, cached."""
    if dirpath not in _folder_meta_cache:
        fp = dirpath / "_folder.json"
        if fp.exists():
            try:
                _folder_meta_cache[dirpath] = json.loads(fp.read_text(encoding="utf-8"))
            except Exception:
                _folder_meta_cache[dirpath] = {}
        else:
            _folder_meta_cache[dirpath] = {}
    return _folder_meta_cache[dirpath]


# ── Index building ────────────────────────────────────────────────────────────
def load_records() -> list[dict]:
    records = []
    for jf in JSON_DIR.rglob("*.json"):
        try:
            rec = json.loads(jf.read_text(encoding="utf-8"))
            if rec.get("type") == "folder_index":
                continue
            rec["_path"] = str(jf)

            # Inherit category and toc_chapter from parent _folder.json if not set
            meta = _folder_meta(jf.parent)
            if meta:
                if not rec.get("category") and meta.get("category"):
                    rec["category"] = meta["category"]
                if not rec.get("toc_chapter") and meta.get("toc_chapter"):
                    rec["toc_chapter"] = meta["toc_chapter"]

            records.append(rec)
        except Exception:
            pass
    return records


def record_searchable_text(rec: dict) -> str:
    """Weight title heavily by repeating it."""
    title = rec.get("title", "")
    parts = [
        title, title, title,                      # 3x title weight
        rec.get("syntax", ""),
        rec.get("parameters", ""),
        rec.get("description", ""),
        rec.get("notes", ""),
        " ".join(rec.get("examples", []) or []),
    ]
    return " ".join(parts)


def build_index():
    print("Loading records...")
    records = load_records()
    print(f"  {len(records)} records")

    docs_tokens = []
    df = Counter()                       # document frequency
    for rec in records:
        toks = tokenize(record_searchable_text(rec))
        docs_tokens.append(toks)
        for t in set(toks):
            df[t] += 1

    N = len(records)
    avgdl = sum(len(t) for t in docs_tokens) / max(N, 1)

    # precompute term frequencies per doc
    doc_tf   = [Counter(t) for t in docs_tokens]
    doc_len  = [len(t) for t in docs_tokens]

    idf = {t: math.log(1 + (N - n + 0.5) / (n + 0.5)) for t, n in df.items()}

    index = {
        "records": [{k: v for k, v in r.items()} for r in records],
        "doc_tf":  doc_tf,
        "doc_len": doc_len,
        "idf":     idf,
        "avgdl":   avgdl,
        "N":       N,
    }
    INDEX_PKL.write_bytes(pickle.dumps(index))
    print(f"Index built -> {INDEX_PKL}  ({INDEX_PKL.stat().st_size // 1024} KB)")
    return index


def load_index():
    if not INDEX_PKL.exists():
        return build_index()
    return pickle.loads(INDEX_PKL.read_bytes())


# ── Search (BM25) ─────────────────────────────────────────────────────────────
def search(index: dict, query: str, n: int = 5, section: str = "Program",
           k1: float = 1.5, b: float = 0.75):
    """
    BM25 search over the KB.

    section: "Program" (default) | "Operator" | "all"
        "Program" filters out Operator duplicates for clean programming results.
        "all" returns results from every section.
    """
    q_tokens = tokenize(query)
    idf, avgdl = index["idf"], index["avgdl"]
    doc_tf, doc_len = index["doc_tf"], index["doc_len"]

    scores = []
    for i in range(index["N"]):
        rec = index["records"][i]
        if section != "all" and rec.get("section", "") != section:
            continue
        tf, dl = doc_tf[i], doc_len[i]
        s = 0.0
        for qt in q_tokens:
            if qt not in tf:
                continue
            f = tf[qt]
            denom = f + k1 * (1 - b + b * dl / avgdl)
            s += idf.get(qt, 0.0) * (f * (k1 + 1)) / denom
        if s > 0:
            scores.append((s, i))

    scores.sort(reverse=True)
    return [(index["records"][i], sc) for sc, i in scores[:n]]


# ── Output ────────────────────────────────────────────────────────────────────
def format_result_brief(rec, score):
    cat      = rec.get("category", "")
    chapter  = rec.get("toc_chapter", "")
    tag_parts = [p for p in [chapter, cat] if p]
    tag = f" [{' · '.join(tag_parts)}]" if tag_parts else ""
    return f"  [{score:5.1f}] {rec['title']:<40} ({rec['section']}/{rec['type']}){tag}"


def format_context_pack(results, query):
    out = [f"## SPEL+ reference for: \"{query}\"\n"]
    for rec, score in results:
        cat     = rec.get("category", "")
        chapter = rec.get("toc_chapter", "")
        meta_parts = [p for p in [chapter, cat] if p]
        meta = f" *({', '.join(meta_parts)})*" if meta_parts else ""
        out.append(f"### {rec['title']}{meta}")

        if rec.get("syntax"):
            out.append(f"**Syntax:**\n```\n{rec['syntax']}\n```")

        if rec.get("parameters"):
            out.append(f"**Parameters:** {_trunc(rec['parameters'], 1500)}")

        if rec.get("description"):
            out.append(f"**Description:** {_trunc(rec['description'], 2000)}")

        if rec.get("notes"):
            out.append(f"**Notes:** {_trunc(rec['notes'], 600)}")

        examples = rec.get("examples") or []
        for ex in examples[:2]:
            out.append("**Example:**\n```spel\n" + _trunc(ex, 1200) + "\n```")

        if rec.get("see_also"):
            out.append(f"**See Also:** {_trunc(rec['see_also'], 400)}")

        out.append("")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description="Search the EPSON SPEL+ KB")
    ap.add_argument("query", nargs="*", help="search terms")
    ap.add_argument("-n", type=int, default=5, help="number of results")
    ap.add_argument("--context", action="store_true", help="print full AI context pack")
    ap.add_argument("--build",   action="store_true", help="rebuild the index")
    ap.add_argument(
        "--section",
        choices=["Program", "Operator", "all"],
        default="Program",
        help="filter by section (default: Program — excludes Operator duplicates)",
    )
    args = ap.parse_args()

    if args.build:
        build_index()
        if not args.query:
            return

    index = load_index()

    if not args.query:
        print("Provide a query, e.g.:  python spel_search.py \"pick and place jump\"")
        return

    query = " ".join(args.query)
    results = search(index, query, n=args.n, section=args.section)

    if not results:
        print(f"No matches for: {query}")
        return

    if args.context:
        print(format_context_pack(results, query))
    else:
        print(f"\nTop {len(results)} matches for: \"{query}\"  [section={args.section}]\n")
        for rec, score in results:
            print(format_result_brief(rec, score))
        print(f"\nTip: add --context to get the full AI-ready reference pack.")


if __name__ == "__main__":
    main()
