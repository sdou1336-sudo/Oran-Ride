from pathlib import Path
import json

def run():
    print("=== Precheck Context ===")

    p = Path("tools/project_index.json")

    if not p.exists():
        print("⚠️ لا يوجد فهرس المشروع")
        print("شغل: فهرس المشروع")
        return

    data = json.loads(p.read_text())

    checks = [
        "NominatimRepository",
        "LocationManager",
        "MainActivity"
    ]

    for item in checks:
        if item in data:
            print(f"✓ Found {item} -> {data[item]}")
        else:
            print(f"⚠️ Missing {item}")

    print("========================")
