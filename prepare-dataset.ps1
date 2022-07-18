$ResourceGroup = "rg-experiments-app-infra"
$WorkspaceName = "5kgyltzmf3tny"

$Year = Get-Date -Format "yyyy"
$Month = Get-Date -Format "MM"
$Day = Get-Date -Format "dd"

$OutputPath = "azureml://datastores/workspaceblobstore/paths/wachttijden/prepared/$Year/$Month/$Day/wachttijden.csv"

Write-Host "OutputPath: $OutputPath"

az ml job create --resource-group $ResourceGroup `
    --workspace-name $WorkspaceName --file ./pipelines/prepare_dataset.yml `
    --set outputs.prepared_dataset.path=$OutputPath `
    --stream