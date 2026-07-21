import json
import os
from datetime import datetime

with open("sidox/tasks/latest_task.json") as f:
    task = json.load(f)

with open("sidox/tasks/selected_files.json") as f:
    files = json.load(f)

analysis = []

for file in files.get("selected_files", []):
    if os.path.exists(file):
        with open(file, "r", errors="ignore") as f:
            content = f.read()

        item = {
            "file": file,
            "size": len(content),
            "contains": []
        }

        for keyword in ["class", "data", "ViewModel", "Repository", "Database", "Map", "Location"]:
            if keyword in content:
                item["contains"].append(keyword)

        analysis.append(item)

result = {
    "time": datetime.now().isoformat(),
    "task": task["task"],
    "analysis": analysis,
    "status": "content_analyzed"
}

with open("sidox/tasks/patch_analysis.json","w") as f:
    json.dump(result,f,indent=2)

print(json.dumps(result,indent=2))
