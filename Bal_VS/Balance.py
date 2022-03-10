import requests
import telebot
from telebot import TeleBot
from telebot import types
import time
from time import sleep
import datetime
from datetime import timedelta, datetime


token='1619367152:AAHv8SLc2vt5mqI4o3QkKTn35Psx2t8p5yU'

bot = telebot.TeleBot(token, threaded=False)
my_id= '544023514'
id_vova= '252807089'


URL = 'https://www.liveinform.ru/api/v2/balance/'


def balance():

    response = requests.post(URL, params={'api_id': 'zJA7g2OU-PgP3lCdA-9xttIsDU-byeJ44xr'})

    a=response.text.split(',')[1].split(':')[1].replace('}', '')

    text= rf"Баланс на Liveinform : {a} руб."

    print(rf"{datetime.now()} : {a} руб.")

    if float(a)<3000:
        print('Отправляю в телегу')
        bot.send_message(my_id, text)
        bot.send_message(id_vova, text)


while True:
    try:
        balance()
    except Exception as e:
        time.sleep(600)
        print(rf"Ошибка {e.args}")
        continue
    
    time.sleep(3600)

