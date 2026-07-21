from pathlib import Path
import json

def run():
    print("=== Apply Task ===")

    p = Path("tools/task.json")

    if not p.exists():
        print("⚠️ لا توجد مهمة")
        return

    task = json.loads(p.read_text())

    if task.get("status") != "waiting":
        print("⚠️ المهمة ليست جاهزة")
        return

    print(f"✓ الملف: {task['file']}")
    print(f"✓ المهمة: {task['task']}")
    print("✓ تم التحقق")
    print("⚠️ بانتظار ربط منفذ التعديل")

    print("==================")
