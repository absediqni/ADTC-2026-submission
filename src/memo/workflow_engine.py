#Create Workflow Engine
import json

with open(
    "config/workflow_rule.json"
    ) as f:
    RULES = json.load(f)
def get_next_step(document_type):

    workflow = RULES.get(
        document_type,
        {})
    steps = workflow.get(
        "steps",
        []
        )
    if steps:
        return steps[0]
    return "Unknown"
    