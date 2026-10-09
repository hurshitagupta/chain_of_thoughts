from chain_runner import run_chain
from wrong_step import wrong_reasoner

def test_wrong_step_detected():
    result = run_chain("Calculate shopping total", wrong_reasoner)

    assert result["answer"] is None
    assert result["error"] == "Step 3 failed verification"

def test_stops_at_step_three():
    result = run_chain("Calculate total", wrong_reasoner)

    assert len(result["trace"]) == 3
    assert result["trace"][0]["verified"] is True
    assert result["trace"][1]["verified"] is True
    assert result["trace"][2]["verified"] is False

def test_wrong_claim():
    result = run_chain("Calculate total", wrong_reasoner)

    assert result["trace"][2]["value"] == 123
    assert result["trace"][2]["verified"] is False

def test_invalid_expression():
    def invalid_reasoner(question):
        return [{"text": "Invalid calculation", "expr": "10/0", "claimed": 5}]

    result = run_chain("Calculate total", invalid_reasoner)

    assert result["answer"] is None
    assert result["error"] == "Division by zero"

def test_invalid_claim_type():
    def invalid_reasoner(question):
        return [{"text": "Calculate total", "expr": "2+2", "claimed": "4"}]

    result = run_chain("Calculate total", invalid_reasoner)

    assert result["answer"] is None
    assert result["error"] == "Invalid claimed value at step 1"
