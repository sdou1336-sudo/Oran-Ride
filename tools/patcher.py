#!/usr/bin/env python3

import sys
from lib.router import resolve
from brain import execute

def main():
    if len(sys.argv) < 2:
        execute("help")
        return

    user_input = " ".join(sys.argv[1:])
    command = resolve(user_input)
    execute(command)

if __name__ == "__main__":
    main()
