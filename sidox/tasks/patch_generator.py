import json
from datetime import datetime

with open("sidox/tasks/composed_patch.json") as f:
    patch = json.load(f)

generated = []

for item in patch["changes"]:
    if item["action"] == "create":
        generated.append({
            "file": item["file"],
            "type": "new_file",
            "content_plan": "Generate Kotlin class structure"
        })

    elif item["action"] == "modify":
        generated.append({
            "file": item["file"],
            "type": "modify",
            "content_plan": "Review and insert required feature changes"
        })

result = {
    "time": datetime.now().isoformat(),
    "mode": "proposal_only",
    "approved": False,
    "generated_changes": generated
}

with open("sidox/tasks/generated_patch.json","w") as f:
    json.dump(result,f,indent=2)

print(json.dumps(result,indent=2))
