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
path.insert(0, rf'C:\Users\User\Desktop\Python\Selenium\liveinform')
from Peremennie import token, my_id, id_vova, IDVova

papka = r'C:\Users\User\Desktop\Kolim\BOT_vikypi'
papka_downloads= r'C:\Users\User\Downloads'


token = '5261255309:AAEw6fD8EbLk1TqK2Y50H9WXGs6XkkWPLQQ'
bot = telebot.TeleBot(token, threaded=False)

# Клавиатура
glavmeny = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
vigr_vrych = types.InlineKeyboardButton("Выгрузить выкупы")
PDF = types.InlineKeyboardButton("Обработать PDF")
glavmeny.add(vigr_vrych, PDF)

#  Переменные
nachaloPeriodaPodscheta = ''
konecPeriodaPoscheta= ''


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
    # try:
    #     sp.Popen('taskkill /im python.exe /f')
    # except Exception:
    #     print('python.exe не запущен')

    files_in_1=os.listdir(path=papka)
    if len(files_in_1)>0:
        for f in files_in_1:
            os.remove(rf'{papka}\{f}')
    print("Зачистил папку назначения")


def vigryzka_Vova_vrych():
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument('window-size=1920x935')
    prefs = {'download.default_directory': papka, 'profile.default_content_setting.popups': 0}
    options.add_experimental_option('prefs', prefs)

    browser = webdriver.Chrome(r'C:\Users\User\Desktop\Python\Drivers\chromedriver.exe', options=options)
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

        browser.get(rf'https://liveinform.ru/account/?multi={IDVova[n]}')
        nazvanie_proekta = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="frame"]/div[1]/div[2]'))).text
        browser.get(rf'https://liveinform.ru/account/archive?event[]=2&event_date[start]={nachaloPeriodaPodscheta}&event_date[end]={konecPeriodaPoscheta}&np=0&sort=date_desc&page=1&limit=100&return_status=10')

        wait = WebDriverWait(browser, 5)
        try:
            net_zakazov=wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="content"]/div[2]/div[2]/div[1]/div/div'), 'Заказов по данному запросу не найдено'))

        except Exception:
            pass
        else:
            text=f'{str(n+1)}. {IDVova[n]} {nazvanie_proekta} c {nachaloPeriodaPodscheta} по {konecPeriodaPoscheta} - 0 шт. количество файлов - {kolichestvo_failov} (нет заказов)'
            print(text)
            file = open(r'C:\Users\User\Desktop\Python\Selenium\liveinform\Отчеты\Выгрузка врученных Вова.txt', 'a+', encoding='utf-8')
            file.write(text+'\n')
            file.close()
            n+=1
            continue

        wait = WebDriverWait(browser, 10)

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
            kolichestvo_failov = int(kolichestvo_failov) + 1
            text=f'{str(n+1)}. {IDVova[n]} {nazvanie_proekta} c {nachaloPeriodaPodscheta} по {konecPeriodaPoscheta} - {str(kolichestvo_zakazov)} шт. количество файлов - {kolichestvo_failov}'
            print(text)
            file = open(r'C:\Users\User\Desktop\Python\Selenium\liveinform\Отчеты\Выгрузка врученных Вова.txt', 'a+', encoding='utf-8')
            file.write(text+'\n')
            file.close()

            summa_zakazov = summa_zakazov + kolichestvo_zakazov
            n+=1
            time.sleep(10)


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

    global name
    name=rf'{papka}\Выкупы {nachaloPeriodaPodscheta}-{konecPeriodaPoscheta}.xlsx'

    combined = pd.DataFrame()
    files = [item for item in glob.glob(papka + str('\*{}').format('.xlsx'))]
    print(files)
    print(str(len(files))+' файлов в папке')

    for file in files:
        file = pd.read_excel(file)
        combined = pd.concat([combined, file])

    combined.to_excel(rf'{papka}\Выкупы {nachaloPeriodaPodscheta}-{konecPeriodaPoscheta}.xlsx')

    # Открываем полученную объединенную таблицу
    tab = openpyxl.load_workbook(rf'{papka}\Выкупы {nachaloPeriodaPodscheta}-{konecPeriodaPoscheta}.xlsx')

    # Открываем активную вкладку
    sheet = tab.active

    # Удаляем первую колонку
    sheet.delete_cols(1)

    # Переименовываем вкладку
    sheet.title = 'Лист'

    # Сохраняем и закрываем таблицу
    tab.save(rf'{papka}\Выкупы {nachaloPeriodaPodscheta}-{konecPeriodaPoscheta}.xlsx')
    tab.close()

    print('Файлы объединены')




