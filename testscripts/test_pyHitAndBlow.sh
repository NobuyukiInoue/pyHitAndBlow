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
    N=$1
    MAX=$2

    start_time=`date "+%Y-%m-%d %H:%M:%S"`
    TARGET_PYTHON_SCRIPT="./pyHitAndBlow_offence.py"
    ENABLE_PRINT="false"
    result_count=()
    TOTAL=0

    for ((i=0; i < $MAX; i++)); do
        ANSWER_NUMBER=`python ./create_random_n_digits_number.py $N`

        printf \
"#------------------------------#\n"\
"# Running ... $((${i} + 1))/$MAX\n"\
"#------------------------------#\n"\

        python $TARGET_PYTHON_SCRIPT $N $ENABLE_PRINT $ANSWER_NUMBER

        result_count+=($?)
        let TOTAL+=${result_count[$i]}
        AVERAGE=`echo "scale=4; ${TOTAL} / ${#result_count[*]}" | bc`

        printf "\n# Latest Average = $AVERAGE\n\n"
    done

    printf "==== ResultCount history =====\n"
    i=0
    for e in ${result_count[@]}; do
        printf "result_count[$i] = ${e}\n"
        let i++
    done

    AVERAGE=`echo "scale=4; ${TOTAL} / ${i}" | bc`
    end_time=`date "+%Y-%m-%d %H:%M:%S"`

    printf \
"==============================\n"\
"average = $AVERAGE\n"\
"==============================\n"\
"start ... $start_time\n"\
"end   ... $end_time\n"\
"Total execution time ... $SECONDS[s]\n"

}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main $N $MAX
fi

