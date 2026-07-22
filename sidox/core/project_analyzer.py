#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(".").resolve()
IGNORE = {".git","build","__pycache__","backups"}

files=[]

for p in ROOT.rglob("*.kt"):
    if any(x in IGNORE for x in p.parts):
        continue
    try:
        text=p.read_text(errors="ignore")
        files.append({
            "file":str(p.relative_to(ROOT)),
            "size":p.stat().st_size,
            "classes":text.count("class "),
            "functions":text.count("fun "),
            "composables":text.count("@Composable")
        })
    except:
        pass

data={"project":ROOT.name,"kotlin_analysis":files}

Path("sidox/project_map.json").write_text(
    json.dumps(data,indent=2,ensure_ascii=False),
    encoding="utf-8"
)

print("Deep analysis complete.")
print("Kotlin files:",len(files))
print("Saved: sidox/project_map.json")
