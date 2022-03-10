import telebot
from telebot import TeleBot
from telebot import types
import glob
import telebot
import os
from telebot import apihelper
from telebot import types
from telebot import TeleBot
from telebot import types
import time
import random
from sys import path
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
import pandas as pd
import xlrd
import glob
import xlsxwriter
import pyexcel as p
import openpyxl
import xlrd
import comtypes.client as cl
from collections import Counter
import subprocess as sp
import pyautogui
from sys import path

IDVova = ['15310', '15045', '15977', '15976', '15450', '15973', '15972', '15084', '15698', '15504',
          '15555', '16229', '11828', '15975', '15974', '15448', '15971', '15970', '12625', '15983',
          '15982', '15939', '15940', '15969', '14358', '15981', '15980', '13142', '15979', '15978',
          '15700', '15968', '15584', '16677', '16678', '16178', '16209', '16089', '16090', '13994',
          '16210', '16213', '16212', '16359', '16360', '16398', '16397', '16416', '16417', '16418',
          '16419', '16469', '16470', '16568', '16567', '16565', '16566', '16585', '16586', '16588',
          '16587', '16604', '16603', '16606', '16605', '16646', '16647', '16690', '16691', '16771',
          '16770', '16785', '16786', '16842', '16841', '16820', '16819', '17007', '17006']

# Словарь с параметрами Володи
Vova={'login': '89050048682',
      'parol': '2129881196',
      'ID': IDVova,
      'txt_all': rf'C:\Users\User\Desktop\Python\Selenium\liveinform\Отчеты\Выгрузка Вова.txt',
      'txt_vigryz_vrych': rf'C:\Users\User\Desktop\Python\Selenium\liveinform\Отчеты\Выгрузка врученных Вова.txt',
      'txt_podchet': rf'C:\Users\User\Desktop\Python\Selenium\liveinform\Отчеты\Ежедневные вручения.txt',
      'telegram_id': '252807089'
      }

# Словарь со ссылками на страницу в лайве с нужными фильтрами
Stat={'all': [rf"https://liveinform.ru/account/archive?add[start]=", "&add[end]=", "np=0&sort=date_desc&page=1&limit=100&return_status=10"],
      'vikypi': [rf"https://liveinform.ru/account/archive?event[]=2&event_date[start]=", "&event_date[end]=", "&np=0&sort=date_desc&page=1&limit=100&return_status=10"]
      }

IDArtyr = ['11375', '10195', '14914', '13749', '10199', '15088', '12068', '15715', '15138', '15089',
           '15087', '11579', '10757', '10197', '10192', '10196', '11915', '10193', '13748', '15557',
           '15599']

IDArtyr2 = ['15995', '14395', '15994', '14398', '15989', '14390', '16000', '15999', '15998', '15959',
            '15997', '15958', '15991', '14391', '14393', '16189', '15992', '14392', '15993', '15957',
            '15996', '14396', '15990', '14394', '16003', '15960', '16325', '16324', '16373', '16374',
            '16005', '15963', '16451', '16450', '16455', '16454', '16449', '16448', '16453', '16452',
            '16427', '16426', '16456', '16457', '16460', '16461', '16458', '16459', '16638', '16639',
            '16695', '16694', '16712', '16711', '16714', '16713', '16739', '16776', '16778', '16777',
            '16839', '16838', '16857', '16856', '16861', '16860', '16859', '16858', '16866', '16865',
            '16875', '16874', '16899', '16898', '16897', '16896', '16980', '16979']

IDGarik = ['10621', '11397', '14292', '13689', '16078', '16552', '16700']


token = '1619367152:AAHv8SLc2vt5mqI4o3QkKTn35Psx2t8p5yU'
bot = telebot.TeleBot(token, threaded=False)
my_id = '544023514'
id_vova = '252807089'


papka = r'C:\Users\User\Downloads\1'
papka_downloads= r'C:\Users\User\Downloads'


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


def del_files(folder):  # Зачищаем папку "1"
    files_in_1=os.listdir(path=folder)
    if len(files_in_1)>0:
        for f in files_in_1:
            os.remove(rf'{folder}\{f}')
    print(rf"Зачистил папку {folder}")


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




