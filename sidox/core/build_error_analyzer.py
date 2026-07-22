#!/usr/bin/env python3
import json
from pathlib import Path

report = Path("sidox/report.json")
out = Path("sidox/build_analysis.json")

data = json.loads(report.read_text(encoding="utf-8")) if report.exists() else {}

log = data.get("log", "").lower()

errors = []

checks = {
    "kotlin_error": ["unresolved reference", "type mismatch"],
    "gradle_error": ["gradle", "build failed"],
    "memory_error": ["outofmemory", "heap"],
    "dependency_error": ["could not resolve", "dependency"]
}

for name, words in checks.items():
    if any(w in log for w in words):
        errors.append(name)

result = {
    "build_status": data.get("status"),
    "errors": errors,
    "suggestion": "generate repair patch" if errors else "inspect logs"
}

out.write_text(
    json.dumps(result, indent=2, ensure_ascii=False),
    encoding="utf-8"
)

print("Build analysis complete.")
print(result)
