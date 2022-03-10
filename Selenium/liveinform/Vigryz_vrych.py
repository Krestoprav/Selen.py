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
from PyQt5 import QtCore, QtGui, QtWidgets
from prog_ua import Ui_MainWindow
import os
import re
import shutil
import pandas as pd
import xlrd
import glob
import xlsxwriter
from Peremennie import IDVova, IDArtyr, IDArtyr2, IDGarik
import pyexcel as p
import openpyxl
import xlrd
import comtypes.client as cl
from collections import Counter
from sys import path
path.insert(0, rf'C:\Users\User\Desktop\Python\Selenium\liveinform')
from Peremennie import bot, token, my_id, id_vova


papka = r'C:\Users\User\Downloads\1'
papka_downloads= r'C:\Users\User\Downloads'

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x935')

n = 0


file = open('11.txt', 'r', encoding='utf-8')
nachaloPeriodaPodscheta = str(file.readline())
file.close()

file = open('22.txt', 'r', encoding='utf-8')
konecPeriodaPoscheta = str(file.readline())
file.close()

# nachaloPeriodaPodscheta = '01.01.2021'
# konecPeriodaPoscheta= (datetime.now()).strftime("%d.%m.%Y")
# konecPeriodaPoscheta= '31.05.2021'


name = rf'{papka}\Выкупы {nachaloPeriodaPodscheta}-{konecPeriodaPoscheta}.xlsx'


def Ishod_spis():
    global files1
    files1 = [item for item in glob.glob(papka_downloads + str('\*{}').format('.xls'))]
    if len(files1)>0:
        print("В папке уже лежат:")
        print(*files1, sep='\n')
    else:
        print("В папке файлов .xls нет\n")
    print("Исходный списко сформирован")


def copy_files():

    for file in files:
        file=file.replace(papka_downloads, '')
        os.replace(papka_downloads + file, papka + file)
    print("Файлы перенесены")


def del_files():  # Зачищаем папку "1"
    files_in_1=os.listdir(path=papka)
    if len(files_in_1)>0:
        for f in files_in_1:
            os.remove(rf'{papka}\{f}')
    print("Зачистил папку 1")


def vigryzka_Vova_vrych():
    browser = webdriver.Chrome(r'C:\Users\User\Desktop\Python\chromedriver.exe')
    browser.maximize_window()

    wait = WebDriverWait(browser, 20)

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
    n = 0
    summa_zakazov = 0
    kolichestvo_failov = 0

    file = open(r'C:\Users\User\Desktop\Python\Selenium\liveinform\Отчеты\Выгрузка врученных Вова.txt', 'a+', encoding='utf-8')
    file.write('\n ! \n')
    file.close()

    while n < len(IDVova):
        time.sleep(15)
        browser.get(rf'https://liveinform.ru/account/?multi={IDVova[n]}')
        nazvanie_proekta = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="frame"]/div[1]/div[2]'))).text
        browser.get(rf'https://liveinform.ru/account/archive?event[]=2&event_date[start]={nachaloPeriodaPodscheta}&event_date[end]={konecPeriodaPoscheta}&np=0&sort=date_desc&page=1&limit=100&return_status=10')

        try:
            kolichestvo_zakazov = int(wait.until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div[2]/div[1]/div/div/b'))).text)

        except Exception:
            text=f'{str(n+1)}. {IDVova[n]} {nazvanie_proekta} c {nachaloPeriodaPodscheta} по {konecPeriodaPoscheta} - 0 шт. количество файлов - {kolichestvo_failov}'
            print(text)
            file = open(r'C:\Users\User\Desktop\Python\Selenium\liveinform\Отчеты\Выгрузка врученных Вова.txt', 'a+', encoding='utf-8')
            file.write(text+'\n')
            file.close()
            n+=1
            continue
        else:
            wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'все результаты'))).click()
            time.sleep(10)
            kolichestvo_failov = int(kolichestvo_failov) + 1
            text=f'{str(n+1)}. {IDVova[n]} {nazvanie_proekta} c {nachaloPeriodaPodscheta} по {konecPeriodaPoscheta} - {str(kolichestvo_zakazov)} шт. количество файлов - {kolichestvo_failov}'
            print(text)
            file = open(r'C:\Users\User\Desktop\Python\Selenium\liveinform\Отчеты\Выгрузка врученных Вова.txt', 'a+', encoding='utf-8')
            file.write(text+'\n')
            file.close()

            summa_zakazov = summa_zakazov + kolichestvo_zakazov
            n+=1

    text = f'Всего вручено у Володи за период с {nachaloPeriodaPodscheta} по {konecPeriodaPoscheta} - {summa_zakazov} шт. \n' \
           f'Количество файлов -  {str(kolichestvo_failov)} шт.'
    print(text)

    file = open(r'C:\Users\User\Desktop\Python\Selenium\liveinform\Отчеты\Выгрузка врученных Вова.txt', 'a+',
                encoding='utf-8')
    file.write(text + '\n\n')
    file.close()

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frame"]/div[1]/div[6]/a/span'))).click()
    time.sleep(10)
    browser.quit()


def spis_xls():  # Получаем список файлов с раcширением .xls после выгрузки
    global files2
    files2 = [item for item in glob.glob(papka_downloads + str('\*{}').format('.xls'))]
    print("В папке лежат после скачивания:")
    print(*files2, sep='\n')


# Вычитаем из конечного списка файлов первичный
def vichet_spis():
    global files
    files = list((Counter(files2) - Counter(files1)).elements())
    print("Чистый список только скаченных файлов:")
    print(*files, sep='\n')


def Obidinenie_excell():

    combined = pd.DataFrame()
    files = [item for item in glob.glob(papka + str('\*{}').format('.xlsx'))]
    print(files)
    print(str(len(files))+' файлов в папке')

    for file in files:
        file = pd.read_excel(file)
        combined = pd.concat([combined, file])

    combined.to_excel(name)

    # Открываем полученную объединенную таблицу
    tab = openpyxl.load_workbook(name)

    # Открываем активную вкладку
    sheet = tab.active

    # Удаляем первую колонку
    sheet.delete_cols(1)

    # Переименовываем вкладку
    sheet.title = 'Лист'

    # Сохраняем и закрываем таблицу
    tab.save(name)
    tab.close()

    print('Файлы объединены')


# # Зачищаем папку "1"
# del_files()
#
# #  Получаем исходный список файлов с раcширением .xls
# Ishod_spis()
#
# # Выгружаем файлы из лайва
# vigryzka_Vova_vrych()
#
# #  Получаем список файлов с раcширением .xls после выгрузки
# spis_xls()
#
# # Вычитаем из конечного списка файлов первичный
# vichet_spis()
#
# # Переносим файлы в папку "1"
# copy_files()
#
#
# # Конвертируем файлы в папке 1 из xls в xlsx
# os.system(rf'C:\Users\User\Desktop\Python\BAT\Convert1.bat')
# print("Файлы конвертированы")
#
#
# # Объединяем файлы в один
# Obidinenie_excell()

# Отправляем файл в телегу

# bot.send_document(my_id, open(name, 'rb'))
# bot.send_document(id_vova, open(name, 'rb'))
# print("Файл отправлен")
