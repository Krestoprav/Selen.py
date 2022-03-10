import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from prog_ua import Ui_MainWindow
import pygame
from pygame import mixer
from playsound import playsound
import winsound
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
from liveinform import IDVova

# Create application
app = QtWidgets.QApplication(sys.argv)

# Инициализация формы и интерфейса
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
print(IDVova)



# Логика
def bp():
    ui.lineEdit.setText(IDVova[1])


ui.pushButton_5.clicked.connect(bp)

# Run
sys.exit(app.exec_())