def Obidinenie_excell(folder, nachaloPeriodaPodscheta, konecPeriodaPoscheta):

    combined = pd.DataFrame()
    files = [item for item in glob.glob(folder + str('\*{}').format('.xlsx'))]
    print(files)
    print(rf"{len(files)} файлов в папке {folder}")

    for file in files:
        file = pd.read_excel(file)
        combined = pd.concat([combined, file])

    name = rf'{papka}\Выкупы {nachaloPeriodaPodscheta}-{konecPeriodaPoscheta}.xlsx'
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


def vigryzka(user,  # Название словаря - имя пользователя
             nachaloPeriodaPodscheta,  # Начало периода подсчета
             konecPeriodaPoscheta,  # Конец периода подсчета
             download_directory,  # Папка для скачивания и дальнейше работы
             stat,  # ссылку с нужным статус скачиваемых файлов (словарь)
             txt_file):  # название ключа нужного текстового файла из словаря пользователя

    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument('window-size=1920x935')
    prefs = {'download.default_directory': download_directory, 'profile.default_content_setting.popups': 0}
    options.add_experimental_option('prefs', prefs)

    browser = webdriver.Chrome(r'C:\Users\User\Desktop\Python\Drivers\chromedriver.exe', options=options)
    browser.maximize_window()

    wait = WebDriverWait(browser, 15)

    browser.get('https://liveinform.ru/account')

    login = browser.find_element_by_xpath('//*[@id="enter-phone"]')
    login.click()  # нажимает войти
    login.send_keys(user['login'])  # вводит логин

    parol = browser.find_element_by_xpath('//*[@id="enter-password"]')
    parol.click()
    parol.send_keys(user['parol'])  # вводит пароль

    enter = browser.find_element_by_xpath('//*[@id="enter-form"]/p[3]/button')
    enter.click()  # нажимает ввод
    time.sleep(10)
    browser.refresh()
    n = 0
    summa_zakazov = 0
    kolichestvo_failov = 0

    file = open(user[txt_file], 'a+', encoding='utf-8')
    file.write('\n ! \n')

    for ID in user['ID']:
        browser.get(rf'https://liveinform.ru/account/?multi={ID}')
        nazvanie_proekta = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="frame"]/div[1]/div[2]'))).text
        browser.get(stat[0]+nachaloPeriodaPodscheta+stat[1]+konecPeriodaPoscheta+stat[2])

        wait = WebDriverWait(browser, 5)
        try:
            net_zakazov=wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="content"]/div[2]/div[2]/div[1]/div/div'), 'Заказов по данному запросу не найдено'))

        except Exception as E:
            pass
        else:
            text=f'{str(n+1)}. {ID} {nazvanie_proekta} c {nachaloPeriodaPodscheta} по {konecPeriodaPoscheta} - 0 шт. количество файлов - {kolichestvo_failov} (нет заказов)'
            print(text)
            file.write(text+'\n')
            n+=1
            continue
        wait = WebDriverWait(browser, 15)

        try:
            kolichestvo_zakazov = int(wait.until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div[2]/div[1]/div/div/b'))).text)

        except Exception:
            text=rf'{str(n + 1)}. {ID} {nazvanie_proekta} с {nachaloPeriodaPodscheta} по {konecPeriodaPoscheta} 0 шт. количество файлов - {kolichestvo_failov} '
            print(text)
            file.write(text+'\n')
            n = n + 1
            continue
        else:
            wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'все результаты'))).click()
            time.sleep(15)
            kolichestvo_failov = int(kolichestvo_failov) + 1
            text=rf'{str(n + 1)}. {ID} {nazvanie_proekta} с {nachaloPeriodaPodscheta} по {konecPeriodaPoscheta} - {str(kolichestvo_zakazov)} шт. количество файлов - {kolichestvo_failov} '
            print(text)

            file.write(text+'\n')

            summa_zakazov = summa_zakazov + kolichestvo_zakazov
            n+=1

    text=rf'Всего заказов у Володи за период с {nachaloPeriodaPodscheta} по {konecPeriodaPoscheta} - {summa_zakazov} шт.'
    print(text)
    file.write(text +'\n')

    text=rf'Количество файлов - {str(kolichestvo_failov)} шт.'
    print(text)
    file.write(rf'Количество файлов - {str(kolichestvo_failov)}шт.'+'\n')
    file.close()

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frame"]/div[1]/div[6]/a/span'))).click()
    time.sleep(10)
    browser.quit()

    # Конвертируем файлы в папке из xls в xlsx
    os.system(rf'C:\Users\User\Desktop\Python\BAT\Convert1.bat')
    print("Файлы конвертированы")