#Приветствие
@bot.message_handler(commands=["start"])
def welcome(message):
    sti = open('Bongyr.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Добрый день, {0.first_name}!\nКнопка внизу!".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=glavmeny)


#Реакция на кнопки

@bot.message_handler(content_types=['text', 'document', 'audio'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == "Выгрузить выкупы":
            bot.send_message(message.from_user.id, "Какая начальная дата? Введи в формате ДД.ММ.ГГГГ.")
            bot.register_next_step_handler(message, get_data_1)  # следующий шаг – функция get_name

        elif message.text == "Обработать PDF":
            bot.send_message(message.from_user.id, "Пришли файл")
            bot.register_next_step_handler(message, get_PDF)  # следующий шаг – функция get_name

        elif message.text == "Тест":
            bot.send_message(message.from_user.id, "Тест ЭХО")


        else:
            bot.send_message(message.chat.id, 'Непонятно! Выбирай из того что есть! Жми кнопку!')



def get_data_1(message):  # Получаем первую дату
    global nachaloPeriodaPodscheta
    nachaloPeriodaPodscheta = message.text
    # file = open(rf'C:\Users\User\Desktop\Python\BOT_выгрузка_врученных\11.txt', 'w', encoding='utf-8')
    # file.write(str(nachaloPeriodaPodscheta))
    # file.close()
    bot.send_message(message.from_user.id, 'Какая конечная дата? Введи в формате ДД.ММ.ГГГГ.')
    bot.register_next_step_handler(message, get_data_2)


def get_data_2(message):  # Получаем вторую дату
    global konecPeriodaPoscheta
    konecPeriodaPoscheta = message.text
    print(nachaloPeriodaPodscheta, konecPeriodaPoscheta)
    bot.send_message(message.from_user.id, 'Ожидай выгрузку')


    # # Получаем исходный список
    # Ishod_spis()

    # Выгружаем файлы из лайва
    bot.send_message(message.from_user.id, 'Приступаю к выгрузке из Лайва')

    # Зачищаем папку

    while True:
        try:
            del_files()
        except Exception:
            continue
        break

    vigryzka_Vova_vrych()

    for i in range(20):
        try:
            bot.send_message(message.from_user.id, 'Выгрузил из лайва')
        except Exception:
            continue
        break

    # #  Получаем список файлов с раcширением .xls после выгрузки
    # spis_xls()

    # for i in range(20):
    #     try:
    #         bot.send_message(message.from_user.id, 'Еще немного')
    #     except Exception:
    #         continue
    #     break

    # # Вычитаем из конечного списка файлов первичный
    # vichet_spis()

    # for i in range(20):
    #     try:
    #         bot.send_message(message.from_user.id, 'Еще чуть-чуть')
    #     except Exception:
    #         continue
    #     break


    # # Переносим файлы в папку "1"
    # copy_files()
    #
    # for i in range(20):
    #     try:
    #         bot.send_message(message.from_user.id, '80% готовности')
    #     except Exception:
    #         continue
    #     break

    # Конвертируем файлы в папке 1 из xls в xlsx
    os.system(rf'C:\Users\User\Desktop\Python\BAT\Convert_bot_vigryz.bat')
    print("Файлы конвертированы")

    for i in range(20):
        try:
            bot.send_message(message.from_user.id, '85% готовности')
        except Exception:
            continue
        break

    # Объединяем файлы в один
    Obidinenie_excell()


    for i in range(20):
        try:
            bot.send_message(message.from_user.id, 'Высылаю файл')
        except Exception:
            continue
        break

    # Высылаем файл в телегу
    while True:
        try:
            bot.send_document(my_id, open(name, 'rb'))
            bot.send_document(message.from_user.id, open(name, 'rb'))
        except Exception as G:
            text='Поймал ошибку при отправке'
            print(text)
            bot.send_message(my_id, rf'{text} {G.args}')
            print(G.args)
            time.sleep(5)
            continue
        break
    print("Файл отправлен")


def get_PDF(message):
    file_pdf = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_pdf.file_path)
    src = rf'C:\Users\User\Desktop\Python\Zamena\1.pdf'
          # + message.document.file_name
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)

    bot.reply_to(message, "Файл сохранен. Приступаю к обработке")
    time.sleep(2)
    # Начало обработки PDF

    os.system(rf'C:\Users\User\Desktop\Python\Zamena\Zamena.bat')

    # Печать
    pyautogui.write("Nalogki")
    pyautogui.press('enter')
    #
    #
    # time.sleep(20)
    # while True:
    #     try:
    #         bot.send_document(message.from_user.id, open(rf'C:\Users\User\Desktop\Python\Zamena\Nalogki', 'rb'))
    #     except Exception as Ex:
    #         print(Ex.args)
    #         time.sleep(30)
    #         continue
    #
    # bot.reply_to(message, "Файл отправлен")


# RUN
if __name__ == '__main__':
    while True:
        try:
          bot.polling(none_stop=True, interval=1, timeout=60)
          #   bot.polling(True)
        except Exception as E:
            time.sleep(15)
            print(E.args)
            # bot.send_message(my_id, rf'Ошибка в цикле bot.polling {E.args}')


