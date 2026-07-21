from pathlib import Path

def run():
    print("=== Search Development Task ===")

    target = Path("app/src/main/java/com/oranride/app/NominatimRepository.kt")

    if target.exists():
        print(f"✓ Target found: {target}")
        print("✓ Backup required before modification")
        print("✓ Task ready: Improve Oran search results")
    else:
        print("✗ Target file missing")

    print("===============================")

    print("")
    print("تشغيل خطة التحسين:")
    from commands import search_plan
    search_plan.run()
