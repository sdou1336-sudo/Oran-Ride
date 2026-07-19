import os
import shutil
from datetime import datetime

TARGET = "app/src/main/java/com/example/ui/RealMap.kt"

def backup_file():
    if os.path.exists(TARGET):
        name = "backup_RealMap_" + datetime.now().strftime("%H%M%S") + ".kt"
        shutil.copy(TARGET, name)
        print("✅ نسخة احتياطية:", name)

def inspect_map():
    if not os.path.exists(TARGET):
        print("❌ الملف غير موجود")
        return

    text = open(TARGET, encoding="utf-8").read()

    print("\n🔎 تحليل RealMap.kt")
    print("Marker موجود:", "Marker" in text)
    print("animateTo موجود:", "animateTo" in text)
    print("MapView موجود:", "MapView" in text)

def prepare():
    print("""
🛠️ المهمة:
إضافة Marker للوجهة

الملف:
RealMap.kt

الحالة:
- سيتم تجهيز التعديل فقط
- لا يوجد تغيير تلقائي بعد
""")

def main():
    print("🤖 Oran Bot v10")
    print("- فحص الخريطة")
    print("- جهز Marker")
    print("- exit")

    while True:
        cmd=input("BOT> ")

        if cmd=="exit":
            break
        elif cmd=="فحص الخريطة":
            inspect_map()
        elif cmd=="جهز Marker":
            backup_file()
            prepare()
        else:
            print("❓ أمر غير معروف")

main()
