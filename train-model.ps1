$ResourceGroup = "rg-experiments-app-infra"
$WorkspaceName = "5kgyltzmf3tny"

az ml job create --resource-group $ResourceGroup `
    --workspace-name $WorkspaceName --file ./pipelines/train_model.yml `
    --stream