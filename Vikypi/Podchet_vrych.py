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
from sys import path
path.insert(0, rf'C:\Users\User\Desktop\Python\Selenium\liveinform')
from Peremennie import IDVova


token='1619367152:AAHv8SLc2vt5mqI4o3QkKTn35Psx2t8p5yU'

bot = telebot.TeleBot(token, threaded=False)
my_id= '544023514'
id_vova= '252807089'

# day='5'  # Номер дня с конца


options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x935')
options.add_argument('log-level=3')


def podschet_vrych():

    browser = webdriver.Chrome(r'C:\Users\User\Desktop\Python\Drivers\chromedriver.exe', options=options)
    browser.maximize_window()

    wait = WebDriverWait(browser, 30)

    browser.get('https://liveinform.ru/account')

    login = browser.find_element_by_xpath('//*[@id="enter-phone"]')
    login.click()  # нажимает войти
    login.send_keys('89050048682')  # вводит логин

    parol = browser.find_element_by_xpath('//*[@id="enter-password"]')
    parol.click()
    parol.send_keys('2129881196')  # вводит пароль

    enter = browser.find_element_by_xpath('//*[@id="enter-form"]/p[3]/button')
    enter.click()  # нажимает ввод
    time.sleep(10)
    browser.refresh()
    data = wait.until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="reportWeek"]/div/table/tbody/tr[{day}]/td[1]'))).text

    file = open(rf'C:\Users\User\Desktop\Python\Selenium\liveinform\Отчеты\Ежедневные вручения.txt', 'a+', encoding='utf-8')
    file.write(data + '\n')
    file.close()

    symm_kolvo_vrych=0
    symm_stoim_vrych=0


    for n in range(len(IDVova)):
        browser.get('https://liveinform.ru/account/?multi=' + IDVova[n])
        nazvanie_proekta = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="frame"]/div[1]/div[2]'))).text
        kolvo_vrych = wait.until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="reportWeek"]/div/table/tbody/tr[{day}]/td[4]/a'))).text
        # print(kolvo_vrych)

        if kolvo_vrych=='0 шт.':
            stoim_vrych = '0'
        else:
            stoim_vrych = wait.until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="reportWeek"]/div/table/tbody/tr[{day}]/td[4]/span'))).text

        # print(stoim_vrych)
        # print(type(stoim_vrych))

        kolvo_vrych_split = (kolvo_vrych.split(" "))
        kolvo_vrych_cif=int(kolvo_vrych_split[0])
        symm_kolvo_vrych+=kolvo_vrych_cif

        if stoim_vrych!='0':
            stoim_vrych_split = (stoim_vrych.split(" "))
            stoim_vrych_cif = int(stoim_vrych_split[0]+stoim_vrych_split[1])
            symm_stoim_vrych += stoim_vrych_cif

        print(str(n+1) + ". " + nazvanie_proekta + " " + data + " " + str(kolvo_vrych) + " на сумму " + str(stoim_vrych))
        # print(symm_kolvo_vrych)
        # print(symm_stoim_vrych)

        file = open(rf'C:\Users\User\Desktop\Python\Selenium\liveinform\Отчеты\Ежедневные вручения.txt', 'a+', encoding='utf-8')
        file.write(str(n+1) + ". " + nazvanie_proekta + " " + data + " " + str(kolvo_vrych) + " на сумму " + str(stoim_vrych) + "\n")
        file.close()

    print(data + " " + str(symm_kolvo_vrych) + " шт. на сумму " + str(symm_stoim_vrych) + " руб.\n\n")

    file = open(rf'C:\Users\User\Desktop\Python\Selenium\liveinform\Отчеты\Ежедневные вручения.txt', 'a+', encoding='utf-8')
    file.write(data + " " + str(symm_kolvo_vrych) + " шт. на сумму " + str(symm_stoim_vrych) + " руб.\n\n")
    file.close()

    while True:
        try:
            bot.send_message(my_id, data + " " + str(symm_kolvo_vrych) + " шт. на сумму " + str(symm_stoim_vrych) + " руб.")
            bot.send_message(id_vova, data + " " + str(symm_kolvo_vrych) + " шт. на сумму " + str(symm_stoim_vrych) + " руб.")
        except Exception:
            continue
        else:
            break

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frame"]/div[1]/div[6]/a/span'))).click()
    time.sleep(10)
    browser.quit()


while True:
    print('Проверяю время ' + datetime.now().strftime('%H:%M:%S'))
    if datetime.now().strftime("%H")=="23" or datetime.now().strftime("%H")=="10":
        if datetime.now().strftime("%H")=="23":
            print('Время вечерней выгрузки ')
            day = '1'  # Номер дня с конца
        elif datetime.now().strftime("%H")=="10":
            print('Время утренней выгрузки')
            day = '2'  # Номер дня с конца
        # while True:
        #     try:
        #         podschet_vrych()
        #         time.sleep(3600*10)
        #     except Exception:
        #         # browser.quit()
        #         print(Exception.args)
        #         continue
        #     else:
        #         break
        podschet_vrych()

        time.sleep(3600)

    time.sleep(3000)

