import os, json

report = {
    "status": "UNKNOWN",
    "error": None,
    "category": None,
    "task": None
}

log_file = "build.log"

if os.path.exists(log_file):
    log = open(log_file, "r", errors="ignore").read()

    if "OutOfMemoryError" in log or "Java heap space" in log:
        report["status"] = "FAILED"
        report["error"] = "Java heap space"
        report["category"] = "Build Memory"

    elif "BUILD FAILED" in log:
        report["status"] = "FAILED"
        report["error"] = "Build failed"
        report["category"] = "Gradle/Kotlin"

    else:
        report["status"] = "SUCCESS"
else:
    report["status"] = "NO_LOG"

os.makedirs("sidox/reports", exist_ok=True)

with open("sidox/reports/latest_report.json", "w") as f:
    json.dump(report, f, indent=2)

print(json.dumps(report, indent=2))
