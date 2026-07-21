from pathlib import Path
import subprocess

def run():
    print("=== Final Prepare ===")

    try:
        subprocess.run(["./gradlew", "--stop"], capture_output=True)

        print("✓ تم إيقاف Gradle")

        build = Path("app/build")
        if build.exists():
            import shutil
            shutil.rmtree(build)

        print("✓ تم تنظيف ملفات البناء")

        print("✓ المشروع جاهز لفحص GitHub Actions")

    except Exception as e:
        print(f"❌ خطأ: {e}")

    print("====================")

