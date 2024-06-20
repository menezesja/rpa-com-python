$exclude = @("venv", "Lab_1.4_-_Desenvolvendo_automação_Desktop_com_IDs.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Lab_1.4_-_Desenvolvendo_automação_Desktop_com_IDs.zip" -Force