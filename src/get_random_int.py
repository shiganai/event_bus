# This function returns header contains timestamp and random int.
# Random int is contained so to avoid name header conflict.

import numpy as np
from src.log_config import *

max_rand = 2**29 # maximal of random number.
def main(return_max_rand: bool = False) -> int:
    logger.info(eval(log_called_func_str))
    
    rand_int = np.random.randint(0,max_rand)
    if return_max_rand:
        return rand_int, max_rand
    else:
        return rand_int

if __name__ == "__main__":
    print(main())