from pathlib import Path
import json

task = json.loads(Path("tools/task.json").read_text(encoding="utf-8"))

target = Path(task["target_path"])

source = target.read_text(encoding="utf-8")

print("=== AI Replace Engine ===")
old = input("TEXT TO REPLACE: ")
new = input("NEW TEXT: ")

if old not in source:
    print("✗ Text not found")
    raise SystemExit

updated = source.replace(old, new, 1)

target.write_text(updated, encoding="utf-8")

task["patch_status"] = "modified"
task["last_replace"] = {
    "old": old,
    "new": new
}

Path("tools/task.json").write_text(
    json.dumps(task, indent=2, ensure_ascii=False),
    encoding="utf-8"
)

print("✓ File modified")
