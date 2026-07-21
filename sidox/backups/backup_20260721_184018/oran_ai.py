import os
import shutil
import subprocess
from datetime import datetime

ROOT="app/src/main/java"

task=""
ok=False


def scan():
    return [
        os.path.join(r,f)
        for r,_,fs in os.walk(ROOT)
        for f in fs if f.endswith(".kt")
    ]


def backup():
    b="backup_"+datetime.now().strftime("%H%M%S")
    os.makedirs(b,exist_ok=True)
    for f in scan():
        shutil.copy(f,b)
    print("🛡️",b)


def analyze():
    fs=scan()
    print("📂 ملفات:",len(fs))
    for f in fs:
        print("-",f)


def plan():
    with open("oran_plan.md","w") as f:
        f.write("المهمة:\n"+task+"\n\n")
        for x in scan():
            f.write(x+"\n")
    print("📝 خطة جاهزة")


def modify():
    print("✍️ تعديل التطبيق")

    new=[
    ("Driver.kt","data class Driver(val id:Int=0,val name:String=\"\")"),
    ("Passenger.kt","data class Passenger(val id:Int=0,val name:String=\"\")"),
    ("Ride.kt","data class Ride(val id:Int=0,val status:String=\"NEW\")")
    ]

    path="app/src/main/java/com/example/data"

    os.makedirs(path,exist_ok=True)

    for name,code in new:
        file=os.path.join(path,name)
        if not os.path.exists(file):
            open(file,"w").write(
                "package com.example.data\n\n"+code
            )
            print("✅",file)


def build():
    print("🔨 Build")
    subprocess.run(["./gradlew","assembleDebug"])


def execute():
    global ok
    if not ok:
        print("اكتب وافق")
        return

    backup()
    plan()
    modify()
    build()
    print("🎯 انتهى التنفيذ")


def run():
    print("🦇 Oran AI")

    while True:
        c=input("> ")

        global task,ok

        if c=="خروج":
            break

        elif c=="تحليل":
            analyze()

        elif c.startswith("مهمة"):
            task=c.replace("مهمة","").strip()
            print(task)

        elif c=="خطة":
            plan()

        elif c=="وافق":
            ok=True
            print("✅")

        elif c=="تنفيذ":
            execute()

        else:
            print("؟")


