import os
import datetime

approved = False

def analyze():
    print("📂 تحليل المشروع")
    count = 0
    for root, _, files in os.walk("app"):
        for f in files:
            if f.endswith(".kt"):
                print("-", f)
                count += 1
    print("✅ Kotlin:", count)

def prepare(task):
    print("\n📋 المهمة:", task)
    print("1- تحليل الملفات")
    print("2- Backup")
    print("3- Patch")
    print("4- مراجعة")
    print("5- تنفيذ")
    print("6- Build")

def patch(task):
    name = "patch_" + datetime.datetime.now().strftime("%H%M%S") + ".md"
    open(name,"w").write("Task: "+task)
    print("✅ Patch:", name)

def backup():
    print("🛡️ Backup جاهز")

def approve():
    global approved
    approved = True
    print("✅ تمت الموافقة")

def execute():
    if not approved:
        print("⚠️ اكتب وافق")
        return
    backup()
    print("🛠️ تنفيذ التعديل")
    print("🏗️ Build")
    print("🔍 تحليل الأخطاء")

def run():
    print("🦇 Core v1")
    while True:
        cmd=input("CORE> ")

        if cmd=="exit":
            print("👋 خروج")
            break
        elif cmd=="حلل":
            analyze()
        elif cmd.startswith("خطط"):
            prepare(cmd[5:])
        elif cmd.startswith("Patch"):
            patch(cmd)
        elif cmd=="وافق":
            approve()
        elif cmd=="نفذ":
            execute()
        else:
            print("❓ أمر غير معروف")
