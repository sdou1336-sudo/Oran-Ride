from pathlib import Path
import json

cfg = {
    "name": "UI Agent",
    "version": 1,
    "build_backend": "github_actions",
    "ignore_local_aapt2": True,
    "vision": {
        "enabled": True,
        "mode": "screenshot"
    },
    "workflow": [
        "capture_ui",
        "analyze_ui",
        "map_to_project_files",
        "create_fix_plan",
        "commit_changes",
        "push_to_github",
        "wait_build_result",
        "analyze_build_log"
    ]
}

Path("tools/ui_agent/config.json").write_text(
    json.dumps(cfg, indent=2, ensure_ascii=False)
)

print("✓ UI Agent initialized")
print("✓ Local AAPT2 ignored")
print("✓ GitHub Actions selected as build backend")
