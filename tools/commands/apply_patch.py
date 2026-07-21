from commands import precheck, search_patch

def run():
    print("=== Apply Patch Engine ===")

    print("1) Running precheck...")
    precheck.run()

    print("")
    print("2) Loading patch proposal...")
    search_patch.run()

    print("")
    print("✓ Ready to apply after approval")
    print("==========================")
