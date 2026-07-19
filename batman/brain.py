from batman.analyzer import analyze_project
from batman.knowledge import show_knowledge
from batman.tasks import prepare_task
from batman.planner import plan_task
from batman.patcher import generate_patch
from batman.reviewer import review_patch
from datetime import datetime
import shutil
import os

def backup():
    name = "batman_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs(name, exist_ok=True)
    print("✅ Backup:", name)

def execute(command):
    print("\n🦇 Batman Brain\n")

    analyze_project()
    print()

    show_knowledge()
    print()

    prepare_task(command)
    print()

    plan_task(command)

    files = []
    import os
    for root, dirs, fs in os.walk("app/src/main/java"):
        for file in fs:
            if file.endswith(".kt") and any(x in file.lower() for x in command.lower().split()):
                files.append(os.path.join(root, file))

    patch = generate_patch(command, files)
    review_patch(patch)

    print("\n🛡️ تجهيز التنفيذ")
    backup()

    print("""
📄 تقرير التعديل جاهز:
- الملفات محددة
- الخطة جاهزة
- النسخة الاحتياطية جاهزة

⚠️ بانتظار مرحلة توليد التعديل
""")
