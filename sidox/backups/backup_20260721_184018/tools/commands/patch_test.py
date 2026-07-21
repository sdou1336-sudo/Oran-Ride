from pathlib import Path
from datetime import datetime

def run():
    print("=== Patch Test ===")

    test_file = Path("tools/test_patch.txt")
    backup_dir = Path("tools/backups")
    log_dir = Path("tools/logs")

    backup_dir.mkdir(parents=True, exist_ok=True)
    log_dir.mkdir(parents=True, exist_ok=True)

    if test_file.exists():
        backup = backup_dir / f"test_patch_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        backup.write_text(test_file.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"✓ Backup: {backup}")

    test_file.write_text(
        "Oran-Ride Patch Test OK\n",
        encoding="utf-8"
    )

    with (log_dir / "changes.log").open("a", encoding="utf-8") as log:
        log.write("Patch test executed\n")

    print("✓ File modified")
    print("✓ Log updated")
    print("==================")
