from fastapi import FastAPI, Query
from pydantic import BaseModel
from services.vectorstore import KBService
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Math Routing Agent")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only, allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

kb = KBService()

class AskResponse(BaseModel):
    question: str
    answer: str | None
    score: float | None = None
    matched_question: str | None = None
    source: str

@app.get("/ask", response_model=AskResponse)
def ask(q: str = Query(..., description="Your math question")):
    result = kb.query(q)
    if not result:
        return AskResponse(
            question=q,
            answer=None,
            matched_question=None,
            score=None,
            source="Not Found in KB"
        )
    return AskResponse(
        question=q,
        answer=result["answer"],
        matched_question=result["matched_question"],
        score=result["score"],
        source="Knowledge Base"
    )

@app.get("/health")
def health():
    return {"status": "ok"}
