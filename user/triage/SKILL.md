---
name: triage
description: Rapidly sort, prioritize, and assign urgency to a backlog of issues, bugs, tasks, alerts, or requests. Use when the user says "triage this", "help me prioritize", "what should I work on first", "sort these issues", "which of these is most urgent", or dumps a list of tasks/bugs/alerts and needs them ordered by priority. Also trigger when the user is overwhelmed with incoming work and needs a structured way to decide what to tackle and in what order.
---

# Triage

Fast, structured prioritization of multiple items. Output: an ordered, actionable priority list.

---

## Step 1 — Intake

Collect all items. If the user gives an unstructured dump (chat messages, meeting notes, email), extract each discrete item before scoring.

For each item capture:
- What is it? (one line description)
- Known severity / impact
- Known urgency / deadline
- Who is affected
- Any stated priority from the requester

---

## Step 2 — Score each item

Use the **Impact × Urgency matrix**:

| | Low Urgency | High Urgency |
|---|---|---|
| **High Impact** | Schedule (important, not urgent) | Do now (critical path) |
| **Low Impact** | Drop or defer | Delegate or batch |

Score each dimension:

**Impact** (what happens if this is NOT done):
- 3 — Production down, safety issue, customer-facing failure, revenue blocked
- 2 — Significant degradation, workaround exists but is painful
- 1 — Minor inconvenience, cosmetic, low-usage path

**Urgency** (time pressure):
- 3 — Must act now or within hours
- 2 — Must act this sprint / this week
- 1 — Can wait for next cycle

**Priority Score** = Impact × Urgency (max 9)

---

## Step 3 — Apply triage rules

Override scoring with these rules when applicable:

| Rule | Action |
|---|---|
| Safety issue | → Automatically P0, act immediately |
| Blocking another person/team | → Bump priority by 1 level |
| Quick win (< 30 min fix, score ≥ 4) | → Do it now, don't schedule |
| Duplicate of existing item | → Merge, don't create new ticket |
| No owner and low score | → Drop or park in backlog |
| Unclear item | → Ask one clarifying question, don't guess |

---

## Step 4 — Output the triage list

```
## Triage Results — [Date]

### 🔴 P0 — Do Immediately (score 7–9 or safety)
1. [ITEM] | Impact: 3 | Urgency: 3 | Score: 9
   → [One-line action]

### 🟠 P1 — Do This Sprint (score 4–6)
2. [ITEM] | Impact: 3 | Urgency: 2 | Score: 6
   → [One-line action]

### 🟡 P2 — Schedule (score 2–3, high impact / low urgency)
3. [ITEM] | Impact: 3 | Urgency: 1 | Score: 3
   → [When to tackle]

### ⚪ P3 — Defer / Drop (score 1 or low impact / low urgency)
4. [ITEM] | Impact: 1 | Urgency: 1 | Score: 1
   → Drop / Park in backlog / Revisit in [timeframe]

### ❓ Needs Clarification Before Triage
5. [ITEM] — Missing: [what info is needed]
```

---

## Triage for specific contexts

### Bug triage
Add: affected users count, reproducibility (always / sometimes / rare), regression or known issue.

### Alert / incident triage
Add: blast radius, data loss risk, SLA breach risk. P0 overrides everything.

### Feature request triage
Add: requestor count, strategic alignment, estimated effort. Score effort as inverse — high effort lowers priority unless impact is 3.

### Project task triage
Add: critical path dependency. Anything on critical path is automatically P1 or higher regardless of urgency score.

---

## Operating rules

- Triage is fast — don't over-analyze. Score in seconds, not minutes.
- If you can't score something, flag it as "needs clarification" — don't guess.
- Re-triage when context changes (new information, new blockers, scope change).
- Triage output expires — items that don't get worked shift in urgency over time.
- A P3 that keeps getting deferred is either wrongly scored or should be dropped.
