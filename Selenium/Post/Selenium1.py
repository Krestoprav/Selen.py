from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from time import sleep
import pyautogui
import pyperclip
import numpy



browser = webdriver.Chrome()
browser.maximize_window()


def vvod_parola():
    browser.get('https://passport.pochta.ru/')
    browser.find_element_by_xpath('//*[@id="header"]/div[2]/div[1]/div/div[3]/div[3]/ROI').click()  # нажимает войти
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="username"]').send_keys('krestoprav@mail.ru')  # вводит логин
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="userpassword"]').send_keys('Volodia2108')  # вводит пароль
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="layout-body"]/div/button').click()  # нажимает ввод


def posilka_str1():

    browser.get('https://www.pochta.ru/parcels')
    time.sleep(t)
    browser.find_element_by_xpath('//*[@id="page-parcel"]/div/div[1]/div/div[1]/div[1]/input').click()
    browser.find_element_by_xpath('//*[@id="page-parcel"]/div/div[1]/div/div[1]/div[1]/input').send_keys(Keys.CONTROL + 'ROI')
    browser.find_element_by_xpath('//*[@id="page-parcel"]/div/div[1]/div/div[1]/div[1]/input').send_keys(Keys.DELETE)
    time.sleep(t)

    Gorod_otpravitela=browser.find_element_by_xpath('//*[@id="page-parcel"]/div/div[1]/div/div[1]/div[1]/input')
    Gorod_otpravitela.send_keys('Москва')
    time.sleep(5)
    Gorod_otpravitela.send_keys(Keys.DOWN)
    time.sleep(t)
    Gorod_otpravitela.send_keys(Keys.ENTER)
    time.sleep(t)

    Gorod_polychatela=browser.find_element_by_xpath('//*[@id="page-parcel"]/div/div[1]/div/div[1]/div[2]/input')
    time.sleep(5)
    Gorod_polychatela.send_keys('Москва')
    time.sleep(5)
    Gorod_polychatela.send_keys(Keys.DOWN)
    time.sleep(t)
    Gorod_polychatela.send_keys(Keys.ENTER)
    time.sleep(t)


    # Вводит массу
    MassaPole = browser.find_element_by_xpath('//*[@id="page-parcel"]/div/div[1]/div/div[1]/div[3]/input')
    MassaPole.send_keys(m[n])  # вводит массу
    time.sleep(5)
    MassaPole.send_keys(Keys.DOWN)
    time.sleep(t)
    MassaPole.send_keys(Keys.ENTER)
    time.sleep(t)
    MassaPole.send_keys(Keys.TAB)
    time.sleep(t)

    # жмет наложенный платеж
    NalogPlateg = browser.find_element_by_xpath("//*[contains(text(), 'Налож')]")
    time.sleep(t)
    NalogPlateg.click()
    time.sleep(5)

    # Жмет "быстрое"

    Bistro = browser.find_element_by_xpath('//*[@id="page-parcel"]/div/div[1]/div/div[4]/div/div[2]')
    Bistro.click()
    time.sleep(15)

    # жмет получить трек

    browser.find_element_by_xpath('//*[@id="page-parcel"]/div/div[3]/div/div[2]/ROI[1]').click()


