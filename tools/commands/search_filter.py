from pathlib import Path

def run():
    file = Path("app/src/main/java/com/oranride/app/NominatimRepository.kt")

    if not file.exists():
        print("⚠️ الملف غير موجود")
        return

    text = file.read_text()

    if "Oran, Algeria" in text and "format" in text:
        print("✓ الفلترة موجودة")
        return

    print("✓ جاهز لإضافة فلترة نتائج الأماكن")
    print("⚠️ لم يتم تغيير الكود بعد")
