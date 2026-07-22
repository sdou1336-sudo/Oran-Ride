#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime

patch = Path("sidox/kotlin_patch.json")
log = Path("sidox/kotlin_execution_log.json")

if not patch.exists():
    print("No Kotlin patch found")
    exit()

data = json.loads(patch.read_text(encoding="utf-8"))

if not data.get("approved", False):
    print("Kotlin patch not approved")
    exit()

results=[]

for item in data.get("files", []):
    file=Path(item["file"])

    if file.exists():
        old=file.read_text(encoding="utf-8")
        file.write_text(
            old + "\n\n// Sidox modification\n",
            encoding="utf-8"
        )
        results.append(str(file))
        print("Modified:", file)
    else:
        print("Missing:", file)

log={
    "time":datetime.now().isoformat(),
    "modified":results
}

log.write_text(
    json.dumps(log,indent=2,ensure_ascii=False),
    encoding="utf-8"
)

print("Kotlin execution complete")
