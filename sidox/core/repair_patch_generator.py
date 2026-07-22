#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime

plan = Path("sidox/repair_plan.json")
out = Path("sidox/repair_patch.json")

data = json.loads(plan.read_text(encoding="utf-8")) if plan.exists() else {}

patch = {
    "created": datetime.now().isoformat(),
    "status": "repair_proposal",
    "approved": False,
    "operations": []
}

for item in data.get("repairs", []):
    patch["operations"].append({
        "type": "inspect",
        "file": item["file"],
        "action": item["action"],
        "reason": item["reason"]
    })

out.write_text(
    json.dumps(patch, indent=2, ensure_ascii=False),
    encoding="utf-8"
)

print("Repair Patch generated")
print("Operations:", len(patch["operations"]))
print("Saved:", out)
