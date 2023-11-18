# Day3 - Part1

function Get-BaseObject {
    param (
    )

    $baseObject = [PSCustomObject]@{
        Index = 0
        Value = 0
    }
    
}

function Get-ListObject {
    param (
        [string]$Line
    )
    
    
}

function Get-CoupleList {
    param (
        [array]$Lines
    )
    
    $coupleList = @()

    for ($i = 0; $i -lt $Lines.Count; $i += 3) {
        $couple = @()
        #TODO : Convert line i and i+1 to list object

        #TODO : Create a couple object and add it to couple list
    }

    #TODO : Return couple list
}

function Invoke-Part1 {
    param (
        [array]$Lines
    )
    
    #TODO : Get couple list
    $couplesList = Get-CoupleList -Lines $Lines

    #TODO : Compare each list and return index of correct couple

    #TODO : Return the sum of couple index


}



# EXECUTION ################################################################################
$filePath = ".\2022\13\input.txt"

$Lines = Get-Content -Path $filePath
$Result = Invoke-Part1 -Lines $Lines