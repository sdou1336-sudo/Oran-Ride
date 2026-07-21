import os
import json
from datetime import datetime

log_file = "build.log"
report_dir = "sidox/reports"

os.makedirs(report_dir, exist_ok=True)

result = {
    "time": datetime.now().isoformat(),
    "status": "UNKNOWN",
    "problem": "No detected issue",
    "category": "unknown"
}

if os.path.exists(log_file):
    log = open(log_file, "r", errors="ignore").read()

    checks = [
        ("OutOfMemoryError", "Java heap space", "memory"),
        ("Compilation failed", "Compilation error", "kotlin/java"),
        ("DexArchiveMergerException", "Dex merge error", "android build"),
        ("BUILD FAILED", "Gradle build failed", "gradle")
    ]

    for key, problem, category in checks:
        if key in log:
            result["status"] = "FAILED"
            result["problem"] = problem
            result["category"] = category
            break
    else:
        result["status"] = "SUCCESS"

else:
    result["status"] = "NO_LOG"

with open(f"{report_dir}/latest_report.json", "w") as f:
    json.dump(result, f, indent=2)

print(json.dumps(result, indent=2))
