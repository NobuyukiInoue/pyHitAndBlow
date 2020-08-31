param($MAX)

if (-Not $MAX) {
    $MAX = 10
}
else {
    if ($MAX -lt 1) {
        Write-Output "$MAX is invalid number."
        return
    }
}

function main() {
    $TargetPythonScript = "./pyHitAndBlow.py"
    $N = 4
    $EnablePrint = "false"

    $ResultCount = @()

    for ($i = 0; $i -lt $MAX; $i++) {
        $AnswerNumber = (python ./testscripts/create_random_n_digits_number.py)

    #   Clear-Host
        Write-Output "#------------------------------#" `
                     "# ($i/$MAX)" `
                     "#------------------------------#"
        python $TargetPythonScript $N $EnablePrint $AnswerNumber
        $ResultCount += $LASTEXITCODE
    }

    Write-Output "================================"
    $i = 0
    $TOTAL = 0

    for ($i = 0; $i -lt $ResultCount.Length; $i++) {
        Write-Output "ResultCount[$i] = $($ResultCount[$i])"
        $TOTAL += $ResultCount[$i]
    }

    $AVERAGE = ${TOTAL} / $ResultCount.Length

    Write-Output "================================"
    Write-Output "average = $AVERAGE"
    Write-Output "================================"
}

main
