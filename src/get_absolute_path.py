# Return absolute path to event directory

import os

apps_path = "\\src"
event_bus_path = "\\event_bus"
gathered_path = event_bus_path + apps_path

def main(target_name: str = None) -> str:
    base_path = os.path.dirname(os.path.abspath(__file__))

    if base_path.__len__() != str.find(base_path, gathered_path) + gathered_path.__len__():
        raise Exception("This function must be located at " + gathered_path)
    
    base_path = base_path[:-(apps_path.__len__()-1)] # remove apps
    # Now that, base path looks like "####/###/##/event_bus/"

    target_path = base_path # set default.
    if target_name is None:
        None # keep the default
    elif target_name == 'new_event_dir':
        target_path = os.path.normpath(os.path.join(base_path, 'new_event_dir'))
    elif target_name == 'old_event_dir':
        target_path = os.path.normpath(os.path.join(base_path, 'old_event_dir'))
    elif target_name == 'log_mode.txt':
        target_path = os.path.normpath(os.path.join(base_path, 'log_mode.txt'))
    elif target_name == 'registered_event':
        target_path = os.path.normpath(os.path.join(base_path, 'registered_event'))
    else:
        raise Exception("target_name: " + target_name + " is not registered")

    return target_path
    
if __name__ == "__main__":
    main()
