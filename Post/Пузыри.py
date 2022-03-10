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

while True:

    # Ссылки на таблицы
    link_sheets = [
                   'https://docs.google.com/spreadsheets/d/1pfzsB7fltwHyxdLyKnsK6YDNA2ffPU0LWq4SyI3Zgx8/edit#gid=754079130',
                   'https://docs.google.com/spreadsheets/d/1V8_RdqLsLwPAS_pNlOBQHCEa3pRf_lraTbhp7yEpqCs/edit#gid=3406987'

                   ]

    # Название таблиц
    name_sheets = [
                   '3. Fugicar FC8 (vladimirsuslov1988@gmail.com) новая корзина'

                   ]
    vkladki = ['Статусы',
               'Статусы'

               ]

    # Номер строки, с которой начнется работа в таблице
    stroki=[
            1,
            1
            ]

    for s in range(len(link_sheets)):  # цикл по обходу таблиц

        print("\nОбработка таблицы " + name_sheets[s])
        # Раздел API почты
        tracking = SingleTracker('YhdmWXIsTUCtVT', '19IvLEmsRkN5')  # Треккинг Володя
        # tracking = SingleTracker('HRixxqSeEHLqWu', 'nH5sLTOCmpnn')  # Треккинг Олег

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x935')

        link = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']   # задаем ссылку на Гугл таблици
        my_creds = ServiceAccountCredentials.from_json_keyfile_name('krestoprav-8e5f49dc5ebe.json', link) #формируем данные для входа из нашего json файла
        client = gspread.authorize(my_creds)    # запускаем клиент для связи с таблицами
        sheet = client.open_by_url(link_sheets[s]).worksheet('Статусы')   # открываем нужную нам таблицу и лист

        n = stroki[s]  # Номер строки с которой таблица начнет работать
        pysto = 0  # начальное количество пустых строк
        z=0 # Количество повторных запросов трека на сайте почты

        # Начало цикла по заполнению таблицы
        while pysto<5:
            try:  # Обарачиваем весь цикл работы с одиним проектом в try

                # Печатает номер строки, сколько было пустых подрад и время
                print('\nСтрока №' + str(n) + ' Пустых подряд ' + str(pysto) + " " + name_sheets[s] + " " +
                      str(datetime.now()))

                # Читаем номер трека с строке
                try:
                    track=str(sheet.cell(n, 5).value)
                    print('Номер трека ' + track)
                except Exception:
                    print("Слишком много обращений к таблице ждем таймаут")
                    time.sleep(60)
                    continue

                # Читаем статус в строке
                try:
                    statys=str(sheet.cell(n, 4).value)
                    print("Текущий статус - " + str(statys))
                except Exception:
                    print("Слишком много обращений к таблице ждем таймаут")
                    time.sleep(60)
                    continue

                #  Если строка полностью пустая
                if str(track)=='None' and str(statys)=='None':
                    print("Пустая строка")
                    pysto+=1
                    n+=1
                    continue

                # Если уже стоит статус возврат
                if statys.find('Возврат') != -1:
                    print("Пропускаем")
                    pysto = 0
                    n+=1
                    time.sleep(2)
                    continue

                # Если стоит стутус оплата получена с верным индексом
                if statys.find('Оплата получена') != -1:
                    if statys.find('101000') != -1 or statys.find('125957') != -1 \
                            or statys.find('125955') != -1 or statys.find('143900') != -1:
                        print("Пропускаем")
                        pysto = 0
                        n+=1
                        time.sleep(2)
                        continue

                # Проверям ячейка с номером трека пустая или текст. Нужно что бы было число
                try:
                    track=int(track)
                except TypeError:
                    print('Ячейка с треком в строке №' + str(n) + ' пустая')
                    x=sheet.cell(n, 3).value
                    sheet.update_cell(n, 4, x)
                    n+=1
                    pysto=0
                    time.sleep(2)
                    continue

                except ValueError:
                    if str(track)=='None':
                        print('Ячейка с треком в строке №' + str(n) + ' пустая')
                    else:
                        print('Ячейка с треком в строке №' + str(n) + ' текст')
                    x=sheet.cell(n, 3).value
                    time.sleep(2)
                    if str(sheet.cell(n, 4).value)=='None' and str(sheet.cell(n, 3).value)!=str(sheet.cell(n, 4).value):
                        sheet.update_cell(n, 4, x)
                    n+=1
                    # if str(x)=='None' and str(track)=='None':
                    #     pysto+=1
                    if str(track)=='None':
                        if x.find('Подтвержден') != -1 or str(x)=='None':
                            pysto+=1
                    else:
                        pysto = 0
                    time.sleep(2)
                    continue

                except Exception:
                    print('Exception')
                    k = 'ON'
                    x = sheet.cell(n, 3).value
                    sheet.update_cell(n, 4, x)
                    n += 1
                    pysto = 0
                    time.sleep(2)
                    continue


                # # Если нет трека
                # if str(track)=='None':
                #     if str(sheet.cell(n, 3).value).find('чс')!=-1 and \
                #             str(sheet.cell(n, 4).value).find('чс')==-1:
                #         time.sleep(2)
                #         sheet.update_cell(n, 4, 'чс')
                #         print("Обновленный статус - чс")
                #     elif str(sheet.cell(n, 4).value).find('чс')!=-1:
                #         print("Пропускаем")
                #     elif str(sheet.cell(n, 3).value).find('Подтвержден')!=-1 and \
                #             str(sheet.cell(n, 4).value).find('Подтвержден')==-1:
                #         time.sleep(2)
                #         sheet.update_cell(n, 4, 'Подтвержден')
                #         print("Обновленный статус - Подтвержден")
                #     elif str(sheet.cell(n, 4).value).find('Подтвержден')!=-1:
                #         print("Пропускаем")
                #     n+= 1
                #     pysto = 0
                #     time.sleep(2)
                #     continue
                # Запуск браузера при необходимости

                try:
                    assert browser.session_id
                    print(browser.session_id)
                except Exception:
                    print('Запускаю браузер')
                    browser = webdriver.Chrome(r'C:\Users\User\Desktop\Python\chromedriver.exe',
                                               options=options)
                    browser.maximize_window()
                    wait = WebDriverWait(browser, 30)

                # Открываем страницу почты россии с текущим треком
                time.sleep(3)

                try:
                    browser.get('https://www.pochta.ru/tracking#' + str(track))
                except Exception:
                    try:
                        browser.quit()  # Закрываем бразер
                        print("Браузер остановлен")
                    except NameError:
                        print('Браузер уже закрыт')

                    print("Перезапускаю браузер")
                    browser = webdriver.Chrome(r'C:\Users\User\Desktop\Python\chromedriver.exe',
                                               options=options)
                    browser.maximize_window()
                    wait = WebDriverWait(browser, 30)
                    continue

                try:
                    time.sleep(3)
                    browser.refresh()
                    #  Достаем все события из сайта
                    a= wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-tracking"]/div/div[2]/div/div[2]/div[2]/div'))).text
                    #  Достаем последнее событие из сайта
                    c= wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-tracking"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]'))).text
                    a=str(a)
                    c=str(c)
                except Exception:
                    browser.quit()
                    z+=1
                    print('Не заработал ' + str(track) + ' ' + str(z) + ' раз')
                    if z>2:
                        print(str(track)+' не заработал более 2 раз. Пропускаем его')
                        n+=1
                        z=0 # Обнуляем счетчик несработок браузера

                    continue

                # Блок с оценкой полученного статуса с почты России
                # Если статус "Выплачен"
                if a.find('выплачен') != -1:
                    if a.find('101000') != -1 and c.find('101000') != -1:
                        a = 'Оплата получена 101000'
                    elif a.find('125957') != -1 and c.find('125957') != -1:
                        a = 'Оплата получена 125957'
                    elif a.find('125955') != -1 and c.find('125955') != -1:
                        a = 'Оплата получена 125955'
                    elif a.find('143900') != -1 and c.find('143900') != -1:
                        a = 'Оплата получена 143900'
                    else:
                        a='Выплачен получателю'

                    # Получаем дату выплаты
                    try:
                        EventDateTime = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-tracking"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/span[2]'))).text
                    except Exception:
                        print("Дата не выгрузилась из сайта почты России")
                    else:
                        # Проставляем дату выплаты в таблицу
                        sheet.update_cell(n, 9, EventDateTime)

                # Если выкупили, но непонятно где наложка
                elif a.find('Почтовый перевод') != -1 and \
                        a.find('принят') != -1 and \
                        a.find('Получено адресатом') != -1 and a.find('101000') == -1:
                    t_statys=str(sheet.cell(n, 4))
                    if t_statys.find('101000') != -1 or t_statys.find('125957') != -1 or \
                            t_statys.find('125955') != -1 or t_statys.find('143900') != -1:
                        n+=1
                        continue
                    else:
                        a='Выкуплен1'

                elif \
                        a.find('Получено адресатом') != -1 and \
                        a.find('101000') == -1:
                    t_statys=str(sheet.cell(n, 4))
                    if t_statys.find('101000') != -1 or t_statys.find('125957') != -1 or \
                            t_statys.find('125955') != -1 or t_statys.find('143900') != -1:
                        n+=1
                        continue
                    else:
                        a='Выкуплен1'

                # Если возврат
                elif \
                        a.find('возврат') != -1 or \
                        a.find('Выслано обратно отправителю') != -1 or \
                        a.find('Получено отправителем') != -1 or \
                        a.find('Отправление ожидает в отделении 143900') != -1 or \
                        a.find('Отправление ожидает в отделении 101000') != -1 or \
                        a.find('Отправление ожидает в отделении 141020') != -1 or \
                        a.find('Отправление ожидает в отделении 143913') != -1:
                    a = 'Возврат'

                # Если доставлено получателю
                elif \
                        a.find('Отправление ожидает в отделении') != -1 and \
                        a.find('Выслано обратно отправителю') == -1:
                    a = 'Доставлен'


                # Если еще в пути
                else:
                    a='Отправлен'

                # Заходим в API если выкуплен
                if a=='Выкуплен' or a=='Выкуплен1' or a=='Выкуплен1 ':

                    try:
                        viplata = tracking.get_order_events_for_mail(str(track))
                        print(viplata)
                    except TypeError:
                        print('Нет данныйх о выплате')
                    except Exception:
                        print("Дневной лимит API закончен")
                        # tracking = SingleTracker('YhdmWXIsTUCtVT', '19IvLEmsRkN5')  # Треккинг Володя
                    else:
                        try:
                            print((viplata[-1]['EventName']) + ' ' + str(viplata[-1]['EventDateTime']) + ' ' + str(
                                viplata[-1]['IndexTo']))
                            if str(viplata[-1]['IndexTo']).find('143900')!=-1 or\
                                    str(viplata[-1]['IndexTo']).find('101000')!=-1 or \
                                    str(viplata[-1]['IndexTo']).find('141020')!=-1 or \
                                    str(viplata[-1]['IndexTo']).find('143913')!=-1 or \
                                    str(viplata[-1]['IndexTo']).find('125957')!=-1 or \
                                    str(viplata[-1]['IndexTo']).find('125955')!=-1:
                                a = 'Выкуплен'
                            else:
                                a = 'Выкуплен1'
                            a=a+' '+str(viplata[-1]['IndexTo'])
                            sheet.update_cell(n, 9, str(viplata[-1]['EventDateTime']))
                        except Exception:
                            print('Нет данныйх о выплате')
                            a = 'Выкуплен1'

                # Печатаем новый статус
                print("Обновленный статус - "+a)

                sheet.update_cell(n, 4, a) # Вносим статус в таблицу

                n+=1 # на одну строку дальше
                k='ON' # браузер включен
                pysto = 0 # пустых подряд ноль

            except Exception:
                print("Общая ошибка ")
                continue

        try:
            browser.quit()  # Закрываем бразер
            print("Браузер остановлен")
        except NameError:
            print('Браузер уже закрыт')

        browser = webdriver.Chrome(r'C:\Users\User\Desktop\Python\chromedriver.exe', options=options)
        browser.maximize_window()
        wait = WebDriverWait(browser, 30)
        print("Браузер запущен после остановки")
