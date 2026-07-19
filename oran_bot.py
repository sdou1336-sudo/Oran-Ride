import os

PLAN_FILE = "indrive_like_plan.md"

def read_plan():
    if os.path.exists(PLAN_FILE):
        print("\n📋 Oran-Ride Plan:\n")
        with open(PLAN_FILE, "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print("❌ ملف الخطة غير موجود")

print("🤖 Oran Bot v2")
print("الأوامر:")
print("- اقرأ الخطة")
print("- exit")

while True:
    cmd = input("BOT> ")

    if cmd == "exit":
        break

    elif cmd == "اقرأ الخطة":
        read_plan()

    else:
        print("❓ أمر غير معروف")
