from pathlib import Path

FILE = Path(".approval")

def approve():
    FILE.write_text("approved", encoding="utf-8")
    print("✅ تمت الموافقة على التعديل")

def status():
    return FILE.exists()
