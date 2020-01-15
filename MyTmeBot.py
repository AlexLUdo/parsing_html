import telebot
from telebot import apihelper
import time
import os
import requests
from bs4 import BeautifulSoup
import csv
import pprint
from Pars3DNews import *


TOKEN = '1069675336:AAFcgWEjjGYgmR3OiZJCUk2uOWYN0nM4eFs'

MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'

# Информация о боте
url = f'{MAIN_URL}/getMe'


proxies = {
    'http': 'http://138.197.136.125:8080',
    'https': 'http://138.197.136.125:8080',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}

result = requests.get(url, proxies=proxies, headers=headers)
pprint.pprint(result.json())

apihelper.proxy = proxies
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['news'])
def send_file(message):
    get_link(get_html('https://3dnews.ru/news'))
    print('Every thing is Fine!  File data.csv is READY to send for request')
    with open('data.csv', 'r') as dt:
        bot.send_document(message.chat.id, dt)
        bot.send_message(message.from_user.id, 'Увлекательного чтения новостей! ;)')
        bot.send_message(message.from_user.id, 'Если хочется еще почитать свежие новочти - повторяем процесс')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'привет':
        bot.send_message(message.from_user.id, f'Привет {message.from_user.username}, чем я могу помочь?')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, "Этот Бот предназначен для получения файла со списком\n"
                                               "свежих статьей и ссылок на них с сайта 3DNEWS в формате\n"
                                                "CSV , вызывается командой /news")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Справка вызывается командой /help.")


bot.polling()
