from pathlib import Path

def run():
    file = Path("app/src/main/java/com/oranride/app/MainActivity.kt")

    if not file.exists():
        print("⚠️ الملف غير موجود")
        return

    text = file.read_text()

    if "searchPlaces" in text:
        print("✓ وظيفة البحث موجودة")
        return

    add = '''
    
    fun searchPlaces(query: String) {
        // ربط زر البحث مع Nominatim
        // سيتم تحديث النتائج هنا
        println("Searching: $query")
    }
    '''

    marker = "val nominatimRepository = NominatimRepository()"

    if marker in text:
        text = text.replace(marker, marker + add)
        file.write_text(text)
        print("✓ تم تفعيل وظيفة البحث")
    else:
        print("⚠️ لم يتم العثور على NominatimRepository")

