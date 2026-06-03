---
name: tdd
description: Test-driven development workflow — write the test first, make it pass, then refactor. Trigger when the user says "TDD", "test-driven", "write tests first", "red-green-refactor", "help me build this with tests", or asks to implement a feature or function using a test-first approach. Also trigger when user asks to add tests to existing code before modifying it.
---

# TDD — Test-Driven Development

Strict Red → Green → Refactor loop. No production code without a failing test first.

---

## The Loop

```
RED    → Write a failing test for the next smallest behavior
GREEN  → Write the minimum code to make it pass (no more)
REFACTOR → Clean up — code and tests — without changing behavior
REPEAT
```

One cycle = one behavior. Keep cycles short (minutes, not hours).

---

## Phase RED — Write the failing test

Before writing any implementation:

1. **Name the behavior** — what should the unit do in one sentence?
2. **Write the test** — assert the expected output/behavior
3. **Run it** — confirm it FAILS (red). If it passes already, the test is wrong or the feature already exists.
4. **Read the failure message** — it should be clear and point at what's missing

Test anatomy:
```
Arrange  — set up inputs and dependencies
Act      — call the unit under test
Assert   — verify the output/behavior
```

Rules:
- One assertion per test (or one logical concept)
- Test behavior, not implementation
- Test name = readable description: `should_return_error_when_input_is_empty`
- No production code until the test is red and readable

---

## Phase GREEN — Make it pass (minimum viable)

Write the **simplest possible code** that makes the test pass.

- Hardcode a return value if that's all it takes — you'll be forced to generalize later by the next test
- No premature generalization
- No "while I'm here" additions
- Run all tests — the new one must pass, existing ones must not break

If an existing test breaks: stop. Fix the regression before adding anything.

---

## Phase REFACTOR — Clean without changing behavior

Tests are green. Now improve the code:

- Remove duplication
- Improve naming
- Simplify logic
- Extract functions/classes if needed
- Clean up the tests too — they're production code

Run tests after every change. If anything goes red: revert, understand why, try again.

---

## Workflow for a new feature

```
1. Break the feature into the smallest testable behaviors (list them)
2. Pick the simplest one first
3. RED → GREEN → REFACTOR
4. Pick the next behavior
5. Repeat until feature is complete
```

When decomposing behaviors, prefer:
- Happy path first
- Then edge cases
- Then error cases
- Then boundary conditions

---

## Workflow for modifying existing code

Before changing anything:
1. Write a test that covers the current behavior you're about to touch
2. Confirm it passes (green)
3. Now make your change — the test is your safety net
4. Refactor

This is called **characterization testing** — lock in existing behavior before modifying.

---

## Common traps

| Trap | Fix |
|---|---|
| Writing too much code in GREEN | Ask: "what's the minimum?" |
| Testing implementation details | Test inputs/outputs only |
| Skipping REFACTOR | Tech debt accumulates fast — don't skip |
| Giant test cycles | Smaller behaviors = smaller cycles |
| No failing test before code | That's not TDD — go back to RED |

---

## Output format when helping with TDD

For each cycle, show:

```
=== RED ===
[test code]
Expected failure: [what error you expect]

=== GREEN ===
[minimum implementation]
All tests pass: ✓

=== REFACTOR ===
[cleaned up version]
All tests still pass: ✓
```
