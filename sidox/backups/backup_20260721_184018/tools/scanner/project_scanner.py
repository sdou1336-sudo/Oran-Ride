from pathlib import Path
import json

def run():
    root = Path(".")
    files = []

    for p in root.rglob("*"):
        if p.is_file() and "build" not in str(p) and ".git" not in str(p):
            files.append(str(p))

    data = {
        "project": "Oran-Ride",
        "files_count": len(files),
        "files": files
    }

    Path("tools/project_map.json").write_text(
        json.dumps(data, indent=2, ensure_ascii=False)
    )

    print(f"✓ Project scanned: {len(files)} files")

if __name__ == "__main__":
    run()
