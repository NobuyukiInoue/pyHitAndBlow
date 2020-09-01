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

    $ResultCount = @()

    for ($i = 0; $i -lt $MAX; $i++) {
        $AnswerNumber = (python ./create_random_n_digits_number.py $N)

    #   Clear-Host
        Write-Output "#------------------------------#" `
                     "# Running ... ($i/$MAX)" `
                     "#------------------------------#"
        python $TargetPythonScript $N $EnablePrint $AnswerNumber
        $ResultCount += $LASTEXITCODE
    }

    Write-Output "==== ResultCount history ====="
    $i = 0
    $TOTAL = 0

    for ($i = 0; $i -lt $ResultCount.Length; $i++) {
        Write-Output "ResultCount[$i] = $($ResultCount[$i])"
        $TOTAL += $ResultCount[$i]
    }

    $AVERAGE = ${TOTAL} / $ResultCount.Length

    Write-Output "=============================="
    Write-Output "average = $AVERAGE"
    Write-Output "=============================="
}

main $N $MAX
