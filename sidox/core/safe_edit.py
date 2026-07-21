from pathlib import Path
import shutil, json
from datetime import datetime

files = ["MainActivity.kt","Driver.kt","DriverRepository.kt","DriverViewModel.kt"]

src = Path("app/src/main/java/com/oranride/app")
backup = Path("sidox/backups/manual_" + datetime.now().strftime("%Y%m%d_%H%M%S"))
backup.mkdir(parents=True, exist_ok=True)

saved = []

for f in files:
    p = src / f
    if p.exists():
        shutil.copy(p, backup / f)
        saved.append(f)

Path("sidox/history/safe_edit.json").parent.mkdir(exist_ok=True)
Path("sidox/history/safe_edit.json").write_text(
    json.dumps({"time": str(datetime.now()), "files": saved}, indent=2)
)

print("Backup completed")
print(saved)
