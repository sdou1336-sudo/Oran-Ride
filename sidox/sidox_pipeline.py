#!/usr/bin/env python3
import subprocess

steps = [
    "python3 sidox/core/project_analyzer.py",
    "python3 sidox/core/context_engine.py",
    "python3 sidox/engines/decision_engine.py",
    "python3 sidox/core/patch_generator.py",
    "python3 sidox/core/repair_executor.py",
    "python3 sidox/core/safe_executor.py",
    "python3 sidox/core/build_verifier.py",
    "python3 sidox/core/build_error_analyzer.py"
]

for step in steps:
    print("\n>>>", step)
    result = subprocess.run(step, shell=True)
    if result.returncode != 0:
        print("Stopped:", step)
        break

print("\nSidox Pipeline finished")
