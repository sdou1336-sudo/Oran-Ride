import json
import os

with open("sidox/tasks/latest_task.json") as f:
    task = json.load(f)

keywords = {
    "driver": ["driver", "ride", "trip", "user"],
    "map": ["map", "location", "gps"],
    "search": ["search", "place", "nominatim"],
    "payment": ["payment", "wallet", "price"]
}

text = task["task"].lower()
selected = []

for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in [".git", ".gradle", "build", "backup", "backups", "sidox"]]
    for file in files:
        path = os.path.join(root, file)
        if any(x in path for x in ["backup_", "/backup", "sidox/", ".gradle/", "build/"]):
            continue
        name = file.lower()
        if any(k in text for k in keywords) and (file.endswith(".kt") or file.endswith(".java")):
            selected.append(path)

result = {
    "task": task["task"],
    "selected_files": selected,
    "status": "files_selected"
}

os.makedirs("sidox/tasks", exist_ok=True)

with open("sidox/tasks/selected_files.json", "w") as f:
    json.dump(result, f, indent=2)

print(json.dumps(result, indent=2))
