from main import my_token

import telebot
from telebot import types
token=my_token
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Кнопка")
    markup.add(item1)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Кнопка")
    item2 = types.KeyboardButton("Кнопка")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=='Кнопка':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Кнопка 2")
        item2 = types.KeyboardButton("Кнопка 3")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
    elif message.text=="Кнопка 2":
        bot.send_message(message.chat.id,"Егор")
    elif message.text == "Кнопка 3":
        bot.send_message(message.chat.id, "Егор")
bot.infinity_polling()
