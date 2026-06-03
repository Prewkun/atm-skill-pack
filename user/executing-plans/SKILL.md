---
name: executing-plans
description: Turn a plan, goal, or objective into an executable step-by-step action sequence with ownership, checkpoints, and risk flags. Use when the user says "help me execute this", "how do I actually do this", "break this into steps", "make a plan", "create an action plan", "how do I get from here to done", or has a goal and needs a concrete execution roadmap. Also trigger when a brainstorm or PRD needs to be turned into an ordered sequence of actions with accountabilities.
---

# Executing Plans

Turn intent into an ordered, executable action sequence. Output is a plan someone can actually follow.

---

## Step 1 — Establish the goal and current state

Before building the plan, confirm:

1. **End state** — what does done look like? (specific, observable)
2. **Current state** — what exists now? What's already done?
3. **Gap** — what needs to happen to get from current to end state?
4. **Constraints** — hard deadlines, budget, people available, dependencies
5. **Risks** — what could block or derail execution?

If the user hasn't defined done clearly, define it before building the plan.

---

## Step 2 — Identify phases

Chunk the gap into logical phases. Each phase has:
- A clear deliverable
- A start condition (what must be true before this phase starts)
- An end condition (how you know the phase is done)

Typical phase patterns:
- **Sequential** — each phase feeds the next (mandatory order)
- **Parallel** — phases can run simultaneously (identify these — they save time)
- **Iterative** — phases that repeat with feedback (prototyping, testing loops)

---

## Step 3 — Break phases into actions

Each action must be:
- **Specific** — clear enough that anyone can execute it without asking what it means
- **Owned** — one person or role responsible
- **Time-bounded** — has a deadline or duration
- **Verifiable** — you can check if it's done

Format:
```
[ ] ACTION-001: [Verb] [Object] [Qualifier if needed]
    Owner: [person/role]
    By: [date or relative timing]
    Done when: [observable condition]
    Depends on: [ACTION-XXX or none]
```

---

## Step 4 — Identify critical path

The critical path = the longest chain of sequential dependencies. Any delay on the critical path delays the whole plan.

Flag:
- **Critical path actions** — ⚠️ mark these
- **Float** — actions with slack (can slip without delaying the plan)
- **Parallel starters** — actions with no dependencies (start these immediately)

---

## Step 5 — Flag risks and mitigations

For each significant risk:
```
RISK: [What could go wrong]
Impact: High / Medium / Low
Probability: High / Medium / Low
Mitigation: [What to do now to reduce probability or impact]
Contingency: [What to do if it happens anyway]
```

---

## Step 6 — Define checkpoints

Checkpoints are scheduled moments to assess plan health. Not just "are we on schedule" — but "is the plan still the right plan?"

Each checkpoint:
- Has a specific date
- Reviews: progress vs. plan, risks, assumptions, scope
- Results in: continue / adjust / escalate

---

## Output format

```
## Execution Plan: [Goal]

**End State:** [What done looks like]
**Current State:** [Where we are now]
**Target Completion:** [Date]
**Owner:** [Lead]

---

### Phase 1: [Name]
**Deliverable:** [What comes out of this phase]
**Duration:** [X days/weeks]
**Start condition:** [What must be true]

Actions:
[ ] ACTION-001: ...
[ ] ACTION-002: ...

---

### Phase 2: [Name]
...

---

### Critical Path
Phase 1 → ACTION-003 → ACTION-007 → Phase 3

⚠️ Critical path actions: ACTION-003, ACTION-007

### Parallel Starters (start immediately)
- ACTION-001
- ACTION-005

### Risk Register
[Risks table]

### Checkpoints
| Date | What to review | Decision point |
|---|---|---|
| [date] | Phase 1 complete? | Proceed / Adjust |

```

---

## Operating rules

- Never build a plan without a clear end state — ask if it's missing
- Always identify what can start in parallel — parallel work compresses timelines
- Flag assumptions embedded in the plan explicitly
- If the plan has more than ~15 actions, use the `to-issues` skill to convert to tickets
- If the plan requires a formal document, use `to-prd` for the requirements first
- Revisit the plan at each checkpoint — a stale plan is worse than no plan
