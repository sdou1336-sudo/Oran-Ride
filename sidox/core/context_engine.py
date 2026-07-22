#!/usr/bin/env python3
import json
from pathlib import Path

source = Path("sidox/project_map.json")
out = Path("sidox/context/project_context.json")

data = json.loads(source.read_text(encoding="utf-8")) if source.exists() else {}

files = data.get("kotlin_analysis", [])

context = {
    "task": "auto_analysis",
    "files": [f["file"] for f in files if f.get("functions",0) or f.get("classes",0)],
    "count": len(files)
}

out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(context, indent=2, ensure_ascii=False), encoding="utf-8")

print("Context generated.")
print("Files:", context["count"])
print("Saved:", out)
