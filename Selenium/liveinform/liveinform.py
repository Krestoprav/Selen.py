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
import openpyxl

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x935')

n = 0
# nachaloPeriodaPodscheta = str('01.' + (datetime.now()).strftime("%m.%Y"))
nachaloPeriodaPodscheta = '01.02.2022'
konecPeriodaPoscheta= '28.02.2022'



def parVova():
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


def parArtyr():
    browser.get('https://liveinform.ru/account')

    login = browser.find_element_by_xpath('//*[@id="enter-phone"]')
    login.click()  # нажимает войти
    login.send_keys('79057604761')  # вводит логин

    parol = browser.find_element_by_xpath('//*[@id="enter-password"]')
    parol.click()
    parol.send_keys('IkxBYkvL')  # вводит пароль

    enter = browser.find_element_by_xpath('//*[@id="enter-form"]/p[3]/button')
    enter.click()  # нажимает ввод
    time.sleep(10)
    browser.refresh()


def vihod():
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frame"]/div[1]/div[6]/a/span'))).click()


def vigryzka_Vova():
    browser = webdriver.Chrome(r'C:\Users\User\Desktop\Python\Drivers\chromedriver.exe')
    browser.maximize_window()
    delta = 100

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
    n = 0
    summa_zakazov = 0
    kolichestvo_failov = 0

    file = open('Выгрузка Вова.txt', 'a+', encoding='utf-8')
    file.write('\n ! \n')
    file.close()

    while n < len(IDVova):
        time.sleep(15)
        browser.get(''.join(('https://liveinform.ru/account/?multi=', IDVova[n])))
        nazvanie_proekta = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="frame"]/div[1]/div[2]'))).text
        browser.get(''.join(('https://liveinform.ru/account/archive?add[start]=',
                             (datetime.now() - timedelta(delta)).strftime("%d.%m.%Y"), '&add[end]=',
                             (datetime.now()).strftime("%d.%m.%Y"),
                             '&np=0&sort=date_desc&page=1&limit=100&return_status=10')))

        try:
            kolichestvo_zakazov = int(wait.until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div[2]/div[1]/div/div/b'))).text)

        except Exception:
            print(str(n + 1) + '. ' + IDVova[n] + ' ' + nazvanie_proekta + ' с ' + (
                        datetime.now() - timedelta(delta)).strftime("%d.%m.%Y") + ' по ' + (datetime.now()).strftime(
                "%d.%m.%Y") + ' - 0 шт.')
            file = open('Выгрузка Вова.txt', 'a+', encoding='utf-8')
            file.write(str(n + 1) + '. ' + IDVova[n] + ' ' + nazvanie_proekta + ' с ' + (
                        datetime.now() - timedelta(delta)).strftime("%d.%m.%Y") + ' по ' + (datetime.now()).strftime(
                "%d.%m.%Y") + ' - 0 шт.\n')
            file.close()
            n = n + 1
            continue
        else:
            wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'все результаты'))).click()
            time.sleep(10)
            print(str(n + 1) + '. ' + IDVova[n] + ' ' + nazvanie_proekta + ' с ' + (
                        datetime.now() - timedelta(delta)).strftime("%d.%m.%Y") + ' по ' + (datetime.now()).strftime(
                "%d.%m.%Y") + ' - ' + str(kolichestvo_zakazov) + ' шт.')

            file = open('Выгрузка Вова.txt', 'a+', encoding='utf-8')
            file.write(str(n + 1) + '. ' + IDVova[n] + ' ' + nazvanie_proekta + ' с ' + (
                        datetime.now() - timedelta(delta)).strftime("%d.%m.%Y") + ' по ' + (datetime.now()).strftime(
                "%d.%m.%Y") + ' - ' + str(kolichestvo_zakazov) + ' шт.\n')
            file.close()

            summa_zakazov = summa_zakazov + kolichestvo_zakazov
            kolichestvo_failov = int(kolichestvo_failov) + 1
            n = n + 1

    print('Всего заказов у Володи за период ', 'с', (datetime.now() - timedelta(delta)).strftime("%d.%m.%Y"), 'по',
          (datetime.now()).strftime("%d.%m.%Y"), ' - ', summa_zakazov, ' шт.')
    print('Количество файлов - ' + str(kolichestvo_failov) + ' шт.')

    file = open('Выгрузка Вова.txt', 'a+', encoding='utf-8')
    file.write(
        'Всего заказов у Володи за период ' + 'с ' + (datetime.now() - timedelta(62)).strftime("%d.%m.%Y") + ' по ' + (
            datetime.now()).strftime("%d.%m.%Y") + ' - ' + str(summa_zakazov) + ' шт.\n')
    file.write('Количество файлов - ' + str(kolichestvo_failov) + ' шт.\n\n')
    file.close()

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frame"]/div[1]/div[6]/a/span'))).click()
    time.sleep(10)
    browser.quit()


