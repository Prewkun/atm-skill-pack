# NW Skill Pack

A collection of Claude skills, knowledge bases, and scripts for industrial robot programming.

---

## Skills

### `/epson-coding`
Generates production-ready EPSON SPEL+ robot programs (`.prg` files) from a natural-language description.

**What it does:**
1. Searches the local SPEL+ KB (extracted from the official EPSON manual)
2. Retrieves exact command references (syntax, parameters, examples)
3. Writes a complete, robot-safe `.prg` file grounded in the real manual
4. Saves output to `output/<name>.prg`

**Usage (in Claude Code):**
```
/epson-coding pick and place for 3 parts with vacuum gripper
/epson-coding palletizing 4x3 grid, output 1 is vacuum
/epson-coding conveyor tracking with vision and error handling
```

---

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/Prewkun/nw-skill-pack.git
cd nw-skill-pack
```

### 2. Install the skill
Copy the skill folder into your Claude skills directory:

**Windows:**
```powershell
Copy-Item -Recurse skills\epson-coding "$env:USERPROFILE\.claude\skills\epson-coding"
```

**macOS / Linux:**
```bash
cp -r skills/epson-coding ~/.claude/skills/epson-coding
```

Restart your Claude Code session — `/epson-coding` will appear in the skill list.

### 3. Update paths in the skill + scripts
Edit `skills/epson-coding/SKILL.md` — change the `cd` path to where you cloned:
```
cd "C:\your\path\to\nw-skill-pack"
python scripts/spel_search.py ...
```

The scripts auto-detect the KB path relative to their own location — no changes needed there.

### 4. Rebuild the search index (optional)
A pre-built `KB/spel_search_index.pkl` is included (ready to use immediately).
To rebuild it from the JSON source files:
```bash
python scripts/kb_cleanup.py
```

---

## Repository structure

```
nw-skill-pack/
├── skills/
│   └── epson-coding/
│       └── SKILL.md              ← Claude skill definition
├── scripts/
│   ├── spel_search.py            ← BM25 search over the KB (no dependencies)
│   ├── spel_generate.py          ← Code generator (optional, needs API key)
│   ├── kb_cleanup.py             ← Clean KB + rebuild search index
│   └── extract_spel_kb.py        ← Re-extract KB from source HTML manual
├── KB/
│   ├── spel_kb_index.json        ← Lightweight index of all 4108 entries
│   ├── spel_operator_kb.md       ← Full Operator reference (human readable)
│   ├── spel_search_index.pkl     ← Pre-built BM25 index (ready to use)
│   └── json/
│       ├── Operator/             ← 421 operator command JSON files
│       └── Program/              ← 3687 program reference JSON files
└── output/                       ← Generated .prg files saved here
```

---

## KB Source

The KB was extracted from the official **EPSON RC+ SPEL+ e-Manual**:
- `Operator` section — 421 commands with syntax, parameters, description, notes, examples
- `Program` section — 3687 reference pages

Total: **4108 structured entries**.

The source HTML manual is **not included** (EPSON copyright). To re-extract from your own copy, place it at `Manual/English/` and run:
```bash
python scripts/extract_spel_kb.py
python scripts/kb_cleanup.py
```

---

## Requirements

- Python 3.10+
- No extra packages for search / skill usage
- `anthropic` package only needed for `spel_generate.py --api` mode

