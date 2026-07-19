from batman.approval import status
import shutil
import os
from datetime import datetime

def backup_file(path):
    if os.path.exists(path):
        name = "before_" + datetime.now().strftime("%H%M%S") + "_" + os.path.basename(path)
        shutil.copy(path, name)
        print("🛡️ Backup:", name)

def apply_change(path, old, new):
    if not status():
        print("⚠️ اكتب وافق أولاً")
        return

    if not os.path.exists(path):
        print("❌ الملف غير موجود")
        return

    backup_file(path)

    text = open(path, encoding="utf-8").read()

    if old not in text:
        print("⚠️ لم يتم العثور على مكان التعديل")
        return

    text = text.replace(old, new, 1)

    open(path, "w", encoding="utf-8").write(text)

    print("✅ تم تطبيق التعديل:", path)

def execute_patch():
    if not status():
        print("⚠️ يجب كتابة: وافق أولاً")
        return

    print("🛠️ بدء تنفيذ التعديل")
    print("✅ الموافقة موجودة")
    print("📂 تجهيز الملفات")