def vigryzka_Artyr():
    browser = webdriver.Chrome(r'C:\Users\User\Desktop\Python\chromedriver.exe')
    browser.maximize_window()
    wait = WebDriverWait(browser, 30)

    browser.get('https://liveinform.ru/account')

    login = browser.find_element_by_xpath('//*[@id="enter-phone"]')
    login.click()  # нажимает войти
    login.send_keys('79057604761')  # вводит логин

    parol = browser.find_element_by_xpath('//*[@id="enter-password"]')
    parol.click()
    parol.send_keys('Israelyan00793')  # вводит пароль

    enter = browser.find_element_by_xpath('//*[@id="enter-form"]/p[3]/button')
    enter.click()  # нажимает ввод
    time.sleep(10)
    browser.refresh()
    n = 0
    summa_zakazov = 0
    kolichestvo_failov = 0

    file = open('Выгрузка Артур.txt', 'a+', encoding='utf-8')
    file.write('! \n')
    file.close()

    while n < len(IDArtyr):
        time.sleep(15)
        browser.get(''.join(('https://liveinform.ru/account/?multi=', IDArtyr[n])))
        nazvanie_proekta = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="frame"]/div[1]/div[2]'))).text
        browser.get(''.join(('https://liveinform.ru/account/archive?add[start]=',
                             (datetime.now() - timedelta(93)).strftime("%d.%m.%Y"), '&add[end]=',
                             (datetime.now()).strftime("%d.%m.%Y"),
                             '&np=0&sort=date_desc&page=1&limit=100&return_status=10')))
        try:
            kolichestvo_zakazov = int(wait.until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div[2]/div[1]/div/div/b'))).text)
        except Exception:
            print(str(n + 1) + '. ' + IDArtyr[n] + ' ' + nazvanie_proekta + ' с ' + (
                        datetime.now() - timedelta(93)).strftime("%d.%m.%Y") + ' по ' + (datetime.now()).strftime(
                "%d.%m.%Y") + ' - 0 шт.')
            file = open('Выгрузка Артур.txt', 'a+', encoding='utf-8')
            file.write(str(n + 1) + '. ' + IDArtyr[n] + ' ' + nazvanie_proekta + ' с ' + (
                        datetime.now() - timedelta(93)).strftime("%d.%m.%Y") + ' по ' + (datetime.now()).strftime(
                "%d.%m.%Y") + ' - 0 шт.\n')
            file.close()
            n = n + 1
            continue

        else:
            wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'все результаты'))).click()
            time.sleep(10)
            print(str(n + 1) + '. ' + IDArtyr[n] + ' ' + nazvanie_proekta + ' с ' + (
                        datetime.now() - timedelta(93)).strftime("%d.%m.%Y") + ' по ' + (datetime.now()).strftime(
                "%d.%m.%Y") + ' - ' + str(kolichestvo_zakazov) + ' шт.')

            file = open('Выгрузка Артур.txt', 'a+', encoding='utf-8')
            file.write(str(n + 1) + '. ' + IDArtyr[n] + ' ' + nazvanie_proekta + ' с ' + (
                        datetime.now() - timedelta(93)).strftime("%d.%m.%Y") + ' по ' + (datetime.now()).strftime(
                "%d.%m.%Y") + ' - ' + str(kolichestvo_zakazov) + ' шт.\n')
            file.close()

            summa_zakazov = summa_zakazov + kolichestvo_zakazov
            kolichestvo_failov = int(kolichestvo_failov) + 1
            n = n + 1

    print('Всего заказов у Артура за период ', 'с ', (datetime.now() - timedelta(93)).strftime("%d.%m.%Y"), 'по ',
          (datetime.now()).strftime("%d.%m.%Y"), ' - ', summa_zakazov, ' шт.')
    print('Количество файлов - ' + str(kolichestvo_failov) + ' шт.')

    file = open('Выгрузка Артур.txt', 'a+', encoding='utf-8')
    file.write(
        'Всего заказов у Артура за период ' + 'с ' + (datetime.now() - timedelta(93)).strftime("%d.%m.%Y") + 'по ' + (
            datetime.now()).strftime("%d.%m.%Y") + ' - ' + str(summa_zakazov) + ' шт.\n')
    file.write('Количество файлов - ' + str(kolichestvo_failov) + ' шт.\n')
    file.close()

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frame"]/div[1]/div[6]/a/span'))).click()
    time.sleep(10)
    browser.quit()


