import os

PLAN_FILE = "indrive_like_plan.md"

def load_tasks():
    tasks = []
    if os.path.exists(PLAN_FILE):
        with open(PLAN_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("-"):
                    tasks.append(line[1:].strip())
    return tasks

print("🤖 Oran Bot v3")
print("الأوامر:")
print("- اقرأ الخطة")
print("- اعرض المهام")
print("- exit")

while True:
    cmd = input("BOT> ")

    if cmd == "exit":
        break

    elif cmd == "اقرأ الخطة":
        if os.path.exists(PLAN_FILE):
            print(open(PLAN_FILE, encoding="utf-8").read())
        else:
            print("❌ ملف الخطة غير موجود")

    elif cmd == "اعرض المهام":
        tasks = load_tasks()
        for i, task in enumerate(tasks, 1):
            print(f"{i}- {task}")

    else:
        print("❓ أمر غير معروف")
