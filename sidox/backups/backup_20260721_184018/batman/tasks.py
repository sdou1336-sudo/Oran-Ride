import os

ROOT = "app/src/main/java"

KEYWORDS = {
    "الخريطة": ["map", "realmap", "location", "route", "place"],
    "البحث": ["search", "place"],
    "السائق": ["driver"],
    "الرحلة": ["ride"],
    "قاعدة البيانات": ["database", "repository"],
}

def prepare_task(task):
    print(f"\n🛠️ تجهيز المهمة: {task}\n")

    words = KEYWORDS.get(task)

    if not words:
        print("❌ المهمة غير معروفة")
        return

    found = []

    for root, dirs, files in os.walk(ROOT):
        for f in files:
            name = f.lower()

            for w in words:
                if w in name:
                    found.append(os.path.join(root, f))
                    break

    if not found:
        print("لم يتم العثور على ملفات مناسبة")
        return

    print("📂 الملفات المقترحة:\n")
    for f in found:
        print("-", f)
