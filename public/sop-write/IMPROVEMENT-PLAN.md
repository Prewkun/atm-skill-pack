# sop-write — Improvement Plan & Progress

> **Status:** Plan ready for implementation. No skill files changed yet.
> **Next implementer:** intended to be executed by Sonnet, phase by phase.
> **Branch:** `claude/sop-write-skill-review-qy1whh`
> **Date:** 2026-06-13

This document captures (1) the findings from reviewing the current skill against
the real house templates, (2) the ground-truth facts those templates reveal, and
(3) a phased plan to bring the skill in line. Work the phases top-down; Phase 1 is
load-bearing and everything else builds on it.

---

## 0. Reference material (ground truth)

Three real documents were added to `public/sop-write/reference/` on the `main`
branch and used to derive everything below. They are large (16–21 MB, embedded
screenshots) and live on `main` only — **do not commit copies into the feature
branch.** To inspect them, check them out locally and discard when done:

```bash
git checkout origin/main -- public/sop-write/reference/AYSEMP-0051797-RevA.docx \
  public/sop-write/reference/AYSEMP-0051797-RevB.docx \
  public/sop-write/reference/AYFEMP-0051798-RevA.docx
# ...inspect (unzip + read word/document.xml, word/styles.xml, headers)...
git reset -q HEAD public/sop-write/reference/*.docx && rm -f public/sop-write/reference/AYS*.docx public/sop-write/reference/AYF*.docx
```

| File | Type | Notes |
|---|---|---|
| `AYSEMP-0051797-RevA.docx` | SOP, Rev A | "New release." baseline |
| `AYSEMP-0051797-RevB.docx` | SOP, Rev B | Shows how a revision update is done vs Rev A |
| `AYFEMP-0051798-RevA.docx` | Form (PM check sheet), Rev A | The companion PM form referenced by the SOP |

Company context: Benchmark Electronics (BEI-Thailand), Product Engineering;
documents managed in Agile PLM (ECO numbers); RoHS-labelled.

---

## 1. Ground-truth facts the templates establish

### 1.1 Document naming / identity
- **`AYS<cust>-<7 digits>-Rev<X>`** = an SOP (e.g. `AYSEMP-0051797-RevB`).
- **`AYF<cust>-<7 digits>-Rev<X>`** = a Form (e.g. `AYFEMP-0051798-RevA`).
- `<cust>` = customer code (here `EMP`). `Rev<X>` = revision letter (A, B, …).
- `docProps/core.xml` `cp:category` = `SOP` or `form`; subject = "Product Engineering".
- Header carries the RoHS logo (green `#99CC00`) plus document-control fields.

### 1.2 Named styles already solve the hard problems
The template defines Word styles that bake in font/size/color/script handling.
**Applying these styles is the correct primary path** — not per-run formatting.

| Style | Latin font (ascii/hAnsi) | Complex-script font (cs) | sz | szCs | Color | Notes |
|---|---|---|---|---|---|---|
| `Normal` | Arial | Arial | (default) | – | auto | body default |
| `Heading1` | Arial | **AngsanaUPC** | 28 (14pt) | 28 | auto | outline-numbered |
| `Heading2` | (inherit) | (inherit) | 24 (12pt) | – | auto | outline-numbered |
| `Heading3` / `Heading4` | (inherit) | (inherit) | – | – | auto | outline-numbered |
| `ThaiTranslate` (para) + `ThaiTranslateChar` (linked char) | Arial | **AngsanaUPC** | 24 (12pt) | **28 (14pt)** | **`0000FF`** | the Thai sibling style |
| `Table` | – | – | – | – | – | table header cells, shaded `CCCCCC` |
| `Text` | – | – | – | – | – | table body cells |

**Critical implications:**
1. Because each run sets **Arial for Latin and AngsanaUPC for complex-script**,
   embedded English inside a Thai line auto-renders Arial. The skill's per-token
   embedded-Latin restyle loop is **unnecessary** when styles are applied.
2. Because `ThaiTranslate`/`Heading1` carry `szCs` in the style, Thai glyphs size
   correctly. The skill's per-run `szCs` OOXML pkg-injection is **unnecessary**
   when styles are applied → demote it to a documented fallback only.

### 1.3 Corrections to current skill claims
- Font is **AngsanaUPC**, NOT "Angsana New".
- Heading sizes are **H1 = 14pt (sz 28), H2 = 12pt (sz 24)** — NOT H1 24pt / H2 18pt.
- Thai body = AngsanaUPC, szCs 28 (14pt), blue `#0000FF` ✅ (blue color was correct).
- Tables use named styles `Table` / `Text` (header shaded `CCCCCC`), NOT "TableGrid".

### 1.4 Real SOP structure (single fixed structure, numbered Heading1)
NOT the five invented type-presets currently in the skill. Real order:

1. **Purpose**
2. **Scope** — sites (e.g. "All BEI-Thailand sites"); **Required Training** (Operator/Technician)
3. **Reference Documents and Forms** — cross-references other AYS/AYF numbers
4. **Equipment**
5. **Safety** — EN statement + Thai sibling (`ThaiTranslate`)
6. **Definitions** — machine/hardware overview, control box, indicators (image-heavy, callout labels EN+TH)
7. **Workflow** — may be "N/A"
8. **Procedure** — numbered Heading2/Heading3 substeps; EN + Thai sibling per step
- **Appendices** — e.g. "None."
- **Revision History** — table (see 1.6)

