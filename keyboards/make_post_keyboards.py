from aiogram import types

cancel_button = types.InlineKeyboardButton('отмена', callback_data='cancel')
confirm_post_button = types.InlineKeyboardButton('отправить пост', callback_data='confirm_post')
cancel_photo_button = types.InlineKeyboardButton('пост без фото', callback_data='cancel_photo')

cancel_photo_keyboard = types.InlineKeyboardMarkup()
cancel_photo_keyboard.add(cancel_photo_button)

confirm_post_keyboard = types.InlineKeyboardMarkup()
confirm_post_keyboard.add(confirm_post_button).add(cancel_button)
