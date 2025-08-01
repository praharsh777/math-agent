from fastapi import FastAPI, Query, Body
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from agents.router import route_question
from services.feedback import save_feedback  #  Feedback service

app = FastAPI(title="Math Routing Agent")

#  Enable CORS (for frontend access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (dev mode)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#  Response model for /ask
class AskResponse(BaseModel):
    question: str
    answer: str | None
    score: float | None = None
    matched_question: str | None = None
    source: str

#  Request model for /feedback
class FeedbackRequest(BaseModel):
    question: str
    answer: str
    feedback: str  # e.g., "good", "bad", "unclear"

#  Guardrail function to allow only math questions
def is_math_question(q: str) -> bool:
    math_keywords = [
        "derivative", "integral", "limit", "log", "solve", "equation", "algebra",
        "x", "y", "+", "-", "*", "/", "^", "∫", "√", "sin", "cos", "tan"
    ]
    return any(kw in q.lower() for kw in math_keywords)

# Main Q&A endpoint
@app.get("/ask", response_model=AskResponse)
def ask(q: str = Query(..., description="Your math question")):
    if not is_math_question(q):
        return AskResponse(
            question=q,
            answer=None,
            matched_question=None,
            score=None,
            source="Rejected: Not a math question"
        )
    
    result = route_question(q)
    return AskResponse(**result)

#  Health check
@app.get("/health")
def health():
    return {"status": "ok"}

#  Feedback logging endpoint
@app.post("/feedback")
def feedback(data: FeedbackRequest):
    save_feedback(data.question, data.answer, data.feedback)
    return {"status": "feedback recorded"}
