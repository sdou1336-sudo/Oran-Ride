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

def scan_project():
    found=[]
    for root,dirs,files in os.walk("."):
        for file in files:
            if file.endswith(".kt"):
                path=os.path.join(root,file)
                try:
                    text=open(path,encoding="utf-8").read()
                    score=0

                    if "RealMap" in text:
                        score+=3
                    if "MapView" in text:
                        score+=3
                    if "GeoPoint" in text:
                        score+=2
                    if "Marker" in text:
                        score+=1
                    if "animateTo" in text:
                        score+=1

                    if score:
                        found.append((score,path))

                except:
                    pass

    return sorted(found,reverse=True)

def analyze(num):
    tasks=load_tasks()

    if num<1 or num>len(tasks):
        print("❌ رقم غير موجود")
        return

    print("\n🔎 المهمة:")
    print(tasks[num-1])

    print("\n📂 الملفات المرتبطة:")
    files=scan_project()

    for score,path in files[:10]:
        print(f"⭐ {score} | {path}")

print("🤖 Oran Bot v6")
print("- اعرض المهام")
print("- حلل المهمة رقم")
print("- exit")

while True:
    cmd=input("BOT> ")

    if cmd=="exit":
        break

    elif cmd=="اعرض المهام":
        for i,t in enumerate(load_tasks(),1):
            print(f"{i}- {t}")

    elif cmd.startswith("حلل المهمة"):
        try:
            analyze(int(cmd.split()[-1]))
        except:
            print("مثال: حلل المهمة 2")

    else:
        print("❓ أمر غير معروف")
