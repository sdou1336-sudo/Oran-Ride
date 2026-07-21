from pathlib import Path
import json

def run():
    print("=== Oran-Ride Project Index ===")

    index = {}

    for f in Path("app/src/main/java").rglob("*.kt"):
        key = f.stem
        index[key] = str(f)

    Path("tools/project_index.json").write_text(
        json.dumps(index, indent=2, ensure_ascii=False)
    )

    print(f"✓ Indexed {len(index)} Kotlin files")
    print("✓ Saved tools/project_index.json")
    print("==============================")
