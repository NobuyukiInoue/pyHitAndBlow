# -*- coding: utf-8 -*-

import random
import sys

from mylibs import lib_hit_and_blow

def main():
    # set n(digits of answer number).
    N = 4
    if len(sys.argv) >= 2:
        if sys.argv[1].isdecimal():
            N = int(sys.argv[1])
            if N < 2 or N > 10:
                print("Give n between 2 and 10 inclusive.")
                return 0
        else:
            print("{0} is not decimal.".format(sys.argv[1]))
            return 0
    
    random.seed()
    print(lib_hit_and_blow.create_random_n_digits_number(N))


if __name__ == '__main__':
    main()
