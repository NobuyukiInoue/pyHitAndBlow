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
    
    random.seed()
    print(create_random_n_digits_number(N))

def create_random_n_digits_number(n:int)->str:
    """
    create n-digit random target number.
    """
    """
    target_number_str = ""
    for _ in range(n):
        while True:
            d = str(random.randint(0, 9))
            if d not in target_number_str:
                target_number_str += d
                break
    return target_number_str
    """
    return "".join([str(_) for _ in random.sample(list(range(10)), n)])

if __name__ == '__main__':
    main()
