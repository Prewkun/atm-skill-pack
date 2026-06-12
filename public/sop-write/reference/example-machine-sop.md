# Worked example — machine-operation SOP (content layout)

Shows correct EN-first / TH-sibling pairing, mandatory safety block, terminology policy
(acronyms untranslated), and section preset. This is the *content/order* reference;
apply formatting + szCs fix per SKILL.md.

---

# Operate the SMT Reflow Oven
*(TH)* การใช้งานเตาอบ Reflow สำหรับ SMT

Reflow oven heats placed PCBs through a defined thermal profile to form solder joints.
*(TH)* เตาอบ Reflow ให้ความร้อนแก่ PCB ตามโปรไฟล์อุณหภูมิที่กำหนด เพื่อสร้างจุดบัดกรี

## Purpose & Scope
This procedure covers daily startup and running of the reflow oven by a line operator.
*(TH)* ขั้นตอนนี้ครอบคลุมการเปิดเครื่องและการใช้งานเตาอบ Reflow ประจำวันโดยพนักงานสายการผลิต

## ⚠ Safety  *(shaded #FFF2CC)*
High surface temperature and 3-phase power. Wear heat-resistant gloves. Apply LOTO before opening panels.
*(TH)* พื้นผิวร้อนจัดและไฟ 3 เฟส สวมถุงมือกันความร้อน ทำ LOTO ก่อนเปิดฝาตู้ควบคุม

## Prerequisites
- Oven powered, N2 supply ≥ 5 bar.
*(TH)* เปิดไฟเตาอบแล้ว และมีแก๊ส N2 แรงดัน ≥ 5 bar
- Correct thermal profile loaded on the HMI.
*(TH)* โหลดโปรไฟล์อุณหภูมิที่ถูกต้องบน HMI แล้ว

## Procedure
1. Switch main breaker ON and wait for the HMI to boot.
*(TH)* เปิดเบรกเกอร์หลักและรอให้ HMI บูตเสร็จ
2. Select the product profile, press Warm-up, wait until all zones reach setpoint.
*(TH)* เลือกโปรไฟล์ผลิตภัณฑ์ กด Warm-up และรอจนทุกโซนถึงค่าที่ตั้งไว้
3. Confirm conveyor speed matches the profile, then start the conveyor.
*(TH)* ตรวจสอบความเร็วสายพานให้ตรงกับโปรไฟล์ แล้วเริ่มเดินสายพาน

## Acceptance criteria
First-article joints pass visual + X-ray; no tombstoning or voids > spec.
*(TH)* จุดบัดกรีชิ้นแรกผ่านการตรวจสายตาและ X-ray ไม่มี tombstoning หรือ void เกินสเปก

## Troubleshooting
- HMI shows zone under temp → check heater fuse and thermocouple.
*(TH)* HMI แสดงอุณหภูมิโซนต่ำกว่ากำหนด → ตรวจฟิวส์ฮีตเตอร์และเทอร์โมคัปเปิล

## Need more help?
Contact Process Engineering (ext. 1420).
*(TH)* ติดต่อแผนก Process Engineering (เบอร์ภายใน 1420)

---
Note how PCB, SMT, HMI, LOTO, N2, X-ray, bar, Reflow stay English (Arial 12) inside TH lines.
