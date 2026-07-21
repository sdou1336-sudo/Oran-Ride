from datetime import datetime

def generate_patch(task, files):
    name = "patch_" + datetime.now().strftime("%H%M%S") + ".md"

    with open(name, "w", encoding="utf-8") as f:
        f.write("# Batman Patch Report\n\n")
        f.write(f"## المهمة: {task}\n\n")
        f.write("## الملفات:\n")

        for file in files:
            f.write(f"- {file}\n")

        f.write("\n## الحالة:\n")
        f.write("جاهز للمراجعة قبل التنفيذ\n")

    print("✅ تم إنشاء:", name)
    return name
