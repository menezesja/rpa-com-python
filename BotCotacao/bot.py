from botcity.web import WebBot, Browser, By

from botcity.maestro import *
from botcity.web.browsers.firefox import default_options

from time import sleep

BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    bot = WebBot()

    # Configurando para rodar no modo headless
    bot.headless = False

    # Setando navegador padrão para o Firefox
    bot.browser = Browser.FIREFOX

    # Setando o caminho do WebDriver do Firefox
    bot.driver_path = r"resources\geckodriver.exe"

    # Abre a página inicial do Google
    bot.browse("https://www.google.com")

    #maximizar janela
    bot.driver.maximize_window()

    # Aguardando 2 segundos para garantir que a janela foi maximizada
    sleep(2)
    
    if not bot.find( "lupa", matching=0.97, waiting_time=10000):
        not_found("lupa")
    
    bot.paste("Cotação Dólar")
    bot.enter()
   
    # Aguardar a página carregar os resultados da pesquisa
    sleep(3)
    
    # Defina o XPath do elemento que você deseja obter o valor
    xpath = '/html/body/div[4]/div/div[12]/div/div[2]/div[2]/div/div/div[1]/div/block-component/div/div[1]/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[3]/div[1]/div[1]/div[2]/span[1]'
    
    # Encontre o elemento usando o XPath
    element = bot.driver.find_element(By.XPATH, xpath)
    
    # Obtenha o innerHTML do elemento
    inner_html = element.get_attribute('innerHTML')
    
    # Print o resultado
    print(f"Dólar => R$ {inner_html}")
 
    bot.wait(1000)
    bot.stop_browser()
    
if __name__ == '__main__':
    main()