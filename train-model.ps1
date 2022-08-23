$ResourceGroup = $env:AZURE_ML_RESOURCE_GROUP
$WorkspaceName = $env:AZURE_ML_WORKSPACE

az ml job create --resource-group $ResourceGroup `
    --workspace-name $WorkspaceName --file ./pipelines/train_model.yml `
    --stream