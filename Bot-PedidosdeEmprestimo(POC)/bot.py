from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from time import sleep

import pandas as pd


BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():

    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    file_path = r'resources\PedidosEmprestimo.xlsx'

    # Ler o arquivo Excel
    df = pd.read_excel(file_path, engine='openpyxl')

    # Exibir os dados
    #print(df)

    # Extrair dados específicos (exemplo)
    #for index, row in df.iterrows():
        #print(f"Linha {index}: {row.to_dict()}")

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.FIREFOX
    bot.driver_path = r"resources\geckodriver.exe"

    bot.browse("https://uibank.uipath.com/welcome")
    bot.driver.maximize_window()
    sleep(3)

    for _ in range(2):  # Rola a página 
        bot.page_down()
        sleep(1)
   
    #realiza clique no button "Apply For Laan"
    xpath = "/html/body/app-root/body/div/app-welcome-page/div[2]/div/div[3]/div/button"
    element = bot.driver.find_element(By.XPATH, xpath)
    element.click()

    sleep(2)
    
    #realiza clique no button "Apply For Laan"
    button_applyForLoan = bot.find_element("applyButton", By.ID)
    button_applyForLoan.click()
    
    for _ in range(1):  # Rola a página 
        bot.page_up()
        sleep(1)
    
   
def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()




