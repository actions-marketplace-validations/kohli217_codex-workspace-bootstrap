param(
    [switch]$UserInstall
)

$ErrorActionPreference = "Stop"

Write-Host "codex-workspace-bootstrap installer"
Write-Host "Checking Python..."

$python = $null
if (Get-Command py -ErrorAction SilentlyContinue) {
    $python = "py"
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    $python = "python"
} else {
    throw "Python was not found. Install Python 3.10 or later and run this script again."
}

& $python --version

$argsList = @("-m", "pip", "install")
if ($UserInstall) {
    $argsList += "--user"
}
$argsList += "git+https://github.com/kohli217/codex-workspace-bootstrap.git"

Write-Host "Installing from GitHub..."
& $python @argsList

if ($LASTEXITCODE -ne 0) {
    throw "pip installation failed with exit code $LASTEXITCODE"
}

Write-Host ""
Write-Host "Installation complete."
Write-Host "Try:"
Write-Host "  codex-workspace-bootstrap audit ."
