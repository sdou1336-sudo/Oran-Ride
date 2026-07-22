#!/data/data/com.termux/files/usr/bin/bash
python3 sidox/analyzer.py
python3 sidox/patch_planner.py
python3 sidox/core/kotlin_patch_executor.py --auto-approve
python3 sidox/core/build_retry.py
