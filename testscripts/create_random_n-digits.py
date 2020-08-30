# -*- coding: utf-8 -*-

import random
import sys

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

    target_number_str = ""
    for _ in range(N):
        while True:
            d = str(int(random.random() * 10))
            if d not in target_number_str:
                target_number_str += d
                break
    
    print(target_number_str)

if __name__ == '__main__':
    main()
