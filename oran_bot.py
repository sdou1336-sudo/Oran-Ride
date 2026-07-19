import os

PLAN_FILE = "indrive_like_plan.md"

pending = None

def load_tasks():
    tasks=[]
    with open(PLAN_FILE,encoding="utf-8") as f:
        for line in f:
            line=line.strip()
            if line.startswith("-"):
                tasks.append(line[1:].strip())
    return tasks

def suggest(num):
    global pending

    tasks=load_tasks()

    if num < 1 or num > len(tasks):
        print("❌ رقم غير موجود")
        return

    pending=num
    task=tasks[num-1]

    print("\n📝 اقتراح تعديل:")
    print("المهمة:", task)

    if "الخريطة" in task:
        print("""
التعديلات المقترحة:
1- تعديل RealMap.kt
2- إضافة Marker للوجهة
3- تحديث حركة الكاميرا عند اختيار المكان
4- ربط إحداثيات البحث بالخريطة
""")

    elif "بحث" in task:
        print("""
التعديلات المقترحة:
1- مراجعة البحث في ViewModel
2- تحسين عرض النتائج
""")

    else:
        print("يحتاج تحليل إضافي")

    print("للتنفيذ اكتب: وافق")

def approve():
    if pending:
        print("✅ تم قبول التعديل")
        print("⚠️ التنفيذ الفعلي سيضاف في النسخة القادمة")
    else:
        print("لا يوجد تعديل معلق")

print("🤖 Oran Bot v9")
print("- اقترح تعديل رقم")
print("- وافق")
print("- exit")

while True:
    cmd=input("BOT> ")

    if cmd=="exit":
        break

    elif cmd.startswith("اقترح تعديل"):
        try:
            suggest(int(cmd.split()[-1]))
        except:
            print("مثال: اقترح تعديل 2")

    elif cmd=="وافق":
        approve()

    else:
        print("❓ أمر غير معروف")
