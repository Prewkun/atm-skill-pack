# Example SOP structure — AYS (BEI-Thailand house template)

Lightweight text distillation of AYSEMP-0051797-RevB. Use as content/structure
reference; apply named styles (`Heading1–4`, `ThaiTranslate`, `Table`, `Text`) per SKILL.md.

---

**Filename:** AYSEMP-0051797-RevB.docx
**`core.xml` category:** SOP | **subject:** Product Engineering
**Company:** Benchmark Electronics (BEI-Thailand), Product Engineering
**Managed in:** Agile PLM

---

# [Heading1] TLA Functional Test (Machine/Process Name)
*(Header: RoHS logo green #99CC00 + doc-control fields)*

## 1. Purpose
States what the machine or process does and why this SOP exists.
*(English only — no Thai sibling.)*

## 2. Scope
**Sites:** All BEI-Thailand sites.
**Required Training:** Operator Level 1; Technician Level 2.
*(English only.)*

## 3. Reference Documents and Forms

| Document No. | Title |
|---|---|
| AYSEMP-0051796-RevA | Related upstream SOP |
| AYFEMP-0051798-RevA | PM Check Sheet (companion form) |

*(English only. Cross-reference other AYS/AYF numbers.)*

## 4. Equipment
- Machine name, model, serial no.
- Tools: torque wrench, IPA 99%, ESD mat, circuit tester.
*(English only.)*

## 5. Safety
EN statement (Normal or Heading2 style):
Do not operate without safety guard in place. Press EMO (Emergency Stop) to halt immediately.
Apply LOTO before servicing any electrical component. Wear ESD wrist strap when handling PCBs.

*(Thai sibling — ThaiTranslate style, AngsanaUPC, blue #0000FF):*
อย่าเดินเครื่องโดยไม่มีฝาครอบความปลอดภัย กด EMO เพื่อหยุดเครื่องทันที
ทำ LOTO ก่อนซ่อมบำรุงชิ้นส่วนไฟฟ้าใดๆ สวมสายรัดข้อมือป้องกันไฟฟ้าสถิตเมื่อหยิบจับ PCB

## 6. Definitions
Machine overview paragraph (English). Callout labels for each component appear as EN + Thai pairs:

- **Control Box** — ตู้ควบคุม
- **EMO button** — ปุ่มหยุดฉุกเฉิน
- **Start button** — ปุ่มเริ่มการทำงาน
- **Stop button** — ปุ่มหยุดการทำงาน
- **Circuit breaker** — เซอร์กิตเบรกเกอร์
- **Air pressure gauge** — เกจวัดแรงดันลม
- **Indicator light** — ไฟสัญญาณ
- **HMI panel** — แผง HMI
- **Conveyor** — สายพาน
- **Fixture** — ฟิกซ์เจอร์

*(Image-heavy section. Callout labels are EN+TH pairs; body paragraphs describing the machine are English-only.)*

## 7. Workflow
N/A *(or flowchart image if applicable)*

## 8. Procedure

### 8.1 Start-up
1. Switch main circuit breaker to ON.
   *(ThaiTranslate:)* เปิดเซอร์กิตเบรกเกอร์หลัก

2. Verify air supply pressure ≥ 0.5 MPa on the gauge.
   *(ThaiTranslate:)* ตรวจสอบแรงดันลม ≥ 0.5 MPa ที่เกจวัด

3. Press Start button; confirm green indicator light is ON.
   *(ThaiTranslate:)* กดปุ่มเริ่มการทำงาน ตรวจสอบว่าไฟสัญญาณสีเขียวติด

4. Log in to HMI; select correct product program.
   *(ThaiTranslate:)* เข้าสู่ระบบ HMI แล้วเลือกโปรแกรมผลิตภัณฑ์ที่ถูกต้อง

### 8.2 PFS TESTLINK Setup
*(Added in Rev B. Substeps follow the same EN + ThaiTranslate sibling pattern.)*

1. Open PFS TESTLINK application on the test PC.
   *(ThaiTranslate:)* เปิดโปรแกรม PFS TESTLINK บนคอมพิวเตอร์ทดสอบ

2. Load the correct test program for the current PN.
   *(ThaiTranslate:)* โหลดโปรแกรมทดสอบที่ถูกต้องสำหรับ PN ปัจจุบัน

### 8.3 AOI Program Selector
*(Added in Rev B.)*

1. Select AOI program matching current board revision.
   *(ThaiTranslate:)* เลือกโปรแกรม AOI ที่ตรงกับ revision ของบอร์ดปัจจุบัน

### 8.4 Universal Fixture Support
*(Added in Rev B.)*

### 8.5 Auto PFS Submit
*(Added in Rev B.)*

## Appendices
None.
*(ThaiTranslate:)* ไม่มี

## Revision History

| Rev | Description of Change | Approved By |
|---|---|---|
| A | New release. | Agile ECO TE0236664 |
| B | - Rename title "CHARMS TLA…" → "TLA…"<br>- Add 8.2 PFS TESTLINK detail<br>- Add 8.3 AOI Program Selector detail<br>- Add 8.4 universal fixture support<br>- Add 8.5 auto PFS submit | Agile ECO TExxxxxxx |

---

**Formatting reminders:**
- Apply `Heading1` (14pt, AngsanaUPC CS) to all numbered section titles.
- Apply `ThaiTranslate` to all Thai sibling paragraphs — Safety, Procedure steps, Definitions labels, and Appendices get Thai siblings. Sections 1–4, 7, and Revision History are English-only.
- Tables use `Table` style (header shaded `CCCCCC`) and `Text` style (body cells).
- Acronyms PLC, HMI, PFS, AOI, SN, PN, IPA, MPa, RoHS, ESD, EMO stay English inside Thai lines.
