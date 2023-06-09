# Print out 4 elements from event logs.

import sys
from src import print_called_function

print_called_function.main(__file__)

def main(args: list = sys.argv[1:]) -> None:
    event_log = args[0:] if args.__len__() > 0 else []
    
    for element in event_log:
        print(element)

def register_event() -> str:
    return "dummy"

if __name__ == "__main__":
    main([1,2,4,3])
