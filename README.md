# pyHitAndBlow

Auto Caluculate Hit & Blow (Master Mind) Script.<br>
Calculate the number of N digits you have decided.<br>
<br>
https://en.wikipedia.org/wiki/Mastermind_(board_game)

## Usage

```
 pyHitAndBlow.py [N [enable print] [answer number]]]
```

## Options

Options:

|Options|Explanation|
|-------|-----------|
N|digits of answer number. (2 <= N <= 10)<br>(default ... 4)
enable print|when "True" then enable print remaining target numbers. <br>(default ... False)
answer number|Predetermined your unique N-digit answer number.

## Execution examples

### sample1

N(digits of answer number) = 4.
Predetermine your unique 4-digit number.<br>
If run with no arguments, enter as many Hit and Blow answers as the number offered by your computer.

```
$ python pyHitAndBlow.py

(remaining count = 5040) Is your number 7016 ?
[1] : please input H, B = 0,1

(remaining count = 1440) Is your number 2950 ?
[2] : please input H, B = 0,1

(remaining count = 378) Is your number 4365 ?
[3] : please input H, B = 0,2

(remaining count = 99) Is your number 3628 ?
[4] : please input H, B = 0,2

(remaining count = 19) Is your number 1234 ?
[5] : please input H, B = 4,0
calculate successful.

===== challenge history =====
[1] (5040) <--- 7016 (0, 1)
[2] (1440) <--- 2950 (0, 1)
[3] ( 378) <--- 4365 (0, 2)
[4] (  99) <--- 3628 (0, 2)
[5] (  19) <--- 1234 (4, 0)
```

### sample2

N(digits of answer number) = 4.
If you give the argument answer_number, it will be in automatic answer mode.

```
$ python pyHitAndBlow.py 4 false 1234
N ... 4
set answer number ... 1234

(remaining count = 5040) Is your number 1653 ?
input response is Hit = 1, Blow = 1

(remaining count = 720) Is your number 7463 ?
input response is Hit = 0, Blow = 2

(remaining count = 165) Is your number 6054 ?
input response is Hit = 1, Blow = 0

(remaining count = 16) Is your number 3257 ?
input response is Hit = 1, Blow = 1

(remaining count = 2) Is your number 1234 ?
input response is Hit = 4, Blow = 0
calculate successful.

===== challenge history =====
[1] (5040) <--- 1653 (1, 1)
[2] ( 720) <--- 7463 (0, 2)
[3] ( 165) <--- 6054 (1, 0)
[4] (  16) <--- 3257 (1, 1)
[5] (   2) <--- 1234 (4, 0)
```

### sample3

N(digits of answer number) = 7.
And give the argument answer_number.

```
$ python pyHitAndBlow.py 7 false 3456789
N ... 7
set answer number ... 3456789

(remaining count = 604800) Is your number 1896204 ?
input response is Hit = 1, Blow = 3

(remaining count = 59640) Is your number 5647803 ?
input response is Hit = 0, Blow = 6

(remaining count = 8370) Is your number 3586027 ?
input response is Hit = 2, Blow = 3

(remaining count = 708) Is your number 1573046 ?
input response is Hit = 0, Blow = 5

(remaining count = 73) Is your number 3756498 ?
input response is Hit = 3, Blow = 4

(remaining count = 11) Is your number 3456789 ?
input response is Hit = 7, Blow = 0
calculate successful.

===== challenge history =====
[1] ( 604800) <--- 1896204 (1, 3)
[2] (  59640) <--- 5647803 (0, 6)
[3] (   8370) <--- 3586027 (2, 3)
[4] (    708) <--- 1573046 (0, 5)
[5] (     73) <--- 3756498 (3, 4)
[6] (     11) <--- 3456789 (7, 0)
```

## test scripts

### create_random_n-digits.py

This script outputs a unique 4-digit number obtained by random numbers.

```
$ python ./testscripts/create_random_n-digits.py 4
2357
```

### test_pyHitAndBlow.sh

This is a bash script that executes continuously and calculates the average value.

```
$ ./testscripts/test_pyHitAndBlow.sh 10
...
...
(remaining count = 2) Is your number 6538 ?
input response is Hit = 1, Blow = 3

(remaining count = 1) Is your number 5368 ?
input response is Hit = 4, Blow = 0
calculate successful.

===== challenge history =====
[1] (5040) <--- 8273 (0, 2)
[2] (1260) <--- 3108 (1, 1)
[3] ( 196) <--- 3029 (0, 1)
[4] (  40) <--- 2418 (1, 0)
[5] (   6) <--- 6358 (2, 2)
[6] (   2) <--- 6538 (1, 3)
[7] (   1) <--- 5368 (4, 0)
================================
RESULT_COUNT[0] = 5
RESULT_COUNT[1] = 5
RESULT_COUNT[2] = 7
RESULT_COUNT[3] = 6
RESULT_COUNT[4] = 5
RESULT_COUNT[5] = 4
RESULT_COUNT[6] = 7
RESULT_COUNT[7] = 6
RESULT_COUNT[8] = 6
RESULT_COUNT[9] = 7
================================
average = 5.80
================================
```

## Licence

[MIT](https://github.com/NobuyukiInoue/pyHitAndBlow/blob/master/LICENSE)


## Author

[Nobuyuki Inoue](https://github.com/NobuyukiInoue/)
