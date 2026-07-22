import json
import os

error_file="sidox/build_error.json"

if not os.path.exists(error_file):
    print("No build error found")
    exit(0)

with open(error_file) as f:
    data=json.load(f)

err=data.get("error","")

text=err.lower()

if "aapt2" in text or "aapt2" in text:
    category="aapt2"
elif "could not resolve" in text or "could not find" in text or "dependency" in text:
    category="dependency"
elif "java heap space" in text or "outofmemory" in text:
    category="memory"
elif "unresolved reference" in text or "cannot find symbol" in text:
    category="kotlin"
elif "duplicate class" in text:
    category="conflict"
else:
    category="gradle"

report={
    "status":"FAILED",
    "problem":err[-1000:],
    "category":category
}

with open("sidox/reports/latest_report.json","w") as f:
    json.dump(report,f,indent=2)

print("Analysis complete:", category)
