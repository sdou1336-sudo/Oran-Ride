ALIASES = {
    "help": "help",
    "مساعدة": "help",

    "status": "status",
    "افحص": "status",
    "افحص المشروع": "status",
    "تشخيص": "status",

    "backup": "backup",
    "نسخة": "backup",
    "نسخة احتياطية": "backup",

    "restore": "restore",
    "استرجاع": "restore",

    "gps": "gps",
    "الموقع": "gps",
    "طور gps": "gps",
    "أضف gps": "gps",

    "search": "search",
    "البحث": "search",
    "طور البحث": "search",

    "build": "build",
    "حلل المشروع": "analyze",
    "فهرس المشروع": "index",
    "اعمل فهرس": "index",
    "افهرس الملفات": "index",

    "تحليل المشروع": "analyze",
    "افحص الملفات": "analyze",

    "بناء": "build",
    "جهز للبناء": "build",


    "engine": "engine",
    "log": "log",
    "patch": "patch",
    "precheck": "precheck",
    "search_patch": "search_patch",
    "apply_patch": "apply_patch",
    "approval": "approval",
    "موافقة": "approval",
    "وافق على التعديل": "approval",
    "السماح بالتعديل": "approval",

    "طبق التعديل": "apply_patch",
    "نفذ التعديل": "apply_patch",
    "تطبيق تعديل البحث": "apply_patch",

    "اقتراح تحسين البحث": "search_patch",
    "اقتراح تعديل Nominatim": "search_patch",

    "فحص قبل التعديل": "precheck",
    "فحص سلامة الملف": "precheck",
    "تحقق قبل التعديل": "precheck",

    "task": "task",
    "تحسين البحث": "search_task",
    "حسن محرك البحث": "search_task",
    "حسن محرك البحث في nominatimrepository": "search_task",
    "حسن نتائج البحث في nominatimrepository": "search_task",
    "حسن عدد نتائج البحث في nominatim": "search_task",
    "زيادة نتائج البحث": "search_task",

    "حسن محرك البحث في nominatimrepository.kt": "search_task",

    "طور البحث": "search_task",

    "نظام مهام": "task",
    "أنشئ نظام مهام": "task",
    "مخطط المهام": "task",

    "test patch": "patch_test",
    "اختبر التعديل": "patch_test",

    "تعديل": "patch",
    "عدل الملف": "patch",
    "طبق التعديل": "patch",

    "السجل": "log",
    "اعرض السجل": "log",
    "سجل التعديلات": "log",

    "نظام تعديل": "engine",
    "أنشئ نظام تعديل": "engine",
    "تعديل آمن": "engine",
    "نسخة احتياطية قبل التعديل": "engine",
    "doctor": "doctor",
    "دكتور": "doctor",
    "طور doctor": "doctor",
    "طور دكتور": "doctor",
    "حلل المشروع": "doctor",
    "حلل المشروع واعطي تقرير": "doctor",
    "اعطي تقرير عن المشاكل": "doctor",

    "search_ui": "search_ui",
    "اربط نتائج nominatim بواجهة البحث": "search_connect",
    "ربط نتائج البحث": "search_connect",

    "طبق تطوير واجهة البحث": "search_ui",
    "طبق تعديل البحث": "search_ui",

    "طور واجهة البحث لعرض نتائج الأماكن": "search_ui",
    "عرض نتائج الأماكن": "search_ui",
    "تطوير واجهة البحث": "search_ui",

    "اعرض سياق المشروع": "context",
    "سياق المشروع": "context",
    "اظهر الملفات": "context",

    "فحص قبل التعديل": "precheck_context",
    "افحص السياق": "precheck_context",
    "تأكد قبل التعديل": "precheck_context",

    "اقترح التعديل": "suggest",
    "اقتراح تعديل": "suggest",
    "حلل التعديل": "suggest",

    "إنشاء مهمة": "task_create",

    "طبق المهمة": "apply_task",

    "نفذ التعديل": "patch_execute",

    "حسن البحث": "search_improve",

    "فلتر البحث": "search_filter",

    "طبق فلترة البحث": "search_filter_apply",

    "طور واجهة النتائج": "search_ui_apply",

    "اربط نتائج البحث": "connect_search_results",

    "اربط Nominatim بالواجهة": "link_nominatim_ui",

    "اربط nominatim بالواجهة": "link_nominatim_ui",

    "فعل البحث": "activate_search",

    "اعرض نتائج Nominatim": "show_nominatim_results",

    "اعرض نتائج nominatim": "show_nominatim_results",

    "اربط النتيجة بالخريطة": "link_map_result",

    "جهز المشروع النهائي": "final_prepare",
}

def resolve(command: str) -> str:
    command = command.strip().lower()
    return ALIASES.get(command, command)

