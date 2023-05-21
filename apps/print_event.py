# Print out 4 elements from event logs.

import sys
from src.log_config import logger, log_called_func_str

def main(args: list = sys.argv[1:]) -> None:
    logger.info(eval(log_called_func_str))

    event_log = args[0:] if args.__len__() > 0 else []
    
    for element in event_log:
        print(element)

def register_event() -> str:
    logger.info(eval(log_called_func_str))
    return "dummy"

if __name__ == "__main__":
    main([1,2,4,3])
