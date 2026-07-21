import json
from datetime import datetime
import os

with open("sidox/tasks/latest_task.json") as f:
    task = json.load(f)

with open("sidox/tasks/patch_analysis.json") as f:
    analysis = json.load(f)

text = task["task"].lower()

plan = []

for item in analysis["analysis"]:
    file = item["file"]
    name = os.path.basename(file).lower()
    score = 0

    if "driver" in name:
        score += 10
    if "ride" in name:
        score += 8
    if "repository" in name:
        score += 5
    if "database" in name:
        score += 5
    if "viewmodel" in name:
        score += 5

    for key in item["contains"]:
        if key in ["Repository", "Database", "ViewModel"]:
            score += 2

    if "driver" in text and any(x in name for x in ["search", "nominatim", "location"]):
        score -= 3

    if score > 0:
        plan.append({
            "file": file,
            "score": score,
            "action": "review_modify"
        })

plan.sort(key=lambda x: x["score"], reverse=True)

result = {
    "time": datetime.now().isoformat(),
    "task": task["task"],
    "decision": plan,
    "status": "decision_filename_improved"
}

with open("sidox/tasks/decision.json","w") as f:
    json.dump(result,f,indent=2)

print(json.dumps(result,indent=2))
