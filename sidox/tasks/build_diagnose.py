import json
import os
from datetime import datetime

report_file = "sidox/tasks/pipeline_report.json"

if not os.path.exists(report_file):
    print("No pipeline report found")
    exit()

with open(report_file) as f:
    report = json.load(f)

diagnosis = {
    "time": datetime.now().isoformat(),
    "type": "unknown",
    "reason": "",
    "action": ""
}

text = json.dumps(report)

if "AAPT2" in text or "Daemon startup failed" in text:
    diagnosis["type"] = "environment"
    diagnosis["reason"] = "Android resource compiler failed to start"
    diagnosis["action"] = "Check Gradle cache, memory and Termux build environment"

elif "Unresolved reference" in text or "Compilation error" in text:
    diagnosis["type"] = "code"
    diagnosis["reason"] = "Kotlin compilation issue"
    diagnosis["action"] = "Review modified Kotlin files"

elif "Duplicate class" in text:
    diagnosis["type"] = "dependency"
    diagnosis["reason"] = "Duplicate dependency/class"
    diagnosis["action"] = "Review Gradle dependencies"

else:
    diagnosis["type"] = "unknown"
    diagnosis["reason"] = "No known pattern detected"
    diagnosis["action"] = "Manual review required"

with open("sidox/tasks/build_diagnosis.json","w") as f:
    json.dump(diagnosis,f,indent=2)

print(json.dumps(diagnosis,indent=2))
