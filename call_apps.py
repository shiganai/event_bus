
import sys
from apps import *
from src import *

PY = '.py'

def main(command: str = sys.argv[1], args: list = sys.argv[2:]):

    command = command[:-3] if command.endswith(PY) else command

    print("Calling ", end='')
    print(command, end='')
    if command in APPS:
        print(" from apps\\")
    elif command in SRCS:
        print(" from src\\")
    else:
        print(" is not in APPS")
        return None
    
    eval(f"{command}.main")(args)

if __name__ == "__main__":

    command = sys.argv[1] if sys.argv.__len__() > 0 else []
    args = sys.argv[2:] if sys.argv.__len__() > 1 else []

    command = command[:-3] if command.endswith(PY) else command

    print("Calling ", end='')
    print(command, end='')
    if command in APPS:
        print(" from apps\\")
    elif command in SRCS:
        print(" from src\\")
    else:
        print(" is not in APPS")
    
    eval(f"{command}.main")(args)