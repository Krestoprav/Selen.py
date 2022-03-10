import telebot
from telebot import TeleBot
import os
from telebot import types
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import datetime
from datetime import timedelta, datetime


token='1619367152:AAHv8SLc2vt5mqI4o3QkKTn35Psx2t8p5yU'

bot = TeleBot(token, threaded=False)
my_id= '544023514'

while True:

    # ua = dict(DesiredCapabilities.CHROME)
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x935')

    browser = webdriver.Chrome(r'C:\Users\User\Desktop\Python\Drivers\chromedriver.exe')
    browser.maximize_window()

    wait = WebDriverWait(browser, 30)

    try:

        # Выгружаем стоимость эфира
        browser.get(r'https://pokur.su/eth/rub/1/')
        c = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page"]/div/div[2]/article/header/div/div[1]/div/div/p'))).text
        print(c + datetime.now().strftime('%H:%M:%S'))

        # Выгружаем количество работающих ферм
        browser.get(r'https://ethermine.org/miners/634d5c770e48242ed838e3d1511fec48d9d2feb4/dashboard')

        # Количество работающийх ферм
        Workers_Active = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[4]/main/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[2]'))).text
        print(Workers_Active)

        # Текущий хэшрейт
        Current=wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[4]/main/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div/div[1]/div/div[2]'))).text
        print(Workers_Active + ' ферма в работе ' + Current + ' MH/s')

        # Вывод кошелька из криптонатора

        # browser.get('https://rf.cryptonator.com/auth/signin')
        #
        # login = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login"]')))
        # login.click()  # нажимает войти
        # login.send_keys('krestoprav@mail.ru')  # вводит логин
        #
        # parol = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="code"]')))
        # parol.click()
        # parol.send_keys('Derparol1@')  # вводит пароль
        #
        # enter = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="signinForm-submit"]')))
        # enter.click()  # нажимает ввод
        #
        # Ethereum = str(wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="currentaccounts"]/div/div[1]/div[2]/div/div[2]/div[1]/div/div[2]'))).text)
        # print(Ethereum)

        # Отправка полученных данных

        while True:
            try:
                # Отправляем стоимость эфира
                bot.send_message(my_id, c +" " + datetime.now().strftime('%H:%M:%S'))

                # # Отправляем информацию о работе фермы
                # if int(Workers_Active)<1:
                #     bot.send_message(my_id, 'Караул! Ферма остановилась')
                # else:
                #     bot.send_message(my_id, 'Средний хэшрейт ' + Current + ' MH/s')

                # Отправляем сколько эфира на кошельке
                # bot.send_message(my_id, Ethereum)

            except Exception:
                continue
            else:
                break

        # Закрываем браузер
        browser.quit()

    except Exception:
        browser.quit()
        time.sleep(300)
        continue
    else:
        # Спим час
        time.sleep(3600)







