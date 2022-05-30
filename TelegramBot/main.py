# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import telebot
# from telebot import types#
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from flask import Flask

bot = telebot.TeleBot("5577161542:AAEJUov8ELBsXiuXmh_MkTz0rTiO6C6Zj7g",
                      parse_mode=None)  # You can set parse_mode by default. HTML or MARKDOWN
content_types = ["text", "sticker", "pinned_message", "photo", "audio"]


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

@bot.callback_query_handler(func=lambda call: "id_assoluti" == call.data)
def classifica_assoluti(message):
    # print(message)
    bot.send_message(message.message.chat.id, "Hai tappato per vedere la classifica Assoluti")

@bot.callback_query_handler(func=lambda call: "id_over45" == call.data)
def classifica_assoluti(message):
    bot.send_message(message.message.chat.id, "Hai tappato per vedere la classifica Over45")

@bot.callback_query_handler(func=lambda call: "id_over55" == call.data)
def classifica_assoluti(message):
    bot.send_message(message.message.chat.id, "Hai tappato per vedere la classifica Over55")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Salve, benvenuto in AIFG. \n Cosa desideri fare ? \n /help per vedere i comandi disponibili")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Elenco dei comandi:\n /start - per iniziare \n /help - aiuto \n"
                          " /tappa - per le classifiche dell'ultima tappa")

# @bot.message_handler(func=lambda m: "AIFG" in m.text.upper())
@bot.message_handler(commands=['tappa'])
def echo_aifg(message):
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("Assoluti", callback_data = "id_assoluti"),
               InlineKeyboardButton("Over45", callback_data = "id_over45"),
               InlineKeyboardButton("Over55", callback_data = "id_over55"))
    bot.send_message(message.chat.id, "Vedi le classifiche dell'ultima tappa", reply_markup = markup)


@bot.message_handler(func=lambda m: "BABBO" in m.text.upper())
def echo_babbo(message):
    bot.send_message(message.chat.id, "Dimmi Martina")


@bot.message_handler(func=lambda m: "ROMA" in m.text.upper())
def echo_roma(message):
    bot.reply_to(message, "ROMA HA VINTO")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('Stefo')
    bot.infinity_polling(interval=0, timeout=20)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
