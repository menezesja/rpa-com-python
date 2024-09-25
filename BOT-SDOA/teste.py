from botcity.web import WebBot, By
from botcity.maestro import *
from time import sleep

import os
import shutil

BotMaestroSDK.RAISE_NOT_CONNECTED = False

# Função para criar um diretório se ele não existir
def criar_diretorio_se_nao_existir(diretorio):
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

# Função para mover arquivos de uma pasta para pastas específicas baseadas em extensão
def mover_arquivos_para_pasta(origem, destino_documentos, destino_imagens):
    for arquivo in os.listdir(origem):
        caminho_arquivo = os.path.join(origem, arquivo)
        
        if os.path.isfile(caminho_arquivo):
            if arquivo.endswith('.pdf'):
                shutil.move(caminho_arquivo, destino_documentos)
            elif arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                shutil.move(caminho_arquivo, destino_imagens)

def main():
    # Inicializa o Maestro e obtém os parâmetros da tarefa
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID: {execution.task_id}")
    print(f"Task Parameters: {execution.parameters}")

    # Configurações WebBot
    bot = WebBot()
    bot.headless = False
    bot.driver_path = 'resources\chromedriver.exe'
    bot.browse('https://unsplash.com/pt-br/')
   # bot.create_tab('https://www.google.com.br/')
    bot.driver.maximize_window()
    sleep(3)

    # XPath dos resultados
    xpath_primeiro_resultado = '//*[@id=":Rb5ue:"]/div/div/div[1]/div[1]/figure/div/div/a'
    btn_baixar = '//*[@id="app"]/div/div/dialog/div/div[4]/div[3]/div/div[1]/div[1]/header/div[2]/div/div/a'

    # Tenta clicar no primeiro resultado
    try:
        bot.driver.find_element(By.XPATH, xpath_primeiro_resultado).click()
        sleep(5)
    except Exception as e:
        print(f"Erro ao clicar no primeiro resultado: {e}")

    bot.driver.find_element(By.XPATH, btn_baixar).click()
    sleep(20)

    bot.type_right()
    sleep(2)
    bot.type_right()

    bot.driver.find_element(By.XPATH, btn_baixar).click()
    sleep(20)

    # Define os diretórios
    '''pasta_bot = os.path.dirname(os.path.abspath(__file__))
    pasta_documentos = os.path.join(pasta_bot, 'documentos')
    pasta_imagens = os.path.join(pasta_bot, 'imagens')

    # Cria os diretórios se não existirem
    criar_diretorio_se_nao_existir(pasta_documentos)
    criar_diretorio_se_nao_existir(pasta_imagens)

    # Move os arquivos baixados para as pastas corretas
    arquivos_restantes = mover_arquivos_para_pasta(pasta_bot, pasta_documentos, pasta_imagens)'''

    bot.wait(1000)
    bot.stop_browser()

if __name__ == '__main__':
    main()