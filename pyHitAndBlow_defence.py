# -*- coding: utf-8 -*-

import sys
from mylibs import lib_hit_and_blow

def main() -> int:
    """
    function main.
    """
    N, enable_print, answer_number = lib_hit_and_blow.check_arguments(sys.argv)
    if N is None:
        return 0

    target_numbers = lib_hit_and_blow.create_target_numbers(N)
    result, history = lib_hit_and_blow.defence(N, target_numbers, enable_print, answer_number)
    lib_hit_and_blow.print_defence_history(N, history, result)

    if result:
        return len(history.response)
    else:
        return 0


if __name__ == '__main__':
    sys.exit(main())
