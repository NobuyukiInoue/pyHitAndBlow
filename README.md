# pyHitAndBlow

Caluculate Hit & Blow on 4 unique digits decimal number.

## Usage

```
 pyHitAndBlow.py [enable print] [answer number]
 ```

## Options

Options:

|Options|Explanation|
|-------|-----------|
enable print|when "True" then enable print remaining target numbers. (default = False)
answer number|answer number(for input check).

## Execution example2

### sample1

Predetermine your unique 4-digit number.
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

If you give the argument answer_number, it will be in automatic answer mode.

```
$ python pyHitAndBlow.py false 1234
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

## Licence

[MIT](https://github.com/NobuyukiInoue/pyHitAndBlow/blob/master/LICENSE)


## Author

[Nobuyuki Inoue](https://github.com/NobuyukiInoue/)
