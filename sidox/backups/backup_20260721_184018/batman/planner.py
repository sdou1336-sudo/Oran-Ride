from batman.tasks import KEYWORDS
import os

ROOT = "app/src/main/java"

def plan_task(task):
    print(f"\n📋 خطة تعديل: {task}\n")

    words = KEYWORDS.get(task)

    if not words:
        print("❌ المهمة غير معروفة")
        return

    for root, dirs, files in os.walk(ROOT):
        for f in sorted(files):
            name = f.lower()

            if any(word in name for word in words):
                print(f"📄 {f}")

                if "map" in name:
                    print("  - تحسين الخريطة")
                    print("  - تحسين Marker")

                elif "location" in name:
                    print("  - مراجعة تحديث الموقع")

                elif "route" in name:
                    print("  - تحسين المسار")

                elif "search" in name or "place" in name:
                    print("  - تحسين البحث")

                elif "repository" in name:
                    print("  - تحديث منطق البيانات")

                elif "database" in name:
                    print("  - مراجعة قاعدة البيانات")

                print()
