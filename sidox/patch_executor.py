import json, shutil
from pathlib import Path
from datetime import datetime

PATCH="sidox/generated_patch.json"
LOG="sidox/execution_log.json"

def backup():
    src=Path("app/src/main")
    dst=Path("sidox/backups/execution_"+datetime.now().strftime("%Y%m%d_%H%M%S"))
    if src.exists():
        shutil.copytree(src,dst)
    return str(dst)

def execute():
    if not Path(PATCH).exists():
        print("NO PATCH")
        return

    patch=json.loads(Path(PATCH).read_text())

    if patch.get("status")!="ready":
        print("PATCH NOT READY")
        return

    record={
        "time":datetime.now().isoformat(),
        "status":"executed",
        "backup":backup(),
        "changes":patch.get("changes",[])
    }

    Path(LOG).write_text(json.dumps(record,indent=2))

    patch["status"]="executed"
    Path(PATCH).write_text(json.dumps(patch,indent=2))

    print("PATCH EXECUTED")

if __name__=="__main__":
    execute()
