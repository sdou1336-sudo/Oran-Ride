#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime

task=Path("sidox/task_plan.json")
out=Path("sidox/generated_kotlin_patch.json")

data=json.loads(task.read_text(encoding="utf-8")) if task.exists() else {}

patch={
    "time":datetime.now().isoformat(),
    "approved":False,
    "task":data.get("task",""),
    "files":[]
}

for f in data.get("targets",[]):
    patch["files"].append({
        "file":f,
        "action":"modify",
        "code":"// Sidox generated Kotlin change"
    })

out.write_text(
    json.dumps(patch,indent=2,ensure_ascii=False),
    encoding="utf-8"
)

print("Task to Code complete")
print("Files:",len(patch["files"]))
print("Saved:",out)
