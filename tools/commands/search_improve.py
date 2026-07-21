from pathlib import Path

def run():
    file = Path("app/src/main/java/com/oranride/app/NominatimRepository.kt")

    if not file.exists():
        print("⚠️ الملف غير موجود")
        return

    text = file.read_text()

    old = 'val result = NominatimClient.api.search("$improvedQuery, Oran, Algeria", limit = 10)'

    new = 'val result = NominatimClient.api.search("$improvedQuery, Oran, Algeria", limit = 20)'

    if new in text:
        print("✓ التحسين موجود")
        return

    if old in text:
        file.write_text(text.replace(old, new))
        print("✓ تم تحسين عدد نتائج البحث")
    else:
        print("⚠️ لم يتم العثور على السطر المطلوب")

