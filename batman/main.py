from batman.analyzer import analyze_project

def run():
    print("🦇 Batman Framework v16")
    print("- حلل المشروع")
    print("- exit")

    while True:
        cmd = input("BATMAN> ")

        if cmd == "exit":
            print("👋 إلى اللقاء")
            break

        elif cmd == "حلل المشروع":
            analyze_project()

        else:
            print("❓ أمر غير معروف")
