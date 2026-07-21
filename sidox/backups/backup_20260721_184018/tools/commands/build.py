import subprocess

def run():
    print("=== Build Check ===")
    try:
        result = subprocess.run(
            ["./gradlew", "assembleDebug", "--no-daemon"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print("✓ Gradle build successful")
        else:
            print("❌ Build environment issue detected")
            if "AAPT2" in result.stderr:
                print("⚠️ AAPT2/Android build tools problem")
            print("Use GitHub Actions build environment")

    except Exception as e:
        print(f"❌ Error: {e}")

    print("===================")
