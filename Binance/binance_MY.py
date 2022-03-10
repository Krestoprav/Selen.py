import telebot
from telebot import TeleBot
import os
from telebot import types
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
from time import sleep
import datetime
from datetime import timedelta, datetime


options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x935')


token='1619367152:AAHv8SLc2vt5mqI4o3QkKTn35Psx2t8p5yU'
bot = TeleBot(token, threaded=False)
id = '544023514'


ROI_1= ''
PNL_1= ''
n=0


while True:
    print("\n" f"{n} {str(datetime.now())}")
    try:

        print('Запускаю браузер')
        browser = webdriver.Chrome(r'C:\Binance\chromedriver.exe', options=options)
        browser.maximize_window()
        wait = WebDriverWait(browser, 30)
        print("Браузер запущен")

        browser.get(r'https://www.binance.com/ru/futures-activity/leaderboard/user?uid=91CDA0C27F7A387F7FDA5D0CA4781194&tradeType=PERPETUAL')
        time.sleep(15)
        ROI = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                         '//*[@id="__APP"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]'))).text
        PNL = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                         '//*[@id="__APP"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]'))).text


        if n==0:

            ROI_1=ROI
            PNL_1=PNL
            text = f"Текущие значения: "\
                   f"\nЕжедневный ROI = {ROI} "\
                   f"\nPNL по дням = {PNL}"
            print(text)

            bot.send_message(id, text)

        elif n//10==0:
            n=0
            ROI_1 = ''
            PNL_1 = ''

            continue

        else:

            if ROI!=ROI_1 or PNL!=PNL_1:
                ROI_1=ROI
                PNL_1=PNL
                text = f"Изменение значений: "\
                       f"\nЕжедневный ROI = {ROI} "\
                       f"\nPNL по дням = {PNL}"

                print(text)
                bot.send_message(id, text)
                bot.send_message('1619367152', text)


            else:
                print(f"Без изменений {str(datetime.now())} {ROI} {PNL}")

    except Exception:
        print(Exception)
        continue

    finally:
        try:
            browser.quit()  # Закрываем бразер
        except NameError:
            print('Браузер уже закрыт')
        else:
            print(f"Браузер остановлен {str(datetime.now())}")

    n+=1
    time.sleep(150)

