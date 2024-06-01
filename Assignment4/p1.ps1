param( [string] $process )

$list = Get-Process $process -ErrorAction SilentlyContinue

if($list){
    Get-Process $process | Out-String | Write-Host 
    Stop-Process -Name $process

    #After Stop
    $newlist = Get-Process
    Write-Output $newlist 
}else{
    Write-Output "No such process is running."
}




