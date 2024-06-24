from botcity.web import WebBot, Browser, By
from botcity.maestro import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    bot = WebBot()
    bot.headless = False

    # Setando Firefox
    bot.browser = Browser.FIREFOX

    bot.driver_path = r"resources\geckodriver.exe"
    
    # Abre o canal da Python Brasil no YouTube
    bot.browse("https://www.youtube.com/@pythonbrasiloficial")
    
    #maximizar janela
    bot.driver.maximize_window()
    
    # Faz a busca por ID
    elemento_inscritos = bot.find_element("subscriber-count", By.ID)

    # Se não encontrar, faz a busca por XPATH
    if not elemento_inscritos:
        elemento_inscritos = bot.find_element('//span[contains(text(), "inscritos")]', By.XPATH)

    inscritos = elemento_inscritos.text
    print(f"Inscritos => {inscritos}")

    bot.wait(3000)
    bot.stop_browser()


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
