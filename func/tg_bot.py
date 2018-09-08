import telebot
import json
import time

with open('keys.json', 'r') as file:
	token = json.loads(file.read())['tg']
bot = telebot.TeleBot(token)

def keyboard(key):
	x = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
	for j in key:
		x.add(*[telebot.types.KeyboardButton(i) for i in j])
	return x