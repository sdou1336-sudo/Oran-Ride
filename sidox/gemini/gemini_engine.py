from pathlib import Path
import json
from datetime import datetime

def analyze(data):
    result = {
        "time": datetime.now().isoformat(),
        "engine": "Gemini-Sidox",
        "mode": "suggestion_only",
        "suggestions": []
    }

    if "AAPT2" in str(data):
        result["suggestions"].append(
            "Use GitHub Actions for Android build environment"
        )

    else:
        result["suggestions"].append(
            "No automatic fix suggested"
        )

    return result


if __name__ == "__main__":
    with open("sidox/build_error.log", errors="ignore") as f:
        log = f.read()

    result = analyze(log)
Path("sidox/gemini/gemini_suggestions.json").write_text(
    json.dumps(result, indent=2)
)
print(json.dumps(result, indent=2))
