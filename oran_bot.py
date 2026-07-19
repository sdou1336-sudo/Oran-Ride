import os
import shutil
from datetime import datetime

PLAN_FILE = "indrive_like_plan.md"

def load_tasks():
    tasks=[]
    with open(PLAN_FILE,encoding="utf-8") as f:
        for line in f:
            line=line.strip()
            if line.startswith("-"):
                tasks.append(line[1:].strip())
    return tasks

def find_files():
    result=[]
    for root,dirs,files in os.walk("."):
        for file in files:
            if file.endswith(".kt"):
                path=os.path.join(root,file)
                text=open(path,encoding="utf-8",errors="ignore").read()
                score=0

                for word in ["RealMap","MapView","GeoPoint","Search","Marker"]:
                    if word in text:
                        score+=1

                if score:
                    result.append((score,path))
    return sorted(result,reverse=True)

def backup(files):
    folder="backup_"+datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs(folder)

    for _,file in files:
        if os.path.exists(file):
            shutil.copy(file,folder)

    print("✅ تم إنشاء نسخة احتياطية:",folder)

def prepare(num):
    tasks=load_tasks()

    if num<1 or num>len(tasks):
        print("❌ رقم غير موجود")
        return

    print("\n🛠️ المهمة:")
    print(tasks[num-1])

    files=find_files()

    print("\n📂 الملفات:")
    for score,path in files[:5]:
        print("-",path)

    backup(files)

    print("\n⚠️ جاهز للتعديل، لكن لم يتم تغيير أي كود")

print("🤖 Oran Bot v8")
print("- جهز المهمة رقم")
print("- exit")

while True:
    cmd=input("BOT> ")

    if cmd=="exit":
        break

    elif cmd.startswith("جهز المهمة"):
        try:
            prepare(int(cmd.split()[-1]))
        except:
            print("مثال: جهز المهمة 2")

    else:
        print("❓ أمر غير معروف")
