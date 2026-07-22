#!/usr/bin/env python3
from pathlib import Path
import json
from datetime import datetime

LOG = Path("build.log")
OUT = Path("sidox/build_error.json")

error = ""

if LOG.exists():
    text = LOG.read_text(errors="ignore")
    lines = text.splitlines()
    for line in lines:
        if "error" in line.lower() or "FAILURE" in line:
            error += line + "\n"

OUT.write_text(
    json.dumps({
        "time": datetime.now().isoformat(),
        "error": error
    }, indent=2),
    encoding="utf-8"
)

print("Error report saved:", OUT)
