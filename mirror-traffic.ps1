$ResourceGroup = "rg-experiments-app-infra"
$WorkspaceName = "5kgyltzmf3tny"

az ml online-endpoint update --name "wachttijden" --mirror-traffic "alternate-v1=50" --workspace-name $WorkspaceName --resource-group $ResourceGroup