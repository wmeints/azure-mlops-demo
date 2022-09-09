$ResourceGroup = $env:AZURE_ML_RESOURCE_GROUP
$WorkspaceName = $env:AZURE_ML_WORKSPACE

az ml data create --file ./data/wachttijden_raw.yml --resource-group $ResourceGroup --workspace $WorkspaceName
