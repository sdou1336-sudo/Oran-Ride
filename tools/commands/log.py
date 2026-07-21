from pathlib import Path

def run():
    print("=== Oran-Ride Logs ===")

    log_file = Path("tools/logs/changes.log")

    if not log_file.exists():
        print("⚠️ لا يوجد سجل بعد")
        return

    content = log_file.read_text(encoding="utf-8")

    if not content.strip():
        print("⚠️ السجل فارغ")
        return

    print(content)
    print("======================")
