import os
from pathlib import Path
import shutil
from datetime import datetime

approved = False
patch_file = Path('.patch_selected').read_text() if Path('.patch_selected').exists() else None

def backup_file(path):
    if os.path.exists(path):
        b = "backup_" + datetime.now().strftime("%H%M%S")
        os.makedirs(b, exist_ok=True)
        shutil.copy(path, b)
        print("🛡️ Backup:", b)

def approve():
    global approved
    approved = True
    print("✅ موافق")

def execute():
    global patch_file

    if not approved:
        print("⚠️ اكتب وافق أولاً")
        return

    if not patch_file:
        print("⚠️ لا يوجد Patch")
        return

    print("🛠️ تنفيذ Patch:", patch_file)

    with open(patch_file, encoding="utf-8") as f:
        for line in f:
            if line.startswith("- app/"):
                file = line.strip("- ").strip()
                print("📂 ملف:", file)

    print("✅ جاهز للتعديل الحقيقي")

def run():
    print("🦇 Editor v2")

    while True:
        cmd = input("> ")

        if cmd == "exit":
            break

        elif cmd == "وافق":
            approve()

        elif cmd.startswith("Patch"):
            patch_file = cmd.replace("Patch", "").strip()
            Path(".patch_selected").write_text(patch_file)
            if os.path.exists(patch_file):
                print("✅ Patch:", patch_file)
            else:
                print("❌ Patch غير موجود")

        elif cmd == "نفذ":
            execute()

        else:
            print("❓ أمر غير معروف")
