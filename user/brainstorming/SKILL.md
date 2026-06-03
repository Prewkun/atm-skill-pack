---
name: brainstorming
description: Structured ideation and creative problem-solving. Use when the user says "brainstorm", "what are my options", "how might we", "give me ideas for", "what are alternatives to", "help me think through", or needs to generate and evaluate multiple solution approaches before committing. Works for engineering concepts, process design, system architecture, product features, and problem-solving. Trigger proactively when a user is stuck or facing a decision with multiple valid paths.
---

# Brainstorming

Generate, organize, and evaluate ideas systematically. Output is a set of options with enough clarity to make a decision.

---

## Phase 1 — Frame the problem

Before generating ideas, lock in the frame:

1. **Core question** — what exactly are we trying to solve? (One sentence)
2. **Constraints** — what can't be changed? (budget, space, timeline, interfaces, standards)
3. **Success criteria** — what does a good solution look like?
4. **Anti-goals** — what would make a solution bad? (avoid bias toward confirming existing ideas)

If the user's framing is vague, ask 1–2 clarifying questions before proceeding.

---

## Phase 2 — Generate ideas (diverge)

Generate broadly. No filtering yet. Quantity over quality at this stage.

Techniques to apply (pick what fits):

**Vary the approach axis:**
- Mechanical / Electrical / Software / Process / Human / Hybrid
- Active vs. Passive
- Prevent vs. Detect vs. Correct
- Centralized vs. Distributed

**Apply first principles:**
- What is the fundamental goal? Strip away assumed constraints.
- What would you do if current method didn't exist?

**Borrow from adjacent domains:**
- How does a different industry solve an equivalent problem?

**Invert:**
- What would make this problem worse? Now reverse it.

**Extremes:**
- What if budget were unlimited? What if budget were near zero?
- What if it had to last 10 years? What if it only needed to work once?

Target: 6–12 distinct ideas minimum before filtering.

---

## Phase 3 — Organize and cluster

Group ideas by:
- Approach type (mechanical, software, process, etc.)
- Risk level (proven vs. novel)
- Cost range
- Implementation complexity

Remove clear duplicates. Merge similar ideas.

---

## Phase 4 — Evaluate and rank

Score each viable idea against the success criteria and constraints.

Quick scoring matrix:

| Idea | Feasibility | Cost | Risk | Fit to Goal | Score |
|---|---|---|---|---|---|
| Idea A | H/M/L | H/M/L | H/M/L | H/M/L | Σ |

Or use a simple 1–5 per criterion if more precision needed.

Highlight:
- **Top pick** — best overall fit
- **Safe default** — lowest risk, proven approach
- **Bold bet** — highest upside, highest risk
- **Quick win** — can be done now with least effort

---

## Phase 5 — Output

```
## Brainstorm: [Topic]

### Problem Frame
[One sentence core question]
Constraints: [list]
Success criteria: [list]

### Ideas Generated
1. [Idea name] — [one line description]
2. ...
(full list, unfiltered)

### Shortlist

#### Option A: [Name] ⭐ Recommended
[Description, how it works, why it scores well]
Pros: ...
Cons: ...
Risk: Low / Medium / High

#### Option B: [Name] — Safe Default
...

#### Option C: [Name] — Bold Bet
...

### Recommendation
[Which to pursue and why, given the constraints]

### Next Step
[What decision needs to be made, or what to prototype/investigate first]
```

---

## Operating rules

- Don't anchor on the user's first idea — treat it as one option, not the default
- Don't filter ideas during generation phase
- Always present at least 3 distinct options — even if one is clearly best
- Label the recommendation clearly but don't hide the tradeoffs
- If the user wants to go deeper on one idea: pivot to `executing-plans` or `to-prd`
