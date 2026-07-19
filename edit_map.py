from pathlib import Path
import shutil
from datetime import datetime

file = Path("app/src/main/java/com/example/ui/OranMap.kt")

if not file.exists():
    print("❌ ملف الخريطة غير موجود")
    exit()

backup = "backup_map_" + datetime.now().strftime("%H%M%S")
shutil.copy(file, backup + ".kt")

data = file.read_text(encoding="utf-8")

if "BATMAN_MAP_UPDATE" not in data:
    data += "\n\n// BATMAN_MAP_UPDATE\n// تحسينات الخريطة القادمة: Marker + Camera + Route\n"

file.write_text(data, encoding="utf-8")

print("🛡️ Backup:", backup)
print("✅ تم تجهيز OranMap.kt للتطوير")
