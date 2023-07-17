# This is debugging function.
# Load is_debugging.txt and return a boolean.

from src import get_absolute_path
import logging

def main() -> None:
    target_path = get_absolute_path.main('log_mode.txt')

    with open(target_path, 'r', encoding='utf-8') as f:
        contents = f.read()
    
    return eval("logging."+contents)

if __name__ == "__main__":
    main()