def posilka_str2():
    time.sleep(10)
    # вводим первую цену

    SymmaObiavlennoi = browser.find_element_by_xpath('//*[@id="InsuranceSum"]')
    SymmaObiavlennoi.click()
    SymmaObiavlennoi.send_keys(Keys.CONTROL + 'ROI')
    SymmaObiavlennoi.send_keys(Keys.DELETE)
    SymmaObiavlennoi.send_keys(symma[n])
    SymmaObiavlennoi.send_keys(Keys.ENTER)

    time.sleep(t)

    # вводим вторую цену

    SymmaNalogen = browser.find_element_by_xpath('//*[@id="CashOnDeliverySum"]')
    SymmaNalogen.click()
    SymmaNalogen.send_keys(Keys.CONTROL + 'ROI')
    SymmaNalogen.send_keys(Keys.DELETE)
    SymmaNalogen.send_keys(symma[n])
    SymmaNalogen.send_keys(Keys.ENTER)

    time.sleep(t)

    # вводим имя отправителя

    Otpravitel = browser.find_element_by_xpath('//*[@id="Sender"]')
    Otpravitel.click()
    Otpravitel.send_keys(Keys.CONTROL + 'ROI')
    Otpravitel.send_keys(Keys.DELETE)
    Otpravitel.send_keys("Иванов Иван Иванович")
    Otpravitel.send_keys(Keys.ENTER)

    time.sleep(t)

    # вводим номер телефона

    Telefon = browser.find_element_by_xpath('//*[@id="SenderPhone"]')
    Telefon.click()
    Telefon.send_keys(Keys.CONTROL + 'ROI')
    Telefon.send_keys(Keys.DELETE)
    Telefon.send_keys("9641111111")
    Telefon.send_keys(Keys.ENTER)

    time.sleep(t)

    # вводим имя получателя

    PolychatelPole = browser.find_element_by_xpath('//*[@id="Recipient"]')
    PolychatelPole.click()
    PolychatelPole.send_keys(Keys.CONTROL + 'ROI')
    PolychatelPole.send_keys(Keys.DELETE)
    PolychatelPole.send_keys(polychatel[n])
    PolychatelPole.send_keys(Keys.ENTER)

    time.sleep(t)

    # вводим адрес получателя

    adressPolychatelPole = browser.find_element_by_xpath(
        '//*[@id="mount_point_productFormF7pPortletV2_WAR_portalportlet_js"]/div/div/form/div[10]/div/div/div/input')
    adressPolychatelPole.click()
    time.sleep(t)
    adressPolychatelPole.send_keys(Keys.CONTROL + 'ROI')
    time.sleep(t)
    adressPolychatelPole.send_keys(Keys.DELETE)
    time.sleep(t)
    adressPolychatelPole.send_keys(adressPolychatel[n])
    time.sleep(5)
    adressPolychatelPole.send_keys(Keys.DOWN)
    time.sleep(t)
    adressPolychatelPole.send_keys(Keys.ENTER)
    time.sleep(t)
    adressPolychatelPole.send_keys(Keys.TAB)
    time.sleep(t)

    # вводим телефон получателя

    telephonPolychatelPole = browser.find_element_by_xpath('//*[@id="RecipientPhone"]')
    telephonPolychatelPole.click()
    telephonPolychatelPole.send_keys(Keys.CONTROL + 'ROI')
    telephonPolychatelPole.send_keys(Keys.DELETE)
    telephonPolychatelPole.send_keys(telephonPolychatel[n])
    telephonPolychatelPole.send_keys(Keys.ENTER)
    telephonPolychatelPole.send_keys(Keys.TAB)

    # #жмум кнопку получить трек
    trackk = browser.find_element_by_xpath(
        '//*[@id="mount_point_productFormF7pPortletV2_WAR_portalportlet_js"]/div/div/form/div[14]/div[2]/div/div/button')
    time.sleep(t)
    trackk.click()

# Вводим пароль


while True:
    try:
        vvod_parola()
    except Exception:
        continue
    else:
        break

#списоко данных
symma=[3000, 5000, 6000] # стоимость посылки
m=[300, 500, 667] #масса посылки
t=2 #время задержки
polychatel=['Петров Петр Петрович', 'Филипп Филиппович Филиппво', 'Андрей Андреевич Андреев']
adressPolychatel=['г Якутск, ул Покрышкина, д.46/2, -', 'г Нижний Новгород, ул Василия Иванова, д.24, кв 19', 'г Ростов-на-Дону, пр-кт 40-летия Победы, д.81, кв 98']
telephonPolychatel=['9124101111', '9081915788', '9511473879']
n=0

while n<len(symma):

    while True:
        try:
            # первая страница
            posilka_str1()
            # перешли на страницу с данными посылки
            posilka_str2()
        except Exception:
            continue
        else:
            break





    #Перешли на страницу с треками

    time.sleep(15)

    # Находит и кликает номер трека

    NomerTracka=browser.find_element_by_xpath("//*[contains(text(), '800')]")
    NomerTracka.click()
    a=pyperclip.paste()
    print(a)

    #жмет расппечатать бланк
    RaspechatacBlank=browser.find_element_by_xpath("//*[contains(text(), 'Распечатать бланк')]")
    RaspechatacBlank.click()

    time.sleep(t)

    #Удаляет трек
    Ydalit=browser.find_element_by_xpath("//*[contains(text(), 'Удалить')]")
    Ydalit.click()

    time.sleep(15)
    browser.refresh()
    time.sleep(t)
    # browser.back()

    n=n+1

browser.quit()
