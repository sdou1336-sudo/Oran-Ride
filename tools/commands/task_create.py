from pathlib import Path
import json

def run():
    task = {
        "task": "تحسين محرك البحث",
        "file": "NominatimRepository.kt",
        "status": "waiting"
    }

    Path("tools/task.json").write_text(
        json.dumps(task, ensure_ascii=False, indent=2)
    )

    print("✓ Task created")
    print("✓ Waiting approval")
