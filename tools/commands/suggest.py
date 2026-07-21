from pathlib import Path
import json

def run():
    print("=== Oran-Ride Modification Suggestion ===")

    p = Path("tools/project_index.json")

    if not p.exists():
        print("⚠️ لا يوجد فهرس المشروع")
        print("شغل: فهرس المشروع")
        return

    data = json.loads(p.read_text())

    targets = {
        "البحث": "NominatimRepository",
        "nominatim": "NominatimRepository",
        "gps": "LocationManager",
        "الموقع": "LocationManager",
        "الخريطة": "MainActivity",
    }

    found = False

    for key, file in targets.items():
        if key in " ".join(data.keys()).lower():
            if file in data:
                print(f"✓ الملف المقترح: {data[file]}")
                print(f"✓ السبب: متعلق بـ {file}")
                found = True
                break

    if not found:
        print("⚠️ لم يتم تحديد الملف المناسب")

    print("======================================")
