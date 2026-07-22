#!/usr/bin/env python3

import json
import shutil
import argparse
from pathlib import Path
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("--auto-approve", action="store_true")
args = parser.parse_args()

PATCH = Path("sidox/generated_kotlin_patch.json")
LOG = Path("sidox/kotlin_execution_log.json")

if not PATCH.exists():
    print("No Kotlin patch found")
    raise SystemExit(1)

data = json.loads(PATCH.read_text(encoding="utf-8"))

if not args.auto_approve and not data.get("approved", False):
    print("Kotlin patch not approved")
    raise SystemExit(1)

results = []

for item in data.get("files", []):
    file = Path(item["file"])

    if not file.exists():
        print("Missing:", file)
        continue

    shutil.copy2(file, str(file) + ".bak")

    content = item.get("content", "")
    if content.strip():
        file.write_text(content, encoding="utf-8")

    if not file.exists():
        shutil.copy2(str(file) + ".bak", file)
        print("Rollback:", file)
        continue

    results.append(str(file))
    print("Modified:", file)

LOG.write_text(
    json.dumps({
        "time": datetime.now().isoformat(),
        "modified": results
    }, indent=2, ensure_ascii=False),
    encoding="utf-8"
)

print("Kotlin execution complete")
