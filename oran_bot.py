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

def analyze_task(num):
    tasks = load_tasks()

    if num < 1 or num > len(tasks):
        print("❌ رقم المهمة غير موجود")
        return

    task = tasks[num-1]
    print("\n🔎 تحليل المهمة:")
    print(task)

    keywords = {
        "بحث": ["Screens.kt", "OranRideViewModel.kt"],
        "الخريطة": ["RealMap.kt", "Screens.kt"],
        "GPS": ["Location", "ViewModel"],
        "Marker": ["RealMap.kt"],
        "رحلة": ["ViewModel", "Screens.kt"],
        "سائق": ["Driver", "ViewModel"]
    }

    print("\n📂 ملفات محتملة:")
    found = False

    for key, files in keywords.items():
        if key in task:
            for f in files:
                print("-", f)
            found = True

    if not found:
        print("- يحتاج بحث يدوي داخل المشروع")

print("🤖 Oran Bot v4")
print("الأوامر:")
print("- اعرض المهام")
print("- حلل المهمة رقم")
print("- exit")

while True:
    cmd = input("BOT> ")

    if cmd == "exit":
        break

    elif cmd == "اعرض المهام":
        for i, task in enumerate(load_tasks(), 1):
            print(f"{i}- {task}")

    elif cmd.startswith("حلل المهمة"):
        try:
            num = int(cmd.split()[-1])
            analyze_task(num)
        except:
            print("اكتب مثال: حلل المهمة 2")

    else:
        print("❓ أمر غير معروف")
