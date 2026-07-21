import json
import shutil
import os
from datetime import datetime

path = os.path.expanduser("~")

usage = shutil.disk_usage(path)

result = {
    "time": datetime.now().isoformat(),
    "path": path,
    "disk_total_mb": usage.total // (1024*1024),
    "disk_free_mb": usage.free // (1024*1024),
    "checks": {}
}

try:
    with open("/proc/meminfo") as f:
        for line in f:
            if line.startswith("MemAvailable"):
                result["checks"]["memory_available_kb"] = int(line.split()[1])
except Exception as e:
    result["checks"]["memory_error"] = str(e)

if result["disk_free_mb"] < 500:
    result["recommendation"] = [
        "Storage is low. Remove unnecessary files."
    ]
else:
    result["recommendation"] = [
        "Storage is acceptable."
    ]

with open("sidox/tasks/environment_report.json","w") as f:
    json.dump(result,f,indent=2)

print(json.dumps(result,indent=2))
