
from src import get_log_mode, get_absolute_path
import logging
from logging import getLogger
import traceback # required for log_called_func_str

logger = getLogger("logger")

log_mode = get_log_mode.main()

# Note: traceback.format_stack(limit=2) returns like
#       ['  File "D:\\Github\\python\\event_bus\\call_apps.py", line 13, in main\n    dummy()\n', '  File "D:\\Github\\python\\event_bus\\call_apps.py", line 36, in dummy\n    print(traceback.format_stack(limit=2))\n']
#       Pick up the first item and trim it from top to the first "\n".
log_called_func_str = "\"is called from \" + traceback.format_stack(limit=2)[0][0:traceback.format_stack(limit=2)[0].find(\"\\n\")]"

base_path = get_absolute_path.main()
logging.basicConfig(filename=base_path+"log.log", 
                    format='%(levelname)s: %(asctime)s, %(pathname)s line %(lineno)d, %(funcName)s() | %(message)s',
                    encoding="utf-8", 
                    level=log_mode)

__all__ = ["logger", "traceback", "log_called_func_str"]