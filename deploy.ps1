param(
  [string]$RemoteUrl = ""
)

Set-Location -Path (Split-Path -Parent $MyInvocation.MyCommand.Definition)
if (-not (Test-Path .git)) {
  git init
}

git add .
try {
  git commit -m "Deploy: update site"
} catch {
  Write-Host "Keine Änderungen zum Committen."
}

if ($RemoteUrl -ne "") {
  git remote remove origin -ErrorAction SilentlyContinue
  git remote add origin $RemoteUrl
  git branch -M main
  git push -u origin main
} else {
  Write-Host "Kein Remote angegeben. Beispiel: ./deploy.ps1 -RemoteUrl 'https://github.com/USER/REPO.git'"
}