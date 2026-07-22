#!/usr/bin/env python3
import json
import shutil
from pathlib import Path
from datetime import datetime

patch = Path("sidox/repair_patch.json")
backup = Path("sidox/backups") / datetime.now().strftime("%Y%m%d_%H%M%S")

if not patch.exists():
    print("No repair patch found")
    exit()

data = json.loads(patch.read_text(encoding="utf-8"))

if not data.get("approved", False):
    print("Repair patch not approved")
    exit()

backup.mkdir(parents=True, exist_ok=True)

for op in data.get("operations", []):
    target = Path(op.get("target", ""))

    if target.exists():
        dst = backup / target
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(target, dst) if target.is_dir() else shutil.copy2(target, dst)
        print("Backup:", target)

    print("Prepared:", op)

print("Repair execution ready.")
