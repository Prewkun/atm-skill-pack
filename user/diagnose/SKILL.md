---
name: diagnose
description: Systematic root-cause diagnosis for any broken system, process, or behavior. Use when the user says "why is X not working", "something is wrong with", "figure out why", "diagnose this", "what's causing", or describes unexpected behavior without a clear cause. Goes deeper than debug-mantra — covers hardware, software, process, integration, and mechanical systems. Trigger proactively whenever the user presents symptoms without a known cause.
---

# Diagnose

Structured diagnosis workflow. Goal: identify root cause before proposing any fix.

---

## Phase 0 — Characterize the symptom

Before touching anything, nail down exactly what is observed vs. expected.

Answer these:
1. **What exactly happens?** (error message, wrong output, physical behavior)
2. **What was expected?**
3. **When did it start?** (always, after change X, intermittent)
4. **What changed recently?** (code, config, hardware, environment, operator)
5. **Is it reproducible?** (always / sometimes / once)
6. **What is the scope?** (one unit, one line, all machines, specific conditions)

Do not skip this phase. Vague symptoms = wasted diagnosis effort.

---

## Phase 1 — Bound the problem space

Split the system into functional blocks. Identify which blocks are:
- **Confirmed good** — verified by data, not assumption
- **Confirmed bad** — verified by data
- **Unknown** — not yet tested

Draw the boundary between known-good and known-bad. The fault lives at or just past that boundary.

Techniques:
- Half-split / binary search the signal chain
- Swap a known-good unit into the suspect position
- Inject a known-good signal at each stage and observe output
- Compare a working instance vs. broken instance — diff the differences

---

## Phase 2 — Generate hypotheses

List 3–5 candidate root causes ranked by:
1. **Probability** — what commonly fails here?
2. **Fit** — does it fully explain all observed symptoms?
3. **Testability** — can it be proven/disproven quickly?

Format:
```
H1: [Hypothesis] — explains [symptom] because [mechanism] — test by [method]
H2: ...
```

Rule: A hypothesis must explain **all** symptoms, not just one. If it only explains part, it's incomplete.

---

## Phase 3 — Test hypotheses (fastest disproof first)

Run the cheapest disproof first. Surviving hypotheses get more expensive tests.

For each test:
- State what you predict will happen if hypothesis is TRUE
- State what you predict if FALSE
- Run the test
- Record the result — update your hypothesis ranking

Do not run confirmatory tests only. Always design a test that can **kill** the hypothesis.

---

## Phase 4 — Identify root cause

Root cause criteria:
- Explains 100% of observed symptoms
- Survives all disproof attempts
- Has a plausible mechanism (not just correlation)
- Fixing it would prevent recurrence (not just mask symptoms)

If no single root cause satisfies all criteria → you have a **multi-factor failure**. Document all contributing factors.

---

## Phase 5 — State the finding

Output format:

```
ROOT CAUSE: [One clear sentence]

MECHANISM: [How the root cause produces the symptoms — step by step]

EVIDENCE: [What data confirms this]

CONTRIBUTING FACTORS: [Anything that made the failure more likely or harder to detect]

FIX: [What to change to resolve it]

RECURRENCE PREVENTION: [What to add/change so it doesn't happen again]
```

---

## Operating rules

- Never propose a fix before Phase 4 is complete.
- If asked "what's wrong?" without enough symptom data, run Phase 0 as a Q&A with the user.
- If the system is hardware/mechanical: pay extra attention to boundary conditions — temperature, wear, contamination, tolerance stack-up.
- If the system is software/integration: check assumptions at every interface — data types, timing, auth, encoding.
- If intermittent: suspect timing, load, temperature, or resource contention first.
- Distinguish **symptom** from **root cause** at every step. Fixing a symptom is not a fix.