def vigryzka_Artyr2():
    browser = webdriver.Chrome(r'C:\Users\User\Desktop\Python\Drivers\chromedriver.exe')
    browser.maximize_window()
    wait = WebDriverWait(browser, 15)

    delta=105

    browser.get('https://liveinform.ru/account')

    login = browser.find_element_by_xpath('//*[@id="enter-phone"]')
    login.click()  # нажимает войти
    login.send_keys('79104901675')  # вводит логин

    parol = browser.find_element_by_xpath('//*[@id="enter-password"]')
    parol.click()
    parol.send_keys('Israelyan00793')  # вводит пароль

    enter = browser.find_element_by_xpath('//*[@id="enter-form"]/p[3]/button')
    enter.click()  # нажимает ввод
    time.sleep(10)
    browser.refresh()
    n = 0
    summa_zakazov = 0
    kolichestvo_failov = 0
    file = open('Выгрузка Артур 2.txt', 'a+', encoding='utf-8')
    file.write('! \n')
    file.close()
    while n < len(IDArtyr2):
        browser.get(''.join(('https://liveinform.ru/account/?multi=', IDArtyr2[n])))
        nazvanie_proekta = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="frame"]/div[1]/div[2]'))).text
        browser.get(''.join(('https://liveinform.ru/account/archive?add[start]=',
                             (datetime.now() - timedelta(delta)).strftime("%d.%m.%Y"), '&add[end]=',
                             (datetime.now()).strftime("%d.%m.%Y"),
                             '&np=0&sort=date_desc&page=1&limit=100&return_status=10')))
        try:
            kolichestvo_zakazov = int(wait.until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div[2]/div[1]/div/div/b'))).text)
        except Exception:
            print(str(n + 1) + '. ' + IDArtyr2[n] + ' ' + nazvanie_proekta + ' с ' + (
                        datetime.now() - timedelta(delta)).strftime("%d.%m.%Y") + ' по ' + (datetime.now()).strftime(
                "%d.%m.%Y") + ' - 0 шт. количество файлов - ' + str(kolichestvo_failov))
            file = open('Выгрузка Артур 2.txt', 'a+', encoding='utf-8')
            file.write(str(n + 1) + '. ' + IDArtyr2[n] + ' ' + nazvanie_proekta + ' с ' + (
                        datetime.now() - timedelta(delta)).strftime("%d.%m.%Y") + ' по ' + (datetime.now()).strftime(
                "%d.%m.%Y") + ' - 0 шт. количество файлов - ' + str(kolichestvo_failov) + '\n')
            file.close()
            n = n + 1
            continue

        else:
            wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'все результаты'))).click()
            time.sleep(15)
            print(str(n + 1) + '. ' + IDArtyr2[n] + ' ' + nazvanie_proekta + ' с ' + (
                        datetime.now() - timedelta(delta)).strftime("%d.%m.%Y") + ' по ' + (datetime.now()).strftime(
                "%d.%m.%Y") + ' - ' + str(kolichestvo_zakazov) + ' шт. количество файлов - ' + str(int(kolichestvo_failov) + 1))

            file = open('Выгрузка Артур 2.txt', 'a+', encoding='utf-8')
            file.write(str(n + 1) + '. ' + IDArtyr2[n] + ' ' + nazvanie_proekta + ' с ' + (
                        datetime.now() - timedelta(delta)).strftime("%d.%m.%Y") + ' по ' + (datetime.now()).strftime(
                "%d.%m.%Y") + ' - ' + str(kolichestvo_zakazov) + ' шт. количество файлов - ' + str(int(kolichestvo_failov) + 1) + '\n')
            file.close()

            summa_zakazov = summa_zakazov + kolichestvo_zakazov
            kolichestvo_failov = int(kolichestvo_failov) + 1
            n = n + 1

    print('Всего заказов у Артура 2 за период ', 'с ', (datetime.now() - timedelta(delta)).strftime("%d.%m.%Y"), 'по ',
          (datetime.now()).strftime("%d.%m.%Y"), ' - ', summa_zakazov, ' шт.')
    print('Количество файлов - ' + str(kolichestvo_failov) + ' шт.')

    file = open('Выгрузка Артур 2.txt', 'a+', encoding='utf-8')
    file.write(
        'Всего заказов у Артура 2 за период ' + 'с ' + (datetime.now() - timedelta(delta)).strftime("%d.%m.%Y") + 'по ' + (
            datetime.now()).strftime("%d.%m.%Y") + ' - ' + str(summa_zakazov) + ' шт.\n')
    file.write('Количество файлов - ' + str(kolichestvo_failov) + ' шт.\n')

    file.close()

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frame"]/div[1]/div[6]/a/span'))).click()
    time.sleep(10)
    browser.quit()


