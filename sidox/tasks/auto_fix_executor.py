import json
import os
import subprocess
import shutil
from datetime import datetime

plan_file = "sidox/tasks/auto_fix_plan.json"

with open(plan_file) as f:
    plan = json.load(f)

result = {
    "time": datetime.now().isoformat(),
    "executed": [],
    "failed": [],
    "status": "completed"
}

for fix in plan["fix_plan"]:

    if fix == "Stop Gradle daemons":
        r = subprocess.run(
            ["./gradlew", "--stop"],
            capture_output=True,
            text=True
        )

        if r.returncode == 0:
            result["executed"].append(fix)
        else:
            result["failed"].append(fix)

    elif fix == "Clean Gradle cache transforms":

        cache = os.path.expanduser(
            "~/.gradle/caches/9.6.1/transforms"
        )

        try:
            if os.path.exists(cache):
                shutil.rmtree(cache)

            result["executed"].append(fix)

        except Exception as e:
            result["failed"].append({
                "fix": fix,
                "error": str(e)
            })

    else:
        result["executed"].append({
            "skipped": fix,
            "reason": "Manual step"
        })

if result["failed"]:
    result["status"] = "partial_failure"

with open("sidox/tasks/auto_fix_report.json","w") as f:
    json.dump(result,f,indent=2)

print(json.dumps(result,indent=2))
