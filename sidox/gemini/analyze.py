import os
import json

report = "sidox/reports/latest_report.json"

if not os.path.exists(report):
    print("No report found")
    exit()

data = json.load(open(report))

print("SIDOX GEMINI INPUT:")
print(json.dumps(data, indent=2))

print("\nGemini connection ready (API will be added later)")
