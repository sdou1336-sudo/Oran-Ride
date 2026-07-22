#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path
from datetime import datetime

report = Path("sidox/report.json")

try:
    result = subprocess.run(
        ["./gradlew", "assembleDebug"],
        capture_output=True,
        text=True,
        timeout=600
    )

    status = "success" if result.returncode == 0 else "failed"
    log = result.stdout[-2000:] + result.stderr[-2000:]

except Exception as e:
    status = "error"
    log = str(e)

data = {
    "time": datetime.now().isoformat(),
    "status": status,
    "build_checked": True,
    "log": log
}

report.write_text(
    json.dumps(data, indent=2, ensure_ascii=False),
    encoding="utf-8"
)

print("Build status:", status)
print("Saved:", report)
