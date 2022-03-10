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

treki=['14390057865114', '14102057163325']

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x935')

browser = webdriver.Chrome(r'C:\Users\User\Desktop\Python\Selenium\liveinform\chromedriver.exe', chrome_options=options)

browser.maximize_window()
wait = WebDriverWait(browser, 30)

#Работа с таблицей

google_tab='https://docs.google.com/spreadsheets/d/1BdPsCkmjihvtlLXdZdQXmYQ49rIH2m_t7EP844c76SQ/edit#gid=359025799'

link = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']   # задаем ссылку на Гугл таблици
my_creds = ServiceAccountCredentials.from_json_keyfile_name('krestoprav-8e5f49dc5ebe.json', link) #формируем данные для входа из нашего json файла
client = gspread.authorize(my_creds)    # запускаем клиент для связи с таблицами
sheet = client.open_by_url(google_tab).worksheet('Статусы')   # открываем нужную нам таблицу и лист



# sheet.update_cell(20, 10, viplata)


for i in range(len(treki)):
    try:
        print(i)
        browser.get('https://www.pochta.ru/tracking#'+treki[i])
        browser.refresh()
        a= wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-tracking"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/h2'))).text
        print(treki[i]+' '+ a)
    except Exception:
        i=i-1
        browser.quit()
    finally:
        continue


browser.quit()

