#!/usr/bin/env python3
import shutil
from pathlib import Path

backup_root = Path("sidox/backups")

if not backup_root.exists():
    print("No backup found")
    exit()

backup = sorted(backup_root.iterdir())[-1]

for src in backup.rglob("*"):
    if src.is_file():
        dest = Path(str(src).replace(str(backup)+"/",""))
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        print("Restored:", dest)

print("Rollback completed")
