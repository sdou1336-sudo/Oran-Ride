from pathlib import Path
import json

def run():
    print("=== Oran-Ride Project Context ===")

    p = Path("tools/project_index.json")

    if not p.exists():
        print("⚠️ لا يوجد فهرس. شغل: فهرس المشروع")
        return

    data = json.loads(p.read_text())

    for name, file in data.items():
        print(f"✓ {name} -> {file}")

    print("==============================")
