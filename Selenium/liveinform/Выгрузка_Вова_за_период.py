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
import openpyxl
import comtypes.client as cl
from collections import Counter
from Peremennie import IDVova, IDArtyr, IDArtyr2, IDGarik, Ishod_spis, \
    spis_xls, vichet_spis, del_files, copy_files, Obidinenie_excell, Vova, vigryzka, Stat

# papka=rf'C:\Users\User\Downloads\{(datetime.now()).strftime("%d.%m.%Y - %H.%M.%S")}'
papka=rf'C:\Users\User\Downloads\1'


n = 0
nachaloPeriodaPodscheta = '01.12.2021'
konecPeriodaPoscheta= (datetime.now()).strftime("%d.%m.%Y")

# Зачищаем папку
del_files(papka)

# Выгружаем файлы из лайва
vigryzka(Vova,  # Название словаря - имя пользователя
         nachaloPeriodaPodscheta,  # Начало периода подсчета
         konecPeriodaPoscheta,  # Конец периода подсчета
         papka,  # Папка для скачивания и дальнейше работы
         Stat['all'],  # ссылку с нужным статус скачиваемых файлов (словарь)
         'txt_all',  # название ключа нужного текстового файла из словаря пользователя
         )

# Объединяем файлы в один
Obidinenie_excell(papka,
                  nachaloPeriodaPodscheta,
                  konecPeriodaPoscheta
                  )

