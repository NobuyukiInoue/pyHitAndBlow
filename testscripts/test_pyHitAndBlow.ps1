param($N, $MAX)

if (-Not $N) {
    $N = 4
}
else {
    if (($N -lt 2) -Or ($N -gt 10)) {
        Write-Output "Give N between 2 and 10 inclusive."
        return
    }
}

if (-Not $MAX) {
    $MAX = 10
}
else {
    if ($MAX -lt 1) {
        Write-Output "$MAX is invalid number."
        return
    }
}

function main([int]$N, [int]$MAX) {
    $TargetPythonScript = "./pyHitAndBlow_offence.py"
    $EnablePrint = "false"

    $StartTime = Get-Date

    $ResultCount = @()
    $TOTAL = 0

    for ($i = 0; $i -lt $MAX; $i++) {
        $AnswerNumber = (python ./create_random_n_digits_number.py $N)

    #   Clear-Host
        Write-Output "#------------------------------#" `
                     "# Running ... $(${i} + 1)/$MAX" `
                     "#------------------------------#"
        python $TargetPythonScript $N $EnablePrint $AnswerNumber
        $ResultCount += $LASTEXITCODE

        $TOTAL += $ResultCount[$ResultCount.Length - 1]
        $AVERAGE = ${TOTAL} / $ResultCount.Length

        Write-Output "`n# Latest Average = $AVERAGE`n"
    }

    Write-Output "==== ResultCount history ====="

    for ($i = 0; $i -lt $ResultCount.Length; $i++) {
        Write-Output "ResultCount[$i] = $($ResultCount[$i])"
    }

    $AVERAGE = ${TOTAL} / $ResultCount.Length
    $EndTime = Get-Date

    Write-Output "==============================" `
                 "Total Average = $AVERAGE" `
                 "==============================" `
                 "start ... $($StartTime.ToString('yyyy-MM-dd HH:mm:ss'))" `
                 "end   ... $($EndTime.ToString('yyyy-MM-dd HH:mm:ss'))"

    Write-Output "Total execution time ... $(($EndTime - $StartTime).TotalSeconds)[s]"
}

main $N $MAX
