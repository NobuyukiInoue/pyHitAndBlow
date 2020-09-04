# pyHitAndBlow

Hit & Blow (Bulls and Cows) Offense & Defense Script by Python3.<br>
Offence Script solve the number of N digits you have decided.<br>
<br>
https://en.wikipedia.org/wiki/Bulls_and_Cows


## 1. pyHitAndBlow_offence.py

Auto Caluculate Hit & Blow (Bulls and Cows) Offence script.

### 1-1. Usage

```
pyHitAndBlow_offence.py [N [enable print] [answer number]]]
```

### 1-2. Options

|Options|Explanation|
|-------|-----------|
N|digits of answer number. (2 <= N <= 10)<br>(default ... 4)
enable print|when "True" then enable print remaining target numbers. <br>(default ... False)
answer number|Predetermined your unique N-digit answer number.

### 1-3. Execution examples

#### sample1

N(digits of answer number) = 4.<br>
Predetermine your unique 4-digit number.<br>
If run with no arguments, enter as many Hit and Blow answers as the number offered by your computer.

```
$ python pyHitAndBlow_offence.py

(remaining count = 5040) Is your number 7016 ?
[1] : please input H, B = 0,1            <--- "0,1", "0 1", "01" are also acceptable.

(remaining count = 1440) Is your number 2950 ?
[2] : please input H, B = 0,1            <--- "0,1", "0 1", "01" are also acceptable.

(remaining count =  378) Is your number 4365 ?
[3] : please input H, B = 0,2            <--- "0,2", "0 2", "02" are also acceptable.

(remaining count =   99) Is your number 3628 ?
[4] : please input H, B = 0,2            <--- "0,2", "0 2", "02" are also acceptable.

(remaining count =   19) Is your number 1234 ?
[5] : please input H, B = 4,0            <--- "4,0", "4 0", "40", "4" are also acceptable.
calculate successful.

===== challenge history =====
[1] (5040) ---> 7016 (0, 1)
[2] (1440) ---> 2950 (0, 1)
[3] ( 378) ---> 4365 (0, 2)
[4] (  99) ---> 3628 (0, 2)
[5] (  19) ---> 1234 (4, 0)
```

#### sample2

N(digits of answer number) = 4.<br>
If you give the argument answer_number, it will be in automatic answer mode.

```
$ python pyHitAndBlow_offence.py 4 false 1234
N ... 4
set answer number ... 1234

(remaining count = 5040) Is your number 1653 ?
input response is Hit = 1, Blow = 1

(remaining count =  720) Is your number 7463 ?
input response is Hit = 0, Blow = 2

(remaining count =  165) Is your number 6054 ?
input response is Hit = 1, Blow = 0

(remaining count =   16) Is your number 3257 ?
input response is Hit = 1, Blow = 1

(remaining count =    2) Is your number 1234 ?
input response is Hit = 4, Blow = 0
calculate successful.

===== challenge history =====
[1] (5040) ---> 1653 (1, 1)
[2] ( 720) ---> 7463 (0, 2)
[3] ( 165) ---> 6054 (1, 0)
[4] (  16) ---> 3257 (1, 1)
[5] (   2) ---> 1234 (4, 0)
```

#### sample3

N(digits of answer number) = 7.<br>
And give the argument answer_number.

```
$ python pyHitAndBlow_offence.py 7 false 3456789
N ... 7
set answer number ... 3456789

(remaining count = 604800) Is your number 1896204 ?
input response is Hit = 1, Blow = 3

(remaining count = 59640) Is your number 5647803 ?
input response is Hit = 0, Blow = 6

(remaining count = 8370) Is your number 3586027 ?
input response is Hit = 2, Blow = 3

(remaining count =  708) Is your number 1573046 ?
input response is Hit = 0, Blow = 5

(remaining count =   73) Is your number 3756498 ?
input response is Hit = 3, Blow = 4

(remaining count =   11) Is your number 3456789 ?
input response is Hit = 7, Blow = 0
calculate successful.

===== challenge history =====
[1] ( 604800) ---> 1896204 (1, 3)
[2] (  59640) ---> 5647803 (0, 6)
[3] (   8370) ---> 3586027 (2, 3)
[4] (    708) ---> 1573046 (0, 5)
[5] (     73) ---> 3756498 (3, 4)
[6] (     11) ---> 3456789 (7, 0)
```

## 2. pyHitAndBlow_defence.py

Auto Caluculate Hit & Blow (Bulls and Cows) Defence Script.

### 2-1. Usage

```
pyHitAndBlow_defence.py [N [enable print] [answer number]]]
```

### 2-2. Options

|Options|Explanation|
|-------|-----------|
N|digits of answer number. (2 <= N <= 10)<br>(default ... 4)
enable print|not use.<br>(default ... False)
answer number|Predetermined unique N-digit answer number.

### 2-3. Execution examples

```
$ python pyHitAndBlow_defence.py 4
N ... 4
When you want to end on the way, please input 0

[1] : select number xxxx = 3429
input response is Hit = 0, Blow = 2
[2] : select number xxxx = 7594
input response is Hit = 0, Blow = 1
[3] : select number xxxx = 9613
input response is Hit = 1, Blow = 2
[4] : select number xxxx = 9386
input response is Hit = 2, Blow = 1
[5] : select number xxxx = 9036
input response is Hit = 1, Blow = 3
[6] : select number xxxx = 9360
input response is Hit = 4, Blow = 0

congratulations!!!
my answer number is 9360.


===== challenge history ======
[1]  .... 3429 (0, 2)
[2]  .... 7594 (0, 1)
[3]  .... 9613 (1, 2)
[4]  .... 9386 (2, 1)
[5]  .... 9036 (1, 3)
[6]  .... 9360 (4, 0)
```


