from aiogram import types


go_to_quest_button = types.InlineKeyboardButton('Заполнить анкету', url='https://t.me/diabetes_qbot')


go_to_quest_keyboard = types.InlineKeyboardMarkup()
go_to_quest_keyboard.add(go_to_quest_button)
