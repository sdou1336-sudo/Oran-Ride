import json
import os
import shutil
from datetime import datetime

with open("sidox/tasks/latest_patch_backup.json") as f:
    backup = json.load(f)

backup_dir = backup["backup"]

restored = []
removed_new = []

for item in backup["saved_files"]:

    if isinstance(item, dict):
        file = item["file"]

        if item.get("status") == "new_file_no_backup":
            if os.path.exists(file):
                os.remove(file)
                removed_new.append(file)

    else:
        file = item
        backup_file = os.path.join(
            backup_dir,
            file.replace("./","")
        )

        if os.path.exists(backup_file):
            os.makedirs(os.path.dirname(file), exist_ok=True)
            shutil.copy2(backup_file, file)
            restored.append(file)

result = {
    "time": datetime.now().isoformat(),
    "status": "ROLLED_BACK",
    "backup": backup_dir,
    "restored_files": restored,
    "removed_new_files": removed_new
}

with open("sidox/tasks/rollback_report.json","w") as f:
    json.dump(result,f,indent=2)

print(json.dumps(result,indent=2))
