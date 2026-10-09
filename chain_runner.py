from safe_evaluator import safe_eval

MAX_STEPS = 10

def mock_reasoner(question: str) -> list[dict]:
    return [{"text": "Calculate pencil cost", "expr": "4*12", "claimed": 48},
        {"text": "Calculate notebook cost", "expr": "3*25", "claimed": 75},
        {"text": "Add both costs", "expr": "48+75", "claimed": 123},
        {"text": "Apply voucher", "expr": "123-20", "claimed": 103}]

def run_chain(question: str, reasoner=mock_reasoner) -> dict:
    trace = []

    if not isinstance(question, str) or not question.strip():
        return {"answer": None, "trace": trace, "error": "Invalid question"}

    try:
        steps = reasoner(question)

        if not isinstance(steps, list) or not steps:
            raise ValueError("Reasoner must return a non-empty list")

        if len(steps) > MAX_STEPS:
            raise ValueError("Step limit exceeded")

        for i, step in enumerate(steps, 1):
            if not isinstance(step, dict):
                raise ValueError(f"Invalid step {i}")

            if not isinstance(step.get("text"), str) or not step["text"].strip():
                raise ValueError(f"Invalid thought at step {i}")

            if not isinstance(step.get("expr"), str):
                raise ValueError(f"Invalid expression at step {i}")

            claimed = step.get("claimed")
            if type(claimed) not in (int, float):
                raise ValueError(f"Invalid claimed value at step {i}")

            actual = safe_eval(step["expr"])
            verified = abs(actual - claimed) < 1e-9

            trace.append({
                "n": i,
                "thought": step["text"],
                "value": actual,
                "verified": verified,
            })

            if not verified:
                return {
                    "answer": None,
                    "trace": trace,
                    "error": f"Step {i} failed verification",
                }

        return {
            "answer": trace[-1]["value"],
            "trace": trace,
            "error": None,
        }

    except (ValueError, ZeroDivisionError, OverflowError) as error:
        return {"answer": None, "trace": trace, "error": str(error)}

if __name__ == "__main__":
    question = "4 pencils at 12 each, 3 notebooks at 25 each, and a 20 voucher. Total?"

    result = run_chain(question)

    for step in result["trace"]:
        print(step)

    print("Answer:", result["answer"])
    print("Error:", result["error"])
