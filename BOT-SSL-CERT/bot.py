from botcity.web import WebBot, Browser
from botcity.maestro import *
from botcity.web.browsers.firefox import default_options

BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.FIREFOX
    bot.driver_path = r"resources\geckodriver.exe"

    # Caminho para a pasta com o certificado
    certificate_db_path = r"cert"

    # Obtendo opcoes padrão com pasta do banco de dados NSS, como pasta de usuario do navegador
    options = default_options(
        headless=bot.headless,
        user_data_dir=certificate_db_path
    )

    # Configurando as opções no navegador
    bot.options = options

    # Website de teste de certificado badssl.com.
    bot.browse("https://client.badssl.com/")

    # Aguardando 5 segundos antes de encerrar
    bot.sleep(5000)

    # Encerrando e liberando recursos
    bot.stop_browser()

   

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
