from services.vectorstore import KBService
from tools.tool_registry import tools

kb = KBService()

def route_question(question: str) -> dict:
    # Step 1: Try querying the KB
    kb_result = kb.query(question)

    if kb_result and kb_result.get("score", 0) >= 0.75:
        return {
            "question": question,
            "answer": kb_result["answer"],
            "matched_question": kb_result["matched_question"],
            "score": kb_result["score"],
            "source": "Knowledge Base"
        }

    # Step 2: If no good KB match, try each registered tool
    for tool in tools:
        try:
            tool_output = tool.run(question)
            if tool_output:  # If tool returns a valid answer
                return {
                    "question": question,
                    "answer": tool_output,
                    "matched_question": None,
                    "score": None,
                    "source": f"Tool: {tool.name}"
                }
        except Exception as e:
            continue  # Skip tool if it fails

    # Step 3: Fallback if no tool works
    return {
        "question": question,
        "answer": None,
        "matched_question": None,
        "score": None,
        "source": "Not Answered by Any Tool"
    }
