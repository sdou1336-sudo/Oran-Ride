from batman.tasks import prepare_task

def plan_task(task):
    print(f"\n📋 خطة ذكية: {task}\n")
    print("1. البحث عن الملفات المرتبطة.")
    print("2. تحليل كل ملف.")
    print("3. تحديد التعديلات المطلوبة.")
    print("4. إنشاء نسخة احتياطية.")
    print("5. انتظار موافقة المستخدم.")
    print("\n📂 الملفات المرشحة:")
    prepare_task(task)
