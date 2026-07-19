import os
import subprocess

def run(cmd):
    print(">>", cmd)
    os.system(cmd)

print("🤖 Oran Bot")
print("اكتب الأمر ثم اضغط Enter")

while True:
    cmd = input("BOT> ")

    if cmd == "exit":
        break

    if cmd.startswith("git"):
        run(cmd)
    else:
        print("الأمر محفوظ للتطوير: ", cmd)

print("تم إيقاف الروبوت")
