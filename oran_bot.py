import os

ERROR_FILE = "build_error.log"

def analyze_error():
    if not os.path.exists(ERROR_FILE):
        print("❌ ملف build_error.log غير موجود")
        return

    error = open(ERROR_FILE, encoding="utf-8").read()

    if not error.strip():
        print("⚠️ ملف الأخطاء فارغ")
        return

    print("\n🔎 تحليل خطأ البناء:")

    if "AAPT2" in error:
        print("المشكلة: خطأ AAPT2")
        print("الاقتراح: مراجعة إعدادات Android Gradle")

    elif "Kotlin" in error or "compile" in error:
        print("المشكلة: خطأ Kotlin")
        print("الاقتراح: مراجعة ملفات .kt")

    elif "Gradle" in error or "BUILD FAILED" in error:
        print("المشكلة: Gradle Build")
        print("الاقتراح: مراجعة dependencies والإعدادات")

    else:
        print("لم يتم تحديد السبب تلقائيًا")
        print("أول أسطر الخطأ:")
        print(error[:500])

print("🤖 Oran Bot v12 - Batman")
print("- حلل خطأ البناء")
print("- exit")

while True:
    cmd = input("BATMAN> ")

    if cmd == "exit":
        break

    elif cmd == "حلل خطأ البناء":
        analyze_error()

    else:
        print("❓ أمر غير معروف")
