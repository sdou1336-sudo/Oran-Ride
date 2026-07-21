from pathlib import Path
import json
import shutil
import time

TASK = Path("tools/task.json")

if not TASK.exists():
    raise SystemExit("task.json not found")

task = json.loads(TASK.read_text(encoding="utf-8"))

if task.get("status") != "waiting":
    print("Nothing to execute")
    raise SystemExit

target = str(task.get("file","")).split(";")[0].strip()

root = Path(".")
matches = list(root.rglob(target))

if not matches:
    print(f"Target file not found: {target}")
    raise SystemExit

file = matches[0]

backup_dir = Path("backup_tasks")
backup_dir.mkdir(exist_ok=True)

backup = backup_dir / f"{file.name}.{int(time.time())}.bak"
shutil.copy2(file, backup)

task["target_path"] = str(file)
task["backup"] = str(backup)
task["execution"] = "file_opened"
task["executor"] = "AI Developer Agent v2"

TASK.write_text(
    json.dumps(task, indent=2, ensure_ascii=False),
    encoding="utf-8"
)

print("✓ Target:", file)
print("✓ Backup:", backup)
