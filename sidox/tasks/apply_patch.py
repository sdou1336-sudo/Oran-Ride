import json
import os
import shutil
from datetime import datetime

patch_file = "sidox/tasks/patches/latest_patch.json"

with open(patch_file) as f:
    patch = json.load(f)

if not patch.get("approved", False):
    print("Patch not approved. No changes applied.")
    exit()

backup_dir = f"sidox/tasks/apply_backups/backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
os.makedirs(backup_dir, exist_ok=True)

log = []

for target in patch.get("targets", []):
    file = target["file"]

    if os.path.exists(file):

        backup_file = os.path.join(backup_dir, file.replace("./",""))
        os.makedirs(os.path.dirname(backup_file), exist_ok=True)

        shutil.copy2(file, backup_file)

        with open(file, "r") as f:
            content = f.read()

        new_content = content.replace(
            "Version 1",
            "Version 2 - Modified by Sidox"
        )

        with open(file, "w") as f:
            f.write(new_content)

        log.append({
            "file": file,
            "status": "modified"
        })

result = {
    "time": datetime.now().isoformat(),
    "backup": backup_dir,
    "changes": log
}

with open("sidox/tasks/apply_log.json","w") as f:
    json.dump(result,f,indent=2)

print(json.dumps(result,indent=2))
