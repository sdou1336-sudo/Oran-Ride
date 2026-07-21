import importlib

def execute(cmd: str):
    try:
        module = importlib.import_module(f"commands.{cmd}")
        module.run()
    except ModuleNotFoundError:
        print(f"⚠️ لا يوجد أمر مطور بعد: {cmd}")
    except Exception as e:
        print(f"❌ خطأ أثناء تنفيذ {cmd}: {e}")
