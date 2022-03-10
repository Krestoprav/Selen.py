import telebot
import os
from telebot import apihelper
from telebot import types
import time
import random

bot = telebot.TeleBot('1116931558:AAHnkDUFaXPruVLtaBSDpAwgKJ4w9O-EUMQ', threaded=False)
# apihelper.proxy = {"https":"socks5://95.179.158.83:9050"}

# Клавиатура
glavmeny = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
knopka_albom = types.InlineKeyboardButton("Выбор альбома")
knopka_random = types.InlineKeyboardButton("Рандомная композиция")
glavmeny.add(knopka_albom, knopka_random)


a=open('D:\Музыка\Оргазм Нострадамуса\Альбомы\_1997-Восхождение к безумию\_01.Весёлые ребята.mp3', 'rb')
b=open('D:\Музыка\Оргазм Нострадамуса\Альбомы\_1997-Восхождение к безумию\_02. Пришла весна.mp3', 'rb')
c=open('D:\Музыка\Оргазм Нострадамуса\Альбомы\_1997-Восхождение к безумию\_03. Быдло.mp3', 'rb')
pesni=[a, b, c]


#Приветствие
@bot.message_handler(commands=["start"])
def welcome(message):
    sti = open('Bongyr.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Здорово, аморал {0.first_name}!\nЯ -  ОРГАЗМ НОСТРАДАМУСА БОТ. Музло ОН на твой выбор! Кнопка внизу!".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=glavmeny)
    bot.send_audio(message.chat.id, random.choice(pesni))

#Команда для альбома восхождение к безумию
#@bot.message_handler(commands=["Voshogdenie"])
#def welcome(message):
    #img = open('D:\Музыка\Оргазм Нострадамуса\Альбомы\_1997-Восхождение к безумию\cover.jpg', 'rb')
    #bot.send_photo(message.chat.id, img)
    #bot.send_audio(message.chat.id, audio=open('D:\Музыка\Оргазм Нострадамуса\Альбомы\_1997-Восхождение к безумию\_01.Весёлые ребята.mp3', 'rb'))
    #bot.send_audio(message.chat.id, audio=open('D:\Музыка\Оргазм Нострадамуса\Альбомы\_1997-Восхождение к безумию\_02. Пришла весна.mp3', 'rb'))
    #bot.send_audio(message.chat.id, audio=open('D:\Музыка\Оргазм Нострадамуса\Альбомы\_1997-Восхождение к безумию\_03. Быдло.mp3', 'rb'))
    #bot.send_audio(message.chat.id, audio=open('D:\Музыка\Оргазм Нострадамуса\Альбомы\_1997-Восхождение к безумию\_04. Горбуны.mp3', 'rb'))
    #bot.send_audio(message.chat.id, audio=open('D:\Музыка\Оргазм Нострадамуса\Альбомы\_1997-Восхождение к безумию\_05. Весеннее жертвоприношение.mp3', 'rb'))
    #bot.send_audio(message.chat.id, audio=open('D:\Музыка\Оргазм Нострадамуса\Альбомы\_1997-Восхождение к безумию\_06. Их специально убивали.mp3', 'rb'))
    #bot.send_audio(message.chat.id, audio=open('D:\Музыка\Оргазм Нострадамуса\Альбомы\_1997-Восхождение к безумию\_07. Птица гном.mp3', 'rb'))
    #bot.send_audio(message.chat.id, audio=open('D:\Музыка\Оргазм Нострадамуса\Альбомы\_1997-Восхождение к безумию\_08. Восхождение к безумию.mp3', 'rb'))
    #bot.send_audio(message.chat.id, audio=open('D:\Музыка\Оргазм Нострадамуса\Альбомы\_1997-Восхождение к безумию\_09. Фигура.mp3', 'rb'))
    #bot.send_audio(message.chat.id, audio=open('D:\Музыка\Оргазм Нострадамуса\Альбомы\_1997-Восхождение к безумию\_10. Откровение анархиста.mp3', 'rb'))
    #bot.send_audio(message.chat.id, audio=open('D:\Музыка\Оргазм Нострадамуса\Альбомы\_1997-Восхождение к безумию\_11. Я теряю контроль.mp3', 'rb'))
    #bot.send_audio(message.chat.id, audio=open('D:\Музыка\Оргазм Нострадамуса\Альбомы\_1997-Восхождение к безумию\_12. Сифилитик.mp3', 'rb'))
    #bot.send_audio(message.chat.id, audio=open('D:\Музыка\Оргазм Нострадамуса\Альбомы\_1997-Восхождение к безумию\_13. Слепоглухонемой пророк.mp3', 'rb'))

#Реакция на кнопки

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == "Выбор альбома":

            markup = types.InlineKeyboardMarkup(row_width=2)
            Ybey_Tinegera = types.InlineKeyboardButton("Убей тинейджера", callback_data='Ybey_Tinegera')

            markup.add(Ybey_Tinegera)

            #bot.send_message(message.chat.id, 'Все альбомы на выбор, уважаемый слушатель:', reply_markup=markup)
            bot.send_message(message.chat.id, 'Все альбомы на выбор, уважаемый слушатель:')
            bot.send_message(message.chat.id, 'ВОСХОЖДЕНИЕ К БЕЗУМИЮ- нажми команду /Voshogdenie')

        if message.text == "Рандомная композиция":
            bot.send_audio(message.chat.id, random.choice(pesni))
        else:
            bot.send_message(message.chat.id, 'Нихера непонятно! Выбирай из того что есть! Жми кнопку!')

#Рекция на выбор альбома
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'Ybey_Tinegera':
                bot.send_audio(call.message.chat.id, audio=open('D:\Музыка\Оргазм Нострадамуса\Альбомы\_1997-Восхождение к безумию\_01.Весёлые ребята.mp3', 'rb'))

            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')


            # remove inline buttons
            #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🤔",
                                 # reply_markup=None)

            # show alert
            #bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                     # text="🤔")

    except Exception as e:
        print(repr(e))

#RUN
while True:
    try:
      bot.polling(none_stop=True, interval=0, timeout=20)
    except Exception as E:
        print(E.args)
        time.sleep(2)
        continue

