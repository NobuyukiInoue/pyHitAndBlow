#!/bin/bash

MAX=10
if [ $# -ge 1 ]; then
    MAX=$1
fi

function main() {
    TARGET_PY="./pyHitAndBlow.py"
    N=4
    ENABLE_PRINT="false"

    RESULT_COUNT=()

    for ((i=0; i < $MAX; i++)); do
        ANSWER_NUMBER=`python ./testscripts/create_random_n-digits.py`
        python $TARGET_PY $N $ENABLE_PRINT $ANSWER_NUMBER
        RESULT_COUNT+=($?)
    done

    printf "================================\n"
    i=0
    TOTAL=0
    for e in ${RESULT_COUNT[@]}; do
        printf "RESULT_COUNT[$i] = ${e}\n"
        let TOTAL+=${e}
        let i++
    done

    AVERAGE=`echo "scale=2; ${TOTAL} / ${i}" | bc`

    printf "================================\n"
    printf "average = $AVERAGE\n"
    printf "================================\n"
}

main
