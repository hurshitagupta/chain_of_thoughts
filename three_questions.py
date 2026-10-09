from chain_runner import run_chain

def shopping_reasoner(question: str) -> list[dict]:
    return [
        {"text": "Calculate book cost", "expr": "3*150", "claimed": 450},
        {"text": "Calculate pen cost", "expr": "5*20", "claimed": 100},
        {"text": "Add total cost", "expr": "450+100", "claimed": 550},
        {"text": "Apply discount", "expr": "550-50", "claimed": 500},
    ]

def travel_reasoner(question: str) -> list[dict]:
    return [
        {"text": "Calculate distance", "expr": "60*3", "claimed": 180},
        {"text": "Calculate remaining distance", "expr": "240-180", "claimed": 60},
        {"text": "Calculate remaining time", "expr": "60/60", "claimed": 1},
    ]

def salary_reasoner(question: str) -> list[dict]:
    return [
        {"text": "Calculate weekly salary", "expr": "500*5", "claimed": 2500},
        {"text": "Calculate monthly salary", "expr": "2500*4", "claimed": 10000},
        {"text": "Add bonus", "expr": "10000+2000", "claimed": 12000},
    ]

QUESTIONS = [
    ("3 books at Rs.150 each and 5 pens at Rs.20 each, with a Rs.50 discount. Find the total.", shopping_reasoner),
    ("A car travels at 60 km/h for 3 hours. For a 240 km journey, how many hours remain at the same speed?", travel_reasoner),
    ("An employee earns Rs.500 per day, works 5 days per week for 4 weeks, and receives a Rs.2000 bonus. Find the total salary.", salary_reasoner)]

def run_questions():
    summary = []

    for question, reasoner in QUESTIONS:
        result = run_chain(question, reasoner)

        print("\nQuestion:", question)
        print("Verification Trace:")

        for step in result["trace"]:
            print(step)

        print("Answer:", result["answer"])
        print("Error:", result["error"])

        summary.append({"question": question, "answer": result["answer"], "steps": len(result["trace"])})

    return summary

if __name__ == "__main__":
    summary = run_questions()

    print("\nSUMMARY TABLE")
    print(f"{'Question':<15} {'Answer':<10} {'Steps':<5}")

    for i, item in enumerate(summary, 1):
        print(f"{'Question ' + str(i):<15} {str(item['answer']):<10} {item['steps']:<5}")
