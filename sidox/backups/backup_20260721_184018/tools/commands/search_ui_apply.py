from pathlib import Path

def run():
    file = Path("app/src/main/java/com/oranride/app/MainActivity.kt")

    if not file.exists():
        print("⚠️ الملف غير موجود")
        return

    text = file.read_text()

    marker = 'Text("البحث عن الأماكن")'

    if "نتائج البحث" in text:
        print("✓ واجهة نتائج البحث موجودة")
        return

    if marker in text:
        text = text.replace(
            marker,
            marker + '\n        Text("نتائج البحث")'
        )
        file.write_text(text)
        print("✓ تمت إضافة قسم عرض نتائج البحث")
    else:
        print("⚠️ لم يتم العثور على واجهة البحث")

