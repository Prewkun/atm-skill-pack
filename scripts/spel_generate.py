"""
SPEL+ Code Generator
Search the KB for relevant commands, then call Claude to write correct SPEL+ code.

Usage:
    python spel_generate.py "pick and place routine for 3 parts"
    python spel_generate.py "palletizing 4x3 grid" --top 8
    python spel_generate.py "conveyor tracking with vision" --save output.prg
    python spel_generate.py "error handling and recovery" --dry-run   (show context only, no API call)

Requires:
    ANTHROPIC_API_KEY environment variable  (or add to .env file in this folder)
"""

import os
import re
import sys
import json
import math
import pickle
import argparse
from pathlib import Path
from collections import Counter

# Force UTF-8 output on Windows terminals
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ── Paths ─────────────────────────────────────────────────────────────────────
ROOT     = Path(__file__).parent
KB       = ROOT / "KB"
INDEX_PKL = KB / "spel_search_index.pkl"

# ── Load .env if present ──────────────────────────────────────────────────────
env_file = ROOT / ".env"
if env_file.exists():
    for line in env_file.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

# ── BM25 search (copied from spel_search.py — no import dependency) ───────────
TOKEN_RE = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]*")

def tokenize(text: str) -> list[str]:
    return [t.lower() for t in TOKEN_RE.findall(text or "")]

def bm25_search(index: dict, query: str, n: int = 6,
                k1: float = 1.5, b: float = 0.75) -> list[tuple[dict, float]]:
    q_tokens = tokenize(query)
    idf, avgdl = index["idf"], index["avgdl"]
    doc_tf, doc_len = index["doc_tf"], index["doc_len"]
    scores = []
    for i in range(index["N"]):
        tf, dl = doc_tf[i], doc_len[i]
        s = sum(
            idf.get(qt, 0.0) * (tf[qt] * (k1 + 1))
            / (tf[qt] + k1 * (1 - b + b * dl / avgdl))
            for qt in q_tokens if qt in tf
        )
        if s > 0:
            scores.append((s, i))
    scores.sort(reverse=True)
    return [(index["records"][i], sc) for sc, i in scores[:n]]

def load_index() -> dict:
    if not INDEX_PKL.exists():
        print("Search index not found. Run:  python spel_search.py --build")
        sys.exit(1)
    return pickle.loads(INDEX_PKL.read_bytes())

# ── Context builder ───────────────────────────────────────────────────────────
def build_context(results: list[tuple[dict, float]]) -> str:
    parts = []
    for rec, score in results:
        block = [f"### {rec['title']}  [{rec['section']}]"]
        if rec.get("syntax"):
            block.append(f"**Syntax:**\n```\n{rec['syntax']}\n```")
        if rec.get("parameters"):
            # truncate long param lists
            p = rec["parameters"]
            block.append(f"**Parameters:**\n{p[:600]}{'...' if len(p)>600 else ''}")
        if rec.get("description"):
            d = rec["description"]
            block.append(f"**Description:**\n{d[:500]}{'...' if len(d)>500 else ''}")
        if rec.get("notes"):
            n = rec["notes"]
            block.append(f"**Notes:**\n{n[:300]}{'...' if len(n)>300 else ''}")
        if rec.get("examples"):
            block.append(f"**Example:**\n```spel\n{rec['examples'][0][:400]}\n```")
        parts.append("\n".join(block))
    return "\n\n---\n\n".join(parts)

# ── System prompt ─────────────────────────────────────────────────────────────
SYSTEM_PROMPT = """You are an expert EPSON robot programmer specialising in SPEL+ (Seiko Epson Programming Language Plus).

Rules you MUST follow:
1. Always set Speed and Accel before any motion command (Go, Jump, Move, Arc).
2. Use Jump for pick-and-place; use Go for direct PTP; use Move for linear paths.
3. Declare all variables at the top of each Function.
4. Use meaningful point names (P1, P2 or named labels like pick, place, home).
5. Add comments with ' to explain non-obvious logic.
6. Every Function ends with Fend; every program entry point is Function main.
7. Use On/Off for digital outputs; Wait for timing; If/Then/Else for logic.
8. Use Xqt to start parallel tasks; use Semaphore for shared-resource protection.
9. Handle errors with TrapErr / ErrCode where appropriate.
10. Only use commands from the provided SPEL+ reference — never invent syntax.

Output ONLY valid SPEL+ source code with comments. No prose outside code comments."""

# ── Main ──────────────────────────────────────────────────────────────────────
def generate(task: str, top: int = 6, dry_run: bool = False,
             save: str | None = None, verbose: bool = False):

    print(f"\nTask: {task}")
    print(f"Searching KB (top {top} references)...")

    index = load_index()
    results = bm25_search(index, task, n=top)

    if verbose:
        print("\nMatched references:")
        for rec, sc in results:
            print(f"  [{sc:5.1f}] {rec['title']:<40} ({rec['section']})")

    context = build_context(results)

    user_message = f"""Using the SPEL+ reference below, write a complete, robot-safe SPEL+ program for:

**Task:** {task}

--- SPEL+ REFERENCE ---
{context}
--- END REFERENCE ---

Write the full program now:"""

    if dry_run:
        print("\n" + "="*60)
        print("DRY RUN — context pack that would be sent to Claude:")
        print("="*60)
        print(user_message)
        # also copy to clipboard if pyperclip available
        try:
            import subprocess
            subprocess.run("clip", input=user_message.encode("utf-8"), check=True)
            print("\n[Context pack copied to clipboard — paste into Claude!]")
        except Exception:
            pass
        return

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("\nERROR: ANTHROPIC_API_KEY not set.")
        print("Add it to a .env file in this folder:  ANTHROPIC_API_KEY=sk-ant-...")
        sys.exit(1)

    try:
        import anthropic
    except ImportError:
        print("ERROR: anthropic package not installed.  pip install anthropic")
        sys.exit(1)

    print("Calling Claude...")
    client = anthropic.Anthropic(api_key=api_key)

    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}],
    )

    code = response.content[0].text

    print("\n" + "="*60)
    print("Generated SPEL+ Program:")
    print("="*60)
    print(code)

    if save:
        out = Path(save)
        out.write_text(code, encoding="utf-8")
        print(f"\nSaved to: {out.resolve()}")

    # usage summary
    u = response.usage
    print(f"\n[Tokens: in={u.input_tokens}  out={u.output_tokens}]")
    return code


def main():
    ap = argparse.ArgumentParser(description="Generate SPEL+ code from a natural-language task")
    ap.add_argument("task", nargs="+", help="What the robot should do")
    ap.add_argument("--top",     type=int, default=6,  help="KB references to retrieve (default 6)")
    ap.add_argument("--dry-run", action="store_true",  help="Print context pack, skip API call")
    ap.add_argument("--save",    type=str, default=None, help="Save output to file")
    ap.add_argument("--verbose", action="store_true",  help="Show matched KB entries")
    args = ap.parse_args()

    generate(
        task=" ".join(args.task),
        top=args.top,
        dry_run=args.dry_run,
        save=args.save,
        verbose=args.verbose,
    )

if __name__ == "__main__":
    main()