def vigryzka_Garik():
    browser = webdriver.Chrome(r'C:\Users\User\Desktop\Python\Drivers\chromedriver.exe')
    browser.maximize_window()
    wait = WebDriverWait(browser, 30)

    browser.get('https://liveinform.ru/account')

    login = browser.find_element_by_xpath('//*[@id="enter-phone"]')
    login.click()  # нажимает войти
    login.send_keys('89060934805')  # вводит логин

    parol = browser.find_element_by_xpath('//*[@id="enter-password"]')
    parol.click()
    parol.send_keys('6705359431')  # вводит пароль

    enter = browser.find_element_by_xpath('//*[@id="enter-form"]/p[3]/button')
    enter.click()  # нажимает ввод
    time.sleep(10)
    browser.refresh()
    n = 0
    summa_zakazov = 0
    kolichestvo_failov = 0

    file = open('Выгрузка Гарик.txt', 'a+', encoding='utf-8')
    file.write('! \n')
    file.close()

    while n < len(IDGarik):
        time.sleep(15)
        browser.get(''.join(('https://liveinform.ru/account/?multi=', IDGarik[n])))
        nazvanie_proekta = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="frame"]/div[1]/div[2]'))).text
        browser.get(''.join(('https://liveinform.ru/account/archive?add[start]=',
                             (datetime.now() - timedelta(105)).strftime("%d.%m.%Y"), '&add[end]=',
                             (datetime.now()).strftime("%d.%m.%Y"),
                             '&np=0&sort=date_desc&page=1&limit=100&return_status=10')))
        try:
            kolichestvo_zakazov = int(wait.until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div[2]/div[1]/div/div/b'))).text)
        except Exception:
            print(str(n + 1) + '. ' + IDGarik[n] + ' ' + nazvanie_proekta + ' с ' + (
                        datetime.now() - timedelta(105)).strftime("%d.%m.%Y") + ' по ' + (datetime.now()).strftime(
                "%d.%m.%Y") + ' - 0 шт.')
            file = open('Выгрузка Гарик.txt', 'a+', encoding='utf-8')
            file.write(str(n + 1) + '. ' + IDGarik[n] + ' ' + nazvanie_proekta + ' с ' + (
                        datetime.now() - timedelta(105)).strftime("%d.%m.%Y") + ' по ' + (datetime.now()).strftime(
                "%d.%m.%Y") + ' - 0 шт.\n')
            file.close()
            n = n + 1
            continue

        else:
            wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'все результаты'))).click()
            time.sleep(10)
            print(str(n + 1) + '. ' + IDGarik[n] + ' ' + nazvanie_proekta + ' с ' + (
                        datetime.now() - timedelta(105)).strftime("%d.%m.%Y") + ' по ' + (datetime.now()).strftime(
                "%d.%m.%Y") + ' - ' + str(kolichestvo_zakazov) + ' шт.')

            file = open('Выгрузка Гарик.txt', 'a+', encoding='utf-8')
            file.write(str(n + 1) + '. ' + IDGarik[n] + ' ' + nazvanie_proekta + ' с ' + (
                        datetime.now() - timedelta(105)).strftime("%d.%m.%Y") + ' по ' + (datetime.now()).strftime(
                "%d.%m.%Y") + ' - ' + str(kolichestvo_zakazov) + ' шт.\n')
            file.close()

            summa_zakazov = summa_zakazov + kolichestvo_zakazov
            kolichestvo_failov = int(kolichestvo_failov) + 1
            n = n + 1

    print('Всего заказов у Гарика за период ', 'с ', (datetime.now() - timedelta(105)).strftime("%d.%m.%Y"), 'по ',
          (datetime.now()).strftime("%d.%m.%Y"), ' - ', summa_zakazov, ' шт.')
    print('Количество файлов - ' + str(kolichestvo_failov) + ' шт.')

    file = open('Выгрузка Гарик.txt', 'a+', encoding='utf-8')
    file.write(
        'Всего заказов у Гарик за период ' + 'с ' + (datetime.now() - timedelta(105)).strftime("%d.%m.%Y") + 'по ' + (
            datetime.now()).strftime("%d.%m.%Y") + ' - ' + str(summa_zakazov) + ' шт.\n')
    file.write('Количество файлов - ' + str(kolichestvo_failov) + ' шт.\n\n')

    file.close()

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frame"]/div[1]/div[6]/a/span'))).click()
    time.sleep(10)
    browser.quit()


