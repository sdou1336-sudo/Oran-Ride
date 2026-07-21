from pathlib import Path
import json

files = []

for p in Path("app/src/main/java").rglob("*.kt"):
    text = p.read_text(errors="ignore")
    files.append({
        "file": str(p),
        "functions": [x.strip().split("(")[0] for x in text.split("fun ")[1:]],
        "classes": [x.strip().split()[0] for x in text.split("class ")[1:]]
    })

Path("sidox/reports/structure.json").write_text(
    json.dumps(files, indent=2, ensure_ascii=False)
)

print("Sidox structure scan completed")
print("Kotlin files:", len(files))
