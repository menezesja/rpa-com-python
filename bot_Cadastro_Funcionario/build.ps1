$exclude = @("venv", "bot_Cadastro_Funcionario.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_Cadastro_Funcionario.zip" -Force