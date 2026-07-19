approved = False

def approve():
    global approved
    approved = True
    print("✅ تمت الموافقة على التعديل")

def status():
    return approved
