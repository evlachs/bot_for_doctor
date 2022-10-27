from aiogram import types


make_a_post_button = types.InlineKeyboardButton('создать пост', callback_data='post')

make_a_post_keyboard = types.InlineKeyboardMarkup()
make_a_post_keyboard.add(make_a_post_button)
