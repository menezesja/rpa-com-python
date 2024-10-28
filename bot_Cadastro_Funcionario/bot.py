from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

import os
import pandas as pd

load_dotenv()
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

BotMaestroSDK.RAISE_NOT_CONNECTED = False



def main():

    maestro = BotMaestroSDK.from_sys_args()

    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()
    bot.headless = False

    bot.browser = Browser.CHROME

    bot.driver_path = ChromeDriverManager().install()

    bot.browse("https://docs.google.com/forms/d/e/1FAIpQLSfDzqYUoNJMY09vo4o9NNmwWWzgoNHMX3on6wctH2z3rQkB1A/viewform")

    bot.driver.maximize_window()

    while len(bot.find_elements('/html/body/div[2]/div/div[2]/div[3]/div[2]/span/span', By.XPATH))<1:
        bot.wait(1000)
        print('carrengado.')

    bot.find_element('/html/body/div[2]/div/div[2]/div[3]/div[2]/span/span', By.XPATH).click()

    while len(bot.find_elements('//*[@id="identifierId"]', By.XPATH))<1:
        bot.wait(1000)
        print('carrengado.')
    
    bot.find_element('//*[@id="identifierId"]', By.XPATH).click()
    bot.paste(EMAIL)
    bot.enter()


    bot.wait(3000100000)

    bot.stop_browser()

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
