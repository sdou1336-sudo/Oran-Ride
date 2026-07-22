from pathlib import Path
import json
from datetime import datetime

with open("sidox/user_task.json") as f:
    t=json.load(f)

req=t.get("request","").lower()
files=[]
targets = []
try:
    import json
    plan=json.load(open("sidox/task_plan.json"))
    targets=plan.get("targets",[])
except:
    pass

for name in targets:
    result=list(Path(".").rglob(name))
    if result:
        files.append({
            "file": str(result[0]),
            "content": f"// Sidox generated update for {name}"
        })

if "indrive" in req or "passenger" in req or "tracking" in req:
    files=[
{"file":"app/src/main/java/com/oranride/app/RideFlow.kt",
"content":"""package com.oranride.app

data class RideFlow(val status:String="WAITING")"""},
{"file":"app/src/main/java/com/oranride/app/RideFlowViewModel.kt",
"content":"""package com.oranride.app

class RideFlowViewModel {
    var status="WAITING"
}"""}
]

elif "compose" in req or "ridepage" in req:
    files=[
{"file":"app/src/main/java/com/oranride/app/RideViewModel.kt",
"content":"package com.oranride.app\n\nclass RideViewModel { var accepted=false }"},
{"file":"app/src/main/java/com/oranride/app/RidePage.kt",
"content":"package com.oranride.app\n\nclass RidePage"}
]

json.dump({
"created":datetime.now().isoformat(),
"status":"pending",
"approved":False,
"task":t,
"files":files
},open("sidox/generated_kotlin_patch.json","w"),indent=2)

print("Kotlin Generator upgraded")
