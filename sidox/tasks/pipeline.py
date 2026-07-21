import subprocess
import json

steps = [
    ("Understand Task", "python3 sidox/tasks/understand_task.py"),
    ("Select Files", "python3 sidox/tasks/file_selector.py"),
    ("Generate Patch", "python3 sidox/tasks/generate_patch.py"),
    ("Apply Patch", "python3 sidox/tasks/apply_patch.py"),
    ("Build Verify", "python3 sidox/tasks/build_verify.py"),
    ("Rollback Check", "python3 sidox/tasks/rollback.py")
]

for name, command in steps:
    print("\n===", name, "===")

    result = subprocess.run(
        command,
        shell=True
    )

    if result.returncode != 0:
        print("Step failed:", name)
        break

print("\nSidox pipeline finished")
