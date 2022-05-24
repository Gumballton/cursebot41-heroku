from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
btnMain = KeyboardButton("⬅ ГЛАВНОЕ МЕНЮ")
# main menu

#btnSub = KeyboardButton('♥ ПОДПИСКА')
#mainMenu = ReplyKeyboardMarkup(resize_keyboard = True)
#mainMenu.add(btnSub)


#sub_inline_markup = InlineKeyboardMarkup(row_width=1)

#btnSubMonth = InlineKeyboardButton(text='Месяц - 150 рублей', callback_data='submonth')

#sub_inline_markup.insert(btnSubMonth)
mainMenu = KeyboardButton('📈 ВАЛЮТЫ')
mainMenu1 = KeyboardButton('📈 КРИПТОВАЛЮТЫ')
mainq = ReplyKeyboardMarkup(resize_keyboard = True).add(mainMenu1, mainMenu)


# other menu
btnBitcoin = KeyboardButton(text='bitcoin', callback_data='cc_bitcoin')
btnEthereum = KeyboardButton(text='ethereum', callback_data='cc_ethereum')
btnSolana = KeyboardButton(text='solana', callback_data='cc_solana')
criptoList = ReplyKeyboardMarkup(resize_keyboard = True).add(btnBitcoin, btnEthereum, btnSolana, btnMain)


