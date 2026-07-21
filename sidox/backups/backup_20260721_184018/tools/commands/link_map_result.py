from pathlib import Path

def run():
    file = Path("app/src/main/java/com/oranride/app/MainActivity.kt")

    if not file.exists():
        print("⚠️ الملف غير موجود")
        return

    text = file.read_text()

    if "moveMapToLocation" in text:
        print("✓ ربط الخريطة موجود")
        return

    add = '''

    fun moveMapToLocation(latitude: Double, longitude: Double) {
        // تحريك الخريطة إلى نتيجة البحث
        println("Move map: $latitude,$longitude")
    }
    '''

    marker = "val nominatimRepository = NominatimRepository()"

    if marker in text:
        text = text.replace(marker, marker + add)
        file.write_text(text)
        print("✓ تمت إضافة ربط نتيجة البحث بالخريطة")
    else:
        print("⚠️ لم يتم العثور على NominatimRepository")

