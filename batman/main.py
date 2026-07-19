from batman.analyzer import analyze_project
from batman.knowledge import show_knowledge
from batman.tasks import prepare_task
from batman.planner import plan_task
from batman.brain import execute
from batman.approval import approve
from batman.executor import execute_patch

def run():
    print("🦇 Batman Framework v20")
    print("- حلل المشروع")
    print("- اعرف المشروع")
    print("- جهز مهمة")
    print("- خطط مهمة")
    print("- exit")

    while True:
        cmd = input("BATMAN> ").strip()

        if cmd == "نفذ التعديل":
            execute_patch()

        elif cmd == "وافق":
            approve()

        elif cmd == "exit":
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

        elif cmd.startswith("نفذ"):
            task = cmd.replace("نفذ", "").strip()
            execute(task)

        else:
            print("❓ أمر غير معروف")
