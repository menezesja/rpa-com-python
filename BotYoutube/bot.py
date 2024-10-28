from botcity.web import WebBot, Browser
from botcity.maestro import *
from datetime import datetime

BotMaestroSDK.RAISE_NOT_CONNECTED = False

from webdriver_manager.chrome import ChromeDriverManager

def main():
    try:
        maestro = BotMaestroSDK.from_sys_args()
        execution = maestro.get_execution()

        bot = WebBot()
        bot.headless = False

        # Definindo o navegador Chrome
        bot.browser = Browser.CHROME
        bot.driver_path = ChromeDriverManager().install()

        test = execution.parameters.get("test")

        # Alerta de início
        maestro.alert(
            task_id=execution.task_id,
            title="BotYoutube - Início",
            message="Iniciando o processo",
            alert_type=AlertType.INFO
        )
    
        bot.browse("https://www.youtube.com/pythonbrasiloficial")
        bot.driver.maximize_window()

        # Espera 3 segundos para garantir que a página carregue
        bot.wait(3000)

        status = AutomationTaskFinishStatus.SUCCESS
        message = "Tarefa BotYoutube finalizada com sucesso"

        bot.save_screenshot("resultado.png")

    except Exception as ex:
        # Salvando captura de tela do erro
        bot.save_screenshot("erro.png")

        # Registrando o erro
        maestro.error(
            task_id=execution.task_id,
            exception=ex,
            screenshot="erro.png",
        )

        status = AutomationTaskFinishStatus.FAILED
        message = "Tarefa BotYoutube finalizada com falha"

    finally:
        bot.wait(2000)
        bot.stop_browser()

        canal = "pythonbrasiloficial"

        maestro.new_log_entry(
            activity_label="botyoutube",
            values = {
                "data_hora": datetime.now().strftime("%Y-%m-%d_%H-%M"),
                "canal": canal
            }
        )

        maestro.post_artifact(
            task_id=execution.task_id,
            artifact_name=f"result-{test}.png",
            filepath="resultado.png"
        )

        # Finalizando a tarefa no Maestro
        maestro.finish_task(
            task_id=execution.task_id,
            status=status,
            message=message
        )

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
