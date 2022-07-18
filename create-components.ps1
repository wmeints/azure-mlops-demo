$ResourceGroup = "rg-experiments-app-infra"
$WorkspaceName = "5kgyltzmf3tny"

$Components = get-childitem components/*/*.yml

foreach($Component in $Components) {
    az ml component create -f $Component.FullName -w $WorkspaceName -g $ResourceGroup
}