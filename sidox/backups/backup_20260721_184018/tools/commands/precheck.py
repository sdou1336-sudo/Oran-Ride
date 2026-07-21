from pathlib import Path

def run():
    print("=== Pre-Modification Check ===")

    files = [
        Path("app/src/main/java/com/oranride/app/NominatimRepository.kt"),
        Path("app/src/main/java/com/oranride/app/NominatimApi.kt"),
    ]

    for file in files:
        if file.exists():
            print(f"✓ File OK: {file.name}")
        else:
            print(f"✗ Missing: {file.name}")

    print("✓ Backup required")
    print("✓ Modification safety check ready")
    print("==============================")
