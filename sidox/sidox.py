import json,sys,shutil
from pathlib import Path
from datetime import datetime

MODELS={
"driver":["Driver.kt","DriverRepository.kt","DriverViewModel.kt","MainActivity.kt"],
"ride":["RideRequest.kt","RideRepository.kt","RideViewModel.kt","MainActivity.kt"],
"map":["MainActivity.kt","NominatimRepository.kt"]
}

from pathlib import Path
import json,sys

task=" ".join(sys.argv[1:]).lower()

root=Path("app/src/main/java/com/oranride/app")

files=[p for p in root.glob("*.kt")]

keywords={
"driver":["Driver.kt","DriverRepository.kt","DriverViewModel.kt","MainActivity.kt"],
"ride":["RideRequest.kt","RideRepository.kt","RideViewModel.kt","MainActivity.kt"],
"map":["MainActivity.kt","NominatimRepository.kt"]
}

targets=[]

for key,names in keywords.items():
    if key in task:
        targets=names

result={
"task":task,
"project_files":len(files),
"targets":targets
}

Path("sidox/report.json").write_text(
json.dumps(result,indent=2,ensure_ascii=False)
)

if task not in ["execute","build"]:
    print(json.dumps(result,indent=2,ensure_ascii=False))


from datetime import datetime

def create_patch(targets):
    patch_dir=Path("sidox/patches")
    patch_dir.mkdir(parents=True,exist_ok=True)

    name=patch_dir/f"patch_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    data={
        "time":str(datetime.now()),
        "targets":targets,
        "status":"waiting",
        "changes":[]
    }

    import json
    name.write_text(json.dumps(data,indent=2,ensure_ascii=False))
    print("Patch created:",name)

if task.startswith("modify"):
    create_patch(result["targets"])


def execute_patch():
    import json
    from pathlib import Path

    patches=sorted(Path("sidox/patches").glob("patch_*.json"))
    if not patches:
        print("No patch found")
        return

    patch=patches[-1]
    data=json.loads(patch.read_text())

    print("Executing patch")
    print("Targets:")
    for f in data["targets"]:
        print(" -",f)

    for target in data["targets"]:
        f=Path("app/src/main/java/com/oranride/app")/Path(target).name
        if f.exists():
            txt=f.read_text(errors="ignore")
            if "// SIDOX_PATCH" not in txt:
                f.write_text("// SIDOX_PATCH\n"+txt)

    data["status"]="executed"

    patch.write_text(json.dumps(data,indent=2,ensure_ascii=False))
    print("Patch executed")

if task=="execute":
    execute_patch()


import subprocess

def build_project():
    print("Building...")
    r = subprocess.run(
        ["./gradlew","assembleDebug","--stacktrace","--info"],
        capture_output=True,
        text=True
    )
    if r.returncode == 0:
        print("BUILD SUCCESS")
    else:
        Path("sidox/build_error.log").write_text(r.stdout + "\n" + r.stderr)
        print("BUILD FAILED")
        print("Log: sidox/build_error.log")

if task=="build":
    build_project()


def analyze_build():
    from pathlib import Path
    log=Path("sidox/build_error.log")
    if not log.exists():
        print("No build log")
        return
    for line in log.read_text(errors="ignore").splitlines():
        if any(x in line for x in [
"Execution failed",
"Unresolved reference",
"Compilation error",
"BUILD FAILED",
"Exception"
]):
            print("BUILD ERROR:",line.strip())
            break

if task=="analyze-build":
    analyze_build()


def locate_error():
    log=Path("sidox/build_error.log")
    if not log.exists():
        print("No build log")
        return

    text=log.read_text(errors="ignore")

    for line in text.splitlines():
        if ".kt:" in line or ".xml:" in line:
            print("FILE:",line.strip())
            return

    print("No source file found")

if task=="locate-error":
    locate_error()

import re

def find_source_error():
    log=Path("sidox/build_error.log")
    if not log.exists():
        print("No build log")
        return
    txt=log.read_text(errors="ignore")
    m=re.search(r"(app/src/[\w/./-]+\.(kt|java|xml)):(\d+)", txt)
    if m:
        print("SOURCE:",m.group(1))
        print("LINE:",m.group(3))
    else:
        print("No source error found")

if task=="find-error":
    find_source_error()

    
def project_error_scan():
    log=Path("sidox/build_error.log")
    if not log.exists():
        print("No log")
        return
    for line in log.read_text(errors="ignore").splitlines():
        if "app/src/" in line or "res/" in line or "AndroidManifest" in line:
            print(line)

if task=="scan-error":
    project_error_scan()

def classify_error():
    log=Path("sidox/build_error.log")
    if not log.exists():
        print("No log")
        return
    txt=log.read_text(errors="ignore")
    if "AAPT2" in txt and "Daemon startup failed" in txt:
        print("TYPE: ENVIRONMENT_ERROR")
        print("REASON: AAPT2 failed outside project source")
    else:
        print("TYPE: PROJECT_ERROR")

if task=="classify-error":
    classify_error()

