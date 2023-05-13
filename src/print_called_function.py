# This is debugging function.
# Simply print out the called function name.
# Paste 'print_called_function.main(__file__)' to use this function.

import os
from src import get_is_debugging

def main(filename: str):

    is_debugging = get_is_debugging.main()

    if is_debugging:
        print("")
        print("-------------------------------------------------------------")
        print(os.path.basename(filename) + " is called")
        print("-------------------------------------------------------------")
        print("")

if __name__ == "__main__":
    main(__file__)