from pathlib import Path
import json

task = json.loads(Path("tools/task.json").read_text(encoding="utf-8"))

target = task.get("target_path")
if not target:
    raise SystemExit("No target_path found. Run executor first.")

file = Path(target)
if not file.exists():
    raise SystemExit(f"Target file not found: {file}")

text = file.read_text(encoding="utf-8")

task["file_size"] = len(text)
task["lines"] = len(text.splitlines())
task["patch_status"] = "loaded"

Path("tools/task.json").write_text(
    json.dumps(task, indent=2, ensure_ascii=False),
    encoding="utf-8"
)

Path("tools/agent/current_source.kt").write_text(
    text,
    encoding="utf-8"
)

print("✓ File loaded")
print("✓ Lines:", task["lines"])
print("✓ Characters:", task["file_size"])
print("✓ Source copied to tools/agent/current_source.kt")
