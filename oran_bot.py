import os

PLAN_FILE = "indrive_like_plan.md"

def load_tasks():
    tasks=[]
    with open(PLAN_FILE,encoding="utf-8") as f:
        for line in f:
            line=line.strip()
            if line.startswith("-"):
                tasks.append(line[1:].strip())
    return tasks

def project_files():
    files=[]
    for root,dirs,names in os.walk("."):
        for name in names:
            if name.endswith(".kt"):
                path=os.path.join(root,name)
                text=open(path,encoding="utf-8",errors="ignore").read()
                score=0

                if "RealMap" in text:
                    score+=3
                if "MapView" in text:
                    score+=3
                if "GeoPoint" in text:
                    score+=2
                if "Search" in text:
                    score+=1
                if "Marker" in text:
                    score+=1

                if score:
                    files.append((score,path))
    return sorted(files,reverse=True)

def prepare(num):
    tasks=load_tasks()

    if num<1 or num>len(tasks):
        print("❌ رقم غير موجود")
        return

    task=tasks[num-1]

    print("\n🛠️ تجهيز المهمة:")
    print(task)

    print("\n📂 الملفات التي ستراجع:")
    for score,path in project_files()[:5]:
        print(f"- {path} (أهمية {score})")

    print("\n📋 اقتراح التنفيذ:")
    
    if "الخريطة" in task:
        print("- مراجعة RealMap.kt")
        print("- إضافة أو تحسين Marker")
        print("- ربط إحداثيات البحث بالخريطة")

    elif "بحث" in task:
        print("- مراجعة Screens.kt")
        print("- مراجعة ViewModel البحث")

    else:
        print("- يحتاج تحليل إضافي")

    print("\n⚠️ لم يتم تعديل أي ملف بعد")

print("🤖 Oran Bot v7")
print("- اعرض المهام")
print("- جهز المهمة رقم")
print("- exit")

while True:
    cmd=input("BOT> ")

    if cmd=="exit":
        break

    elif cmd=="اعرض المهام":
        for i,t in enumerate(load_tasks(),1):
            print(f"{i}- {t}")

    elif cmd.startswith("جهز المهمة"):
        try:
            prepare(int(cmd.split()[-1]))
        except:
            print("مثال: جهز المهمة 2")

    else:
        print("❓ أمر غير معروف")
