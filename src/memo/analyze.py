from .classifier import classify_document
from .extractor import extract_information
from .prioritizer import determine_priority
from .workflow_engine import get_next_step

def analyze_document(text):
    doc_type = classify_document(text)
    details = extract_information(text)
    priority = determine_priority(text)
    next_step = get_next_step(doc_type)

    return {
        "document_type": doc_type,
        "priority": priority,
        "next_step": next_step,
        "details": details
    }