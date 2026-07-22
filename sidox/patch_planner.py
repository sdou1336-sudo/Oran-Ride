import os
import json
from datetime import datetime

report="sidox/reports/latest_report.json"
out="sidox/generated_kotlin_patch.json"

with open(report) as f:
    data=json.load(f)

patches=[]

category=data.get("category")

if category=="aapt2":
    patches.append({
        "file":"gradle.properties",
        "action":"append",
        "target":"android.aapt2FromMavenOverride",
        "old":"",
        "new":"android.aapt2FromMavenOverride=/data/data/com.termux/files/usr/bin/aapt2",
        "backup":True
    })

elif category=="memory":
    patches.append({
        "file":"gradle.properties",
        "action":"replace",
        "target":"org.gradle.jvmargs",
        "old":"",
        "new":"org.gradle.jvmargs=-Xmx4096m",
        "backup":True
    })

elif "AAPT2" in data.get("problem","") or "aapt2" in data.get("problem","").lower():
    patches.append({
        "file":"gradle.properties",
        "action":"append",
        "target":"android.aapt2",
        "old":"",
        "new":"android.aapt2FromMavenOverride=/data/data/com.termux/files/usr/bin/aapt2",
        "backup":True
    })

elif category=="gradle":
    patches.append({
        "file":"gradle.properties",
        "action":"append",
        "target":"android.useAndroidX",
        "old":"",
        "new":"android.useAndroidX=true\nandroid.enableJetifier=true",
        "backup":True
    })

patch={
    "created":datetime.now().isoformat(),
    "status":"pending",
    "approved":False,
    "problem":data.get("problem"),
    "category":category,
    "patches":patches
}

with open(out,"w") as f:
    json.dump(patch,f,indent=2)

print("Repair patch generated")
