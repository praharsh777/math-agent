import json
from datetime import datetime

FEEDBACK_FILE = "feedback_log.jsonl"

def save_feedback(question: str, answer: str, feedback: str):
    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "question": question,
        "answer": answer,
        "feedback": feedback
    }
    with open(FEEDBACK_FILE, "a") as f:
        f.write(json.dumps(record) + "\n")
