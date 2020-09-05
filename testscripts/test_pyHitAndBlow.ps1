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
    $startTime = Get-Date
    $resultCount = @()
    $Total = 0

    for ($i = 0; $i -lt $MAX; $i++) {
        $AnswerNumber = (python ./create_random_n_digits_number.py $N)

    #   Clear-Host
        Write-Output "#------------------------------#" `
                     "# Running ... $(${i} + 1)/$MAX" `
                     "#------------------------------#"
        python $TargetPythonScript $N $EnablePrint $AnswerNumber
        $resultCount += $LASTEXITCODE

        $total += $resultCount[$resultCount.Length - 1]
        $average = ${total} / $resultCount.Length

        Write-Output "`n# Latest Average = $Average`n"
    }

    Write-Output "==== ResultCount history ====="
    for ($i = 0; $i -lt $resultCount.Length; $i++) {
        Write-Output "ResultCount[$i] = $($resultCount[$i])"
    }

    Write-Output "======== distribution ========"
    $questionCount = @(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    foreach ($temp in $resultCount) {
        $questionCount[$temp]++
    }

    $questionCountTotal = 0
    for ($i = 0; $i -lt $questionCount.Length; $i++) {
        Write-Output "$i ... $($questionCount[$i])"
        $questionCountTotal += $($questionCount[$i])
    }
    Write-Output "Distribution list Total = $questionCountTotal"

    $average = ${total} / $resultCount.Length
    $endTime = Get-Date

    Write-Output "==============================" `
                 "Total Questions = $total" `
                 "Total Average   = $average" `
                 "==============================" `
                 "start ... $($startTime.ToString('yyyy-MM-dd HH:mm:ss'))" `
                 "end   ... $($endTime.ToString('yyyy-MM-dd HH:mm:ss'))"

    Write-Output "Total execution time ... $(($endTime - $startTime).TotalSeconds)[s]"
}

main $N $MAX
