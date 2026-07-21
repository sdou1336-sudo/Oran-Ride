from pathlib import Path
import json

root = Path(".")
files = []

for p in root.rglob("*"):
    if p.is_file() and not any(x in str(p) for x in [".gradle","build",".git"]):
        files.append(str(p))

report = {
    "project": root.name,
    "files_count": len(files),
    "important_files": [f for f in files if f.endswith((".kt",".kts",".xml"))][:100]
}

Path("sidox/reports").mkdir(exist_ok=True)
Path("sidox/reports/project_analysis.json").write_text(
    json.dumps(report, indent=2, ensure_ascii=False)
)

print("Sidox project analysis completed")
print("Files:", len(files))
