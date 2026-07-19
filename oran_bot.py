import os

PLAN_FILE = "indrive_like_plan.md"

def load_tasks():
    tasks = []
    with open(PLAN_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line=line.strip()
            if line.startswith("-"):
                tasks.append(line[1:].strip())
    return tasks

def search_files(keywords):
    results=[]
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".kt"):
                path=os.path.join(root,file)
                try:
                    text=open(path,encoding="utf-8").read()
                    if any(k.lower() in text.lower() for k in keywords):
                        results.append(path)
                except:
                    pass
    return results

def analyze(num):
    tasks=load_tasks()
    if num<1 or num>len(tasks):
        print("❌ رقم غير موجود")
        return

    task=tasks[num-1]

    print("\n🔎 المهمة:")
    print(task)

    keywords=task.split()

    print("\n📂 البحث داخل المشروع...")
    files=search_files(keywords)

    if files:
        for f in files[:10]:
            print("-",f)
    else:
        print("لا توجد ملفات مطابقة")

print("🤖 Oran Bot v5")
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
