#!/usr/bin/env python3

import json
from pathlib import Path
from datetime import datetime

TASK_FILE = Path("sidox/user_task.json")
PLAN_FILE = Path("sidox/task_plan.json")
PATCH_FILE = Path("sidox/code_patch.json")

BASE = Path("app/src/main/java/com/oranride/app")

KEYWORDS = {
    "driver": [
        "Driver.kt",
        "DriverViewModel.kt"
    ],
    "map": [
        "RealMap.kt",
        "LocationManager.kt"
    ],
    "search": [
        "SearchBar.kt",
        "NominatimRepository.kt"
    ],
    "ride": [
        "RideRequest.kt",
        "RideViewModel.kt"
    ]
}

if not TASK_FILE.exists():
    print("Create sidox/user_task.json first")
    raise SystemExit(1)

task = json.loads(
    TASK_FILE.read_text(
        encoding="utf-8"
    )
)

request = task.get(
    "task",
    ""
).lower()

plan = {
    "time": datetime.now().isoformat(),
    "task": request,
    "action": "analyze",
    "targets": []
}

for keyword, files in KEYWORDS.items():
    if keyword in request:
        for f in files:
            if f not in plan["targets"]:
                plan["targets"].append(f)

PLAN_FILE.write_text(
    json.dumps(
        plan,
        indent=2,
        ensure_ascii=False
    ),
    encoding="utf-8"
)

patch = {
    "time": datetime.now().isoformat(),
    "approved": False,
    "targets": [],
    "changes": []
}

for name in plan["targets"]:
    path = BASE / name
    if path.exists():
        patch["targets"].append(str(path))
        patch["changes"].append({
            "file": str(path),
            "action": "generate_or_modify",
            "content": ""
        })

PATCH_FILE.write_text(
    json.dumps(
        patch,
        indent=2,
        ensure_ascii=False
    ),
    encoding="utf-8"
)

print("Task plan generated")
print("Targets:", plan["targets"])
print("Changes:", len(patch["changes"]))
