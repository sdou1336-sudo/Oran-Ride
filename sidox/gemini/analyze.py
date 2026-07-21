import os
import json

report = "sidox/reports/latest_report.json"

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("GEMINI_API_KEY not configured")
else:
    print("Gemini API key detected")

if os.path.exists(report):
    with open(report) as f:
        data = json.load(f)

    print("SIDOX REPORT")
    print(json.dumps(data, indent=2))
else:
    print("No report found")
