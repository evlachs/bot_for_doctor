from aiogram import types


links_type_button = types.InlineKeyboardButton('Ссылки на источиники', callback_data='links_type')
quest_type_button = types.InlineKeyboardButton('Ссылка на анкету', callback_data='quest_type')

post_types_keyboard = types.InlineKeyboardMarkup()
post_types_keyboard.add(links_type_button).add(quest_type_button)
