import json, shutil
from pathlib import Path
from datetime import datetime

PATCH=Path("sidox/generated_kotlin_patch.json")
LOG=Path("sidox/kotlin_execution_log.json")

data=json.loads(PATCH.read_text())

if not data.get("approved", False):
    print("Kotlin patch not approved")
    exit(1)

results=[]

for item in data.get("files", []):
    file=Path(item["file"])
    file.parent.mkdir(parents=True, exist_ok=True)

    if file.exists():
        shutil.copy2(file, str(file)+".bak")

    file.write_text(item.get("content",""), encoding="utf-8")
    results.append(str(file))
    print("Modified:", file)

LOG.write_text(json.dumps({
"time":datetime.now().isoformat(),
"modified":results
},indent=2))

print("Kotlin execution complete")
