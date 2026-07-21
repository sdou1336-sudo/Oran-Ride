import json
import os
import shutil
from datetime import datetime

with open("sidox/tasks/generated_patch.json") as f:
    patch = json.load(f)

snapshot_dir = "sidox/tasks/snapshots/snapshot_" + datetime.now().strftime("%Y%m%d_%H%M%S")
os.makedirs(snapshot_dir, exist_ok=True)

snapshot = {
    "time": datetime.now().isoformat(),
    "snapshot": snapshot_dir,
    "existing_files": [],
    "new_files": []
}

for item in patch["generated_changes"]:
    file = item["file"]

    if os.path.exists(file):
        target = snapshot_dir + "/" + file.replace("./","")
        os.makedirs(os.path.dirname(target), exist_ok=True)
        shutil.copy2(file, target)
        snapshot["existing_files"].append(file)
    else:
        snapshot["new_files"].append(file)

with open("sidox/tasks/pre_execution_snapshot.json","w") as f:
    json.dump(snapshot,f,indent=2)

print(json.dumps(snapshot,indent=2))
