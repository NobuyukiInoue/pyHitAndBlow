# -*- coding: utf-8 -*-

import random

class HistoryRecords:
    """
    HistoryRecords class.
    """
    def __init__(self):
        self.challenge = []
        self.response = []
        self.remaining_count = []


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
                print("answer number {0} digits is not {1}".format(answer_number, N))
                return None, None, None
            print("set answer number ... {0}".format(answer_number))
        else:
            print("{0} is not decimal.".format(argv[3]))
            return None, None, None

    return N, enable_print, answer_number


def create_target_numbers(n:int)-> [str]:
    """
    create target numbers.
    """
    target_numbers = []

    def sub_create_target_numbers(n, workStr):
        if n == 0:
            target_numbers.append(workStr)
            return
        for i in range(10):
            if str(i) not in workStr:
                sub_create_target_numbers(n - 1, workStr + str(i))

    if n == 1:
        for i in range(10):
            target_numbers.append(str(i))
    
    elif n > 1:
        for i in range(10):
            sub_create_target_numbers(n - 1, str(i))

    return target_numbers


def create_random_n_digits_number(n:int) -> str:
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


def offence(n:int, target_numbers:str, enable_print:bool, answer_number:str) -> (bool, HistoryRecords):
    """
    caluculate Your number.
    """
    H, B = 0, 0
    challenge_count = 0
    history = HistoryRecords()
    random.seed()

    while H < n:
        """
        remaining count check.
        """
        remainig_count = print_and_count_remaining(target_numbers, enable_print, answer_number)
        history.remaining_count.append(remainig_count)

        if remainig_count <= 0:
            return False, history

        challenge_count += 1

        if n == 4:
            selected_number = create_canidiate_number4_Minimum_question_strategy(n, target_numbers, history)
        #   selected_number = create_canidiate_number4_Highest_winning_strategy(n, target_numbers, history)

        else:
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


def defence(n:int, target_numbers:str, enable_print:bool, answer_number:str) -> (bool, HistoryRecords):
    """
    caluculate Your number.
    """

    print("When you want to end on the way, please input 0\n")

    H, B = 0, 0
    challenge_count = 0
    history = HistoryRecords()

    if answer_number == "" or answer_number is None:
        answer_number = create_random_n_digits_number(n)

    while H < n:
        """
        remaining count check.
        """
        challenge_count += 1

        selected_number = input_selected_number(n, challenge_count)
        if selected_number is None:
            print("break.")
            return False, history

        history.challenge.append(selected_number)

        H, B = response_check(n, answer_number, selected_number)
        history.response.append([H, B])
        print("input response is Hit = {0}, Blow = {1}".format(H, B))

    print("\n"
          "congratulations!!!\n"
          "my answer number is {0}.".format(answer_number))

    return True, history


def create_canidiate_number(n:int, target_numbers:[str], history:HistoryRecords) -> str:
    """
    create canidiate number.
    """
    if len(history.challenge) == 0:
        index = random.randint(0, len(target_numbers) - 1)
        return str(target_numbers[index])
    else:
        while True:
            index = random.randint(0, len(target_numbers) - 1)
            selected_number = str(target_numbers[index])
            if selected_number in history.challenge:
                continue
            return selected_number


def create_canidiate_number_same_response(n:int, target_numbers:[str], history:HistoryRecords) -> str:
    """
    create canidiate number.
    """
    if len(history.challenge) == 0:
        index = random.randint(0, len(target_numbers) - 1)
        return str(target_numbers[index])
    else:
        while True:
            index = random.randint(0, len(target_numbers) - 1)
            selected_number = str(target_numbers[index])
            if selected_number in history.challenge:
                continue
            H, B = response_check(n, history.challenge[-1], selected_number)
            if history.response[-1] == [H, B]:
                return selected_number


def create_canidiate_number4_Minimum_question_strategy(n:int, target_numbers:[str], history:HistoryRecords) -> str:
    """
    create canidiate number.
    (Minimum question strategy)
    """
    if len(history.challenge) == 1:
        while True:
            """
            index = random.randint(0, len(target_numbers) - 1)
            selected_number = str(target_numbers[index])
            """
            selected_number = create_random_n_digits_number(n)
            if selected_number in history.challenge:
                continue
            H, B = response_check(n, history.challenge[-1], selected_number)

            if history.response[-1] == [3, 0]:
                if (H, B) == (1, 1):
                    return selected_number
            elif history.response[-1] == [2, 2]:
                if (H, B) == (2, 2):
                    return selected_number
            elif history.response[-1] == [2, 1]:
                if (H, B) == (2, 0):
                    return selected_number
            elif history.response[-1] == [2, 0]:
                if (H, B) == (1, 1):
                    return selected_number
            elif history.response[-1] == [1, 3]:
                if (H, B) == (2, 1):
                    return selected_number
            elif history.response[-1] == [1, 2]:
                if (H, B) == (1, 1):
                    return selected_number
            elif history.response[-1] == [1, 1]:
                if (H, B) == (1, 1):
                    return selected_number
            elif history.response[-1] == [1, 0]:
                if (H, B) == (1, 0):
                    return selected_number
            elif history.response[-1] == [0, 4]:
                if (H, B) == (0, 4):
                    return selected_number
            elif history.response[-1] == [0, 3]:
                if (H, B) == (0, 2):
                    return selected_number
            elif history.response[-1] == [0, 2]:
                if (H, B) == (0, 2):
                    return selected_number
            elif history.response[-1] == [0, 1]:
                if (H, B) == (0, 1):
                    return selected_number
            elif history.response[-1] == [0, 0]:
                if (H, B) == (0, 0):
                    return selected_number
            else:
                return selected_number

    else:
        while True:
            index = random.randint(0, len(target_numbers) - 1)
            selected_number = str(target_numbers[index])
            if selected_number in history.challenge:
                continue
            return selected_number


