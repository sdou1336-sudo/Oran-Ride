import json
import os
from datetime import datetime

snapshot_file = "sidox/tasks/pre_execution_snapshot.json"
patch_file = "sidox/tasks/generated_patch.json"

if not os.path.exists(snapshot_file):
    print("No pre-execution snapshot found. Execution stopped.")
    exit()

with open(snapshot_file) as f:
    snapshot = json.load(f)

with open(patch_file) as f:
    patch = json.load(f)

if not patch.get("approved"):
    print("Patch not approved. Execution stopped.")
    exit()

result = {
    "time": datetime.now().isoformat(),
    "status": "SAFE_EXECUTION_READY",
    "snapshot": snapshot["snapshot"],
    "files_checked": len(patch["generated_changes"])
}

with open("sidox/tasks/safe_execution_report.json","w") as f:
    json.dump(result,f,indent=2)

print(json.dumps(result,indent=2))
