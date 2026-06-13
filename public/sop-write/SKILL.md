---
name: sop-write
description: Write a bilingual (English + Thai) SOP or PM form matching the Benchmark Electronics (BEI-Thailand) house template. Two real doc types: AYS (SOP) with 8 fixed sections + Revision History, and AYF (PM check-sheet) in landscape with a PM matrix table. Named styles (Heading1–4, ThaiTranslate, Table, Text) are the primary formatting path. Use when asked to draft an SOP, work instruction, operating procedure, PM form, or any bilingual (EN/TH) procedure document in the BEI-Thailand / Agile PLM format.
---

Write a bilingual English + Thai SOP or PM form matching the Benchmark Electronics (BEI-Thailand) house template. Named Word styles are the primary formatting path — apply them first; reach for raw OOXML only as a fallback.

## When to use
- Draft an SOP (AYS), work instruction, or operating procedure for BEI-Thailand.
- Draft a PM form / preventive maintenance check-sheet (AYF).
- Update an existing SOP to a new revision.
- "The SOP template", "the same format", or any bilingual (EN/TH) procedure in the house style.

## Phase 0 — Intake
Establish from input or by asking at most 4 questions:
1. **Doc type** → `AYS` (SOP) | `AYF` (PM form).
2. **Identity** → customer code (e.g. `EMP`), 7-digit document number, revision letter (A, B, …), and title.
3. **Source material** → uploaded doc / notes / verbal. Never invent procedure content — if missing, ask.
4. **Revision update?** → if yes, ask which sections changed and what the Agile ECO number is.

## Document identity (all docs)
Filename and header must carry the full identifier:

| Field | Format | Example |
|---|---|---|
| SOP filename | `AYS<cust>-<7digits>-Rev<X>.docx` | `AYSEMP-0051797-RevB.docx` |
| Form filename | `AYF<cust>-<7digits>-Rev<X>.docx` | `AYFEMP-0051798-RevA.docx` |
| `core.xml` `cp:category` | `SOP` or `form` | `SOP` |
| `core.xml` `cp:subject` | `Product Engineering` | |
| Header | Doc-control fields. RoHS logo (green `#99CC00`) present on RoHS docs; **omitted on non-RoHS docs**. | |

## AYS — SOP structure (fixed 8-section order)

| # | Section | Bilingual? | Notes |
|---|---|---|---|
| 1 | **Purpose** | English only | What the machine/process does |
| 2 | **Scope** | English only | Sites; Required Training (Operator/Technician) |
| 3 | **Reference Documents and Forms** | English only | Cross-ref other AYS/AYF numbers |
| 4 | **Equipment** | English only | Machine list, tools, materials |
| 5 | **Safety** | **EN + Thai sibling** | EN statement then `ThaiTranslate` paragraph |
| 6 | **Definitions** | EN labels + Thai callout labels | Machine overview, control box, indicators (image-heavy) |
| 7 | **Workflow** | English only | May be "N/A" |
| 8 | **Procedure** | **EN + Thai sibling per step** | Numbered `Heading2`/`Heading3` substeps |
| — | **Appendices** | **EN + Thai sibling** | e.g. "None." + Thai sibling |
| — | **Revision History** | English only | 3-column table: Rev / Description of Change / Approved By |

**Bilingual rule:** Thai siblings (`ThaiTranslate` paragraphs) appear on Safety statements, Procedure steps, Definitions labels, and Appendices. Purpose, Scope, Reference, Equipment, Workflow, and Revision History are English-only. Do NOT add Thai siblings to every paragraph.

## AYF — PM Form structure (landscape)
- **Orientation:** landscape.
- **Top blanks:** `MACHINE ID` / `MACHINE NAME` / `MODEL` / `SERIAL NO`.
- **Title:** PREVENTIVE MAINTENANCE INSTRUCTIONS.
- **PM matrix table:** numbered columns 1–13 (= occurrence/month), rows grouped by interval (`MONTHLY`, `SEMI-ANNUAL`), each row: `Area | Item | Execution`.
- **Sign-off row:** `Checked By | Date | Inspected by` — "Tick after completing the items."
- **Preventive maintenance action record** (separate table): `Date | Problem Description | Action | By`.

See `reference/example-form.md` for full layout.

## Named styles — primary formatting path
The house template defines these styles. Apply them by name rather than setting per-run font/size.

| Style | Use for | Latin font | CS font | pt | Color |
|---|---|---|---|---|---|
| `Heading1` | H1 section titles | Arial | **AngsanaUPC** | **14pt (sz 28)** | auto |
| `Heading2` | H2 subsections | Arial | **AngsanaUPC** | **12pt (sz 24)** | auto |
| `Heading3`, `Heading4` | deeper sub-levels | (inherit) | (inherit) | (inherit) | auto |
| `Normal` | body default | Arial | Arial | (default) | auto |
| `ThaiTranslate` | Thai sibling paragraphs | Arial | **AngsanaUPC** | 12pt (sz 24) | **`#0000FF`** |
| `ThaiTranslateChar` | inline Thai char style | — | AngsanaUPC | — | blue |
| `Table` | table header cells, shaded `CCCCCC` | — | — | — | — |
| `Text` | table body cells | — | — | — | — |

