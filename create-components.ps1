$ResourceGroup = $env:AZURE_ML_RESOURCE_GROUP
$WorkspaceName = $env:AZURE_ML_WORKSPACE

$components = @(
    "./components/fix_missing_values"
    "./components/select_features"
)

foreach($component in $components) {
    az ml component create -f $component -w $WorkspaceName -g $ResourceGroup
}