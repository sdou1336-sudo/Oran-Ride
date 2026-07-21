from pathlib import Path
import json

vision = {
    "enabled": True,
    "input": "tools/ui_agent/current_screen.png",
    "analysis_file": "tools/ui_agent/ui_state.json",
    "status": "waiting_for_screenshot",
    "next_step": "analyze_ui"
}

Path("tools/ui_agent/ui_state.json").write_text(
    json.dumps(vision, indent=2, ensure_ascii=False)
)

print("✓ Vision Capture initialized")
print("Place a screenshot at:")
print("tools/ui_agent/current_screen.png")
