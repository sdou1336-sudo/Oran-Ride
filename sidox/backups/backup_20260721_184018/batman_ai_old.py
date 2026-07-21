import os
import shutil
from datetime import datetime
from pathlib import Path

ROOT = "app/src/main/java"

approved = False
task = None


def analyze():
    print("\n📂 ملفات المشروع:")
    count = 0
    for root, dirs, files in os.walk(ROOT):
        for f in files:
            if f.endswith(".kt"):
                print("-", os.path.join(root, f))
                count += 1
    print(f"\n✅ عدد ملفات Kotlin: {count}")


def backup():
    name = "backup_" + datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs(name, exist_ok=True)
    print("🛡️ Backup جاهز:", name)


def prepare(t):
    global task
    task = t
    print("\n🧠 المهمة:", task)
    print("🔎 سيتم تحليل الملفات المناسبة...")
    analyze()


def approve():
    global approved
    approved = True
    print("✅ تمت الموافقة")


def execute():
    if not approved:
        print("⚠️ اكتب: وافق أولاً")
        return

    backup()
    print("🛠️ تنفيذ المهمة:", task)
    print("⚠️ مرحلة التعديل الآلي ستضاف بعد ربط المولد")
    

def run():
    print("🦇 Batman Unified v1")
    print("الأوامر:")
    print("- حلل المشروع")
    print("- مهمة <الوصف>")
    print("- وافق")
    print("- نفذ")
    print("- exit")

    while True:
        cmd = input("BATMAN> ").strip()

        if cmd == "exit":
            break

        elif cmd == "حلل المشروع":
            analyze()

        elif cmd.startswith("مهمة"):
            prepare(cmd.replace("مهمة", "").strip())

        elif cmd == "وافق":
            approve()

        elif cmd == "نفذ":
            execute()

        else:
            print("❓ أمر غير معروف")
