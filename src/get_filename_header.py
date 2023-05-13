# This function returns header contains timestamp and random int.
# Random int is contained so to avoid name header conflict.

import datetime
import numpy as np
from src import print_called_function
from src import get_random_int

print_called_function.main(__file__)

def main() -> str:
    now_datetime = datetime.datetime.now()
    now_str = now_datetime.strftime("%Y_%m_%d_%H_%M_%S_") + str(now_datetime.microsecond)

    rand_int, max_rand = get_random_int.main(True)

    header = now_str + "_" + str(rand_int).zfill(int(np.ceil(np.log10(max_rand)))) + "_"

    return header

if __name__ == "__main__":
    print(main())