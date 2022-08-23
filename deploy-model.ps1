$ResourceGroup = $env:AZURE_ML_RESOURCE_GROUP
$WorkspaceName = $env:AZURE_ML_WORKSPACE

# Create the endpoint first.
az ml online-endpoint --file ./endpoints/wachttijden.yml --resource-group $ResourceGroup --workspace-name $WorkspaceName

# Then deploy the model.
az ml online-deployment create --resource-group $ResourceGroup `
    --workspace-name $WorkspaceName --file ./deployments/wachttijden.yml `
    --endpoint-name wachttijden