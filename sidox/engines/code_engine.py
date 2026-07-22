#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime

decision=Path("sidox/decision.json")
out=Path("sidox/code_patch.json")

data=json.loads(decision.read_text()) if decision.exists() else {}

patch={
 "time":datetime.now().isoformat(),
 "approved":False,
 "targets":data.get("targets",[]),
 "changes":[]
}

for f in patch["targets"][:10]:
    patch["changes"].append({
        "file":f,
        "action":"analyze_and_modify"
    })

out.write_text(json.dumps(patch,indent=2,ensure_ascii=False))
print("Code Engine ready")
print("Saved:",out)
