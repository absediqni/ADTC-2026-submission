#Connect Local LLM
import ollama
import time
#System prompt
SYSTEM_PROMPT = """
You are OpsMind AI.

You are an enterprise operations assistant.

Rules:

1. Answer only from supplied context.
2. Never mention "provided context".
3. Never mention retrieval.
4. Give concise operational answers.
5. Use bullet points when appropriate.
6. If information is missing, say:

"I could not find that information in the available documents."
"""


#Add chat function
def ask_llm(
        question: str,
        context: str
        ) -> str:
    """
    Ask the LLM a question with the provided context.
    """
    prompt = f"""
    Organizational Knowledge:

    {context}

    User Question:

    {question}

    Provide a concise operational answer.
    """
    # Track response time
    start = time.time()
    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    elapsed = time.time() - start
    print(f"LLM responded in {elapsed:.2f}s")
    
    return response.message.content or ""