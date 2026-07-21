import json
import os
import shutil
from datetime import datetime

build_file = "sidox/tasks/build_result.json"

with open(build_file) as f:
    build = json.load(f)

if build.get("status") != "BUILD_FAILED":
    print("Build successful. Rollback not needed.")
    exit()

backup_root = "sidox/tasks/apply_backups"

if not os.path.exists(backup_root):
    print("No backup found.")
    exit()

backups = sorted(os.listdir(backup_root))

if not backups:
    print("No backup found.")
    exit()

latest = os.path.join(backup_root, backups[-1])

restored = []

for root, dirs, files in os.walk(latest):
    for file in files:
        backup_file = os.path.join(root, file)
        original = backup_file.replace(latest + "/", "./")

        os.makedirs(os.path.dirname(original), exist_ok=True)
        shutil.copy2(backup_file, original)

        restored.append(original)

result = {
    "time": datetime.now().isoformat(),
    "status": "ROLLED_BACK",
    "backup": latest,
    "restored_files": restored
}

with open("sidox/tasks/rollback_result.json","w") as f:
    json.dump(result,f,indent=2)

print(json.dumps(result,indent=2))
