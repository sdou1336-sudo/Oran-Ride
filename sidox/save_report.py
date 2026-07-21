import os, json, datetime, shutil

src = "sidox/reports/latest_report.json"
dst_dir = "sidox/history"

if os.path.exists(src):
    name = datetime.datetime.now().strftime("report_%Y%m%d_%H%M%S.json")
    shutil.copy(src, os.path.join(dst_dir, name))
    print("Report saved:", name)
else:
    print("No report found")
