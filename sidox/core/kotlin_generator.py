#!/usr/bin/env python3

import json
from pathlib import Path
from datetime import datetime

SOURCE = Path("sidox/code_patch.json")
OUTPUT = Path("sidox/generated_kotlin_patch.json")

if not SOURCE.exists():
    print("No code patch found")
    raise SystemExit(1)

data = json.loads(SOURCE.read_text(encoding="utf-8"))

patch = {
    "time": datetime.now().isoformat(),
    "approved": data.get("approved", False),
    "files": []
}

for item in data.get("changes", []):
    patch["files"].append({
        "file": item["file"],
        "language": "kotlin",
        "action": item.get("action", "generate_or_modify"),
        "content": item.get("content") or "package com.oranride.app\n\n// Sidox generated Kotlin code\n"
    })

OUTPUT.write_text(
    json.dumps(
        patch,
        indent=2,
        ensure_ascii=False
    ),
    encoding="utf-8"
)

print("Kotlin Generator ready")
print("Files:", len(patch["files"]))
print("Saved:", OUTPUT)
