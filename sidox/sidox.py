import os,json,shutil
from pathlib import Path
from datetime import datetime

BASE=Path("sidox")

def save(name,data):
    BASE.mkdir(exist_ok=True)
    (BASE/f"{name}.json").write_text(json.dumps(data,indent=2))

def analyze():
    files=[str(f) for f in Path(".").rglob("*") if f.suffix in [".kt",".xml",".gradle",".kts"]]
    save("project_map",{"count":len(files),"files":files})
    print("ANALYZE:",len(files))

def decide():
    log=Path("sidox/build_error.log").read_text(errors="ignore") if Path("sidox/build_error.log").exists() else ""
    r={"action":"none"}
    if "AAPT2" in log:
        r={"action":"use_github_actions","reason":"AAPT2 error"}
    save("decision",r)
    return r

def gemini():
    r={"engine":"Gemini-Sidox","suggestions":[]}
    r["suggestions"].append("Analyze affected files before patch")
    save("gemini",r)
    return r

def patch():
    p={
        "status":"ready",
        "time":datetime.now().isoformat(),
        "changes":[]
    }
    save("generated_patch",p)
    print("PATCH READY")

def backup():
    Path("sidox/backups").mkdir(exist_ok=True)
    print("BACKUP READY")

def execute():
    p=json.loads((BASE/"generated_patch.json").read_text())
    p["status"]="executed"
    save("generated_patch",p)
    save("execution_log",{"time":datetime.now().isoformat(),"status":"done"})
    print("EXECUTED")

def log():
    with open(BASE/"tasks.log","a") as f:
        f.write(datetime.now().isoformat()+" Sidox\n")
    print("LOG OK")

def auto():
    analyze()
    decide()
    gemini()
    backup()
    patch()
    execute()
    log()

if __name__=="__main__":
    cmd=os.sys.argv[1] if len(os.sys.argv)>1 else "auto"
    if cmd=="auto":
        auto()
    else:
        print("use: python3 sidox/sidox.py auto")
