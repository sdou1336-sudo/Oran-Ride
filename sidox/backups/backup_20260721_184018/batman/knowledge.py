import os
import re

ROOT = "app/src/main/java"

def show_knowledge():
    print("\n🧠 معرفة المشروع:\n")

    for root, dirs, files in os.walk(ROOT):
        for f in sorted(files):
            if not f.endswith(".kt"):
                continue

            path = os.path.join(root, f)

            try:
                text = open(path, encoding="utf-8").read()
            except:
                continue

            classes = len(re.findall(r'(?:data\s+)?class\s+\w+', text))
            composables = len(re.findall(r'@Composable\s+fun\s+\w+', text))
            functions = len(re.findall(r'fun\s+\w+\(', text))

            print(f"📄 {f}")
            print(f"   Classes: {classes}")
            print(f"   Composable: {composables}")
            print(f"   Functions: {functions}\n")
