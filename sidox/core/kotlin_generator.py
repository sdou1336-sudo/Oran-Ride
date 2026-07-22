#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime

source = Path("sidox/code_patch.json")
out = Path("sidox/kotlin_patch.json")

data = json.loads(source.read_text()) if source.exists() else {}

patch = {
    "time": datetime.now().isoformat(),
    "type": "kotlin_generation",
    "approved": False,
    "files": []
}

for item in data.get("changes", []):
    patch["files"].append({
        "file": item.get("file"),
        "language": "kotlin",
        "action": "generate_or_modify",
        "content": "// Sidox Kotlin patch placeholder"
    })

out.write_text(
    json.dumps(patch, indent=2, ensure_ascii=False),
    encoding="utf-8"
)

print("Kotlin Generator ready")
print("Files:", len(patch["files"]))
print("Saved:", out)