### 1.5 Bilingual rule (corrected — NOT "everything gets Thai")
Thai siblings (via `ThaiTranslate`) appear on **Safety statements and Procedure
steps** (and Definitions labels). Purpose, Scope, Equipment, and Reference
sections are **English-only**. The current skill's hard gate "every EN paragraph
has a TH sibling" is **wrong** for this house style and must be relaxed.

### 1.6 Revision History + rev-update workflow (what RevA→RevB demonstrates)
Revision History is a 3-column table at the end of the body:

| Rev | Description of Change | Approved By |
|---|---|---|
| A | New release. | Agile ECO TE0236664 |
| B | - Rename title "CHARMS TLA…" → "TLA…"  - Add 8.2 PFS TESTLINK detail  - Add 8.3 AOI Program Selector detail  - Add 8.4 universal fixture support  - Add 8.5 auto PFS submit | Agile ECO TExxxxxxx |

**A revision update therefore means:**
1. Bump the filename `Rev A` → `Rev B`.
2. Update the title in the body **and** header if it was renamed.
3. Add/modify the numbered subsections (RevB added 8.2–8.5).
4. **Append one Revision History row** describing each change **by section number**.
5. Cite the **Agile ECO** number in "Approved By".
6. Update `core.xml` modified date (the PLM does revision counters separately).

### 1.7 Form (AYF / PM check sheet) — a distinct doc type
The current `maintenance-pm` preset (Frequency/Tools/Steps/Sign-off) does NOT
match. The real PM form is:
- **Landscape** orientation.
- Top blanks: `MACHINE ID / MACHINE NAME / MODEL / SERIAL NO`.
- Title: **PREVENTIVE MAINTENANCE INSTRUCTIONS**.
- PM **matrix table**: numbered columns (1–13 = occurrence/months), grouped by
  service interval (`MONTHLY`, `SEMI-ANNUAL`), with `Area / Item / Execution`
  rows (e.g. "Test EMO buttons", "Clean fixture with 99% IPA").
- Sign-off row: `Checked By / Date / Inspected by`; "Tick after completing the items".
- Separate **Preventive maintenance action record** table: `Date | Problem Description | Action | By`.

---

## 2. Phased improvement plan

### Phase 1 — Re-base the skill on the real template (HIGHEST PRIORITY)
- Replace the five invented presets with the **two real document types**:
  - **AYS — SOP**: fixed 8-section structure + Appendices + Revision History (§1.4).
  - **AYF — Form**: PM check-sheet layout (§1.7).
- Rewrite the formatting section to **"apply the house named styles"**
  (`Heading1–4`, `ThaiTranslate`, `Table`, `Text`) as the primary path.
- Correct the font to **AngsanaUPC** and the heading sizes (§1.3).
- Demote `szCs` pkg-injection and embedded-Latin restyle to an explicit
  **fallback** ("only when the template styles are unavailable") (§1.2).
- Relax the bilingual rule: Thai sibling required on **Safety + Procedure steps**
  (and Definitions labels), other sections English-only (§1.5).

### Phase 2 — Add the missing house mechanics
- **Document identity** section: `AYS/AYF<cust>-<digits>-Rev<X>` convention,
  customer code, `core.xml` category, header doc-control/RoHS block (§1.1).
- **Revision History** section + documented **rev-update workflow** (§1.6).
- Add the **Reference Documents and Forms** and **Appendices** sections
  (currently absent from the skill).

### Phase 3 — Ground-truth references & glossary
- Add `reference/example-sop.md` and `reference/example-form.md` — lightweight
  text/structure distillations of the real docs (NOT the binaries).
- Build `reference/glossary.md` (EN→TH) from the Thai actually used in these docs,
  e.g.:
  - Emergency button (EMO) → ปุ่มหยุดฉุกเฉิน
  - Stop button → ปุ่มหยุดการทำงาน
  - Start button → ปุ่มเริ่มการทำงาน
  - circuit breaker → เซอร์กิตเบรกเกอร์
  - Check air supply pressure → ตรวจสอบแรงดันลม
  - plus the acronym keep-list (PLC, HMI, PFS, AOI, SN, PN, IPA, MPa, RoHS, ESD…)
  This wires up the skill's existing dangling "domain glossary" references.
- Rewrite `reference/ooxml-snippets.md` to use **AngsanaUPC** and frame the
  snippets as the **fallback** path (style application is primary).

### Phase 4 — Verification gate (rewrite to match reality)
Replace the current gate with checks that reflect the house template:
- [ ] House styles applied (`Heading1–4`, `ThaiTranslate`, `Table`/`Text`).
- [ ] Thai runs use AngsanaUPC (cs) with `szCs` present; blue `#0000FF`.
- [ ] Thai sibling present on **Safety + Procedure steps + Definitions labels**
      (NOT on Purpose/Scope/Equipment/Reference).
- [ ] Acronyms/identifiers left untranslated (PFS, AOI, HMI, PN, SN…).
- [ ] Filename + header carry correct `AYS/AYF<cust>-<digits>-Rev<X>`.
- [ ] Revision History has a row for the current rev, by section number + Agile ECO.
- [ ] For AYF forms: landscape, machine-ID blanks, PM matrix, sign-off, action record.
- [ ] Tables flat; lists/headings numbered continuously via outline numbering.

---

## 3. Progress log
- 2026-06-13 — Reviewed current `SKILL.md` + `reference/`; produced initial plan.
- 2026-06-13 — User supplied real templates (RevA/RevB SOP + PM form). Re-reviewed
  against ground truth; discovered named-style mechanism, AngsanaUPC font, correct
  section structure, revision workflow, and AYF form layout. Plan revised (this file).
- **Next:** implement Phase 1 (Sonnet).
