import os
import json
from datetime import datetime

report = "sidox/reports/latest_report.json"
out = "sidox/patches/latest_patch.json"

import os
os.makedirs("sidox/patches", exist_ok=True)

if not os.path.exists(report):
    print("No report found")
    exit(1)

with open(report) as f:
    data = json.load(f)

patch = {
    "created": datetime.now().isoformat(),
    "mode": "proposal_only",
    "approved": False,
    "problem": data.get("problem"),
    "category": data.get("category"),
    "changes": [],
    "note": "Gemini suggestions will be stored here before applying"
}

with open(out, "w") as f:
    json.dump(patch, f, indent=2)

print("Patch proposal created")
