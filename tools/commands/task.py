def run():
    print("=== Oran-Ride Task Planner ===")

    tasks = {
        "تحسين البحث": "NominatimRepository.kt",
        "تطوير GPS": "LocationManager.kt",
        "تعديل الخريطة": "MainActivity.kt",
    }

    for name, file in tasks.items():
        print(f"✓ {name} -> {file}")

    print("==============================")
