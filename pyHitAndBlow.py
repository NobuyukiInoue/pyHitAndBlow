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

    result_table = create_table()

#   print_and_count_result(result_table, True)

    calc(result_table, enable_print, answer_number)

def create_table():
    result_table = []
    for n1 in range(0, 10):
        for n2 in range(0, 10):
            if n2 == n1:
                continue
            for n3 in range(0, 10):
                if n3 == n2 or n3 == n1:
                    continue
                for n4 in range(0, 10):
                    if n4 == n3 or n4 == n2 or n4 == n1:
                        continue
                    result_table.append(TargetArray(str(n1) + str(n2) + str(n3) + str(n4), True))
    return result_table

class History:
    def __init__(self):
        self.challenge = []
        self.response = []
        self.remaining_count = []

def calc(result_table, enable_print, answer_number):
    H, B = 0, 0
    challenge_count = 0
    history = History()

    while H < 4:
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
            n = int(random.random() * len(result_table))
            target_number = str(result_table[n].number)
            if result_table[n].enabled and target_number not in history.challenge:
                history.challenge.append(target_number)
                print("target is {0} ?".format(target_number))
                break

        # input response.
        while True:
            print("[{0:2d}] : ".format(challenge_count), end = "")
            workStr = input("please input H, B = ")
            flds = workStr.replace(" ", "").split(",")
            if len(flds) == 2:
                try:
                    H, B = int(flds[0]), int(flds[1])
                    if H < 0 or H > 4:
                        continue
                    if B < 0 or B > 4:
                        continue
                    if H == 3 and B == 1:
                        continue
                    break
                except:
                    continue

            print("input response is Hit = {0}, Blow = {1}".format(H, B))
            if answer_number != "":
                check_H, check_B = response_check(answer_number, target_number)
                if not (check_H == H and check_B == B):
                    print("response check Error!! collect is ({0}, {1})".format(check_H, check_B))
                    continue
                break

        history.response.append([H, B])

        for i in range(len(result_table)):
            if result_table[i].enabled == False:
                continue

            if answer_check(result_table[i].number, target_number, H, B) == False:
                result_table[i].enabled = False

    print_history(history, True)


def response_check(answer_number, target_number):
    H, B = 0, 0
    for col in range(0, 4):
        if target_number[col] == answer_number[col]:
            H += 1

    if target_number[0] == answer_number[1] \
    or target_number[0] == answer_number[2] \
    or target_number[0] == answer_number[3]:
        B += 1

    if target_number[1] == answer_number[0] \
    or target_number[1] == answer_number[2] \
    or target_number[1] == answer_number[3]:
        B += 1

    if target_number[2] == answer_number[0] \
    or target_number[2] == answer_number[1] \
    or target_number[2] == answer_number[3]:
        B += 1

    if target_number[3] == answer_number[0] \
    or target_number[3] == answer_number[1] \
    or target_number[3] == answer_number[2]:
        B += 1

    return H, B

def answer_check(table_number, target_number, H, B):
    check_H, check_B = 0, 0
    for col in range(0, 4):
        if target_number[col] == table_number[col]:
            check_H += 1
    
    if check_H != H:
       return False

    if target_number[0] == table_number[1] \
    or target_number[0] == table_number[2] \
    or target_number[0] == table_number[3]:
        check_B += 1

    if target_number[1] == table_number[0] \
    or target_number[1] == table_number[2] \
    or target_number[1] == table_number[3]:
        check_B += 1

    if target_number[2] == table_number[0] \
    or target_number[2] == table_number[1] \
    or target_number[2] == table_number[3]:
        check_B += 1

    if target_number[3] == table_number[0] \
    or target_number[3] == table_number[1] \
    or target_number[3] == table_number[2]:
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

    print("\nremaining count = {0}".format(remaing_count))

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
