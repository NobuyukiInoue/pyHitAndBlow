# -*- coding: utf-8 -*-

import datetime
import os
import random
import sys
import time

class TargetArray:
    def __init__(self, number, enabled):
        self.number = number
        self.enabled = enabled


class History:
    def __init__(self):
        self.challenge = []
        self.response = []
        self.remaining_count = []


def main():
    enable_print = False
    if len(sys.argv) >= 2:
         if sys.argv[1].upper() == "TRUE":
             enable_print = True

    answer_number = ""
    if len(sys.argv) >= 3:
        if sys.argv[2].isdecimal():
            answer_number = sys.argv[2]
            print("debug_mode ... True")
            print("set answer ... {0}".format(answer_number))

    result_table = create_table(4)

#   print_and_count_result(result_table, True)

    calc(4, result_table, enable_print, answer_number)

def create_table(n):
    result_table = []

    def sub_create_table(n, workStr):
        if n == 0:
            result_table.append(TargetArray(workStr, True))
            return
        for i in range(0, 10):
            if str(i) not in workStr:
                sub_create_table(n - 1, workStr + str(i))

    if n == 1:
        for i in range(0, 10):
            result_table.append(TargetArray(str(i), True))
    
    elif n > 1:
        for i in range(0, 10):
            sub_create_table(n - 1, str(i))

    return result_table

def calc(n, result_table, enable_print, answer_number):
    H, B = 0, 0
    challenge_count = 0
    history = History()

    while H < n:
        if answer_number == "":
            remainig_count = print_and_count_result(result_table, enable_print, "")
        else:
            remainig_count = print_and_count_result(result_table, enable_print, answer_number)

        history.remaining_count.append(remainig_count)

        if remainig_count <= 0:
            print_history(history, False)
            return False

        challenge_count += 1

        # print canidiate number.
        while True:
            num = int(random.random() * len(result_table))
            target_number = str(result_table[num].number)
            if result_table[num].enabled and target_number not in history.challenge:
                history.challenge.append(target_number)
                print("Your number is {0} ?".format(target_number))
                break

        # input response.
        if answer_number != "":
            H, B = response_check(n, answer_number, target_number)
        else:
            while True:
                print("[{0:2d}] : ".format(challenge_count), end = "")
                workStr = input("please input H, B = ")
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

        print("input response is Hit = {0}, Blow = {1}".format(H, B))

        history.response.append([H, B])

        for i in range(len(result_table)):
            if result_table[i].enabled == False:
                continue

            if answer_check(n, result_table[i].number, target_number, H, B) == False:
                result_table[i].enabled = False

    print_history(history, True)


def response_check(n, answer_number, target_number):
    H, B = 0, 0
    for col in range(0, n):
        if target_number[col] == answer_number[col]:
            H += 1

    for i in range(0, n):
        for j in range(0, n):
            if i != j and target_number[i] == answer_number[j]:
                B += 1

    return H, B

def answer_check(n, table_number, target_number, H, B):
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


def print_and_count_result(result_table, enable_print, answer_number):
    remaing_count = 0
    is_left_answer = False
    for i in range(len(result_table)):
        if result_table[i].enabled == True:
            remaing_count += 1
            if enable_print:
                print("{0:04}: ({1}, {2})".format(remaing_count, result_table[i].number, result_table[i].enabled))
            if result_table[i].number == answer_number:
                is_left_answer = True

    if answer_number != "":
        if is_left_answer:
            print("The answer {0} is left.".format(answer_number))
        else:
            print("Error!! The answer {0} is not left.".format(answer_number))
            return -1

    print("\n(remaining count = {0}) ".format(remaing_count), end = "")

    return remaing_count


def print_history(history, result):
    if result:
        print("calculate successful.")
    else:
        print("calculate failed.")

    print("\n===== challenge history =====")
    for i in range(len(history.challenge)):
        print("{0} ({1:4d}) <--- {2} ({3}, {4})".format(i + 1, history.remaining_count[i], history.challenge[i], history.response[i][0], history.response[i][1]))

    return True


if __name__ == '__main__':
    main()
