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



#browser=webdriver.Chrome()
# browser.maximize_window()
# wait=WebDriverWait(browser, 30)
IDVova=['15310', '15045', '15450', '15084',
        '15504', '15698', '15555', '11828',
        '15448', '12625', '13142', '15700',
        '15584', '14358']
IDArtyr=['11375', '10195', '14914', '13749', '10199',
         '15088', '12068', '15715', '15138',
         '15089', '15087', '11579', '10757', '10197',
         '10192', '10196', '11915', '10193', '13748',
         '15557', '15599']

n=0
nachaloPeriodaPodscheta='01.01.2021'

def parVova():

    browser.get('https://liveinform.ru/account')

    login=browser.find_element_by_xpath('//*[@id="enter-phone"]')
    login.click()  # нажимает войти
    login.send_keys('89050048682')  # вводит логин

    parol=browser.find_element_by_xpath('//*[@id="enter-password"]')
    parol.click()
    parol.send_keys('2129881196')  # вводит пароль

    enter=browser.find_element_by_xpath('//*[@id="enter-form"]/p[3]/button')
    enter.click()  # нажимает ввод
    time.sleep(10)
    browser.refresh()
def parArtyr():

    browser.get('https://liveinform.ru/account')

    login=browser.find_element_by_xpath('//*[@id="enter-phone"]')
    login.click()  # нажимает войти
    login.send_keys('79057604761')  # вводит логин

    parol=browser.find_element_by_xpath('//*[@id="enter-password"]')
    parol.click()
    parol.send_keys('IkxBYkvL')  # вводит пароль

    enter=browser.find_element_by_xpath('//*[@id="enter-form"]/p[3]/button')
    enter.click()  # нажимает ввод
    time.sleep(10)
    browser.refresh()
def vihod():
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frame"]/div[1]/div[6]/ROI/span'))).click()
def vigryzka_Vova():
    parVova()
    n=0
    while n<len(IDVova):
        time.sleep(15)
        browser.get(''.join(('https://liveinform.ru/account/?multi=', IDVova[n])))
        browser.get(''.join(('https://liveinform.ru/account/archive?add[start]=', (datetime.now()-timedelta(62)).strftime("%d.%m.%Y"), '&add[end]=', (datetime.now()).strftime("%d.%m.%Y"), '&np=0&sort=date_desc&page=1&limit=100&return_status=10')))
        wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'все результаты'))).click()
        time.sleep(10)
        print((n + 1), IDVova[n], 'готов', datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        n=n+1

    vihod()
def vigryzka_Artyr():
    parArtyr()
    n=0
    while n<len(IDArtyr):
        time.sleep(15)
        browser.get(''.join(('https://liveinform.ru/account/?multi=', IDArtyr[n])))
        browser.get(''.join(('https://liveinform.ru/account/archive?add[start]=', (datetime.now()-timedelta(62)).strftime("%d.%m.%Y"), '&add[end]=', (datetime.now()).strftime("%d.%m.%Y"), '&np=0&sort=date_desc&page=1&limit=100&return_status=10')))
        wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'все результаты'))).click()
        time.sleep(10)
        print((n + 1), IDArtyr[n], 'готов', datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        n=n+1

    vihod()
def podschet_zakazov_Vova():
    summa_zakazov=0
    n=0
    parVova()
    while n < len(IDVova):
        try:
            browser.get(''.join(('https://liveinform.ru/account/?multi=', IDVova[n])))
            nazvanie_proekta=wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="frame"]/div[1]/div[2]'))).text
            browser.get(''.join(('https://liveinform.ru/account/archive?add[start]=',
                             nachaloPeriodaPodscheta,
                             '&add[end]=',
                             (datetime.now()).strftime("%d.%m.%Y"),
                             '&np=0&sort=date_desc&page=1&limit=25&return_status=10')))
            kolichestvo_zakazov=int(wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div[2]/div[1]/div/div/b'))).text)
            print(IDVova[n], ' ', nazvanie_proekta, nachaloPeriodaPodscheta, (datetime.now()).strftime("%d.%m.%Y"), kolichestvo_zakazov)
            n=n+1
            summa_zakazov=summa_zakazov+kolichestvo_zakazov
        except Exception:
            print(IDVova[n], ' ', nazvanie_proekta, nachaloPeriodaPodscheta, (datetime.now()).strftime("%d.%m.%Y"), '0')
            n=n+1
            continue
    print('Всего заказов у Володи за период ', nachaloPeriodaPodscheta, (datetime.now()).strftime("%d.%m.%Y"), ' - ', summa_zakazov)
    vihod()
def podschet_zakazov_Artyr():
    summa_zakazov=0
    n=0
    parArtyr()
    while n < len(IDArtyr):
        try:
            browser.get(''.join(('https://liveinform.ru/account/?multi=', IDArtyr[n])))
            nazvanie_proekta=wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="frame"]/div[1]/div[2]'))).text
            browser.get(''.join(('https://liveinform.ru/account/archive?add[start]=',
                             nachaloPeriodaPodscheta,
                             '&add[end]=',
                             (datetime.now()).strftime("%d.%m.%Y"),
                             '&np=0&sort=date_desc&page=1&limit=25&return_status=10')))
            kolichestvo_zakazov=int(wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div[2]/div[1]/div/div/b'))).text)
            print(IDArtyr[n], ' ', nazvanie_proekta, nachaloPeriodaPodscheta, (datetime.now()).strftime("%d.%m.%Y"), kolichestvo_zakazov)
            n=n+1
            summa_zakazov=summa_zakazov+kolichestvo_zakazov
        except Exception:
            print(IDArtyr[n], ' ', nazvanie_proekta, nachaloPeriodaPodscheta, (datetime.now()).strftime("%d.%m.%Y"), '0')
            n=n+1
            continue
    print('Всего заказов у Артура за период ', nachaloPeriodaPodscheta, (datetime.now()).strftime("%d.%m.%Y"), ' - ', summa_zakazov)
    vihod()

vigryzka_Vova()

#
# time.sleep(30)
# browser.quit()
