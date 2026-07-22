import subprocess
import json
from datetime import datetime

log="sidox/build_error.json"

result = subprocess.run(
    ["./gradlew","assembleDebug"],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print("Build SUCCESS")
else:
    error = {
        "time": datetime.now().isoformat(),
        "error": result.stderr[:3000] + "\n...\n" + result.stderr[-3000:]
    }
    with open(log,"w") as f:
        json.dump(error,f,indent=2)
    print("Build FAILED - error saved")
