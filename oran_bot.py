import os
import re

ROOT = "app/src/main/java"

print("🤖 Batman v14")
print("- افهم المشروع")
print("- exit")

while True:
    cmd = input("BATMAN> ")

    if cmd == "exit":
        break

    elif cmd == "افهم المشروع":

        report = ["# Project Brain\n"]

        for root, dirs, files in os.walk(ROOT):
            for f in sorted(files):
                if not f.endswith(".kt"):
                    continue

                path = os.path.join(root, f)

                try:
                    text = open(path, encoding="utf-8").read()
                except:
                    continue

                report.append(f"\n## {f}")

                composables = re.findall(r'@Composable\s+fun\s+(\w+)', text)
                classes = re.findall(r'(?:data\s+)?class\s+(\w+)', text)
                funcs = re.findall(r'fun\s+(\w+)\(', text)

                if classes:
                    report.append("Classes:")
                    for c in classes:
                        report.append(f"- {c}")

                if composables:
                    report.append("Composable:")
                    for c in composables:
                        report.append(f"- {c}")

                other = [x for x in funcs if x not in composables]
                if other:
                    report.append("Functions:")
                    for fn in other[:15]:
                        report.append(f"- {fn}")

        with open("project_brain.md","w",encoding="utf-8") as out:
            out.write("\n".join(report))

        print("✅ تم إنشاء project_brain.md")

    else:
        print("❓ أمر غير معروف")
