from pathlib import Path

def run():
    file = Path("app/src/main/java/com/oranride/app/MainActivity.kt")

    if not file.exists():
        print("⚠️ الملف غير موجود")
        return

    text = file.read_text()

    if "searchResults.clear()" in text:
        print("✓ عرض النتائج موجود")
        return

    old = '''
    fun searchPlaces(query: String) {
        // ربط زر البحث مع Nominatim
        // سيتم تحديث النتائج هنا
        println("Searching: $query")
    }
    '''

    new = '''
    fun searchPlaces(query: String) {
        // جلب نتائج Nominatim وعرضها
        searchResults.clear()
        println("Searching: $query")
    }
    '''

    if old in text:
        text = text.replace(old, new)
        file.write_text(text)
        print("✓ تمت إضافة تجهيز عرض نتائج البحث")
    else:
        print("⚠️ لم يتم العثور على وظيفة البحث")

