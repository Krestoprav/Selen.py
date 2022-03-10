
import telebot
from telebot import apihelper
from telebot import types
import time
import random

bot = telebot.TeleBot('1103866902:AAGOs_JkUYGekE6yZ5SDSo6T5jXxYZ5myEI', threaded=False)
apihelper.proxy = {"https":"socks5://195.201.15.253:1080"}

# Клавиатура
glavmeny = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
tovar = types.InlineKeyboardButton("Наши товары")
oplata = types.InlineKeyboardButton("Способы оплаты")
dostavka = types.InlineKeyboardButton("Способы доставки")
glavmeny.add(tovar, oplata, dostavka)

#Приветствие
@bot.message_handler(commands=["start"])
def welcome(message):
    sti = open('Magaz\HI.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Привет, {0.first_name}!\nЯ -  бот магазина. Что пожелаете? Кнопки внизу.".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=glavmeny)

#Реакция на кнопки
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == "Способы оплаты":

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Карта", callback_data='good')
            item2 = types.InlineKeyboardButton("Наличка", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Наши способы оплаты', reply_markup=markup)

        else:
            bot.send_message(message.chat.id, 'напишите /start')




#RUN
try:
    bot.polling(none_stop=True, interval=0)
except:
    pass

while True:
    try:
      bot.polling(none_stop=True, interval=0, timeout=20)
    except Exception as E:
        print(E.args)
        time.sleep(2)