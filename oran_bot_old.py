import os, shutil
from datetime import datetime

ROOT="app/src/main/java"
task=""
approved=False

def run():
    global task, approved

    print("🦇 Batman Final")

    while True:
        c=input("BATMAN> ")

        if c=="exit":
            break

        elif c=="حلل المشروع":
            files=[]
            for r,_,fs in os.walk(ROOT):
                for f in fs:
                    if f.endswith(".kt"):
                        files.append(os.path.join(r,f))
            print("📂 ملفات:",len(files))
            for x in files:
                print("-",x)

        elif c.startswith("مهمة"):
            task=c.replace("مهمة","").strip()
            print("🧠 المهمة:",task)

        elif c=="وافق":
            approved=True
            print("✅ موافق")

        elif c=="نفذ":
            if not approved:
                print("⚠️ اكتب وافق")
                continue

            b="backup_"+datetime.now().strftime("%H%M%S")
            os.makedirs(b,exist_ok=True)

            with open("batman_plan.md","w") as f:
                f.write("المهمة:\n"+task)

            print("🛡️ Backup:",b)
            print("📝 تم إنشاء خطة التعديل")

        else:
            print("❓ أمر غير معروف")

run()
