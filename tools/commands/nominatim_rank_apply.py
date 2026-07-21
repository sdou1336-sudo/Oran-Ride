
from pathlib import Path
import shutil
from datetime import datetime

file = Path("app/src/main/java/com/oranride/app/NominatimRepository.kt")

if not file.exists():
    print("⚠️ NominatimRepository.kt غير موجود")
    exit()

backup = Path("backup_tasks")
backup.mkdir(exist_ok=True)

shutil.copy(
    file,
    backup / f"NominatimRepository.kt.{datetime.now().timestamp()}"
)

text = file.read_text()

old = """lastError = "SUCCESS: ${result.size}"
                      result"""

new = """val ranked = result.sortedByDescending { it.importance ?: 0.0 }

                      lastError = "SUCCESS: ${ranked.size}"
                      ranked"""

if old in text:
    file.write_text(text.replace(old, new))
    print("✓ تم إضافة ترتيب نتائج Nominatim حسب importance")
else:
    print("⚠️ لم يتم العثور على مكان التعديل")
