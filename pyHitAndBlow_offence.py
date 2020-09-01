# -*- coding: utf-8 -*-

import sys

from mylibs import lib_hit_and_blow

def main() -> int:
    """
    function main.
    """
    N, enable_print, answer_number = check_arguments(sys.argv)
    if N is None:
        return

    target_numbers = lib_hit_and_blow.create_target_numbers(N)
    result, history = lib_hit_and_blow.offence(N, target_numbers, enable_print, answer_number)
    lib_hit_and_blow.print_offence_history(N, history, result)

    if result:
        return len(history.response)
    else:
        return 0

def check_arguments(argv:[str]) -> (int, bool, str):
    """
    check arguments
    """
    # set n(digits of answer number).
    N = 4
    if len(argv) >= 2:
        if argv[1].isdecimal():
            N = int(sys.argv[1])
            if N < 2 or N > 10:
                print("Give n between 2 and 10 inclusive.")
                return None, None, None
            print("N ... {0}".format(N))
        else:
            print("{0} is not decimal.".format(argv[1]))
            return None, None, None

    # set enable_print
    enable_print = False
    if len(argv) >= 3:
         if argv[2].upper() == "TRUE":
             enable_print = True

    # set answer number
    answer_number = ""
    if len(argv) >= 4:
        if argv[3].isdecimal():
            answer_number = argv[3]
            if len(answer_number) != N:
                print("answer number digits is not {0}".format(N))
                return 0
            print("set answer number ... {0}".format(answer_number))
        else:
            print("{0} is not decimal.".format(argv[3]))
            return None, None, None

    return N, enable_print, answer_number


if __name__ == '__main__':
    sys.exit(main())
