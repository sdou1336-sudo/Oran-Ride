import subprocess
import json
import sys
from datetime import datetime

task = " ".join(sys.argv[1:])

if not task:
    print("Usage: python3 full_pipeline.py \"your task\"")
    exit()

steps = [
    ("Analyze Task", "sidox/tasks/understand_task.py"),
    ("Select Files", "sidox/tasks/file_selector.py"),
    ("Decision Engine", "sidox/tasks/decision_engine.py"),
    ("Create Patch Plan", "sidox/tasks/patch_composer.py"),
    ("Snapshot", "sidox/tasks/pre_execution_snapshot.py"),
    ("Safe Executor Check", "sidox/tasks/executor_safe.py"),
    ("Build Verify", "sidox/tasks/build_verify.py")
]

report = {
    "time": datetime.now().isoformat(),
    "task": task,
    "steps": []
}

for name, cmd in steps:
    print("\n==========")
    print(name)
    print("==========")

    if "understand_task.py" in cmd:
        process = subprocess.run(
            ["python3", cmd],
            input=task,
            text=True,
            capture_output=True
        )
    else:
        process = subprocess.run(
            ["python3", cmd],
            capture_output=True,
            text=True
        )

    output = process.stdout + process.stderr

    print(output)

    report["steps"].append({
        "step": name,
        "status": "success" if process.returncode == 0 else "failed",
        "output": output[-1000:]
    })

    if process.returncode != 0:
        print("Pipeline stopped.")
        break

with open("sidox/tasks/pipeline_report.json","w") as f:
    json.dump(report,f,indent=2)

print("Pipeline finished")
