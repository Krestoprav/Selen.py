import telebot
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
import pyautogui
import pyperclip
import numpy
import datetime
from datetime import timedelta, datetime
import sys
import os
import re
import shutil
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
import gspread  # импортируем gspread
from oauth2client.service_account import ServiceAccountCredentials  # ипортируем ServiceAccountCredentials
import pprint   # импортируем pprint
from pprint import PrettyPrinter
import pochta
from pochta import SingleTracker, BatchTracker, tracking
from zeep import CachingClient, Settings, helpers

# Блок запуска гугл таблицы
link = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']  # задаем ссылку на Гугл таблици
my_creds = ServiceAccountCredentials.from_json_keyfile_name('krestoprav-8e5f49dc5ebe.json',
                                                            link)  # формируем данные для входа из нашего json файла
client = gspread.authorize(my_creds)  # запускаем клиент для связи с таблицами

URL="https://docs.google.com/spreadsheets/d/1d7Qc8Do1MRM246ZmoTC5WW6D7uP0RbBnUy_ZoZzUvGI/edit#gid=715714864"
main = client.open_by_url(URL).worksheet('Ответы на форму (1)')  # открываем нужную нам таблицу и лист
statysi = client.open_by_url(URL).worksheet('Статусы')  # открываем нужную нам таблицу и лист

n=1  # Начаьная строка для поиска
x="+"
while main.cell(n, 1)!=None:
    a=main.cell(n, 4).value  # Проверяем нужный нам трек
    print(rf"Строка {n} {a}")

    while True:
        try:
            stroka=statysi.find(a, in_column=5).row  # Находим проверяемый трек в статусах
        except Exception:
            print("Не найден")
            x="-"
        else:
            x="+"
        break
    if x=="-":
        n+=1
        continue

    statys=statysi.cell(stroka, 3).value  # находим актуальный статус по данному треку

    main.update_cell(n, 2, statys)  # Вставляем актуальный статус
    print("Статус вставлен")

    x="+"
    n+=1
    time.sleep(10)







