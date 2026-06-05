---
name: epson-coding
description: >
  Generate EPSON SPEL+ robot programs (.prg files) from a natural-language description.
  Use this skill whenever the user calls /epson-coding, mentions writing a SPEL+ program,
  asks for robot code for an EPSON arm, or describes a robot task like pick-and-place,
  palletizing, conveyor tracking, IO control, or any motion routine.
  The skill searches a local SPEL+ knowledge base extracted from the official EPSON manual,
  retrieves the exact command references needed, then writes a complete, robot-safe .prg file.
  Trigger proactively any time the user describes what a robot should DO and expects code out.
---

# EPSON SPEL+ Code Generator

You are generating production-quality SPEL+ code for EPSON robots.
You have access to a local knowledge base (KB) extracted from the official EPSON manual.
Always search it before writing code — never guess syntax.

---

## Step 1 — Search the KB

Run this command to retrieve relevant command references.
**Replace `<REPO_PATH>` with the path where you cloned nw-skill-pack.**

```bash
cd "<REPO_PATH>"
python scripts/spel_search.py "<keywords from the user's task>" -n 8 --context
```

Extract 2–4 keyword phrases from the user's task. Run multiple searches if the task
covers multiple areas (e.g., motion AND I/O AND error handling). Read all output carefully.

**Examples of good keyword choices:**
- "palletizing 4x3 grid loop"  → search `"palletizing pallet offset loop"`
- "pick and place with vacuum"  → search `"Jump pick place"` and `"On Off gripper IO"`
- "conveyor tracking vision"    → search `"conveyor tracking VRun"`
- "error handling recovery"     → search `"TrapErr ErrCode error recovery"`

---

## Step 2 — Write the SPEL+ program

Using ONLY the commands found in the KB output, write a complete `.prg` file.

### Hard rules (never break these):
1. **Speed AND Accel before every motion block** — Go, Jump, Move, Arc all need both set first.
2. **Declare all variables at the top** of each Function — Integer, Real, String, Boolean.
3. **Every Function ends with `Fend`** — no exceptions.
4. **Entry point is `Function main`** — always present.
5. **Use only commands confirmed by KB search** — if you didn't find it in the KB, don't use it.
6. **Point names** — use descriptive labels (home, pick, place, park) or P1/P2 notation.
7. **Comments** — use `'` to explain every non-obvious line.
8. **Digital outputs** — On/Off for outputs, In() for inputs.
9. **Parallel tasks** — use Xqt; protect shared resources with Semaphore.
10. **Error handling** — add TrapErr / ErrCode for any production routine.

### Program structure template:
```spel
'================================================
' [Program Title]
' Robot: EPSON [model if known]
' Description: [what this does]
'================================================

Function main
    ' Startup
    Motor On
    Power High

    ' Set motion parameters
    Speed [value]
    Accel [value], [value]

    ' Go to safe home position
    Go home

    ' Call main routine
    Xqt MainRoutine

Fend

Function MainRoutine
    ' Variable declarations
    Integer i
    ' ... (all vars at top)

    ' Your logic here

Fend
```

---

## Step 3 — Save the .prg file

Derive a short snake_case filename from the user's task description.
Save to: `<REPO_PATH>\output\<filename>.prg`

Create the output directory if it doesn't exist.

Then confirm to the user:
- What file was saved and where
- A brief summary of what the program does
- Key points / SPEL+ commands used
- Any assumptions made about point names, I/O numbers, or robot model
- What they need to teach/configure in RC+ before running (points, I/O mapping)

---

## What good output looks like

- Complete, runnable program — not a skeleton or pseudocode
- Every command has correct syntax matching the KB reference
- All variables declared, all functions terminated with Fend
- Enough comments that a technician can follow the logic
- Robot-safe: Speed/Accel always set, home position used, I/O states explicit

If the user's request is ambiguous (e.g., "3 parts" — fixed positions or array?),
make a reasonable assumption, note it in a comment at the top of the file, and mention
it in your summary so they can ask for a revision.
