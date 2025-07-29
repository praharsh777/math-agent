import os, json
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.schema import Document

load_dotenv()

DATA_PATH = os.path.join(os.path.dirname(__file__), "../data/math_data.json")
SIMILARITY_THRESHOLD = float(os.getenv("SIMILARITY_THRESHOLD", "0.78"))

class KBService:
    def __init__(self):
        self.db = None
        self._load_index()

    def _load_index(self):
        with open(DATA_PATH, "r") as f:
            raw = json.load(f)
        docs = [
            Document(page_content=q["question"], metadata={"answer": q["answer"]})
            for q in raw
        ]
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.db = FAISS.from_documents(docs, embeddings)

    def query(self, question: str):
        if not self.db:
            return None
        results = self.db.similarity_search_with_relevance_scores(question, k=1)
        if not results:
            return None
        doc, score = results[0]
        if score < SIMILARITY_THRESHOLD:
            return None
        return {
            "answer": doc.metadata["answer"],
            "matched_question": doc.page_content,
            "score": score
        }
