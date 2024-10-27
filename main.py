import datetime
import os
import random

import Text.Analys.main as textAnalis
import Container as Container
import Web.main as web
import threading
import telebot
from telebot import types
import Container as con
import Audio.Analys.main as audioAnalys
from Email.main import send_code

token = '7594023121:AAEzmV06OdsswTGajipWrQy9zUsTqXQ-RK4'
bot = telebot.TeleBot(token)


def Init():
    textAnalis.Init()


#text = input("Введите текст: ")
#print(textAnalis.FindWords(text))

Web = threading.Thread(target=web.Start)
Web.start()
print("Ok")
LoginUsers = {}


@bot.message_handler(content_types='text')
def message_reply(message: telebot.types.Message):
    if message.from_user.id == bot.user.id:
        return
    if message.text == "/start":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🚪 Войти")
        markup.add(button)

        bot.send_message(message.chat.id, "Это бот команды Danski для проекта TTS", reply_markup=markup)

    elif message.text == "🚪 Войти":
        LoginUsers[message.from_user.id] = -1
        bot.send_message(message.chat.id, "Введите вашу почту:")
    elif message.from_user.id in LoginUsers:
        if LoginUsers[message.from_user.id] == -1:
            if "@" in message.text:
                code = str(random.randint(0, 999999)).zfill(6)
                LoginUsers[message.from_user.id] = code
                send_code(code, message.text)
                bot.send_message(message.chat.id, f"Введите код, он был отправлен на {message.text}:\n")
            else:
                bot.send_message(message.chat.id, f"Вы ввели неверную почту:\n{message.text}")
        else:
            if message.text == LoginUsers[message.from_user.id]:
                bot.send_message(message.chat.id, "Вы успешно ввели код!")
                del LoginUsers[message.from_user.id]
            else:
                bot.send_message(message.chat.id, "Вы ввели не правильный код!")
    else:
        mes = textAnalis.FindWords(message.text)
        mes = mes.replace("{name}", message.from_user.first_name)
        mes = mes.replace("{nickname}", message.from_user.username)
        mes = mes.replace("{time}", str(datetime.datetime.now().time()))
        mes = mes.replace("{date}", str(datetime.datetime.now().date()))
        if mes != "":
            bot.send_message(message.chat.id, mes)
        else:
            bot.send_message(message.chat.id, mes)


@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    print("audio")
    file = bot.get_file(message.voice.file_id).file_path
    voice_data = bot.download_file(file)
    thread = threading.Thread(target=process_audio, args=(voice_data, message.chat.id, message))
    thread.start()


def process_audio(voice_data, chat_id, message):
    text = audioAnalys.GetAudio(voice_data)
    print("audio2")
    mes = textAnalis.FindWords(text)
    print(mes)
    mes = mes.replace("{name}", message.from_user.first_name)
    mes = mes.replace("{nickname}", message.from_user.username)
    mes = mes.replace("{time}", str(datetime.datetime.now().time()))
    mes = mes.replace("{date}", str(datetime.datetime.now().date()))
    bot.send_message(chat_id, mes)


bot.infinity_polling()
