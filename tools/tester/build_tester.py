from pathlib import Path
import subprocess
import json

def run():
    print("=== Build Tester ===")

    try:
        result = subprocess.run(
            ["./gradlew", "assembleDebug"],
            text=True,
            capture_output=True,
            timeout=600
        )

        success = result.returncode == 0

        data = {
            "status": "success" if success else "failed",
            "error": "" if success else result.stderr[-3000:],
            "log": result.stdout[-3000:]
        }

        Path("tools/build_result.json").write_text(
            json.dumps(data, indent=2, ensure_ascii=False)
        )

        print("✓ Build success" if success else "✗ Build failed")
        if not success:
            print(data["error"])

    except Exception as e:
        print("ERROR:", e)

if __name__ == "__main__":
    run()
