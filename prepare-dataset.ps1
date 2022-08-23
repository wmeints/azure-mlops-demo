$ResourceGroup = $env:AZURE_ML_RESOURCE_GROUP
$WorkspaceName = $env:AZURE_ML_WORKSPACE

$Year = Get-Date -Format "yyyy"
$Month = Get-Date -Format "MM"
$Day = Get-Date -Format "dd"

$OutputPath = "azureml://datastores/workspaceblobstore/paths/wachttijden/prepared/$Year/$Month/$Day/wachttijden.csv"

Write-Host "OutputPath: $OutputPath"

az ml job create --resource-group $ResourceGroup `
    --workspace-name $WorkspaceName --file ./pipelines/prepare_dataset.yml `
    --set outputs.prepared_dataset.path=$OutputPath `
    --stream