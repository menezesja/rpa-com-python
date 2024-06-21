$exclude = @("venv", "BOT-SSL-CERT.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "BOT-SSL-CERT.zip" -Force