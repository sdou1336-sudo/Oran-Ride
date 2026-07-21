import os
import shutil
import json
from datetime import datetime

targets = [
    os.path.expanduser("~/.gradle/caches"),
    "./app/build",
    "./build"
]

result = {
    "time": datetime.now().isoformat(),
    "cleaned": [],
    "failed": []
}

for target in targets:
    try:
        if os.path.exists(target):
            shutil.rmtree(target)
            result["cleaned"].append(target)
    except Exception as e:
        result["failed"].append({
            "path": target,
            "error": str(e)
        })

with open("sidox/tasks/storage_repair_report.json","w") as f:
    json.dump(result,f,indent=2)

print(json.dumps(result,indent=2))
