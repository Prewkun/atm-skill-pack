"""
Reclassify files in KB/json/*/Misc/ into their proper TOC-chapter folders.

Rules applied in order (first match wins). Based on title + description keywords.

Usage:
    python reclassify_misc.py           # dry-run — preview only
    python reclassify_misc.py --apply   # execute moves + regenerate _folder.json + rebuild index
"""

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

_SCRIPTS_DIR = Path(__file__).resolve().parent
_REPO_ROOT   = _SCRIPTS_DIR.parent
KB_ROOT      = _REPO_ROOT / "KB"
JSON_DIR     = KB_ROOT / "json"


# ── Classification rules ──────────────────────────────────────────────────────
# Each rule: (target_chapter_folder, predicate(title, description, rec))
# First matching rule wins.

def _contains(text: str, *terms: str) -> bool:
    t = text.lower()
    return any(term.lower() in t for term in terms)


RULES: list[tuple[str, callable]] = [
    # GUI Builder — already tagged category == gui_control
    ("GUI_Builder", lambda title, desc, rec:
        rec.get("category") == "gui_control"),

    # Conveyor Tracking — Cnv_ prefix or conveyor keywords
    ("Conveyor_Tracking", lambda title, desc, rec:
        title.startswith("Cnv_") or _contains(title, "Conveyor", "conveyor")
        or _contains(title, "AIO_Tracking", "AIO_TrackingSet", "AIO_TrackingStart", "AIO_TrackingEnd", "AIO_TrackingOn")),

    # Distance Tracking Function
    ("Distance_Tracking_Function", lambda title, desc, rec:
        title.startswith("Dist") and not _contains(title, "DistCheck") or
        _contains(title, "DistCorrect", "Distance_Tracking")),

    # Force Sensing — force/contact/alignment object properties
    ("Force_Sensing", lambda title, desc, rec:
        _contains(title,
            "AlignCheck", "AlignEnabled", "AlignFirmness", "AlignOrient",
            "ContactDis", "ContactDist", "ContactForce", "ContactOrient",
            "ContactStiffness", "ContactTorque",
            "DecelStartRatio", "CollisionForce", "AvgForce", "EndForce",
            "ForceCondOK", "FGGet", "FGRun", "FGSet",
            "ApproachDist", "ApproachPoint", "ContactProbe",
            "CFEnabled", "CPEnabled")),

    # ECP Motion
    ("ECP_Motion", lambda title, desc, rec:
        _contains(title, "ECP", "ECPSet") and not _contains(title, "ECPSet_Stmt") or
        title in ("ECP_Keyword", "ECPSet_Keyword")),

    # Vision Guide — ArcFinder, ArcInspector, and vision result properties
    ("Vision_Guide", lambda title, desc, rec:
        _contains(title,
            "ArcFinder", "ArcInspector", "VisionSeq", "VisionStep",
            "AllFound", "AllPassed", "AngleAccuracy", "AngleBase", "AngleEnable",
            "AngleEnd", "AngleMode", "AngleObject", "AngleOffset", "AngleRange",
            "AngleStart", "AngleResult",
            "AutoReference", "AutoRefMode", "AutoRefFinal", "AutoRefInit",
            "AutoRefMove", "AutoRefTolerance", "AutoRefMoveMode",
            "AutoCamPoints", "AdjustingThreshold", "AdjustingWhite",
            "Acquire", "AcquireState",
            "DictionaryMode", "Directed",
            "AllRobotXYU", "Angle1", "Angle2")
        or (rec.get("type") == "result" and _contains(desc,
            "vision", "Vision", "camera", "image", "blob", "barcode"))),

    # Parts Feeding
    ("Parts_Feeding", lambda title, desc, rec:
        _contains(title, "PF", "PartsFeed", "Parts_Feed", "Parts_Detect")),

    # Additional Axis
    ("Additional_Axis", lambda title, desc, rec:
        _contains(title, "AdditionalAxis", "Additional_Axis", "AddAxis")),

    # The SPEL+ Language — keyword/definition entries and utility functions
    ("The_SPELplus_Language", lambda title, desc, rec:
        title.endswith("_Keyword") or
        title.endswith("_def") or
        _contains(title,
            "DateTimeFormat", "ascii_def", "bcd_def",
            "DiffPoint", "Errb", "Cnv_Offset",
            "ColumnCount", "RowCount")),
]


def classify(rec: dict) -> str | None:
    """Return target chapter folder name, or None to stay in Misc."""
    title = rec.get("title", "")
    desc  = rec.get("description", "") or ""
    for target, predicate in RULES:
        try:
            if predicate(title, desc, rec):
                return target
        except Exception:
            pass
    return None


def _write_folder_json(folder: Path, rec: dict) -> None:
    """Write or update _folder.json in a chapter folder using the chapter's existing file if present."""
    fp = folder / "_folder.json"
    if fp.exists():
        return  # already has one
    # Create a minimal pointer
    chapter_name = folder.name.replace("_", " ").replace("plus", "+")
    fp.write_text(json.dumps({
        "type": "folder_index",
        "toc_chapter": chapter_name,
        "category": folder.name.lower().replace("_", "_"),
        "title": chapter_name,
        "instruction": f"References for the '{chapter_name}' section.",
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description="Reclassify Misc KB files into proper chapters")
    ap.add_argument("--apply", action="store_true", help="Execute moves (default: dry-run preview)")
    args = ap.parse_args()
    dry_run = not args.apply

    if dry_run:
        print("DRY RUN — no files will be moved.  Pass --apply to execute.\n")

    moves: list[tuple[Path, Path]] = []
    stay_count = 0

    for section_root in [JSON_DIR / "Program", JSON_DIR / "Operator"]:
        misc_dir = section_root / "Misc"
        if not misc_dir.exists():
            continue
        for jf in sorted(misc_dir.glob("*.json")):
            if jf.name.startswith("_"):
                continue
            try:
                rec = json.loads(jf.read_text(encoding="utf-8"))
            except Exception:
                continue
            target = classify(rec)
            if target:
                dest_dir = section_root / target
                moves.append((jf, dest_dir / jf.name))
            else:
                stay_count += 1

    # Group moves by target for display
    from collections import defaultdict
    by_target: dict[str, list[tuple[Path, Path]]] = defaultdict(list)
    for src, dst in moves:
        by_target[dst.parent.name].append((src, dst))

    print(f"Files to move:  {len(moves)}")
    print(f"Files staying in Misc: {stay_count}\n")
    for target, pairs in sorted(by_target.items(), key=lambda x: -len(x[1])):
        print(f"  -> {target:<45}  {len(pairs)} files")
        for src, dst in pairs[:3]:
            print(f"      {src.name}")
        if len(pairs) > 3:
            print(f"      … and {len(pairs)-3} more")

    if dry_run:
        print("\nRun with --apply to execute.")
        return

    # Execute moves
    moved = 0
    for src, dst in moves:
        dst.parent.mkdir(exist_ok=True)
        shutil.move(str(src), str(dst))
        moved += 1

    # Ensure _folder.json exists in any newly populated folder
    touched_dirs: set[Path] = {dst.parent for _, dst in moves}
    for d in touched_dirs:
        _write_folder_json(d, {})

    print(f"\nMoved {moved} files.")

    # Rebuild index
    print("\nRebuilding search index...")
    result = subprocess.run(
        [sys.executable, str(_SCRIPTS_DIR / "spel_search.py"), "--build"],
        capture_output=True, text=True
    )
    print(result.stdout.strip())
    if result.returncode != 0:
        print("Index rebuild failed:", result.stderr)


if __name__ == "__main__":
    main()
