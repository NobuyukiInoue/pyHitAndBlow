# -*- coding: utf-8 -*-

import os
import random
import sys

class HistoryRecords:
    """
    HistoryRecords class.
    """
    def __init__(self):
        self.challenge = []
        self.response = []
        self.remaining_count = []


def main()-> int:
    """
    function main.
    """

    # set n(digits of answer number).
    N = 4
    if len(sys.argv) >= 2:
        if sys.argv[1].isdecimal():
            N = int(sys.argv[1])
            if N < 2 or N > 10:
                print("Give n between 2 and 10 inclusive.")
                return 0
            print("N ... {0}".format(N))
        else:
            print("{0} is not decimal.".format(sys.argv[1]))
            return 0

    # set enable_print
    enable_print = False
    if len(sys.argv) >= 3:
         if sys.argv[2].upper() == "TRUE":
             enable_print = True

    # set answer number
    answer_number = ""
    if len(sys.argv) >= 4:
        if sys.argv[3].isdecimal():
            answer_number = sys.argv[3]
            if len(answer_number) != N:
                print("answer number digits is not {0}".format(N))
                return 0
            print("set answer number ... {0}".format(answer_number))
        else:
            print("{0} is not decimal.".format(sys.argv[3]))
            return 0

    target_numbers = create_target_numbers(N)
    result, history = calc(N, target_numbers, enable_print, answer_number)
    print_history(N, history, result)

    if result:
        return len(history.response)
    else:
        return 0

def create_target_numbers(n:int)-> [str]:
    """
    create target numbers.
    """
    target_numbers = []

    def sub_create_target_numbers(n, workStr):
        if n == 0:
            target_numbers.append(workStr)
            return
        for i in range(0, 10):
            if str(i) not in workStr:
                sub_create_target_numbers(n - 1, workStr + str(i))

    if n == 1:
        for i in range(0, 10):
            target_numbers.append(str(i))
    
    elif n > 1:
        for i in range(0, 10):
            sub_create_target_numbers(n - 1, str(i))

    return target_numbers


def calc(n:int, target_numbers:str, enable_print:bool, answer_number:str)-> (bool, HistoryRecords):
    """
    caluculate Your number.
    """
    H, B = 0, 0
    challenge_count = 0
    history = HistoryRecords()

    while H < n:
        """
        remaining count check.
        """
        remainig_count = print_and_count_remaining(target_numbers, enable_print, answer_number)
        history.remaining_count.append(remainig_count)

        if remainig_count <= 0:
            return False, history

        challenge_count += 1

        selected_number = create_canidiate_number(n, target_numbers, history)
        history.challenge.append(selected_number)

        # print canidiate number.
        print("Is your number {0} ?".format(selected_number))

        # input response.
        if answer_number != "":
            H, B = response_check(n, answer_number, selected_number)
        else:
            H, B = response_input(n, challenge_count)

        print("input response is Hit = {0}, Blow = {1}".format(H, B))

        history.response.append([H, B])

        # create new canidiates numbers list.
        new_target_numbers = []

        for current_number in target_numbers:
            if answer_check(n, current_number, selected_number, H, B):
                # new candidates number add.
                new_target_numbers.append(current_number)

        target_numbers = new_target_numbers

    return True, history

def create_canidiate_number(n:int, target_numbers:[str], history:HistoryRecords)->str:
    """
    create canidiate number.
    """
    while True:
        index = int(random.random() * len(target_numbers))
        selected_number = str(target_numbers[index])
        if selected_number not in history.challenge:
            break
    return selected_number

def response_check(n:int, answer_number:str, target_number:str)->(int, int):
    """
    response check.
    """
    H, B = 0, 0
    for col in range(0, n):
        if target_number[col] == answer_number[col]:
            H += 1

    for i in range(0, n):
        for j in range(0, n):
            if i != j and target_number[i] == answer_number[j]:
                B += 1

    return H, B


def response_input(n, challenge_count)->(int, int):
    """
    response input
    """
    while True:
        print("[{0:d}] : ".format(challenge_count), end = "")
        workStr = input("please input H, B = ").strip()

        if workStr == str(n):
            return n, 0

        flds = workStr.replace(" ", "").split(",")
        if len(flds) == 2:
            try:
                H, B = int(flds[0]), int(flds[1])
                if H < 0 or H > n:
                    continue
                if B < 0 or B > n:
                    continue
                if H == n - 1 and B == 1:
                    continue
                break
            except:
                continue

    return H, B


def answer_check(n:int, table_number:str, target_number:str, H:int, B:int)->bool:
    """
    answer check.
    """
    check_H, check_B = 0, 0

    for col in range(0, n):
        if target_number[col] == table_number[col]:
            check_H += 1
    
    if check_H != H:
       return False

    for i in range(0, n):
        for j in range(0, n):
            if i != j and target_number[i] == table_number[j]:
                check_B += 1

    if check_B != B:
        return False

    return True


def print_and_count_remaining(target_numbers:list, enable_print:bool, answer_number:str)->int:
    """
    print and count remaining.
    """
    remaing_count = 0
    is_left_answer = False

    if enable_print:
        print("----+-----")

    for i in range(len(target_numbers)):
        remaing_count += 1
        if enable_print:
            print("{0:04}: {1}".format(remaing_count, target_numbers[i]))
        if target_numbers[i] == answer_number:
            is_left_answer = True

    if enable_print:
        print("----+-----")

    if answer_number != "":
        if not is_left_answer:
            print("Error!! The answer {0} is not left.".format(answer_number))
            return 0

    print("\n(remaining count = {0}) ".format(remaing_count), end = "")

    return remaing_count


def print_history(n:int, history:HistoryRecords, result:bool):
    """
    print history.
    """
    if result:
        print("calculate successful.")
    else:
        print("calculate failed.")

    format_str = "[{0}] ({1:" + str(n) + "d}) <--- {2} ({3}, {4})"
    print("\n===== challenge history =====")
    for i in range(len(history.challenge)):
        print(format_str.format(i + 1, history.remaining_count[i], history.challenge[i], history.response[i][0], history.response[i][1]))


if __name__ == '__main__':
    sys.exit(main())
