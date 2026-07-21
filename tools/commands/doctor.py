from pathlib import Path

def run():
    print("=== Oran-Ride Doctor ===")

    checks = {
        "AndroidManifest": Path("app/src/main/AndroidManifest.xml"),
        "MainActivity": Path("app/src/main/java/com/oranride/app/MainActivity.kt"),
        "LocationManager": Path("app/src/main/java/com/oranride/app/LocationManager.kt"),
        "LocationState": Path("app/src/main/java/com/oranride/app/LocationState.kt"),
        "NominatimApi": Path("app/src/main/java/com/oranride/app/NominatimApi.kt"),
        "NominatimRepository": Path("app/src/main/java/com/oranride/app/NominatimRepository.kt"),
        "Gradle": Path("app/build.gradle.kts"),
    }

    for name, file in checks.items():
        if file.exists():
            print(f"✓ {name}")
        else:
            print(f"✗ {name} missing")

    print("========================")
