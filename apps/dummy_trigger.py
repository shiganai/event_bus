# Test event trigger.
# The event info is simple as <timestamp, random number, ["dummy", "string"], path_to_data>

import os, sys
import time, datetime
from src import get_filename_header
from src import print_called_function
from src import get_absolute_path
from src import get_random_int

print_called_function.main(__file__)

def main(args: list = sys.argv[1:]) -> None:
    header = get_filename_header.main()

    new_event_dir_path = get_absolute_path.main('new_event_dir')

    filename = os.path.basename(__file__)
    filename = filename[:-3] # remove .py

    saving_event_path = new_event_dir_path + "\\" + header + filename + ".txt"

    event_data = [
        str(time.time()),
        str(get_random_int.main()),
        "dummy",
        "None"
        ]
    event_data = "\n".join(event_data) # insert "Return"

    with open(saving_event_path, 'w', encoding='utf-8') as f:
        f.write(event_data)

def register_event() -> str:
    return "None"

if __name__ == "__main__":
    main()