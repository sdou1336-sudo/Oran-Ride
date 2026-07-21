import json
import os
import shutil
from datetime import datetime

with open("sidox/tasks/generated_patch.json") as f:
    patch = json.load(f)

backup_dir = "sidox/tasks/patch_backups/backup_" + datetime.now().strftime("%Y%m%d_%H%M%S")
os.makedirs(backup_dir, exist_ok=True)

saved = []

for item in patch["generated_changes"]:
    file = item["file"]

    if os.path.exists(file):
        target = backup_dir + "/" + file.replace("./","")
        os.makedirs(os.path.dirname(target), exist_ok=True)
        shutil.copy2(file, target)
        saved.append(file)

    else:
        saved.append({
            "file": file,
            "status": "new_file_no_backup"
        })

result = {
    "time": datetime.now().isoformat(),
    "backup": backup_dir,
    "saved_files": saved
}

with open("sidox/tasks/latest_patch_backup.json","w") as f:
    json.dump(result,f,indent=2)

print(json.dumps(result,indent=2))
