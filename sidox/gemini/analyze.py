import os
import json
import urllib.request

report = "sidox/reports/latest_report.json"
key = os.getenv("GEMINI_API_KEY")

if not key:
    print("Missing GEMINI_API_KEY")
    exit(1)

if not os.path.exists(report):
    print("No report found")
    exit(1)

with open(report) as f:
    data = json.load(f)

prompt = "Analyze this Android project build report and explain the problem:\n" + json.dumps(data, ensure_ascii=False)

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=" + key

body = json.dumps({
    "contents": [
        {
            "parts": [
                {"text": prompt}
            ]
        }
    ]
}).encode()

req = urllib.request.Request(
    url,
    data=body,
    headers={"Content-Type": "application/json; charset=utf-8"}
)

try:
    with urllib.request.urlopen(req) as r:
        result = json.loads(r.read())
    print(json.dumps(result, indent=2))
except Exception as e:
    print("Gemini analysis unavailable:")
    print(e)
