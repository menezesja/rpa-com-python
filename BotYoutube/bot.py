from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from datetime import datetime

BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    try:
        maestro = BotMaestroSDK.from_sys_args()
        execution = maestro.get_execution()

        bot = WebBot()
        bot.headless = True

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
        bot.browse(f"https://www.youtube.com/@{canal}")
        bot.driver.maximize_window()
        
        # Faz a busca por ID
        elemento_inscritos = bot.find_element("subscriber-count", By.ID)

        # Coletando o conteúdo de texto do elemento
        inscritos = elemento_inscritos.text

        # Printando os dados coletados
        print(f"Inscritos => {inscritos}")

        status = AutomationTaskFinishStatus.SUCCESS
        message = "Tarefa BotYoutube finalizada com sucesso"

        # Salvando uma captura de tela
        bot.save_screenshot("captura.png")

        # Enviando para a plataforma com o nome "Captura Canal..."
        maestro.post_artifact(
            task_id=execution.task_id,
            artifact_name=f"Captura Canal {canal}.png",
            filepath="captura.png"
        )

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
        
        maestro.new_log_entry(
            activity_label="EstatisticasYoutub",
            values = {
                "data_hora": datetime.now().strftime("%Y-%m-%d_%H-%M"),
                "canal": canal,
                "inscritos": inscritos
            }
        )

        maestro.finish_task(
            task_id=execution.task_id,
            status=status,
            message=message
        )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
