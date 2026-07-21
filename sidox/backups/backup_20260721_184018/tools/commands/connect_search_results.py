from pathlib import Path

def run():
    file = Path("app/src/main/java/com/oranride/app/MainActivity.kt")

    if not file.exists():
        print("⚠️ الملف غير موجود")
        return

    text = file.read_text()

    if "searchResults" in text:
        print("✓ ربط النتائج موجود")
        return

    insert = '''
    
    var searchResults = remember { mutableStateListOf<String>() }
    '''

    marker = 'Text("نتائج البحث")'

    if marker in text:
        text = text.replace(marker, marker + insert)
        file.write_text(text)
        print("✓ تم تجهيز قائمة نتائج البحث")
    else:
        print("⚠️ لم يتم العثور على قسم النتائج")

