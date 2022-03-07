import telebot
from telebot import TeleBot
import os
from telebot import types
import os
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
import requests
from sys import path
path.insert(0, rf'C:\Users\User\Desktop\Python\Selenium\liveinform')
from Peremennie import IDVova, IDArtyr, IDArtyr2, IDGarik, Ishod_spis, \
    spis_xls, vichet_spis, del_files, copy_files, Obidinenie_excell, Vova, vigryzka, Stat, vigryzka_podchet, bot

# Словарь для времени
hour = {'23': ['Время вечерней выгрузки', 0],
        '10': ['Время утренней выгрузки', 1]
        }

papka = rf'C:\Users\User\Desktop\Kolim\Vikypi\Podchet_vrych_V2'

# Цикл работы кода
while True:
    print('Проверяю время ' + datetime.now().strftime('%H:%M:%S'))
    if datetime.now().strftime("%H")=="23" or datetime.now().strftime("%H")=="10":
        print(hour[datetime.now().strftime("%H")][0])  # вывод наименования выгрузки вечерняя/утренняя
        delta = hour[datetime.now().strftime("%H")][1]  # дельта текущего и нужного дня
        day = delta+1  # день выгрузки кол-ва и суммы выкупов

        """Проверка остатка на счете"""

        # bot = telebot.TeleBot(token, threaded=False)

        polychatels=['544023514', '252807089']

        response = requests.post('https://www.liveinform.ru/api/v2/balance/', params={'api_id': 'zJA7g2OU-PgP3lCdA-9xttIsDU-byeJ44xr'})

        a = response.text.split(',')[1].split(':')[1].replace('}', '')

        text = rf"Баланс на Liveinform : {a} руб. Выгрузить выкупы невозможно. Нужно пополнить баланс"

        if float(a) <= 0:
            print('Баланс на лайве недостаточный. Отправляю в телегу баланс лайва.')

            # Отправка сообщения о низком балансе
            while True:
                try:
                    # Цикл обхода списка получателей
                    for polychatel in polychatels:
                        bot.send_message(polychatel, text)  # отправка текста
                    print("Файл отправлен")

                except Exception as E:
                    print(rf"Ошибка при отправке текста {E.args}")
                    continue
                else:
                    break

            time.sleep(600)
            continue

        # Запускаем код
        while True:
            try:
                del_files(papka)
                # print(papka)
                # os.makedirs(papka)  # Создаем папку
                # file = open(rf'C:\Users\User\Desktop\Python\Vikypi\papka.txt', 'w',
                #             encoding='utf-8')  # открываем txt файл
                # file.write(papka)  # вписываем название папки в txt файл
                # file.close()  # закрываем txt файл

                vigryzka_podchet(Vova,  # Название словаря - имя пользователя
                                 (datetime.now() - timedelta(delta)).strftime("%d.%m.%Y"),  # Начало периода подсчета
                                 (datetime.now() - timedelta(delta)).strftime("%d.%m.%Y"),  # Конец периода подсчета
                                 papka,  # Папка для скачивания и дальнейше работы
                                 Stat['vikypi'],  # ссылку с нужным статус скачиваемых файлов (словарь)
                                 'txt_podchet',  # название ключа нужного текстового файла из словаря пользователя
                                 day)

                time.sleep(3600)

            except Exception as E:
                # browser.quit()
                print(rf'Ошибка при выгрузке {E.args}')
                continue
            else:
                break

    time.sleep(3000)

