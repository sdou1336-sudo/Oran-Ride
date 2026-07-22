#!/usr/bin/env python3

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FILES = {
    "sidox/core/project_analyzer.py": "# Project Analyzer\n",
    "sidox/core/context_engine.py": "# Context Engine\n",
    "sidox/core/patch_generator.py": "# Patch Generator\n",
    "sidox/core/safe_executor.py": "# Safe Executor\n",
    "sidox/core/build_verifier.py": "# Build Verifier\n",
    "sidox/engines/code_engine.py": "# Code Engine\n",
    "sidox/engines/decision_engine.py": "# Decision Engine\n",
}

for rel, content in FILES.items():
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content, encoding="utf-8")
        print(f"[+] Created {rel}")
    else:
        print(f"[=] Exists {rel}")

print("\nSidox bootstrap completed.")
