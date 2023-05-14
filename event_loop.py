# main loop for event bus

import os
import numpy as np
import csv
import time
from src import *
from apps import *

def main() -> None:
    None
    new_event_path = get_absolute_path.main('new_event_dir')
    old_event_path = get_absolute_path.main('old_event_dir')
    
    loop_count = 0
    # Main loop
    while True:
        loop_count = loop_count + 1
        print("loop_count:" + str(loop_count))

        # Reload registered event
        registered_pair = read_registered_list()
        
        # Load new event log
        new_events = os.listdir(new_event_path)
        for each_event in new_events:
            with open(new_event_path + "\\" + each_event,'r',encoding='utf-8') as f:
                event_data = f.read().splitlines()
                print("received event_data is as follows --------------------")
                print(event_data)
                print("------------------------------------------------------")

                # trigger app
                category = event_data[2]
                matched_index = np.where(registered_pair[:,1]==category)
                for loop_index in matched_index:
                    app = registered_pair[loop_index,0][0]
                    eval(f"{app}.main")(args=event_data)
                    print("done")
                
            os.rename(new_event_path + "\\" + each_event, old_event_path + "\\" + each_event)

        time.sleep(1)

def read_registered_list() -> list:
    # Read trigger key for each apps.

    # Get filenames
    registered_event_path = get_absolute_path.main('registered_event')
    filenames = os.listdir(registered_event_path)

    # Sort them based on modified dates
    modified_dates = []
    for filename in filenames:
        modified_dates.append(os.path.getmtime(registered_event_path + "\\" + filename))
    sorted_index = np.argsort( np.array(modified_dates) )

    # Pick up the latest one.
    filepath = registered_event_path + "\\" + filenames[sorted_index[-1]]

    # Delete older ones.
    # for ii in range(filenames.__len__() - 1):
    #     filename = filenames[sorted_index[ii]]
    #     os.remove(registered_event_path + "\\" + filename)

    # Read the file
    with open(filepath, 'r', encoding='utf-8') as f:
        csvreader = csv.reader(f)
        content = [row for row in csvreader]

    # Convert list into ndarray so to access 2D-way
    content = np.array(content)

    return content

def write_registered_event() -> None:
    header = get_filename_header.main()
    header = header[:-1] # remove "_"
    
    registered_event_path = get_absolute_path.main('registered_event')
    filename_to_write = registered_event_path + "\\" + header + ".csv"

    with open(filename_to_write, 'w', encoding='utf-8') as f:
        for app in APPS:
            registered_event = eval(f"{app}.register_event")()
            f.write(app + ',' + registered_event)
            f.write("\n")

if __name__ == "__main__":
    # write_registered_event()
    main()