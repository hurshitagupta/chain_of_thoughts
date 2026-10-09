from chain_runner import run_chain, MAX_STEPS

def test_correct_chain():
    result = run_chain("Calculate shopping total")

    assert result["answer"] == 103
    assert result["error"] is None
    assert len(result["trace"]) == 4
    assert all(step["verified"] for step in result["trace"])

def test_trace_structure():
    result = run_chain("Calculate total")
    first_step = result["trace"][0]

    assert first_step["n"] == 1
    assert first_step["thought"] == "Calculate pencil cost"
    assert first_step["value"] == 48
    assert first_step["verified"] is True

def test_empty_question():
    result = run_chain("")

    assert result["answer"] is None
    assert result["error"] == "Invalid question"

def test_empty_steps():
    result = run_chain("Calculate total", lambda question: [])

    assert result["answer"] is None
    assert result["error"] == "Reasoner must return a non-empty list"

def test_step_limit():
    def long_reasoner(question):
        return [{"text": "Add numbers", "expr": "2+2", "claimed": 4}
            for _ in range(MAX_STEPS + 1)]

    result = run_chain("Calculate total", long_reasoner)

    assert result["answer"] is None
    assert result["error"] == "Step limit exceeded"

def test_invalid_claim():
    def invalid_reasoner(question):
        return [{"text": "Add numbers", "expr": "2+2", "claimed": "four"}]

    result = run_chain("Calculate total", invalid_reasoner)

    assert result["answer"] is None
    assert result["error"] == "Invalid claimed value at step 1"

def test_unsafe_expression():
    def unsafe_reasoner(question):
        return [{"text": "Run function", "expr": "open('x')", "claimed": 5}]

    result = run_chain("Calculate total", unsafe_reasoner)

    assert result["answer"] is None
    assert result["error"] == "Unsupported expression"
