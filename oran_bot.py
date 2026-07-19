import os

ROOT = "app/src/main"

print("🤖 Batman v13")
print("- افهم المشروع")
print("- exit")

while True:
    cmd = input("BATMAN> ")

    if cmd == "exit":
        break

    elif cmd == "افهم المشروع":

        report = []

        for root, dirs, files in os.walk(ROOT):
            kt = [f for f in files if f.endswith(".kt")]
            if kt:
                report.append(f"\n📂 {root}")
                for f in sorted(kt):
                    report.append(f" - {f}")

        with open("project_map.md", "w", encoding="utf-8") as out:
            out.write("# Project Map\n\n")
            out.write("\n".join(report))

        print("✅ تم إنشاء project_map.md")

    else:
        print("❓ أمر غير معروف")