**Correct font:** **AngsanaUPC** (NOT "Angsana New") for all Thai / complex-script runs.
**Heading sizes:** H1 = 14pt (sz 28), H2 = 12pt (sz 24) — NOT H1 24pt / H2 18pt.

Apply styles via Office JS:
```js
para.style = "Heading1";        // H1 section titles
para.style = "ThaiTranslate";   // Thai sibling paragraphs
cell.paragraphs.getFirst().style = "Table"; // table header cells
```

Because each style sets Arial for Latin and AngsanaUPC for complex-script, embedded English inside a Thai line auto-renders correctly in Arial — no per-token embedded-Latin restyle loop needed when styles are applied.

## Terminology policy
Technical acronyms and identifiers stay English — do NOT translate them:
`PLC, HMI, PFS, AOI, SN, PN, IPA, MPa, RoHS, ESD, EMO, LOTO, BOM, FMEA, ECO, PLM, TLA, PCB, SMT`
Only translate descriptive prose around them. Reuse `reference/glossary.md` for consistent Thai term mapping.

## Revision History table
Always the last body element. 3 columns: **Rev | Description of Change | Approved By**.

```
| Rev | Description of Change               | Approved By         |
|-----|-------------------------------------|---------------------|
| A   | New release.                        | Agile ECO TE0236664 |
| B   | - Rename title "CHARMS TLA…"→"TLA…" | Agile ECO TExxxxxxx |
|     | - Add 8.2 PFS TESTLINK detail        |                     |
|     | - Add 8.3 AOI Program Selector       |                     |
```

**Rev-update workflow** (e.g. Rev A → Rev B):
1. Bump filename `RevA` → `RevB`.
2. Update title in body **and** header if renamed.
3. Add/modify the changed numbered subsections.
4. Append one Revision History row; list each change **by section number**.
5. Cite the **Agile ECO** number in "Approved By".
6. Update `core.xml` modified date.

## Fallback OOXML path (only when named styles are unavailable)
Use raw OOXML pkg-injection only when the house template styles are absent from the target document.

**Thai run sizing problem:** `font.size` writes only `<w:sz>`, not `<w:szCs>`. Thai glyphs need both.
**Fix:** insert content-scoped OOXML with `<w:sz w:val="28"/>` AND `<w:szCs w:val="28"/>`, NO `<w:cs/>`.
Use `thPara.getRange("Content").insertOoxml(pkg, "Replace")`, NOT paragraph/table range.

Fallback font: **AngsanaUPC** (not Angsana New). Snippets: `reference/ooxml-snippets.md`.

Verify each Thai run after insert:
```js
const xml = thPara.getOoxml(); await ctx.sync();
const ok = /w:szCs/.test(xml.value) && !/<w:cs\/>/.test(xml.value);
```

## Tables
House styles: `Table` (header cells, shaded `CCCCCC`) and `Text` (body cells). NOT "TableGrid".
Flat only — never nest tables inside cells. PM matrix layout: `reference/example-form.md`.

## Environment fallback
If `execute_office_js`/`verify_doc_visual` are unavailable, fall back to the `docx` skill's OOXML path — the same pkg wrappers and AngsanaUPC font apply when writing `document.xml` directly.

## Build order (one execute_office_js call per section)
1. Set filename; write `core.xml` identity fields.
2. Header (RoHS logo + doc-control fields).
3. Body sections in fixed order (AYS: 1–8 + Appendices + Revision History; AYF: blanks + PM matrix + sign-off + action record).
4. Apply named styles to all paragraphs.
5. Add `ThaiTranslate` siblings for Safety + Procedure steps (AYS only; AYF is English-only).
6. Fallback szCs sweep only if named styles were unavailable.
7. Verification gate.

## Verification gate (HARD — do not deliver until all pass)
- [ ] House styles applied: `Heading1–4`, `ThaiTranslate`, `Table`/`Text`.
- [ ] Font is **AngsanaUPC** (cs) everywhere Thai is used; color `#0000FF`; `szCs` present; `<w:cs/>` absent.
- [ ] Thai siblings present on Safety + Procedure steps + Definitions labels + Appendices; absent from Purpose/Scope/Reference/Equipment/Workflow/Revision History.
- [ ] Acronyms/identifiers untranslated (PFS, AOI, HMI, PN, SN, IPA, RoHS, ESD…).
- [ ] Filename + header carry `AYS/AYF<cust>-<7digits>-Rev<X>`.
- [ ] Revision History has a row for the current rev listing section-number changes + Agile ECO.
- [ ] AYF forms: landscape, machine-ID blanks, PM matrix, sign-off row, action record table.
- [ ] Tables flat; heading/list numbering continuous via outline numbering.

Reference files: `reference/example-sop.md`, `reference/example-form.md`, `reference/glossary.md`, `reference/ooxml-snippets.md`.
