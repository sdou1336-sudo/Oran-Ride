#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime

analysis = Path("sidox/build_analysis.json")
out = Path("sidox/repair_patch.json")

data = json.loads(analysis.read_text(encoding="utf-8")) if analysis.exists() else {}

errors = data.get("errors", [])

patch = {
    "created": datetime.now().isoformat(),
    "status": "repair_proposal",
    "approved": False,
    "errors": errors,
    "operations": []
}

for e in errors:
    if e == "dependency_error":
        patch["operations"].append({
            "type": "inspect",
            "target": "build.gradle.kts",
            "action": "check dependencies"
        })

    elif e == "gradle_error":
        patch["operations"].append({
            "type": "inspect",
            "target": "gradle",
            "action": "check build configuration"
        })

out.write_text(
    json.dumps(patch, indent=2, ensure_ascii=False),
    encoding="utf-8"
)

print("Repair patch generated.")
print("Errors:", errors)
print("Saved:", out)
