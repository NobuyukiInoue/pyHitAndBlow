# -*- coding: utf-8 -*-

import datetime
import sys
import time
from mylibs import lib_hit_and_blow

def main():
    """
    function main.
    """
    N = check_arguments(sys.argv)
    if N is None:
        return

    result_count = []
    total = 0
    start_time = time.time()
    answer_numbers = lib_hit_and_blow.create_target_numbers(N)
    for i in range(len(answer_numbers)):
        print("#------------------------------#\n"
              "# Running ... {0:d}/{1:d}\n"
              "#------------------------------#"
              .format(i + 1, len(answer_numbers)))

        answer_number = answer_numbers[i]
        target_numbers = lib_hit_and_blow.create_target_numbers(N)
        result, history = lib_hit_and_blow.offence(N, target_numbers, False, answer_number)
        lib_hit_and_blow.print_defence_history(N, history, result)

        if result:
            result_count.append(len(history.response))
        else:
            result_count.append(0)
        
        total += result_count[-1]
        average = total / len(result_count)
        print("\n# Latest Average = {0:.4f}\n".format(average))

    end_time = time.time()

    print("==== ResultCount history =====")
    for i in range(len(result_count)):
        print("ResultCount[{0:d}] = {1}".format(i, result_count[i]))

    print("==============================\n"
          "Total Average = {0}\n"
          "==============================\n"
          "start ... {1}\n"
          "end   ... {2}\n"
          "Total execution time ... {3:.4f}[s]"
          .format(average, datetime.datetime.fromtimestamp(start_time), datetime.datetime.fromtimestamp(end_time), end_time - start_time))
#         .format(average, time.strftime("%Y-%m-%d %H:%M:%S",  time.strptime(start_time)), time.strftime("%Y-%m-%d %H:%M:%S", end_time), end_time - start_time))

def check_arguments(argv:[str]) -> (int, bool, str):
    """
    check arguments
    """
    # set n(digits of answer number).
    N = 4
    if len(argv) >= 2:
        if argv[1].isdecimal():
            N = int(argv[1])
            if N < 2 or N > 10:
                print("Give n between 2 and 10 inclusive.")
                return None, None
            print("N ... {0}".format(N))
        else:
            print("{0} is not decimal.".format(argv[1]))
            return None, None

    return N


if __name__ == '__main__':
    main()
