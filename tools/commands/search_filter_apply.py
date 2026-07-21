from pathlib import Path

def run():
    file = Path("app/src/main/java/com/oranride/app/NominatimRepository.kt")

    if not file.exists():
        print("⚠️ الملف غير موجود")
        return

    text = file.read_text()

    old = 'val result = NominatimClient.api.search("$improvedQuery, Oran, Algeria", limit = 20)'

    new = '''val result = NominatimClient.api.search(
                "$improvedQuery, Oran, Algeria",
                limit = 20,
                addressdetails = 1
            )'''

    if "addressdetails = 1" in text:
        print("✓ الفلترة موجودة")
        return

    if old in text:
        file.write_text(text.replace(old, new))
        print("✓ تمت إضافة تفاصيل العنوان لتحسين فلترة النتائج")
    else:
        print("⚠️ لم يتم العثور على سطر البحث")

