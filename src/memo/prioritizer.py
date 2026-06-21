#Create Priority Engine
def determine_priority(text):
    text = text.lower()
    if "urgent" in text:
        return "Critical"
    if "immediately" in text:
        return "Critical"
    if "Within 24 hours" in text:
        return "High"
    if "deadline" in text:
        return "Medium"
    return "Low"