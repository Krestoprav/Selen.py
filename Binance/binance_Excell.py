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
import openpyxl


options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x935')


token='1688974578:AAH9ZxY2yMVGgIkOF-p-9VdQI9xYLrOwxGE'
bot = TeleBot(token, threaded=False)
my_ids= ['544023514', '214264530']

# ROI_1= ''
# PNL_1= ''
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

        book = openpyxl.open(r'C:\Binance\Binance.xlsx')
        print('Книга открыта')
        sheet = book.active

        if n==0:

            # ROI_1=ROI
            # PNL_1=PNL
            print(f"Текущие значения: "
                  f"\nЕжедневный ROI = {ROI} "
                  f"\nPNL по дням = {PNL}")

            for id in my_ids:
                bot.send_message(id, f"Текущие значения: "
                                     f"\nЕжедневный ROI = {ROI} "
                                     f"\nPNL по дням = {PNL}")
                time.sleep(5)

            sheet['A1']=ROI
            sheet['B1']=PNL

        else:


            if ROI!=sheet['A1'].value or PNL!=sheet['B1'].value:
                # ROI_1=ROI
                # PNL_1=PNL
                print(f"Изменение значений: "
                      f"\nЕжедневный ROI = {ROI} "
                      f"\nPNL по дням = {PNL}")
                for id in my_ids:
                    bot.send_message(id, f"Изменение значений: "
                                         f"\nЕжедневный ROI = {ROI} "
                                         f"\nPNL по дням = {PNL}")
                    time.sleep(5)

                print('Изменения отправлены')
                sheet['A1'] = ROI
                sheet['B1'] = PNL
                print('Переменные обновлены')

            else:
                print(f"Без изменений {str(datetime.now())} {ROI} {PNL}")

    except Exception:
        print('Ошибка!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        continue


    finally:
        book.save(r'C:\Binance\Binance.xlsx')
        print('Книга сохранена')
        book.close()
        print('Книга закрыта')
        try:
            browser.quit()  # Закрываем бразер
        except NameError:
            print('Браузер уже закрыт')
        else:
            print(f"Браузер остановлен {str(datetime.now())}")

    time.sleep(150)
    n+=1

