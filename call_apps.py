
import sys
from apps import *
from src import *
from src.log_config import *

PY = '.py'

def main(command: list, args: list):
    logger.info(eval(log_called_func_str))

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

    command = sys.argv[1] if sys.argv.__len__() > 1 else ""
    args = sys.argv[2:] if sys.argv.__len__() > 2 else []

    main(command=command, args=args)