def podschet_zakazov_Vova():
    browser = webdriver.Chrome(r'C:\Users\User\Desktop\Python\Drivers\chromedriver.exe', options=options)
    browser.maximize_window()
    wait = WebDriverWait(browser, 15)
    summa_zakazov = 0
    n = 0

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

    file = open('Подсчет Вова.txt', 'a+', encoding='utf-8')
    file.write(nachaloPeriodaPodscheta+' - '+konecPeriodaPoscheta+'\n')
    file.close()

    while n < len(IDVova):
        browser.get(''.join(('https://liveinform.ru/account/?multi=', IDVova[n])))
        nazvanie_proekta = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="frame"]/div[1]/div[2]'))).text
        browser.get(''.join(('https://liveinform.ru/account/archive?add[start]=',
                             nachaloPeriodaPodscheta,
                             '&add[end]=',
                             konecPeriodaPoscheta,
                             '&np=0&sort=date_desc&page=1&limit=25&return_status=10')))

        wait = WebDriverWait(browser, 5)
        try:
            net_zakazov=wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="content"]/div[2]/div[2]/div[1]/div/div'), 'Заказов по данному запросу не найдено'))

        except Exception as E:
            pass
        else:
            text=f'{str(n+1)}. {IDVova[n]} {nazvanie_proekta} c {nachaloPeriodaPodscheta} по {konecPeriodaPoscheta} - 0 шт. (нет заказов)'
            print(text)
            file = open('Подсчет Вова.txt', 'a+', encoding='utf-8')
            file.write(text+'\n')
            file.close()
            n+=1
            continue
        wait = WebDriverWait(browser, 15)

        try:
            kolichestvo_zakazov = int(wait.until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div[2]/div[1]/div/div/b'))).text)

        except Exception:
            print(str(n+1)+'. '+IDVova[n], ' ', nazvanie_proekta, 'с', nachaloPeriodaPodscheta, 'по',
                  konecPeriodaPoscheta, ' - 0 шт.')
            file = open('Подсчет Вова.txt', 'a+', encoding='utf-8')
            file.write(str(n+1)+'. '+
                IDVova[n] + ' ' + nazvanie_proekta + ' с ' + nachaloPeriodaPodscheta + ' по ' + konecPeriodaPoscheta + ' - 0 шт.\n')
            file.close()
            n = n + 1
            continue
        else:
            print(str(n+1)+'. '+IDVova[n], ' ', nazvanie_proekta, 'с', nachaloPeriodaPodscheta, 'по',
                  konecPeriodaPoscheta, ' - ', kolichestvo_zakazov, ' шт.')
            file = open('Подсчет Вова.txt', 'a+', encoding='utf-8')
            file.write(str(n+1)+'. '+
                IDVova[n] + ' ' + nazvanie_proekta + ' с ' + nachaloPeriodaPodscheta + ' по ' + konecPeriodaPoscheta + ' - ' + str(kolichestvo_zakazov) + ' шт.\n')
            file.close()
            n = n + 1
            summa_zakazov = summa_zakazov + kolichestvo_zakazov
    print('Всего заказов у Володи за период ', 'с', nachaloPeriodaPodscheta, 'по',
          konecPeriodaPoscheta, ' - ', summa_zakazov, ' шт.')

    file = open('Подсчет Вова.txt', 'a+', encoding='utf-8')
    file.write('Всего заказов у Володи за период ' + ' с ' + nachaloPeriodaPodscheta + ' по ' + konecPeriodaPoscheta + ' - ' + str(summa_zakazov) + ' шт.\n\n')
    file.close()

    time.sleep(15)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frame"]/div[1]/div[6]/a/span'))).click()

    time.sleep(10)
    browser.quit()


def podschet_zakazov_Garik():
    browser = webdriver.Chrome(r'C:\Users\User\Desktop\Python\Drivers\chromedriver.exe')
    browser.maximize_window()
    wait = WebDriverWait(browser, 30)
    summa_zakazov = 0
    n = 0

    browser.get('https://liveinform.ru/account')

    login = browser.find_element_by_xpath('//*[@id="enter-phone"]')
    login.click()  # нажимает войти
    login.send_keys('89060934805')  # вводит логин

    parol = browser.find_element_by_xpath('//*[@id="enter-password"]')
    parol.click()
    parol.send_keys('6705359431')  # вводит пароль

    enter = browser.find_element_by_xpath('//*[@id="enter-form"]/p[3]/button')
    enter.click()  # нажимает ввод
    time.sleep(10)
    browser.refresh()

    file = open('Подсчет Гарик.txt', 'a+', encoding='utf-8')
    file.write(nachaloPeriodaPodscheta+' - '+konecPeriodaPoscheta+'\n')
    file.close()

    while n < len(IDGarik):
        time.sleep(5)
        browser.get(''.join(('https://liveinform.ru/account/?multi=', IDGarik[n])))
        nazvanie_proekta = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="frame"]/div[1]/div[2]'))).text
        browser.get(''.join(('https://liveinform.ru/account/archive?add[start]=',
                             nachaloPeriodaPodscheta,
                             '&add[end]=',
                             konecPeriodaPoscheta,
                             '&np=0&sort=date_desc&page=1&limit=25&return_status=10')))

        wait = WebDriverWait(browser, 5)
        try:
            net_zakazov=wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="content"]/div[2]/div[2]/div[1]/div/div'), 'Заказов по данному запросу не найдено'))

        except Exception as E:
            pass
        else:
            text=f'{str(n+1)}. {IDGarik[n]} {nazvanie_proekta} c {nachaloPeriodaPodscheta} по {konecPeriodaPoscheta} - 0 шт. (нет заказов)'
            print(text)
            file = open('Подсчет Вова.txt', 'a+', encoding='utf-8')
            file.write(text+'\n')
            file.close()
            n+=1
            continue
        wait = WebDriverWait(browser, 15)


        try:
            kolichestvo_zakazov = int(wait.until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div[2]/div[1]/div/div/b'))).text)

        except Exception:
            print(str(n+1)+'. '+IDGarik[n], ' ', nazvanie_proekta, 'с', nachaloPeriodaPodscheta, 'по',
                  konecPeriodaPoscheta, ' - 0 шт.')
            file = open('Подсчет Гарик.txt', 'a+', encoding='utf-8')
            file.write(str(n+1)+'. '+
                IDGarik[n] + ' ' + nazvanie_proekta + 'с' + nachaloPeriodaPodscheta + 'по' + konecPeriodaPoscheta + ' - 0 шт.\n')
            file.close()
            n = n + 1
            continue
        else:
            print(str(n+1)+'. '+IDGarik[n], ' ', nazvanie_proekta, 'с', nachaloPeriodaPodscheta, 'по',
                  konecPeriodaPoscheta, ' - ', kolichestvo_zakazov, ' шт.')
            file = open('Подсчет Гарик.txt', 'a+', encoding='utf-8')
            file.write(str(n+1)+'. '+
                IDGarik[n] + ' ' + nazvanie_proekta + ' с ' + nachaloPeriodaPodscheta + ' по ' + konecPeriodaPoscheta + ' - ' + str(kolichestvo_zakazov) + ' шт.\n')
            file.close()
            n = n + 1
            summa_zakazov = summa_zakazov + kolichestvo_zakazov

    print('Всего заказов у Гарика за период ', 'с', nachaloPeriodaPodscheta, 'по', konecPeriodaPoscheta, ' - ', str(summa_zakazov), ' шт.')

    file = open('Подсчет Гарик.txt', 'a+', encoding='utf-8')
    file.write('Всего заказов у Гарика за период ' + ' с ' + nachaloPeriodaPodscheta + ' по ' + konecPeriodaPoscheta + ' - ' + str(summa_zakazov) + ' шт.\n\n')
    file.close()

    time.sleep(15)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frame"]/div[1]/div[6]/a/span'))).click()

    time.sleep(10)
    browser.quit()


def bp():
    ui.lineEdit.setText('Подсчет заказов Вова')
    podschet_zakazov_Vova()


def sort():
    folder = r'C:\Users\User\Downloads'
    folder_excel = r'C:\Users\User\Downloads\EXCEL'
    folder1 = r'C:\Users\User\Downloads\1'
    folder2 = r'C:\Users\User\Downloads\2'
    folder3 = r'C:\Users\User\Downloads\3'

    try:
        os.makedirs(folder_excel)
    except OSError:
        print("Создать директорию %s не удалось" % folder_excel)
    else:
        print("Успешно создана директория %s " % folder_excel)
    finally:

        # Получаем списки файлов в папках

        a = os.listdir(path=folder)
        b = os.listdir(path=folder_excel)
        c1 = os.listdir(path=folder1)
        c2 = os.listdir(path=folder2)
        c3 = os.listdir(path=folder3)

        w = [c1, c2, c3, b]
        total_size = [0, 0, 0]
        papki = [folder1, folder2, folder3, folder_excel]

        # очищаем папки 1,2,3

        for n in range(len(w)):
            try:
                for i in range(len(w[n])):
                    os.remove(papki[n] + "/" + w[n][i])
            except Exception:
                continue
        print("Папки зачищены")

        # Вырезаем все нужные файлы в соответствующую папку

        for i in range(len(a)):
            x = a[i].split(".")
            if x[-1] == 'xls':
                file = folder + "/" + a[i]
                new_path = folder_excel + "/" + a[i]
                os.rename(file, new_path)

        b = os.listdir(path=folder_excel)

        while True and len(b) > 0:

            for n in range(1, 4):

                razmeri_v_excel = []

                #  Получаем список с размерами файлов:

                for i in range(len(b)):
                    file_size = os.path.getsize(folder_excel + "/" + b[i])
                    razmeri_v_excel += [file_size / 1024 ** 2]
                    # print(b[i] + ' - ' + str(razmeri_v_excel[i]))  # выводит название файла и его размер
                # print(razmeri_v_excel)  # выводит список к размерами
                # print(str(len(razmeri_v_excel)) + " - " + str(len(b)))  # выводит длину списка с размерам и списка с файлами
                try:
                    index = razmeri_v_excel.index(max(razmeri_v_excel))  # определяем индекс файла с макс размером
                except ValueError:
                    break
                else:

                    # Отправляем файл с макс размером в папки 1,2,3 попеременно попеременно

                    b = os.listdir(path=folder_excel)
                    file = folder_excel + "/" + b[index]
                    new_path = folder + "/" + str(n) + "/" + b[index]
                    os.rename(file, new_path)
                    b = os.listdir(path=folder_excel)
                    # print((len(b)))


def Obidinenie_excell():

    papki = [r'C:\Users\User\Downloads\1', r'C:\Users\User\Downloads\2', r'C:\Users\User\Downloads\3']

    for papka in papki:
        combined = pd.DataFrame()
        print(papka)
        files = [item for item in glob.glob(papka + str('\*{}').format('.xlsx'))]
        print(files)
        print(str(len(files))+' файлов в папке')

        for file in files:
            file = pd.read_excel(file)
            combined = pd.concat([combined, file])

        combined.to_excel(papka + '\Сумм.xlsx')

        # Открываем полученную объединенную таблицу
        tab = openpyxl.load_workbook(papka + '\Сумм.xlsx')

        # Открываем активную вкладку
        sheet = tab.active

        # Удаляем первую колонку
        sheet.delete_cols(1)

        # Переименовываем вкладку
        sheet.title = 'Лист'

        # Сохраняем и закрываем таблицу
        tab.save(papka + '\Сумм.xlsx')
        tab.close()

    print('Файлы объединены')


# Create application
app = QtWidgets.QApplication(sys.argv)

# Инициализация формы и интерфейса
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

# Логика

ui.pushButton.clicked.connect(vigryzka_Artyr)
ui.pushButton_2.clicked.connect(vigryzka_Artyr2)
ui.pushButton_5.clicked.connect(vigryzka_Vova)
ui.pushButton_6.clicked.connect(podschet_zakazov_Garik)
ui.pushButton_7.clicked.connect(Obidinenie_excell)
ui.pushButton_8.clicked.connect(vigryzka_Garik)
ui.pushButton_9.clicked.connect(podschet_zakazov_Vova)
ui.pushButton_13.clicked.connect(sort)



# Run

sys.exit(app.exec_())
