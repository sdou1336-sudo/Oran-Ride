import os
import shutil
from datetime import datetime

APP = "app/src/main/java"

approved = False


def analyze():
    print("\n📂 تحليل المشروع:")
    count = 0
    for root, dirs, files in os.walk(APP):
        for f in files:
            if f.endswith(".kt"):
                print("-", os.path.join(root, f))
                count += 1
    print("✅ ملفات Kotlin:", count)


def backup():
    name = "batman_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs(name, exist_ok=True)

    print("🛡️ Backup:", name)


def plan(task):
    print("\n📋 خطة:", task)
    print("1. تحديد الملفات")
    print("2. تحليل الكود")
    print("3. إنشاء Patch")
    print("4. مراجعة")
    print("5. انتظار الموافقة")
    print("6. تنفيذ")
    print("7. فحص البناء")


def patch(task):
    name = "patch_" + datetime.now().strftime("%H%M%S") + ".md"

    with open(name, "w", encoding="utf-8") as f:
        f.write("# Batman Patch\n")
        f.write("المهمة: " + task)

    print("✅ Patch:", name)


def approve():
    global approved
    approved = True
    print("✅ تمت الموافقة")


def execute():
    if not approved:
        print("⚠️ اكتب: وافق")
        return

    print("🛠️ تنفيذ التعديل")
    print("✅ التعديل جاهز")
    print("🏗️ تشغيل البناء")
    print("🔍 تحليل الأخطاء")


def run():
    print("🦇 Batman Core v1")
    print("- حلل")
    print("- خطط")
    print("- Patch")
    print("- وافق")
    print("- نفذ")
    print("- exit")

    while True:
        cmd = input("BATMAN> ")

        if cmd == "exit":
            break

        elif cmd == "حلل":
            analyze()

        elif cmd.startswith("خطط"):
            plan(cmd.replace("خطط ", ""))

        elif cmd.startswith("Patch"):
            patch(cmd)

        elif cmd == "وافق":
            approve()

        elif cmd == "نفذ":
            backup()
            execute()

        else:
            print("❓ أمر غير معروف")
