import json
from agents.router import route_question

def benchmark(file_path="data/jee_dataset.json"):
    with open(file_path, "r") as f:
        dataset = json.load(f)

    correct = 0
    total = len(dataset)
    detailed_results = []

    for item in dataset:
        question = item["question"]
        expected = item["answer"]
        result = route_question(question)
        predicted = result.get("answer", "")
        matched_question = result.get("matched_question", "")
        score = result.get("score", 0)

        is_correct = expected.lower().strip() in predicted.lower().strip()
        if is_correct:
            correct += 1

        detailed_results.append({
            "question": question,
            "expected": expected,
            "predicted": predicted,
            "matched_question": matched_question,
            "score": score,
            "is_correct": is_correct
        })

    accuracy = correct / total * 100
    print(f"\n🧪 Benchmarking Complete:")
    print(f"Total: {total}, Correct: {correct}, Accuracy: {accuracy:.2f}%\n")

    for res in detailed_results:
        print(f"Q: {res['question']}")
        print(f"✅ Match: {res['is_correct']}")
        print(f"Expected: {res['expected']}")
        print(f"Predicted: {res['predicted']}")
        print(f"Score: {res['score']}")
        print("------")

    return {"accuracy": accuracy, "results": detailed_results}
