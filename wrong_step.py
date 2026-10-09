from chain_runner import run_chain

def wrong_reasoner(question: str) -> list[dict]:
    return [
        {"text": "Calculate pencil cost", "expr": "4*12", "claimed": 48},
        {"text": "Calculate notebook cost", "expr": "3*25", "claimed": 75},
        {"text": "Add both costs", "expr": "48+75", "claimed": 125},
        {"text": "Apply voucher", "expr": "123-20", "claimed": 103},
    ]

if __name__ == "__main__":
    question = "4 pencils at 12 each, 3 notebooks at 25 each, and a 20 voucher. Total?"

    result = run_chain(question, wrong_reasoner)

    print("Verification Trace:")

    for step in result["trace"]:
        print(step)

    print("Answer:", result["answer"])
    print("Error:", result["error"])
    print("Steps executed:", len(result["trace"]))
