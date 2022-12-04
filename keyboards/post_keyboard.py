from aiogram import types

URLS = {
    'smart_compensation': 'https://intensiv.leibiman.com/kompens_cd1',
    'course': 'https://intensiv.leibiman.com/kurs_sd6m',
    'genetic': 'https://intensiv.leibiman.com/nevgen',
    'constructor': 'https://diabet.mnc-clinic.co.il/diabeticheskij-konstruktor-pitaniya/?partner=rfx3r8240',
    'close_club': 'https://intensiv.leibiman.com/dxaim_club',
    'culinary_library': 'https://diabetica.leibiman.com/#/',
    'thermofutlar': 'https://club.leibiman.com/page12vivi-cap-1',
    'mail': 'https://intensiv.leibiman.com/rassilka',
    'news_channel': 'https://t.me/diabetesNews2022',
}


smart_compensation_button = types.InlineKeyboardButton('Умная компенсация', url=URLS['smart_compensation'])
genetic_button = types.InlineKeyboardButton('Генетическая панель сахарного диабета', url=URLS['genetic'])
course_button = types.InlineKeyboardButton('Курс по основам и правилам компенсации', url=URLS['course'])
constructor_button = types.InlineKeyboardButton('Диабетический конструктор питания (ДКП)', url=URLS['constructor'])
closed_club_button = types.InlineKeyboardButton('Закрытый клуб', url=URLS['close_club'])
culinary_library_button = types.InlineKeyboardButton('Первая кулинарная библиотека', url=URLS['culinary_library'])
mail_button = types.InlineKeyboardButton('Почтовая рассылка Стоп диабет', url=URLS['mail'])
thermofutlar_button = types.InlineKeyboardButton('Термо-футляр для инсулиновых ручек', url=URLS['thermofutlar'])
news_button = types.InlineKeyboardButton('Новостной канал Все о сахарном диабете 1 типа', url=URLS['news_channel'])


post_keyboard = types.InlineKeyboardMarkup()
post_keyboard.add(smart_compensation_button).add(genetic_button).add(course_button).add(constructor_button)\
    .add(closed_club_button).add(culinary_library_button).add(mail_button).add(thermofutlar_button).add(news_button)
