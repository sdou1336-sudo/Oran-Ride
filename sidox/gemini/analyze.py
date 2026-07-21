import json
import os

report = "sidox/reports/latest_report.json"

if not os.path.exists(report):
    print("No sidox report found")
    exit(1)

with open(report) as f:
    data = json.load(f)

print("SIDOX REPORT FOR AI ANALYSIS")
print(json.dumps(data, indent=2))

print("Gemini connector ready")
