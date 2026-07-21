from pathlib import Path

def run():
    file = Path("app/src/main/java/com/oranride/app/MainActivity.kt")

    if not file.exists():
        print("⚠️ الملف غير موجود")
        return

    text = file.read_text()

    if "NominatimRepository" in text:
        print("✓ ربط Nominatim موجود")
        return

    marker = "var searchResults = remember { mutableStateListOf<String>() }"

    add = '''
    
    // ربط نتائج Nominatim
    // سيتم تحديث القائمة عند تنفيذ البحث
    val nominatimRepository = NominatimRepository()
    '''

    if marker in text:
        text = text.replace(marker, marker + add)
        file.write_text(text)
        print("✓ تم تجهيز ربط Nominatim مع الواجهة")
    else:
        print("⚠️ لم يتم العثور على قائمة النتائج")

