import json
from datetime import datetime

with open("sidox/tasks/decision.json") as f:
    decision = json.load(f)

with open("sidox/tasks/new_file_plan.json") as f:
    new_files = json.load(f)

patch = {
    "created": datetime.now().isoformat(),
    "mode": "proposal_only",
    "approved": False,
    "modify_files": [],
    "create_files": [],
    "changes": []
}

for item in decision.get("decision", []):
    patch["modify_files"].append(item["file"])
    patch["changes"].append({
        "file": item["file"],
        "action": "modify",
        "reason": "Selected by decision engine"
    })

for item in new_files.get("new_files", []):
    patch["create_files"].append(item["file"])
    patch["changes"].append({
        "file": item["file"],
        "action": "create",
        "reason": item["reason"]
    })

with open("sidox/tasks/composed_patch.json","w") as f:
    json.dump(patch,f,indent=2)

print(json.dumps(patch,indent=2))
