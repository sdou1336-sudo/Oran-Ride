#!/usr/bin/env python3
import json
import shutil
from pathlib import Path
from datetime import datetime

plan = Path("sidox/repair_plan.json")
backup = Path("sidox/backups") / datetime.now().strftime("%Y%m%d_%H%M%S")

if not plan.exists():
    print("No repair plan")
    exit()

data = json.loads(plan.read_text(encoding="utf-8"))

if not data.get("approved", False):
    print("Repair plan not approved")
    exit()

backup.mkdir(parents=True, exist_ok=True)

for repair in data.get("repairs", []):
    file = Path(repair["file"])

    if file.exists():
        dst = backup / file
        dst.parent.mkdir(parents=True, exist_ok=True)
        if file.is_dir():
            shutil.copytree(file, dst)
        else:
            shutil.copy2(file, dst)

    print("Prepared repair:", file)

print("Repair execution completed")
