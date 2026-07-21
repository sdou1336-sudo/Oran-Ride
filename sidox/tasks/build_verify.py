import json
import subprocess
from datetime import datetime

result = {
    "time": datetime.now().isoformat(),
    "status": "",
    "output": ""
}

try:
    process = subprocess.run(
        ["./gradlew", "assembleDebug"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        timeout=600
    )

    result["output"] = process.stdout[-3000:]

    if process.returncode == 0:
        result["status"] = "BUILD_SUCCESS"
    else:
        result["status"] = "BUILD_FAILED"

except Exception as e:
    result["status"] = "ERROR"
    result["output"] = str(e)

with open("sidox/tasks/build_result.json","w") as f:
    json.dump(result,f,indent=2)

print(json.dumps(result,indent=2))
