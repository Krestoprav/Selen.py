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
from zeep import CachingClient, Settings, helpers
import openpyxl
from openpyxl import Workbook, load_workbook, formatting

slovar_fio = {'Антонова Олеся А.': 'Антонову Олесю Альфировну',
              'Яшина Екатерина М.': 'Яшину Екатерину Михайловну',
              'Рудак Вячеслав Евгеньевич': 'Рудака Вячеслава Евгеньевича',
              'Савенков Руслан Анатольевич': 'Савенкова Руслана Анатольевича',
              'Шишкин Денис Владимирович': 'Шишкина Дениса Владимировича',
              'Нигматуллин Ильдар И.': 'Нигматуллина Ильдара Ильгамовича',
              'Шишкина Жанна В.': 'Шишкину Жанну Владимировну'
              }

f_name = r'C:\Users\User\Desktop\kolim\Розыск наложек\Список.xlsx'

def FIO():
    #  Открываем файл с заявлением и списком
    zaiavlenie = load_workbook(f_name)
    sheet_zaiavlenie = zaiavlenie.active  # Открываем вкладку со списком
    print('Заявление и список открыты')
    #  Блока запуска браузера

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x935')

    browser = webdriver.Chrome(r'C:\Users\User\Desktop\Python\chromedriver.exe')
    browser.maximize_window()
    wait = WebDriverWait(browser, 30)

    # Первая строка в таблицу, с которой начинается обход (чтение из файла)
    file = open('1.txt', 'r', encoding='utf-8')
    n=int(file.readline())
    file.close()

    # Цикл обхода строк вкладки, пока первый столбец не пустой
    while str(sheet_zaiavlenie[fr'A{n}'].value) != 'None':

        track = sheet_zaiavlenie[fr'D{n}'].value  # Получаем номер трека
        # Если столбец с треком не пустой то заполняем отправителя
        if str(track) != 'None':
            print(rf"{n} заполняем {track}")

            browser.get(rf"https://www.pochta.ru/tracking#{str(track)}")  # Вводим трек в почту России
            browser.refresh()

            # Получаем ФИО отправителя
            # Цикл обхода ошибки при получении ФИО из почты России. Не более 3 раз.

            for i in range(3):
                try:
                    FIO = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tracking-card-portal"]/div[4]/div[2]'))).text
                except Exception:
                    print("Ошибка почты России")
                    # В случае ошибки перезапускаем браузер и снова открываем страницу с треком
                    browser.quit()
                    browser = webdriver.Chrome(r'C:\Users\User\Desktop\Python\chromedriver.exe', options=options)
                    browser.maximize_window()
                    wait = WebDriverWait(browser, 30)
                    browser.get(rf"https://www.pochta.ru/tracking#{str(track)}")  # Вводим трек в почту России
                    browser.refresh()
                    FIO="Ошибка"
                    continue
                break

            # Если по итогу обхода цикла ФИО не получилось вытащить, то идем в следующую строку
            if FIO=="Ошибка":
                print("Ошибка почты России, пропускаем")
                n+=1
                file = open('1.txt', 'w', encoding='utf-8')
                file.write(str(n))
                file.close()
                continue

            # Цикл обхода ошибки при форматировании
            for i in range(2):
                print(rf"{FIO} на итерации № {i}")
                try:
                    FIO = str(FIO).split(":")[1]  # Форматируем имя отправителя
                except Exception:
                    if i==0:
                        FIO = wait.until(EC.visibility_of_element_located(
                        (By.XPATH, '//*[@id="page-tracking"]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[2]'))).text
                        continue
                    if i==1:
                        print("Ошибка при форматрировании")
                        FIO = "Ошибка"
                break


            # Если по итогу обхода цикла ФИО не получилось отформатировать, то идем в следующую строку
            if FIO=="Ошибка":
                n+=1
                file = open('1.txt', 'w', encoding='utf-8')
                file.write(str(n))
                file.close()
                continue

            FIO=slovar_fio[FIO]

            # Вставляем ФИО в таблицу
            sheet_zaiavlenie[rf'E{n}']=FIO


            browser.refresh()  # Еще раз обновляем браузер

        else:
            print(rf"{n} пропускаем")
            time.sleep(2)

        # Завершение петли
        n+=1
        file = open('1.txt', 'w', encoding='utf-8')
        file.write(str(n))
        file.close()


    browser.quit()  # Закрываем браузер по окончанию цикла
    print("Список закончился")

    #  Сохраняем файл
    zaiavlenie.save(f_name)

    # Прописываем начальную строку в файл для начала следующего цикла
    file = open('1.txt', 'w', encoding='utf-8')
    file.write(str(2))
    file.close()


FIO()

