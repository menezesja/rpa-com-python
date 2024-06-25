from botcity.web import WebBot, Browser, By
from botcity.maestro import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    try:
        maestro = BotMaestroSDK.from_sys_args()
        execution = maestro.get_execution()

        bot = WebBot()
        bot.headless = False

        # Setando Firefox
        bot.browser = Browser.FIREFOX

        bot.driver_path = r"resources\geckodriver.exe"

        maestro.alert(
        task_id=execution.task_id,
        title="BotYoutube - Inicio",
        message="Estamos iniciando o processo",
        alert_type=AlertType.INFO
        )
        
        canal = execution.parameters.get("canal", "pythonbrasiloficial")

        # Abrindo o navegador com o canal informado
        bot.browse(f"https://www.youtube.com/@{canal}")
        
        #maximizar janela
        bot.driver.maximize_window()
        
        # Faz a busca por ID
        elemento_inscritos = bot.find_element("subscriber-count", By.ID)

        # Se não encontrar, faz a busca por XPATH
        if not elemento_inscritos:
            elemento_inscritos = bot.find_element('//span[contains(text(), "inscritos")]', By.XPATH)

        inscritos = elemento_inscritos.text
        print(f"Inscritos => {inscritos}")

        status = AutomationTaskFinishStatus.SUCCESS
        message = "Tarefa BotYoutube finalizada com sucesso"

        # Forcando uma exception para registrarmos um erro
        x = 0/0

    except Exception as ex:
        # Salvando captura de tela do erro
        bot.save_screenshot("erro.png")

        # Dicionario de tags adicionais
        tags = {"canal": canal}

        # Registrando o erro
        maestro.error(
            task_id=execution.task_id,
            exception=ex,
            screenshot="erro.png",
            tags=tags
        )

        status = AutomationTaskFinishStatus.FAILED
        message = "Tarefa BotYoutube finalizada com falha"

    finally:
        bot.wait(2000)
        bot.stop_browser()

    maestro.finish_task(
        task_id=execution.task_id,
        status=AutomationTaskFinishStatus.SUCCESS,
        message="Tarefa BotYoutube finalizada com sucesso"
    )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
