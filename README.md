# Chain of Thought Verification System

## Project Overview

This project implements a simple Chain of Thought Verification System using Python. It represents reasoning as a sequence of structured steps and verifies each calculation before accepting the final answer.

Each step contains:
- **Thought:** Description of the reasoning step.
- **Expression:** Mathematical calculation to perform.
- **Claimed Value:** Result provided by the reasoner.

The system uses Python's `ast` module to safely evaluate expressions without using `eval()` or `exec()`.

If a step contains an incorrect calculation, the system stops immediately and reports the failed step.

## Project Structure

```text
chain_of_thought/
│
├── safe_evaluator.py
├── chain_runner.py
├── wrong_step.py
├── three_questions.py
├── explanation_topic5.md
│
├── tests/
│   ├── test_safe_evaluator.py
│   ├── test_chain_runner.py
│   ├── test_wrong_step.py
│   └── test_three_questions.py
│
├── outputs/
│   ├── safe_evaluator_output.txt
│   ├── test_safe_evaluator.txt
│   ├── chain_runner_output.txt
│   ├── test_chain_runner.txt
│   ├── wrong_step_output.txt
│   ├── test_wrong_step.txt
│   ├── three_questions_output.txt
│   ├── test_three_questions.txt
│
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.11 or newer
- pytest

No API key or external LLM is required. The project uses deterministic mock reasoners.

## Installation

**1. Open the project folder**

```bash
cd chain_of_thought
```

**2. Create and activate a virtual environment (optional)**

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains:

```text
pytest
```

## Implementation

### Task 1 — Safe Evaluator

**File:** `safe_evaluator.py`

Implemented `safe_eval()` using Python's `ast` module.

Features:
- Supports addition, subtraction, multiplication, and division.
- Rejects unsafe expressions, function calls, and unsupported operators.
- Handles division by zero and invalid inputs.
- Applies expression length and depth limits.

Run:

```bash
python safe_evaluator.py
```

### Task 2 — Chain Runner

**File:** `chain_runner.py`

Implemented `run_chain()` to verify structured reasoning steps.

Features:
- Receives reasoning steps from a mock reasoner.
- Evaluates each mathematical expression.
- Compares actual and claimed values.
- Records each step in a verification trace.
- Returns the final answer only when every step passes.
- Enforces a maximum of 10 steps.

Run:

```bash
python chain_runner.py
```

**Expected final result:**

```text
Answer: 103
Error: None
```

### Task 3 — Wrong Step Detection

**File:** `wrong_step.py`

Introduced an incorrect claimed value at Step 3.

The reasoner claims:

```text
48 + 75 = 125
```

However, the actual result is `123`.

The system detects the mismatch and stops immediately.

**Expected result:**

```text
Answer: None
Error: Step 3 failed verification
Steps executed: 3
```

Run:

```bash
python wrong_step.py
```

### Task 4 — Three Word Problems

**File:** `three_questions.py`

Implemented three different problems using separate mock reasoners.

| Problem | Expected Answer | Steps |
|---|---|---|
| Shopping calculation | ₹500 | 4 |
| Travel time | 1 hour | 3 |
| Salary calculation | ₹12,000 | 3 |

Each problem produces a verification trace containing the calculated value and verification status.

Run:

```bash
python three_questions.py
```

The program also prints a summary table containing the question number, final answer, and executed steps.

### Task 5 — Explanation

**File:** `explanation.md`

Explains:
- Why verifying intermediate steps is safer than trusting only the final answer.
- How the system detects incorrect calculations.
- A realistic example of a plausible but incorrect step.


## Testing

All test cases are written using pytest.

Run individual test files:

```bash
python -m pytest tests/test_safe_evaluator.py -q
python -m pytest tests/test_chain_runner.py -q
python -m pytest tests/test_wrong_step.py -q
python -m pytest tests/test_three_questions.py -q
```

Run all tests:

```bash
python -m pytest tests/ -q
```

## Guardrails

| Guardrail | Implementation |
|---|---|
| Step limit | Maximum 10 reasoning steps |
| Input validation | Validates questions, expressions, and claimed values |
| Safe execution | Uses `ast` instead of `eval()` or `exec()` |
| Error handling | Returns clear error messages |
| Determinism | Uses predefined mock reasoners |
| Secret hygiene | No hardcoded API keys or credentials |