## 3. create_random_n_digits_number.py

This script outputs a unique 4-digit number obtained by random numbers.

### 3-1. Usage

```
create_random_n_digits_number.py [N]
```

### 3-2. Options

|Options|Explanation|
|-------|-----------|
N|digits of answer number. (2 <= N <= 10)<br>(default ... 4)

### 3-3. Execution example

```
$ python create_random_n_digits_number.py 4
2357
```

## 4. test scripts.

### 4-1. test_pyHitAndBlow.py

This is a python script that executes continuously and calculates the average value.
(Faster than ./testscripts/test_pyHitAndBlow.sh or ./testscripts/test_pyHitAndBlow.ps)

#### 4-1-1. Usage.
```
python test_pyHitAndBlow.py [N [MAX]]
```

#### 4-1.2. Options.

|Options|Explanation|
|-------|-----------|
N|digits of answer number. (2 <= N <= 10)<br>(default ... 4)
MAX|repeat count.<br>(default ... 10)

#### 4-1-3. Execution example

```
$ python test_pyHitAndBlow.py
...
...
(remaining count =    2) Is your number 3970 ?
input response is Hit = 2, Blow = 2

(remaining count =    1) Is your number 9370 ?
input response is Hit = 4, Blow = 0

===== challenge history ======
[1]  .... 5076 (1, 1)
[2]  .... 6049 (0, 2)
[3]  .... 5634 (0, 1)
[4]  .... 4870 (2, 0)
[5]  .... 3970 (2, 2)
[6]  .... 9370 (4, 0)

# Latest Average = 5.4000

==== ResultCount history =====
ResultCount[0] = 7
ResultCount[1] = 5
ResultCount[2] = 6
ResultCount[3] = 5
ResultCount[4] = 4
ResultCount[5] = 5
ResultCount[6] = 5
ResultCount[7] = 5
ResultCount[8] = 6
ResultCount[9] = 6
==============================
Total Average = 5.4
==============================
start ... 2020-09-04 16:50:27.382880
end   ... 2020-09-04 16:50:27.594878
Total execution time ... 0.2120[s]
```

### 4-2. test_pyHitAndBlow.sh

This is a bash script that executes continuously and calculates the average value.

#### 4-2-1. Usage.
```
test_pyHitAndBlow.sh [N [MAX]]
```

#### 4-2.2. Options.

|Options|Explanation|
|-------|-----------|
N|digits of answer number. (2 <= N <= 10)<br>(default ... 4)
MAX|repeat count.<br>(default ... 10)

#### 4-2-3. Execution example

```
$ ./testscripts/test_pyHitAndBlow.sh 4 10
...
...
(remaining count =    6) Is your number 6097 ?
input response is Hit = 0, Blow = 2

(remaining count =    1) Is your number 8160 ?
input response is Hit = 4, Blow = 0
calculate successful.

===== challenge history ======
[1] (5040) ---> 4065 (1, 1)
[2] ( 720) ---> 4203 (0, 1)
[3] ( 180) ---> 8495 (1, 0)
[4] (  26) ---> 1467 (1, 1)
[5] (   6) ---> 6097 (0, 2)
[6] (   1) ---> 8160 (4, 0)

# Latest Average = 5.4000

==== ResultCount history =====
result_count[0] = 4
result_count[1] = 5
result_count[2] = 6
result_count[3] = 5
result_count[4] = 6
result_count[5] = 4
result_count[6] = 5
result_count[7] = 6
result_count[8] = 7
result_count[9] = 6
==============================
average = 5.4000
==============================
start ... 2020-09-01 22:01:00
end   ... 2020-09-01 22:01:01
Total execution time ... 1[s]
```

### 4-3. test_pyHitAndBlow.ps1

This is a PowerShell script that executes continuously and calculates the average value.
(It is slower than the other two scripts due to the large process startup/termination overhead on MS-Windows.)

#### 4-3-1. Usage.
```
test_pyHitAndBlow.ps1 [N] [MAX]
```

#### 4-3-2. Options.

|Options|Explanation|
|-------|-----------|
N|digits of answer number. (2 <= N <= 10)<br>(default ... 4)
MAX|repeat count.<br>(default ... 10)

#### 4-3-3. Execution example

```
D:\pyHitAndBlow> .\testscripts\test_pyHitAndBlow.ps1 4 10
...
...
(remaining count =   16) Is your number 3895 ?
input response is Hit = 2, Blow = 2

(remaining count =    1) Is your number 5893 ?
input response is Hit = 4, Blow = 0
calculate successful.

===== challenge history ======
[1] (5040) ---> 6380 (0, 2)
[2] (1260) ---> 4069 (0, 1)
[3] ( 304) ---> 1938 (0, 3)
[4] (  16) ---> 3895 (2, 2)
[5] (   1) ---> 5893 (4, 0)

# Latest Average = 5.4

==== ResultCount history =====
ResultCount[0] = 6
ResultCount[1] = 5
ResultCount[2] = 7
ResultCount[3] = 4
ResultCount[4] = 5
ResultCount[5] = 7
ResultCount[6] = 4
ResultCount[7] = 6
ResultCount[8] = 5
ResultCount[9] = 5
==============================
Total Average = 5.4
==============================
start ... 2020-09-01 22:09:06
end   ... 2020-09-01 22:09:07
Total execution time ... 1.5060625[s]
```

## Licence

[MIT](https://github.com/NobuyukiInoue/pyHitAndBlow/blob/master/LICENSE)


## Author

[Nobuyuki Inoue](https://github.com/NobuyukiInoue/)
