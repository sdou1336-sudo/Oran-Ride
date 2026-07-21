def create_change_plan(files, task):
    print("\n📝 خطة التغيير:\n")

    for file in files:
        print("📄", file)

        if "Map" in file or "map" in file:
            print("  - تحسين الخريطة")
            print("  - مراجعة Marker")
            print("  - مراجعة المسار")

        elif "Location" in file:
            print("  - تحسين تحديث الموقع")

        elif "Repository" in file:
            print("  - مراجعة منطق البيانات")

        elif "Database" in file:
            print("  - مراجعة قاعدة البيانات")

        else:
            print("  - مراجعة الملف")

        print()

    print("⚠️ الخطة جاهزة قبل التنفيذ")
