def review_patch(filename):
    print("\n🔍 مراجعة التعديل:\n")

    try:
        with open(filename, encoding="utf-8") as f:
            print(f.read())

        print("\n✅ التعديل جاهز للمراجعة")
        print("الأمر القادم سيكون: وافق")

    except:
        print("❌ ملف التعديل غير موجود")
