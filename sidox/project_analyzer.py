import os
import json
from datetime import datetime

result = {
    "time": datetime.now().isoformat(),
    "project": "Oran-Ride",
    "files": {
        "kotlin": [],
        "gradle": [],
        "ui": [],
        "map": [],
        "search": []
    }
}

for root, dirs, files in os.walk("."):
    if ".git" in root or "build" in root:
        continue

    for file in files:
        path = os.path.join(root, file)

        if file.endswith(".kt"):
            result["files"]["kotlin"].append(path)

        if "gradle" in file.lower():
            result["files"]["gradle"].append(path)

        if any(x in path.lower() for x in ["ui", "layout", "screen", "activity"]):
            result["files"]["ui"].append(path)

        if any(x in path.lower() for x in ["map", "gps", "location"]):
            result["files"]["map"].append(path)

        if "search" in path.lower():
            result["files"]["search"].append(path)

os.makedirs("sidox/reports", exist_ok=True)

with open("sidox/reports/project_map.json", "w") as f:
    json.dump(result, f, indent=2)

print("Project analysis completed")
