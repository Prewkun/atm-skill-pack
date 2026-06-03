---
name: to-prd
description: Convert raw inputs — VOC notes, meeting notes, requirements dump, feature requests, problem statements, or rough ideas — into a structured Product/Project Requirements Document (PRD). Use when the user says "write a PRD", "turn this into requirements", "create a requirements doc", "document this feature", "write up the spec", or hands over rough notes and wants a formal requirements document. Also trigger for automation project specs, system integration specs, and machine/equipment requirement documents in manufacturing or engineering contexts.
---

# to-prd

Convert raw input into a structured requirements document. Works for software features, automation systems, equipment specs, and integration projects.

---

## Step 1 — Extract raw intent

Read everything the user provided. Pull out:
- **Problem being solved** — what pain, gap, or goal?
- **Who needs this** — stakeholders, operators, end users
- **What success looks like** — how do we know it's done and working?
- **Constraints** — budget, timeline, space, interfaces, regulations
- **Assumptions** — things being taken as true that haven't been confirmed
- **Out of scope** — what this explicitly does NOT cover

If critical info is missing, ask targeted questions before writing. Don't pad the PRD with guesses.

---

## Step 2 — Write the PRD

Use this structure:

---

### [Project / Feature Name]

**Version:** 1.0  
**Date:** [date]  
**Author:** [if known]  
**Status:** Draft

---

#### 1. Problem Statement
One paragraph. What problem does this solve? Why does it need solving now? What happens if it's not solved?

#### 2. Objectives
Bullet list. Specific, measurable outcomes this project must achieve.

#### 3. Scope

**In scope:**
- [what this covers]

**Out of scope:**
- [what this explicitly excludes]

#### 4. Stakeholders

| Role | Name / Team | Interest |
|---|---|---|
| Sponsor | | Funding / approval |
| Owner | | Day-to-day ownership |
| User | | Operates or uses the output |
| Reviewer | | Technical sign-off |

#### 5. Requirements

##### 5.1 Functional Requirements
What the system/feature must DO.

| ID | Requirement | Priority |
|---|---|---|
| FR-01 | [Must do X] | Must / Should / Nice-to-have |
| FR-02 | | |

##### 5.2 Non-Functional Requirements
Performance, reliability, safety, compliance, maintainability.

| ID | Requirement | Target |
|---|---|---|
| NFR-01 | Uptime | ≥ 99% |
| NFR-02 | Cycle time | ≤ X sec |

##### 5.3 Interface Requirements (if applicable)
Mechanical, electrical, software, network, operator interfaces.

#### 6. Constraints
Hard limits that cannot be changed: budget cap, physical envelope, existing infrastructure, regulations, standards (ISO, IEC, OSHA, customer-specific).

#### 7. Assumptions
Things assumed true. If any assumption is wrong, re-scope.

#### 8. Acceptance Criteria
How do we formally confirm this is done and working?

| ID | Criteria | Verification Method |
|---|---|---|
| AC-01 | [Observable, testable condition] | Test / Inspection / Demo |

#### 9. Open Questions
Unresolved items that need answers before or during execution.

| # | Question | Owner | Due |
|---|---|---|---|
| 1 | | | |

#### 10. Revision History

| Version | Date | Changes |
|---|---|---|
| 1.0 | [date] | Initial draft |

---

## Writing rules

- Requirements use **shall** (mandatory) or **should** (preferred) — never vague words like "fast", "easy", "robust" without a measurable target
- Each requirement is independently testable
- No implementation details in requirements (what, not how)
- Every AC maps to at least one requirement
- Flag assumptions explicitly — don't silently embed them

## Output

Produce the full PRD as a markdown document. If the user has docx skill available, offer to export as .docx.
