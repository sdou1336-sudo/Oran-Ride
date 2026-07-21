import sys, json, subprocess

task = " ".join(sys.argv[1:])

keywords = {
    "driver": ["Driver.kt","DriverRepository.kt","DriverViewModel.kt","MainActivity.kt"],
    "ride": ["RideRequest.kt","RideRepository.kt","RideViewModel.kt","MainActivity.kt"],
    "map": ["MainActivity.kt","NominatimRepository.kt"]
}

found = []
for k, files in keywords.items():
    if k in task.lower():
        found = files

plan = {
    "task": task,
    "files": found,
    "status": "ready"
}

print(json.dumps(plan, indent=2, ensure_ascii=False))
