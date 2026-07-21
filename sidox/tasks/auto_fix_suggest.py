import json
import os
from datetime import datetime

diagnosis_file = "sidox/tasks/build_diagnosis.json"

if not os.path.exists(diagnosis_file):
    print("No diagnosis found")
    exit()

with open(diagnosis_file) as f:
    diagnosis = json.load(f)

result = {
    "time": datetime.now().isoformat(),
    "diagnosis": diagnosis["type"],
    "fix_plan": []
}

if diagnosis["type"] == "environment":
    result["fix_plan"] = [
        "Stop Gradle daemons",
        "Clean Gradle cache transforms",
        "Run build again",
        "Check available memory"
    ]

elif diagnosis["type"] == "code":
    result["fix_plan"] = [
        "Review modified Kotlin files",
        "Check imports",
        "Run compiler again"
    ]

elif diagnosis["type"] == "dependency":
    result["fix_plan"] = [
        "Review Gradle dependencies",
        "Check duplicate libraries"
    ]

else:
    result["fix_plan"] = [
        "Manual investigation required"
    ]

with open("sidox/tasks/auto_fix_plan.json","w") as f:
    json.dump(result,f,indent=2)

print(json.dumps(result,indent=2))
