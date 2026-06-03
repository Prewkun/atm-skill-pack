---
name: to-issues
description: Break down a PRD, spec, plan, or feature description into a structured list of actionable work items / issues / tasks. Trigger when the user says "break this into issues", "create tasks from this", "make a task list", "break this down into tickets", "what are the work items", or hands over a spec/PRD and wants it decomposed into executable chunks. Also use for decomposing automation project phases into work packages.
---

# to-issues

Convert a PRD, spec, or plan into a flat list of actionable, assignable work items.

---

## Step 1 — Parse the input

Read the source document and identify:
- Major functional areas or system components
- Dependencies between areas
- Sequential vs. parallel work
- Work that needs to happen before other work can start (blockers)

---

## Step 2 — Decompose into issues

Each issue must be:
- **Actionable** — starts with a verb (Implement, Design, Test, Configure, Integrate, Document)
- **Completable by one person** — not a project, a task
- **Estimable** — small enough to estimate (target: hours to a few days)
- **Independently verifiable** — has a clear done condition

Group issues by phase or component. Within each group, order by dependency.

---

## Step 3 — Output format

```
## [Phase / Component Name]

### ISSUE-001: [Verb] [What]
**Type:** Feature / Bug / Task / Spike / Doc  
**Priority:** P1 / P2 / P3  
**Estimate:** [hours or days]  
**Depends on:** [ISSUE-XXX or none]  
**Description:**  
[2–4 sentences: what needs to be done and why]

**Acceptance Criteria:**
- [ ] [Observable, testable condition]
- [ ] [Another condition]

---

### ISSUE-002: ...
```

---

## Issue types

| Type | Use when |
|---|---|
| Feature | New capability being built |
| Task | Setup, config, integration, procurement |
| Spike | Research or investigation with time-box — output is a decision or doc, not code |
| Test | Verification, validation, FAT/SAT activities |
| Doc | Documentation, manuals, training material |
| Bug | Something broken that was previously working |

---

## Priority levels

| Level | Meaning |
|---|---|
| P1 | Blocks other work or is on critical path |
| P2 | Required for delivery, not blocking |
| P3 | Nice-to-have, can defer if needed |

---

## Dependency rules

- If issue B cannot start until issue A is done → B depends on A
- Identify the critical path: the longest chain of dependencies
- Flag issues that have no dependencies — those can start immediately (parallel starters)

---

## After generating issues

Offer to:
1. Export as a markdown checklist
2. Export as CSV for import into Jira / Azure DevOps / Asana
3. Organize into a sprint/phase plan
4. Identify the critical path

---

## CSV export format (if requested)

```
ID,Title,Type,Priority,Estimate,Depends On,Description,AC
ISSUE-001,...
```
