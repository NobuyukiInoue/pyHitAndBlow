#!/bin/bash

N=4
if [ $# -ge 1 ]; then
    N=$1
fi

MAX=10
if [ $# -ge 2 ]; then
    MAX=$2
fi

function main() {
    TARGET_PYTHON_SCRIPT="./pyHitAndBlow_offence.py"
    ENABLE_PRINT="false"

    RESULT_COUNT=()

    for ((i=0; i < $MAX; i++)); do
        ANSWER_NUMBER=`python ./create_random_n_digits_number.py $N`

        printf "#------------------------------#\n"
        printf "# Running ... ($i/$MAX)\n"
        printf "#------------------------------#\n"

        python $TARGET_PYTHON_SCRIPT $N $ENABLE_PRINT $ANSWER_NUMBER
        RESULT_COUNT+=($?)
    done

    printf "==== ResultCount history =====\n"
    i=0
    TOTAL=0
    for e in ${RESULT_COUNT[@]}; do
        printf "RESULT_COUNT[$i] = ${e}\n"
        let TOTAL+=${e}
        let i++
    done

    AVERAGE=`echo "scale=2; ${TOTAL} / ${i}" | bc`

    printf "==============================\n"
    printf "average = $AVERAGE\n"
    printf "==============================\n"
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
