from pathlib import Path
import json

def run(task):
    project = Path("tools/project_map.json")

    if not project.exists():
        print("⚠️ Run Project Scanner first")
        return

    data = json.loads(project.read_text())

    print("=== AI Developer Agent ===")
    print("Task:", task)
    print("Project files:", data.get("files_count"))

    matches = []
    for f in data["files"]:
        if any(x.lower() in f.lower() for x in ["mainactivity", "search", "repository", "map"]):
            matches.append(f)

    print("Related files:")
    for m in matches:
        print("-", m)

    Path("tools/agent_task.json").write_text(
        json.dumps({
            "task": task,
            "files": matches,
            "status": "analysis_ready"
        }, indent=2, ensure_ascii=False)
    )

    print("✓ Agent analysis saved")

if __name__ == "__main__":
    run("Analyze project")
