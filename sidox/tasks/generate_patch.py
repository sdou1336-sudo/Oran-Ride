import json
from datetime import datetime
import os

with open("sidox/tasks/latest_task.json") as f:
    task = json.load(f)

with open("sidox/tasks/selected_files.json") as f:
    files = json.load(f)

targets = []

for file in files["selected_files"]:
    targets.append({
        "file": file,
        "reason": "Related to requested feature",
        "action": "review_and_modify"
    })

patch = {
    "created": datetime.now().isoformat(),
    "mode": "proposal_only",
    "approved": False,
    "task": task["task"],
    "targets": targets,
    "changes": [],
    "confidence": "medium",
    "note": "Waiting for approval before applying changes."
}

os.makedirs("sidox/tasks/patches", exist_ok=True)

with open("sidox/tasks/patches/latest_patch.json", "w") as f:
    json.dump(patch, f, indent=2)

print("Improved patch proposal created")
print(json.dumps(patch, indent=2))
