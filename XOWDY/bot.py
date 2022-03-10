
import telebot
from XOWDY import config
from telebot import apihelper
from telebot import types
import time
import random

bot = telebot.TeleBot(config.TOKEN, threaded=False)
apihelper.proxy = {"https":"socks5://195.201.15.253:1080"}

#Приветствие
@bot.message_handler(commands=["start"])
def welcome(message):
    sti = open('XO_HI.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # Клавиатура
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.InlineKeyboardButton("🎲 Рандомное число")
    item2 = types.InlineKeyboardButton("😊 Как дела?")
    markup.add(item1, item2)


    bot.send_message(message.chat.id, "Привет, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == '😊 Как дела?':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, "Вот и отличненько 😊")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Замечательно',
                                      reply_markup=None)
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Жаль',
                                      reply_markup=None)

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🤔",
                                  reply_markup=None)

            # show alert
            #bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                     # text="🤔")

    except Exception as e:
        print(repr(e))
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