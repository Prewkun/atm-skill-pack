"""
SPEL+ KB Search — zero-dependency BM25 retrieval over the extracted KB.

Usage:
    python spel_search.py "pick and place jump motion"      # search
    python spel_search.py "set speed before motion" -n 8    # top 8 results
    python spel_search.py "palletizing" --context           # print full context pack
    python spel_search.py --build                            # (re)build the index

The --context flag prints a ready-to-paste block you can feed to any AI
("here is the relevant SPEL+ reference, now write me ...").
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


# ── Index building ────────────────────────────────────────────────────────────
def load_records() -> list[dict]:
    records = []
    for jf in JSON_DIR.rglob("*.json"):
        try:
            rec = json.loads(jf.read_text(encoding="utf-8"))
            rec["_path"] = str(jf)
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
def search(index: dict, query: str, n: int = 5, k1: float = 1.5, b: float = 0.75):
    q_tokens = tokenize(query)
    idf, avgdl = index["idf"], index["avgdl"]
    doc_tf, doc_len = index["doc_tf"], index["doc_len"]

    scores = []
    for i in range(index["N"]):
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
    return f"  [{score:5.1f}] {rec['title']:<35} ({rec['section']}/{rec['type']})"


def format_context_pack(results, query):
    out = [f"## SPEL+ reference for: \"{query}\"\n"]
    for rec, score in results:
        out.append(f"### {rec['title']}")
        if rec.get("syntax"):
            out.append(f"**Syntax:**\n```\n{rec['syntax']}\n```")
        if rec.get("parameters"):
            out.append(f"**Parameters:** {rec['parameters'][:500]}")
        if rec.get("description"):
            out.append(f"**Description:** {rec['description'][:600]}")
        if rec.get("examples"):
            out.append("**Example:**\n```spel\n" + (rec["examples"][0][:600]) + "\n```")
        out.append("")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description="Search the EPSON SPEL+ KB")
    ap.add_argument("query", nargs="*", help="search terms")
    ap.add_argument("-n", type=int, default=5, help="number of results")
    ap.add_argument("--context", action="store_true", help="print full AI context pack")
    ap.add_argument("--build", action="store_true", help="rebuild the index")
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
    results = search(index, query, n=args.n)

    if not results:
        print(f"No matches for: {query}")
        return

    if args.context:
        print(format_context_pack(results, query))
    else:
        print(f"\nTop {len(results)} matches for: \"{query}\"\n")
        for rec, score in results:
            print(format_result_brief(rec, score))
        print(f"\nTip: add --context to get the full AI-ready reference pack.")


if __name__ == "__main__":
    main()
