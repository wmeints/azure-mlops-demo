$ResourceGroup = $env:AZURE_ML_RESOURCE_GROUP
$WorkspaceName = $env:AZURE_ML_WORKSPACE

$components = @(
    "./components/fix_missing_values/fix_missing_values.yml"
    "./components/select_features/select_features.yml"
)

foreach($component in $components) {
    az ml component create -f $component -w $WorkspaceName -g $ResourceGroup
}