def vigryzka_podchet(user,  # Название словаря - имя пользователя
             nachaloPeriodaPodscheta,  # Начало периода подсчета
             konecPeriodaPoscheta,  # Конец периода подсчета
             download_directory,  # Папка для скачивания и дальнейше работы
             stat,  # ссылку с нужным статус скачиваемых файлов (словарь)
             txt_file,  # название ключа нужного текстового файла из словаря пользователя
             day):  # номер дня с конца

    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument('window-size=1920x935')
    prefs = {'download.default_directory': download_directory, 'profile.default_content_setting.popups': 0}
    options.add_experimental_option('prefs', prefs)

    browser = webdriver.Chrome(r'C:\Users\User\Desktop\Python\Drivers\chromedriver.exe', options=options)
    browser.maximize_window()

    wait = WebDriverWait(browser, 15)

    browser.get('https://liveinform.ru/account')

    login = browser.find_element_by_xpath('//*[@id="enter-phone"]')
    login.click()  # нажимает войти
    login.send_keys(user['login'])  # вводит логин

    parol = browser.find_element_by_xpath('//*[@id="enter-password"]')
    parol.click()
    parol.send_keys(user['parol'])  # вводит пароль

    enter = browser.find_element_by_xpath('//*[@id="enter-form"]/p[3]/button')
    enter.click()  # нажимает ввод
    time.sleep(10)
    browser.refresh()
    data = wait.until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="reportWeek"]/div/table/tbody/tr[{day}]/td[1]'))).text

    n = 0
    summa_zakazov = 0
    kolichestvo_failov = 0
    symm_kolvo_vrych=0
    symm_stoim_vrych=0

    file = open(user[txt_file], 'a+', encoding='utf-8')
    file.write('\n ! \n')


    while n < len(user['ID']):

    # for ID in user['ID']:

        ID=user['ID'][n]
        browser.get(rf'https://liveinform.ru/account/?multi={ID}')
        nazvanie_proekta = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="frame"]/div[1]/div[2]'))).text

        kolvo_vrych = wait.until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="reportWeek"]/div/table/tbody/tr[{day}]/td[4]/a'))).text
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

        file.write(str(n+1) + ". " + nazvanie_proekta + " " + data + " " + str(kolvo_vrych) + " на сумму " + str(stoim_vrych) + "\n")

        # Начало скачивания
        browser.get(stat[0]+nachaloPeriodaPodscheta+stat[1]+konecPeriodaPoscheta+stat[2])

        wait = WebDriverWait(browser, 5)
        try:
            net_zakazov=wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="content"]/div[2]/div[2]/div[1]/div/div'), 'Заказов по данному запросу не найдено'))

        except Exception:
            pass
        else:
            text=f'{str(n+1)}. {ID} {nazvanie_proekta} c {nachaloPeriodaPodscheta} по {konecPeriodaPoscheta} - 0 шт. количество файлов - {kolichestvo_failov} (нет заказов)'
            print(text)
            file.write(text+'\n')
            n+=1
            continue
        wait = WebDriverWait(browser, 60)

        try:
            kolichestvo_zakazov = int(wait.until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div[2]/div[1]/div/div/b'))).text)
            if int(kolichestvo_zakazov) != int(kolvo_vrych_cif):
                print(r"Количество выкупов не бьется -  ВЫГРУЖАЕМ ЭТОТ ID СНОВА!!!")
                continue
        except Exception:
            text=rf'{str(n + 1)}. {ID} {nazvanie_proekta} с {nachaloPeriodaPodscheta} по {konecPeriodaPoscheta} 0 шт. количество файлов - {kolichestvo_failov} '
            print(text)
            file.write(text+'\n')
            n = n + 1
            continue
        else:
            wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'все результаты'))).click()
            time.sleep(15)
            kolichestvo_failov = int(kolichestvo_failov) + 1
            text=rf'{str(n + 1)}. {ID} {nazvanie_proekta} с {nachaloPeriodaPodscheta} по {konecPeriodaPoscheta} - {str(kolichestvo_zakazov)} шт. количество файлов - {kolichestvo_failov} '
            print(text)

            file.write(text+'\n')

            summa_zakazov = summa_zakazov + kolichestvo_zakazov
            n = n + 1


    print(data + " " + str(symm_kolvo_vrych) + " шт. на сумму " + str(symm_stoim_vrych) + " руб.\n\n")

    file.write(data + " " + str(symm_kolvo_vrych) + " шт. на сумму " + str(symm_stoim_vrych) + " руб.\n\n")

    text=rf'Всего выкупов у Володи за период с {nachaloPeriodaPodscheta} по {konecPeriodaPoscheta} - {summa_zakazov} шт.'
    print(text)
    file.write(text +'\n')

    text=rf'Количество файлов - {str(kolichestvo_failov)} шт.'
    print(text)
    file.write(rf'Количество файлов - {str(kolichestvo_failov)}шт.'+'\n')
    file.close()

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frame"]/div[1]/div[6]/a/span'))).click()
    time.sleep(10)
    browser.quit()

    # Конвертируем файлы в папке из xls в xlsx
    os.system(rf'C:\Users\User\Desktop\Python\Vikypi\Convert.bat')
    #
    # os.system(rf'C:\Users\User\Desktop\Python\Vikypi\xls_to_xlsx.bat')
    print("Файлы конвертированы")


    # Объединение файлов
    combined = pd.DataFrame()
    files = [item for item in glob.glob(download_directory + str('\*{}').format('.xlsx'))]
    print(files)
    print(rf"{len(files)} файлов в папке {download_directory}")

    for file in files:
        file = pd.read_excel(file)
        combined = pd.concat([combined, file])

    name = rf'{download_directory}\Выкупы {nachaloPeriodaPodscheta}-{konecPeriodaPoscheta}.xlsx'
    combined.to_excel(name)

    # Открываем полученную объединенную таблицу
    tab = openpyxl.load_workbook(name)

    # Открываем активную вкладку
    sheet = tab.active

    # Удаляем первую колонку
    sheet.delete_cols(1)

    # Переименовываем вкладку
    sheet.title = 'Лист'

    # Сохраняем таблицу
    tab.save(name)

    print('Файлы объединены')

    # Блок фильтрации файла со всеми выкупами
    m=2
    while str(sheet[f'A{m}'].value) != 'None':
        print(f'Обрабатываем {m} строку')
        #  Если индекс 140079 и 101000, удаляем строку
        if sheet[f'U{m}'].value == 140079 or sheet[f'U{m}'].value == 101000:
            print(f"Удаляем")
            sheet.delete_rows(m)
            continue
        m+=1

    fail_index_name=rf"{name.replace('.xlsx', '')} неверные индексы.xlsx"  # имя для отфильтрованного файла
    tab.save(fail_index_name)  # Сохраняем отфильтрованный файл

    # Закрываем таблицу
    tab.close()


    # Списокв с получателями
    polychatels= [my_id, user['telegram_id']]
    # polychatels= [my_id]

    # Отправка готового файла
    while True:
        try:
            # Формирование текста для отправки
            text = rf"{data} {str(symm_kolvo_vrych)} шт. на сумму {str(symm_stoim_vrych)} руб."
            # Цикл обхода списка получателей
            for polychatel in polychatels:
                bot.send_message(polychatel, text)  # отправка текста
                bot.send_document(polychatel, open(name, 'rb'))  # отправка со всеми выкупами
                bot.send_document(polychatel, open(fail_index_name, 'rb'))  # отправка отфильтрованного файла
            print("Файл отправлен")
        except Exception as E:
            print(rf"Ошибка при отправке текста и файла {E.args}")
            continue
        else:
            break
