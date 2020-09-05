# -*- coding: utf-8 -*-

import datetime
import sys
import time
from mylibs import lib_hit_and_blow

def main():
    """
    function main.
    """
    N, MAX = check_arguments(sys.argv)
    if N is None:
        return

    result_count = []
    total = 0
    start_time = time.time()
    for i in range(MAX):
        print("#------------------------------#\n"
              "# Running ... {0:d}/{1:d}\n"
              "#------------------------------#"
              .format(i + 1, MAX))

        answer_number = lib_hit_and_blow.create_random_n_digits_number(N)
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

    print("======== distribution ========")
    question_count = [0 for _ in range(13)]
    for num in result_count:
        question_count[num] += 1
    for i in range(len(question_count)):
        print("{0} ... {1}".format(i, question_count[i]))
    print("Distribution list Total = {0}".format(sum(question_count)))

    print("==============================\n"
          "Total Questions = {0}\n"
          "Total Average   = {1}\n"
          "==============================\n"
          "start ... {2}\n"
          "end   ... {3}\n"
          "Total execution time ... {4:.4f}[s]"
          .format(total, average, datetime.datetime.fromtimestamp(start_time), datetime.datetime.fromtimestamp(end_time), end_time - start_time))

    return


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

    # set MAX(repeat count)
    MAX = 10
    if len(argv) >= 3:
         if argv[2].isdecimal():
             MAX = int(argv[2])

    return N, MAX


if __name__ == '__main__':
    main()
