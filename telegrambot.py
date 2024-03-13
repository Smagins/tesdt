from telebot import *

bot = telebot.TeleBot("7076729797:AAG6J4iE689-_QFgRwmQYrW6bYqij7vLxZY")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"1 - balance\n2 - mining")

@bot.message_handler()
def get_user_text(message):
    if message.text == "1":
        bot.send_message(message.chat.id,"sas")

bot.polling(none_stop = True)
