
from src import get_log_mode, get_absolute_path
import logging
from logging import getLogger
import os

logger = getLogger("logger")

log_mode = get_log_mode.main()

log_called_func_str = "\"is called\""

base_path = get_absolute_path.main()
logging.basicConfig(filename=base_path+"log.log", 
                    format='%(levelname)s: %(asctime)s, %(pathname)s line %(lineno)d, %(funcName)s() | %(message)s',
                    encoding="utf-8", 
                    level=log_mode)