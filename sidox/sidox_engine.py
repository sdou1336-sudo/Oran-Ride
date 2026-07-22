import os, json, shutil
from datetime import datetime
from pathlib import Path

BASE="sidox"

def save(name,data):
    Path(BASE).mkdir(exist_ok=True)
    Path(f"{BASE}/{name}.json").write_text(json.dumps(data,indent=2))

def analyze():
    files=[str(f) for f in Path(".").rglob("*") if f.suffix in [".kt",".xml",".gradle",".kts"]]
    save("project_map",{"time":datetime.now().isoformat(),"files":files})
    print("ANALYZE OK:",len(files),"files")

def decide():
    log=Path("sidox/build_error.log").read_text(errors="ignore") if Path("sidox/build_error.log").exists() else ""
    result={"action":"none"}
    if "AAPT2" in log:
        result={"action":"use_github_actions","reason":"AAPT2 environment error"}
    save("decision",result)
    print(json.dumps(result,indent=2))

def gemini():
    result={"engine":"Gemini-Sidox","mode":"suggestion_only","suggestions":[]}
    log=Path("sidox/build_error.log").read_text(errors="ignore") if Path("sidox/build_error.log").exists() else ""
    if "AAPT2" in log:
        result["suggestions"].append("Use GitHub Actions for Android build environment")
    save("gemini_suggestions",result)
    print(json.dumps(result,indent=2))

def patch():
    gem=json.loads(Path("sidox/gemini_suggestions.json").read_text())
    patch={"status":"ready","created":datetime.now().isoformat(),"changes":gem["suggestions"]}
    save("generated_patch",patch)
    print("PATCH READY")

def backup():
    Path("sidox/backups").mkdir(exist_ok=True)
    print("BACKUP OK")

def log():
    with open("sidox/tasks.log","a") as f:
        f.write(datetime.now().isoformat()+" Sidox\n")
    print("LOG OK")

cmd=os.sys.argv[1] if len(os.sys.argv)>1 else ""

{
"analyze":analyze,
"decide":decide,
"gemini":gemini,
"patch":patch,
"backup":backup,
"log":log
}.get(cmd,lambda:print("commands: analyze decide gemini patch backup log"))()
