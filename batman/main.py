from batman.analyzer import analyze_project
from batman.knowledge import show_knowledge
from batman.tasks import prepare_task
from batman.planner import plan_task

def run():
    print("🦇 Batman Framework v20")
    print("- حلل المشروع")
    print("- اعرف المشروع")
    print("- جهز مهمة")
    print("- خطط مهمة")
    print("- exit")

    while True:
        cmd = input("BATMAN> ").strip()

        if cmd == "exit":
            print("👋 إلى اللقاء")
            break

        elif cmd == "حلل المشروع":
            analyze_project()

        elif cmd == "اعرف المشروع":
            show_knowledge()

        elif cmd.startswith("جهز مهمة"):
            task = cmd.replace("جهز مهمة", "").strip()
            prepare_task(task)

        elif cmd.startswith("خطط مهمة"):
            task = cmd.replace("خطط مهمة", "").strip()
            plan_task(task)

        else:
            print("❓ أمر غير معروف")
