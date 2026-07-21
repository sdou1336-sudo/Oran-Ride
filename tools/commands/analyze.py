from pathlib import Path

def run():
    print("=== Oran-Ride Project Analyzer ===")

    files = list(Path("app/src/main/java").rglob("*.kt"))

    for f in files:
        name = f.name.lower()

        if "location" in name:
            print(f"✓ Location file -> {f}")
        elif "map" in name:
            print(f"✓ Map file -> {f}")
        elif "nominatim" in name:
            print(f"✓ Search file -> {f}")
        elif "main" in name:
            print(f"✓ Main UI -> {f}")

    print("==============================")
