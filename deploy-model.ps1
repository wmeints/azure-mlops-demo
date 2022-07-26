$ResourceGroup = "rg-experiments-app-infra"
$WorkspaceName = "5kgyltzmf3tny"

az ml online-deployment create --resource-group $ResourceGroup `
    --workspace-name $WorkspaceName --file ./deployments/wachttijden.yml `
    --endpoint-name wachttijden