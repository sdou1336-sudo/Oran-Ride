import os
import shutil
from datetime import datetime

approved = False

def backup_file(path):
    if os.path.exists(path):
        b = "backup_" + datetime.now().strftime("%H%M%S")
        os.makedirs(b, exist_ok=True)
        shutil.copy(path, b)
        print("🛡️ Backup:", b)

def edit_file(path, old, new):
    global approved

    if not approved:
        print("⚠️ اكتب وافق أولاً")
        return

    if not os.path.exists(path):
        print("❌ الملف غير موجود")
        return

    backup_file(path)

    data = open(path, encoding="utf-8").read()

    if old not in data:
        print("⚠️ لم يجد مكان التعديل")
        return

    data = data.replace(old, new, 1)

    open(path, "w", encoding="utf-8").write(data)

    print("✅ تم تعديل:", path)

def approve():
    global approved
    approved = True
    print("✅ موافق")

def run():
    print("🦇 Editor v1")

    while True:
        cmd=input("> ")

        if cmd=="exit":
            break

        elif cmd=="وافق":
            approve()

        elif cmd=="اختبر":
            edit_file(
            "app/src/main/java/com/example/ui/OranMap.kt",
            "// BATMAN_MAP_UPDATE",
            "// تحسين الخريطة")
