import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from pycoingecko import CoinGeckoAPI
import requests
from aiogram.types.message import ContentType
from datetime import datetime
import telebot
import markups as nav
from flask import Flask, request

logging.basicConfig(level=logging.INFO)

Bot_TOKEN = '2112552145:AAGrb-XjK_3As5BOooWlybyGvt_OPeBzSGc'
APP_URL = "https://cursebot41.herokuapp.com/" + Bot_TOKEN

YOOTOKEN = '381764678:TEST:36416'

bot = Bot(token=Bot_TOKEN)

dp = Dispatcher(bot)
cg = CoinGeckoAPI()

server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)



@server.route(f"/{Bot_TOKEN}", methods=['POST'])
def redirect_message():
	json_string = request.get_data().decode("utf-8")
	update = telebot.types.Update.de_json(json_string)
	bot.process_new_updates([update])
	return "1", 200


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	if message.chat.type == 'private':
		await bot.send_message(message.from_user.id, 'Выберите валюту/криптовалюту:', reply_markup=nav.mainq)

@dp.message_handler(content_types = 'text')
async def bot_message(message: types.Message):
	if message.chat.type == 'private':
		if message.text == '📈 КРИПТОВАЛЮТЫ':
			await bot.send_message(message.from_user.id, 'Выберите криптовалюту или введите свою с маленькой буквы:', reply_markup=nav.criptoList)
		elif message.text == 'bitcoin':
			result = cg.get_price(ids=message.text, vs_currencies='usd')
			await bot.send_message(message.from_user.id, f"Криптовалюта: {message.text}\nСтоимость на данный момент: {result[message.text]['usd']} долларов")
		elif message.text == 'ethereum':
			result = cg.get_price(ids=message.text, vs_currencies='usd')
			await bot.send_message(message.from_user.id, f"Криптовалюта: {message.text}\nСтоимость на данный момент: {result[message.text]['usd']} долларов")
		elif message.text == 'solana':
			result = cg.get_price(ids=message.text, vs_currencies='usd')
			await bot.send_message(message.from_user.id, f"Криптовалюта: {message.text}\nСтоимость на данный момент: {result[message.text]['usd']} долларов")
		elif message.text == '⬅ ГЛАВНОЕ МЕНЮ':
			await bot.send_message(message.from_user.id, 'Выберите валюту/криптовалюту:', reply_markup=nav.mainq)
		if message.text == '📈 ВАЛЮТЫ':
			await bot.send_message(message.from_user.id, 'В процессе разработки...')
	else:
		bot.send_message(call.from_user.id, 'Я тебя не понимаю(((')



if __name__ == '__main__':
	bot.delete_webhook()
	bot.set_webhook(url=APP_URL)
	server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))


