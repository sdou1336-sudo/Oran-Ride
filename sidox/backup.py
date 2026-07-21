import os
import shutil
from datetime import datetime

source = "."
backup_dir = "sidox/backups"

os.makedirs(backup_dir, exist_ok=True)

name = datetime.now().strftime("backup_%Y%m%d_%H%M%S")
target = os.path.join(backup_dir, name)

os.makedirs(target, exist_ok=True)

for item in os.listdir(source):
    if item not in ["sidox", ".git"]:
        src = os.path.join(source, item)
        dst = os.path.join(target, item)

        if os.path.isdir(src):
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)

print("Backup created:", target)
