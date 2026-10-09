# Task 5 — Why Step-by-Step Verification Is Safer

## 1. Introduction

In this project, chain of thought is represented as a sequence of structured steps. Each step contains a description, a mathematical expression, and a claimed result.

Instead of directly trusting the final answer, the system verifies every calculation using the `safe_eval()` function.

## 2. Why Is Step-by-Step Verification Safer?

Step-by-step verification is safer for the following reasons:

1. **Early error detection:** If a calculation is incorrect, the system identifies the mistake immediately rather than continuing with an incorrect value.

2. **Traceability:** Each step is recorded with its calculated value and verification status, making it easier to understand where an error occurred.

3. **Prevents incorrect answers:** The system returns a final answer only when all arithmetic claims are verified.

4. **Safe execution:** The `safe_eval()` function allows only supported arithmetic operations and rejects unsafe expressions such as `open('x')` or `__import__('os')`.

5. **Controlled execution:** The chain runner enforces a maximum step limit, validates inputs, and stops when verification fails.

## 3. Example of a Plausible but Wrong Step

Consider a shopping problem:

A customer purchases 4 pencils costing ₹12 each and 3 notebooks costing ₹25 each. A ₹20 voucher is applied.

The reasoning steps are:

| Step | Expression | Claimed Value | Actual Value | Status |
|---|---|---|---|---|
| 1 | 4 × 12 | 48 | 48 | Verified |
| 2 | 3 × 25 | 75 | 75 | Verified |
| 3 | 48 + 75 | 125 | 123 | Failed |
| 4 | 123 − 20 | 103 | 103 | Not executed |

In Step 3, the reasoner claims that `48 + 75 = 125`, which appears plausible but is mathematically incorrect.

The evaluator calculates the correct value of `123` and compares it with the claimed value of `125`.

Since the values do not match, the runner stops at Step 3 and returns:

```text
Answer: None
Error: Step 3 failed verification
Steps executed: 3
```

This prevents the system from accepting an incorrect intermediate calculation.

##  Conclusion

Verifying each step is safer than blindly trusting the final answer because it detects incorrect calculations, provides a clear verification trace, and prevents unverified results from being returned.

The implementation demonstrates this through a safe arithmetic evaluator, a bounded chain runner, error handling, and automated tests.