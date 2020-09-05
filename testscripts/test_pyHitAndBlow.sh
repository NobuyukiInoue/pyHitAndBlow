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
    total=0

    for ((i=0; i < $MAX; i++)); do
        ANSWER_NUMBER=`python ./create_random_n_digits_number.py $N`

        printf \
"#------------------------------#\n"\
"# Running ... $((${i} + 1))/$MAX\n"\
"#------------------------------#\n"\

        python $TARGET_PYTHON_SCRIPT $N $ENABLE_PRINT $ANSWER_NUMBER

        result_count+=($?)
        let total+=${result_count[$i]}
        average=`echo "scale=4; ${total} / ${#result_count[*]}" | bc`

        printf "\n# Latest average = $average\n\n"
    done

    printf "==== result_count history =====\n"
    i=0
    for temp in ${result_count[@]}; do
        printf "result_count[$i] = ${temp}\n"
        let i++
    done

    average=`echo "scale=4; ${total} / ${i}" | bc`
    end_time=`date "+%Y-%m-%d %H:%M:%S"`

    printf "======== distribution ========\n"
    question_count=(0 0 0 0 0 0 0 0 0 0 0 0 0)
    for temp in ${result_count[@]}; do
        let question_count[${temp}]++
    done

    question_count_total=0
    for ((i=0; i < ${#question_count[@]}; i++)); do
        printf "${i} ... ${question_count[${i}]}\n"
        let question_count_total+=${question_count[${i}]}
    done
    printf "Distribution list total = $question_count_total\n"


    printf \
"==============================\n"\
"Total Questions = $total\n"\
"Total average   = $average\n"\
"==============================\n"\
"start ... $start_time\n"\
"end   ... $end_time\n"\
"total execution time ... $SECONDS[s]\n"

}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main $N $MAX
fi

