import os
import json
from datetime import datetime

patch_file = "sidox/patches/latest_patch.json"
log_file = "sidox/execution_log.json"

if not os.path.exists(patch_file):
    print("No patch found")
    exit(1)

with open(patch_file) as f:
    patch = json.load(f)

if not patch.get("approved", False):
    print("Patch not approved. No changes applied.")
    exit(0)

log = {
    "time": datetime.now().isoformat(),
    "status": "approved_patch_ready",
    "patch": patch
}

with open(log_file, "w") as f:
    json.dump(log, f, indent=2)

print("Patch execution recorded")
