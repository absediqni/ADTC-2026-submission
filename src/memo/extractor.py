#Create Extractor
import ollama
import json

def extract_information(text):

    prompt = f"""
    Exract:

    - sender
    - department
    - budget
    - deadline
    - action_items

    Retun valid JSON only.

    Docuemnt: {text}
    """

    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {"role": "user",
            "content": prompt}
        ]
    )
    return json.loads(
        response['message']['content'].strip()
        )