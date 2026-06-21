#Create Classifier
import ollama

def classify_document(text):

    prompt = f"""
    Classify this document into one of:
    - Fund Request
    - Procurement Request
    - Leave Request
    - Travel Request
    - HR Memo
    - General Memo
    Return ONLY the category.

    document:
    {text}
    """
    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {"role": "user",
            "content": prompt}
        ]
    )
    return response['message']['content'].strip()