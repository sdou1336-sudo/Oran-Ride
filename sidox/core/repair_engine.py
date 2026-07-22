#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime

analysis = Path("sidox/build_analysis.json")
out = Path("sidox/repair_plan.json")

data = json.loads(analysis.read_text(encoding="utf-8")) if analysis.exists() else {}

errors = data.get("errors", [])

plan = {
    "time": datetime.now().isoformat(),
    "status": "ready",
    "approved": False,
    "repairs": []
}

for error in errors:
    if error == "dependency_error":
        plan["repairs"].append({
            "file": "app/build.gradle.kts",
            "action": "inspect_dependencies",
            "reason": "dependency failure detected"
        })

    elif error == "gradle_error":
        plan["repairs"].append({
            "file": "gradle.properties",
            "action": "inspect_gradle_config",
            "reason": "gradle failure detected"
        })

out.write_text(
    json.dumps(plan, indent=2, ensure_ascii=False),
    encoding="utf-8"
)

print("Repair Engine ready")
print("Repairs:", len(plan["repairs"]))
print("Saved:", out)
