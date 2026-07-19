import os

ROOT = "app/src/main/java"

def analyze_project():
    print("\n📂 تحليل المشروع:\n")

    count = 0

    for root, dirs, files in os.walk(ROOT):
        for f in sorted(files):
            if f.endswith(".kt"):
                print("-", os.path.join(root, f))
                count += 1

    print(f"\n✅ عدد ملفات Kotlin: {count}")
