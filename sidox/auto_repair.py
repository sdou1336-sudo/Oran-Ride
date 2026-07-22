#!/usr/bin/env python3
import subprocess

steps=[
"python3 sidox/core/project_analyzer.py",
"python3 sidox/core/context_engine.py",
"python3 sidox/engines/decision_engine.py",
"python3 sidox/core/repair_engine.py",
"python3 sidox/core/repair_patch_generator.py",
"python3 sidox/core/kotlin_generator.py",
"python3 sidox/core/kotlin_patch_executor.py",
"python3 sidox/core/build_verifier.py",
"python3 sidox/core/build_error_analyzer.py"
]

for s in steps:
    print("\n>>>",s)
    r=subprocess.run(s,shell=True)
    if r.returncode:
        print("Stopped:",s)
        break

print("\nSidox Auto Repair finished")
