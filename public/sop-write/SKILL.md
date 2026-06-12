---
name: sop-write
description: Write a bilingual (English + Thai) SOP / work instruction / how-to guide matching the house template — H1/H2 Arial headings, paired English/Thai paragraphs, a capability or procedure table, numbered steps, safety block, and troubleshooting. Covers software SOPs, machine operating procedures, maintenance/PM procedures, changeover instructions, and safety procedures. Use when the user asks to draft an SOP, work instruction, operating procedure, PM procedure, user guide, quick-start, or any bilingual (EN/TH) procedure document in this format.
---

Write a bilingual English + Thai SOP / procedure that matches the house template. English appears first; its Thai translation is the immediately-following separate paragraph.

## When to use
- Draft an SOP, work instruction (WI), operating procedure, PM/maintenance procedure, changeover guide, how-to, user guide, or quick-start.
- A bilingual (EN/TH) guide, or "the SOP template" / "the same format".

## Phase 0 — Intake (do this before writing)
Establish, from the user's input or by asking max 3 questions:
1. **SOP type** → `software` | `machine-operation` | `maintenance-pm` | `changeover` | `safety`. This selects the section preset below.
2. **Source** → uploaded doc / notes / screenshots / verbal. Read it first (use `file-reading` skill if a file path is given and content isn't in context). Never invent a procedure.
3. **Actor + trigger** → who performs it (operator / technician / engineer) and what starts it.

If source material is missing and the procedure can't be inferred, ask — do not write blind.

## Common structure (all types)
1. **H1 title** — guide/procedure name.
2. **Overview paragraph** — 1–2 sentences: what it is, what it does.
3. **[Type-specific middle section — see presets]**
4. **H2 "Troubleshooting"** — symptom → fix pairs.
5. **H2 "Need more help?"** — support pointer.

Every English heading / paragraph / list item is followed by a **separate paragraph** with its Thai translation.

## Section presets by type
**software**
- H2 "What can [X] do?" + Capability table (Capability / What to ask / Example)
- H2 "Quick-start steps" (numbered)
- H2 "What's New" (optional)

**machine-operation**
- H2 "Purpose & Scope"
- **H2 "Safety" (mandatory — see Safety block)**
- H2 "Prerequisites" (machine state, materials, tools)
- H2 "Procedure" (numbered steps)
- H2 "Acceptance criteria" (how to confirm done/good)

**maintenance-pm**
- H2 "Frequency" (daily/weekly/monthly/by cycle count)
- **H2 "Safety / Lockout-Tagout" (mandatory)**
- H2 "Tools & spare parts" (table)
- H2 "Steps" (numbered)
- H2 "Sign-off" (date / tech / result row)

**changeover**
- **H2 "Safety" (mandatory)**
- H2 "From → To" (product/config table)
- H2 "Procedure" (numbered, with SMED internal/external tags if relevant)
- H2 "Acceptance criteria"

**safety**
- H2 "Hazards"
- H2 "Required PPE" (table)
- H2 "Procedure"
- H2 "In case of incident"

## Safety block (mandatory for non-software types)
A highlighted callout near the top: hazard summary, required PPE, and LOTO note where energy is present. Paired EN/TH. Style: shaded paragraph (light fill `#FFF2CC`), bold EN label "⚠ Safety", Thai sibling below. Keep warnings imperative and short.

## Formatting rules (apply explicitly per paragraph — do not rely on Normal style)
**English / Latin / digits:** Arial, color #000000.
- H1 24pt · H2 18pt · body & table & list 12pt.

**Thai:** Angsana New, 14pt, color #0000FF (blue) — everywhere, including table cells.

**Latin/digits embedded in a Thai paragraph** (e.g. "Claude", "PLC", "24V", a model no.): restyle just those chars to Arial 12pt; leave surrounding Thai as Angsana New 14pt blue. Find with `thPara.search(token,{matchCase:true})` per `text.match(/[A-Za-z0-9]+/g)` token, then `.font.name="Arial"; .font.size=12`.
- **Terminology policy:** technical acronyms and identifiers (PLC, HMI, FAT, SAT, BOM, FMEA, LOTO, part/model numbers) stay English — do NOT translate them; only translate descriptive prose around them. Reuse the domain glossary for consistent TH wording.

**Lists:** numbered → "List Number"; bullets → "List Bullet".

## Critical: Thai font sizing (szCs)
`font.size` writes only `<w:sz>`, never `<w:szCs>`. Thai glyphs are sized by `szCs` when a run carries `<w:cs/>` — so Thai renders too small (~12pt) even with `sz=28`.

**Fix:** replace each Thai run's content via a content-scoped OOXML insert with a full pkg wrapper containing BOTH `<w:sz w:val="28"/><w:szCs w:val="28"/>` and NO `<w:cs/>` flag. Use a content-scoped range (`thPara.getRange("Content")` or `cell.body.search(thaiText)`), NOT paragraph/table range — those re-nest a table or throw GeneralException.

Snippets: see `reference/ooxml-snippets.md` (TH heading / TH body / TH table cell pkg wrappers — copy, don't re-derive).

**Done when:** every Thai run reads back with `szCs` present and `<w:cs/>` absent — verify via `getOoxml()` and `/w:szCs/.test(xml) && !/<w:cs\/>/.test(xml)`.

## Capability / procedure tables
Flat (NOT nested) table, "TableGrid" style, `headerRowCount = 1`. Each cell = 2 paragraphs: English (Arial 12 black) top, Thai (Angsana New 14 blue) below.

Build with `carrier.insertTable(rows, cols, "After", values)` for English, then add the Thai paragraph per cell and apply the szCs fix. **Never** build nested 1×1 tables inside cells — original defect. After building, verify every cell has exactly 2 paragraphs and 0 nested tables (`cell.body.tables.items.length === 0`).

## Environment fallback
If the Word add-in (`execute_office_js`, `verify_doc_visual`) is unavailable, fall back to the `docx` skill's OOXML path — the same pkg wrappers and szCs rule apply when writing `document.xml` directly.

## Build order (one execute_office_js call per section for visible progress)
1. Title + overview (EN + TH).
2. Safety block (non-software types).
3. Type-specific middle section + table.
4. Numbered steps (EN + TH per step).
5. Troubleshooting / Need more help.
6. Thai szCs sweep + embedded-Latin restyle.
7. Verification gate.

## Verification gate (HARD — do not deliver until all pass)
Run and confirm each; on any fail, fix and re-run:
- [ ] Every EN heading/para/list-item has a TH sibling paragraph directly after it.
- [ ] Every Thai run: `szCs` present, `<w:cs/>` absent (read back OOXML).
- [ ] Embedded Latin/digits in TH paras are Arial 12pt; surrounding TH is Angsana New 14pt blue.
- [ ] Acronyms/identifiers left untranslated per terminology policy.
- [ ] Tables flat: every cell exactly 2 paragraphs, 0 nested tables; lists numbered continuously.
- [ ] Non-software types: Safety block present (LOTO note where energy is involved).
- [ ] `verify_doc` / `verify_doc_visual`: layout uniform, TH matches body size visually.

A worked machine-operation example: `reference/example-machine-sop.md`.
