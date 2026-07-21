import json
from datetime import datetime

task = input("Sidox Task: ")

result = {
    "time": datetime.now().isoformat(),
    "task": task,
    "status": "analyzed",
    "plan": [
        "Understand requested feature",
        "Find related project files",
        "Prepare safe patch proposal"
    ]
}

with open("sidox/tasks/latest_task.json", "w") as f:
    json.dump(result, f, indent=2)

print("Task analyzed:")
print(json.dumps(result, indent=2))
