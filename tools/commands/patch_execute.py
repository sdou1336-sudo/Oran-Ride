from pathlib import Path
import json
import shutil
from datetime import datetime

def run():
    print("=== Patch Execute ===")

    task = Path("tools/task.json")

    if not task.exists():
        print("⚠️ لا توجد مهمة")
        return

    data = json.loads(task.read_text())

    file = data.get("file")

    target = None
    for p in Path(".").rglob(file):
        if "build" not in str(p):
            target = p
            break

    if not target:
        print("⚠️ الملف غير موجود")
        return

    backup = Path("backup_tasks")
    backup.mkdir(exist_ok=True)

    shutil.copy(target, backup / f"{target.name}.{datetime.now().timestamp()}")

    print(f"✓ نسخة احتياطية: {target.name}")
    print("⚠️ منفذ التعديل جاهز")
    print("✓ لم يتم تغيير الكود بعد")

    print("===================")
