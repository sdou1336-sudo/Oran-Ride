#!/usr/bin/env python3
import json
from pathlib import Path

ctx = Path("sidox/context/project_context.json")
out = Path("sidox/decision.json")

context = json.loads(ctx.read_text(encoding="utf-8")) if ctx.exists() else {}

files = context.get("files", [])

decision = {
    "task": context.get("task", "auto"),
    "target_files": files,
    "operation": "modify",
    "plan": [
        "analyze target files",
        "generate patch",
        "verify build"
    ],
    "status": "ready"
}

out.write_text(
    json.dumps(decision, indent=2, ensure_ascii=False),
    encoding="utf-8"
)

print("Decision generated.")
print("Targets:", len(files))
print("Saved:", out)
