import json
import os
from datetime import datetime

with open("sidox/tasks/latest_task.json") as f:
    task = json.load(f)

with open("sidox/tasks/decision.json") as f:
    decision = json.load(f)

text = task["task"].lower()

new_files = []

if "driver" in text:
    candidates = [
        "Driver.kt",
        "DriverRepository.kt",
        "DriverViewModel.kt"
    ]

    for file in candidates:
        exists = False

        for item in decision.get("decision", []):
            if file.lower() in item["file"].lower():
                exists = True

        if not exists:
            new_files.append({
                "file": "./app/src/main/java/com/oranride/app/" + file,
                "action": "create",
                "reason": "Required for driver system"
            })

if "ride" in text:
    new_files.append({
        "file": "./app/src/main/java/com/oranride/app/Ride.kt",
        "action": "create",
        "reason": "Ride data model"
    })

result = {
    "time": datetime.now().isoformat(),
    "task": task["task"],
    "new_files": new_files,
    "status": "new_file_plan_created"
}

with open("sidox/tasks/new_file_plan.json","w") as f:
    json.dump(result,f,indent=2)

print(json.dumps(result,indent=2))