def create_canidiate_number4_Highest_winning_strategy(n:int, target_numbers:[str], history:HistoryRecords) -> str:
    """
    create canidiate number.
    (Highest winning strategy)
    """
    if len(history.challenge) == 1:
        while True:
            selected_number = create_random_n_digits_number(n)
            if selected_number in history.challenge:
                continue
            H, B = response_check(n, history.challenge[-1], selected_number)

            if history.response[-1] == [3, 0]:
                if (H, B) == (1, 0):
                    return selected_number
            elif history.response[-1] == [2, 2]:
                if (H, B) == (1, 2):
                    return selected_number
            elif history.response[-1] == [2, 1]:
                if (H, B) == (2, 0):
                    return selected_number
            elif history.response[-1] == [2, 0]:
                if (H, B) == (1, 0):
                    return selected_number
            elif history.response[-1] == [1, 3]:
                if (H, B) == (2, 1):
                    return selected_number
            elif history.response[-1] == [1, 2]:
                if (H, B) == (1, 1):
                    return selected_number
            elif history.response[-1] == [1, 1]:
                if (H, B) == (2, 0):
                    return selected_number
            elif history.response[-1] == [1, 0]:
                if (H, B) == (0, 1):
                    return selected_number
            elif history.response[-1] == [0, 4]:
                if (H, B) == (0, 3):
                    return selected_number
            elif history.response[-1] == [0, 3]:
                if (H, B) == (0, 2):
                    return selected_number
            elif history.response[-1] == [0, 2]:
                if (H, B) == (0, 2):
                    return selected_number
            elif history.response[-1] == [0, 1]:
                if (H, B) == (0, 1):
                    return selected_number
            elif history.response[-1] == [0, 0]:
                if (H, B) == (0, 0):
                    return selected_number
            else:
                return selected_number

    else:
        while True:
            index = random.randint(0, len(target_numbers) - 1)
            selected_number = str(target_numbers[index])
            if selected_number in history.challenge:
                continue
            return selected_number


def response_check(n:int, answer_number:str, target_number:str) -> (int, int):
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


def input_selected_number(n:int, challenge_count:int) -> str:
    """
    input selected number
    """
    format_str = "[{0}] : select number " + "x"*n + " = "
    while True:
        print(format_str.format(challenge_count), end = "")
        # input number.
        selected_number = input()

        if selected_number == "0" :
            return None

        if len(selected_number) != n:
            print("{0} is invalid number.".format(selected_number))
            continue

        if not selected_number.isdecimal():
            print("{0} is invalid number.".format(selected_number))
            continue

        enable_return = True
        for i in range(len(selected_number) - 1):
            if selected_number[i] in selected_number[i + 1:]:
                enable_return = False
                break
        
        if enable_return:
            return selected_number

        print("{0} is invalid number.".format(selected_number))


def response_input(n:int, challenge_count:int) -> (int, int):
    """
    response input
    """
    while True:
        print("[{0:d}] : ".format(challenge_count), end = "")
        workStr = input("please input H, B = ").strip()

        if workStr == str(n):
            return n, 0

        while "  " in workStr:
            workStr = workStr.replace("  ", " ")

        if "," in workStr:
            flds = workStr.replace(" ", "").split(",")
        elif " " in workStr:
            flds = workStr.split(" ")
        elif len(workStr) == 2:
            flds = [workStr[0], workStr[1]]
        else:
            print("{0} is invalid.".format(workStr))
            continue

        if len(flds) == 2:
            try:
                H, B = int(flds[0]), int(flds[1])
                if H == n and B == 0:
                    break
                elif (H + B > n) \
                or (H < 0 or H > n) \
                or (B < 0 or B > n) \
                or (H == n - 1 and B == 1):
                    print("{0} is invalid.".format(workStr))
                    continue
                break
            except:
                continue

    return H, B


def answer_check(n:int, table_number:str, target_number:str, H:int, B:int) -> bool:
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


def print_and_count_remaining(target_numbers:list, enable_print:bool, answer_number:str) -> int:
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

    print("\n(remaining count = {0:4d}) ".format(remaing_count), end = "")

    return remaing_count


def print_offence_history(n:int, history:HistoryRecords, result:bool):
    """
    print history.
    """
    if result:
        print("calculate successful.")
    else:
        print("calculate failed.")

    format_str = "[{0}] ({1:" + str(n) + "d}) ---> {2} ({3}, {4})"
    print("\n===== challenge history ======")
    for i in range(len(history.challenge)):
        print(format_str.format(i + 1, history.remaining_count[i], history.challenge[i], history.response[i][0], history.response[i][1]))


def print_defence_history(n:int, history:HistoryRecords, result:bool):
    """
    print history.
    """
    format_str = "[{0}]  .... {1} ({2}, {3})"
    print("\n===== challenge history ======")
    for i in range(len(history.challenge)):
        print(format_str.format(i + 1, history.challenge[i], history.response[i][0], history.response[i][1]))
