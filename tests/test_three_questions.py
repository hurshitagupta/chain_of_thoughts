from chain_runner import run_chain
from three_questions import shopping_reasoner, travel_reasoner, salary_reasoner, run_questions

def test_shopping_question():
    result = run_chain("Calculate shopping cost", shopping_reasoner)

    assert result["answer"] == 500
    assert result["error"] is None
    assert len(result["trace"]) == 4

def test_travel_question():
    result = run_chain("Calculate remaining travel time", travel_reasoner)

    assert result["answer"] == 1
    assert result["error"] is None
    assert len(result["trace"]) == 3

def test_salary_question():
    result = run_chain("Calculate salary", salary_reasoner)

    assert result["answer"] == 12000
    assert result["error"] is None
    assert len(result["trace"]) == 3

def test_all_steps_verified():
    reasoners = [shopping_reasoner, travel_reasoner, salary_reasoner]

    for reasoner in reasoners:
        result = run_chain("Test question", reasoner)

        assert all(step["verified"] for step in result["trace"])

def test_summary_table():
    summary = run_questions()

    assert len(summary) == 3
    assert [item["answer"] for item in summary] == [500, 1, 12000]
    assert [item["steps"] for item in summary] == [4, 3, 3]

def test_wrong_claim_rejected():
    def wrong_salary_reasoner(question):
        return [{"text": "Weekly salary", "expr": "500*5", "claimed": 2500},
            {"text": "Monthly salary", "expr": "2500*4", "claimed": 11000},
            {"text": "Add bonus", "expr": "10000+2000", "claimed": 12000}]

    result = run_chain("Calculate salary", wrong_salary_reasoner)

    assert result["answer"] is None
    assert result["error"] == "Step 2 failed verification"
    assert len(result["trace"]) == 2
