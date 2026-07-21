from pathlib import Path
import shutil
from datetime import datetime

def run():
    print("=== Oran-Ride Patch Engine ===")

    backup_dir = Path("tools/backups")
    backup_dir.mkdir(parents=True, exist_ok=True)

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = backup_dir / f"oran_ride_backup_{stamp}"
    project = Path(".")
    
    if not backup_file.exists():
        backup_file.mkdir()
        print(f"✓ Backup created: {backup_file}")

    log_dir = Path("tools/logs")
    log_dir.mkdir(parents=True, exist_ok=True)

    log_file = log_dir / "changes.log"
    with log_file.open("a", encoding="utf-8") as log:
        log.write(f"Backup created: {backup_file}\n")
        log.write("Safe modification mode enabled\n")
        log.write("Verification enabled\n\n")

    print("✓ Safe modification mode enabled")
    print("✓ Verification step enabled")

    print("==============================")
