from pathlib import Path
import shutil
from datetime import datetime

file = Path("app/src/main/java/com/example/ui/OranMap.kt")

backup = "backup_real_" + datetime.now().strftime("%H%M%S")
shutil.copy(file, backup + ".kt")

data = file.read_text(encoding="utf-8")

old = "// تحسينات الخريطة القادمة: Marker + Camera + Route"

new = """// تحسينات الخريطة القادمة: Marker + Camera + Route

// Driver Marker Enhancement
// تحسين مؤشر السائق
// سيتم ربطه لاحقاً بالحركة الحية والاتجاه"""

if old in data:
    data = data.replace(old, new, 1)
    file.write_text(data, encoding="utf-8")
    print("🛡️ Backup:", backup)
    print("✅ تم تجهيز Marker السائق")
else:
    print("❌ العلامة غير موجودة")
