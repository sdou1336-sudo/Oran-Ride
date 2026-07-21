from pathlib import Path
import json

screen = Path("tools/ui_agent/current_screen.png")
state = Path("tools/ui_agent/ui_state.json")

if not screen.exists():
    print("✗ Screenshot not found")
    exit()

analysis = {
    "status": "ready_for_ai_analysis",
    "image": str(screen),
    "detected": [
        "map",
        "search_bar",
        "buttons",
        "text"
    ],
    "next_step": "developer_agent"
}

state.write_text(json.dumps(analysis, indent=2, ensure_ascii=False))

print("✓ UI analyzed")
print("✓ Waiting for AI Developer Agent")
