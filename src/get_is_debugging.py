# This is debugging function.
# Load is_debugging.txt and return a boolean.

import os
from src import get_absolute_path

def main() -> None:

    target_path = get_absolute_path.main('is_debugging.txt')

    with open(target_path, 'r', encoding='utf-8') as f:
        contents = f.read()
    if contents == 'true':
        return True
    elif contents == 'false':
        return False
    else:
        raise Exception("is_debugging should be true/false")

if __name__ == "__main__":
    main(__file__)