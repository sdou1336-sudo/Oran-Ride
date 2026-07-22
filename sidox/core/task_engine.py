#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime

task = Path("sidox/user_task.json")
out = Path("sidox/task_plan.json")

if not task.exists():
    print("Create sidox/user_task.json first")
    exit()

data=json.loads(task.read_text(encoding="utf-8"))
request=data.get("task","")

plan={
    "time":datetime.now().isoformat(),
    "task":request,
    "targets":[],
    "action":"analyze"
}

keywords={
    "driver":["Driver.kt","DriverViewModel.kt"],
    "map":["RealMap.kt","LocationManager.kt"],
    "search":["SearchBar.kt","NominatimRepository.kt"],
    "ride":["RideRequest.kt","RideViewModel.kt"]
}

for k,files in keywords.items():
    if k.lower() in request.lower():
        plan["targets"].extend(files)

out.write_text(json.dumps(plan,indent=2,ensure_ascii=False))
print("Task plan generated")
print("Targets:",plan["targets"])