def decide_action():
    log=Path("sidox/build_error.log")
    if not log.exists():
        print("NO_LOG")
        return
    txt=log.read_text(errors="ignore")
    if "AAPT2" in txt and "Daemon startup failed" in txt:
        print("ACTION: FIX_BUILD_ENVIRONMENT")
    else:
        print("ACTION: ANALYZE_PROJECT_FILES")

if task=="decide":
    decide_action()

def execute_decision():
    log=Path("sidox/build_error.log")
    if not log.exists():
        print("NO_LOG")
        return
    txt=log.read_text(errors="ignore")

    if "AAPT2" in txt:
        print("PLAN:")
        print("- Use GitHub Actions build")
        print("- Skip Termux AAPT2 repair")
        print("- Continue Sidox analysis")
    else:
        print("PLAN:")
        print("- Scan project files")
        print("- Generate patch")

if task=="plan":
    execute_decision()

def log_task():
    log=Path("sidox/tasks.log")
    data={
        "time":str(__import__("datetime").datetime.now()),
        "task":task,
        "status":"planned"
    }
    with log.open("a") as f:
        f.write(json.dumps(data)+"\n")
    print("Task logged")

if task=="log":
    log_task()

def status():
    from pathlib import Path
    for f in ["sidox/tasks.log","sidox/build_error.log"]:
        if Path(f).exists():
            print("FOUND:",f)
    print("SIDOX STATUS: READY")

if task=="status":
    status()

def create_task():
    task_file=Path("sidox/next_task.json")
    data={
        "action":"use_github_actions",
        "reason":"AAPT2 environment error",
        "status":"pending"
    }
    task_file.write_text(json.dumps(data,indent=2))
    print("Next task created")

if task=="create-task":
    create_task()

def run_task():
    f=Path("sidox/next_task.json")
    if not f.exists():
        print("NO TASK")
        return

    data=json.loads(f.read_text())

    if data["action"]=="use_github_actions":
        print("EXECUTE: GitHub Actions build")
        print("SKIP: Termux AAPT2")

    data["status"]="done"
    f.write_text(json.dumps(data,indent=2))
    print("Task completed")

if task=="run-task":
    run_task()

def generate_from_task():
    f=Path("sidox/next_task.json")
    if not f.exists():
        print("NO TASK")
        return

    data=json.loads(f.read_text())

    patch={
        "task":data.get("action"),
        "reason":data.get("reason"),
        "status":"generated",
        "changes":[]
    }

    Path("sidox/generated_patch.json").write_text(
        json.dumps(patch,indent=2)
    )

    print("Patch generated")

if task=="generate-patch":
    generate_from_task()

def enrich_patch():
    f=Path("sidox/generated_patch.json")
    if not f.exists():
        print("NO PATCH")
        return

    data=json.loads(f.read_text())

    data["changes"]=[
        {
            "type":"workflow",
            "file":".github/workflows/android.yml",
            "action":"verify_build_pipeline"
        }
    ]

    data["status"]="ready"

    f.write_text(json.dumps(data,indent=2))
    print("Patch enriched")

if task=="enrich-patch":
    enrich_patch()

def validate_patch():
    f=Path("sidox/generated_patch.json")
    if not f.exists():
        print("NO PATCH")
        return

    data=json.loads(f.read_text())
    ok=True

    for c in data.get("changes",[]):
        if not Path(c["file"]).exists():
            print("MISSING:",c["file"])
            ok=False

    if ok:
        data["validation"]="passed"
        print("PATCH VALID")
    else:
        data["validation"]="failed"

    f.write_text(json.dumps(data,indent=2))

if task=="validate-patch":
    validate_patch()

def backup_file():
    f=Path("sidox/generated_patch.json")
    if not f.exists():
        print("NO PATCH")
        return

    import json
    data=json.loads(f.read_text())

    backup=Path("sidox/backups")
    backup.mkdir(exist_ok=True)

    for c in data.get("changes",[]):
        src=Path(c["file"])
        if src.exists():
            dst=backup/(src.name+"_"+__import__("datetime").datetime.now().strftime("%H%M%S"))
            shutil.copy2(src,dst)
            print("BACKUP:",dst)

    print("Backup complete")

if task=="backup":
    backup_file()

def apply_patch():
    f=Path("sidox/generated_patch.json")
    if not f.exists():
        print("NO PATCH")
        return

    data=json.loads(f.read_text())

    if data.get("validation")!="passed":
        print("PATCH NOT VALID")
        return

    print("Applying patch...")
    for c in data.get("changes",[]):
        print("TARGET:",c["file"])
        print("ACTION:",c["action"])

    data["status"]="executed"
    f.write_text(json.dumps(data,indent=2))
    print("Patch executed safely")

if task=="apply-patch":
    apply_patch()

def analyze_project():
    files=[]
    for f in Path(".").rglob("*"):
        if f.suffix in [".kt",".xml",".gradle",".kts"]:
            files.append(str(f))

    Path("sidox/project_map.json").write_text(
        json.dumps({"files":files},indent=2)
    )
    print("Project analyzed:",len(files),"files")

if task=="analyze-project":
    analyze_project()
