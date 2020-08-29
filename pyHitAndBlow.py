# -*- coding: utf-8 -*-

import datetime
import os
import random
import sys
import time

class TargetNumber:
    """
    TargetNumber class.
    """
    def __init__(self, number, enabled):
        self.number = number
        self.enabled = enabled


class History:
    """
    Answer storage class.
    """
    def __init__(self):
        self.challenge = []
        self.response = []
        self.remaining_count = []


def main():
    """
    function main.
    """
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

    target_numbers = create_target_numbers(4)
    calc(4, target_numbers, enable_print, answer_number)

def create_target_numbers(n:int)-> list:
    """
    create target numbers.
    """
    target_numbers = []

    def sub_create_target_numbers(n, workStr):
        if n == 0:
            target_numbers.append(TargetNumber(workStr, True))
            return
        for i in range(0, 10):
            if str(i) not in workStr:
                sub_create_target_numbers(n - 1, workStr + str(i))

    if n == 1:
        for i in range(0, 10):
            target_numbers.append(TargetNumber(str(i), True))
    
    elif n > 1:
        for i in range(0, 10):
            sub_create_target_numbers(n - 1, str(i))

    return target_numbers

def calc(n:int, target_numbers:str, enable_print:bool, answer_number:str)-> bool:
    """
    caluculate Your number.
    """
    H, B = 0, 0
    challenge_count = 0
    history = History()

    while H < n:
        """
        remaining count check.
        """
        if answer_number == "":
            remainig_count = print_and_count_remaining(target_numbers, enable_print, "")
        else:
            remainig_count = print_and_count_remaining(target_numbers, enable_print, answer_number)

        history.remaining_count.append(remainig_count)

        if remainig_count <= 0:
            print_history(history, False)
            return False

        challenge_count += 1

        # print canidiate number.
        while True:
            index = int(random.random() * len(target_numbers))
            target_number = str(target_numbers[index].number)
            if target_numbers[index].enabled and target_number not in history.challenge:
                history.challenge.append(target_number)
                print("Is your number {0} ?".format(target_number))
                break

        # input response.
        if answer_number != "":
            H, B = response_check(n, answer_number, target_number)
        else:
            while True:
                print("[{0:d}] : ".format(challenge_count), end = "")
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

        for i in range(len(target_numbers)):
            if target_numbers[i].enabled == False:
                # continue if not a candidate.
                continue

            if answer_check(n, target_numbers[i].number, target_number, H, B) == False:
                # Remove from candidates.
                target_numbers[i].enabled = False

    print_history(history, True)


def response_check(n:int, answer_number:str, target_number:str):
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

def answer_check(n:int, table_number:str, target_number:str, H:int, B:int):
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


def print_and_count_remaining(target_numbers:list, enable_print:bool, answer_number:str):
    """
    print and count remaining.
    """
    remaing_count = 0
    is_left_answer = False
    for i in range(len(target_numbers)):
        if target_numbers[i].enabled == True:
            remaing_count += 1
            if enable_print:
                print("{0:04}: ({1}, {2})".format(remaing_count, target_numbers[i].number, target_numbers[i].enabled))
            if target_numbers[i].number == answer_number:
                is_left_answer = True

    if answer_number != "":
        if is_left_answer:
            print("The answer {0} is left.".format(answer_number))
        else:
            print("Error!! The answer {0} is not left.".format(answer_number))
            return -1

    print("\n(remaining count = {0}) ".format(remaing_count), end = "")

    return remaing_count


def print_history(history:History, result:bool):
    """
    print history.
    """
    if result:
        print("calculate successful.")
    else:
        print("calculate failed.")

    print("\n===== challenge history =====")
    for i in range(len(history.challenge)):
        print("[{0}] ({1:4d}) <--- {2} ({3}, {4})".format(i + 1, history.remaining_count[i], history.challenge[i], history.response[i][0], history.response[i][1]))

    return True


if __name__ == '__main__':
    main()
