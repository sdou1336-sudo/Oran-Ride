import os

def read_patch(filename):
    if not os.path.exists(filename):
        print("❌ Patch غير موجود")
        return []

    files = []

    with open(filename, encoding="utf-8") as f:
        for line in f:
            if line.startswith("- app/"):
                files.append(line.strip("- ").strip())

    print("📄 الملفات من Patch:")
    for f in files:
        print("-", f)

    return files
