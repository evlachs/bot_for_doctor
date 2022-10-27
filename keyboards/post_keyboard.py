from aiogram import types

URLS = {
    'smart_compensation': 'https://intensiv.leibiman.com/kompens_cd1',
    'genetic': 'https://intensiv.leibiman.com/genetika',
    'webinar': 'https://intensiv.leibiman.com/vebinar_po_pn',
    'diabetes': 'https://diabet.mnc-clinic.co.il/diabeticheskij-konstruktor-pitaniya/?partner=rfx3r8240',
    'closed_club': 'https://club.leibiman.com/month_of_open_door',
    'culinary_library': 'https://diabetica.leibiman.com/#/',
    'thermofutlar': 'https://club.leibiman.com/page12vivi-cap-1',
}


smart_compensation_button = types.InlineKeyboardButton('Умная компенсация', url=URLS['smart_compensation'])
genetic_button = types.InlineKeyboardButton('Генетическая панель сахарного диабета', url=URLS['genetic'])
webinar_button = types.InlineKeyboardButton('Еженедельные вебинары по понедельникам', url=URLS['webinar'])
diabetes_button = types.InlineKeyboardButton('Диабетический конструктор питания (ДКП)', url=URLS['diabetes'])
closed_club_button = types.InlineKeyboardButton('Закрытый клуб', url=URLS['closed_club'])
culinary_library_button = types.InlineKeyboardButton('Первая кулинарная библиотека', url=URLS['culinary_library'])
thermofutlar_button = types.InlineKeyboardButton('Термо-футляр для инсулиновых ручек', url=URLS['thermofutlar'])


post_keyboard = types.InlineKeyboardMarkup()
post_keyboard.add(smart_compensation_button).add(genetic_button).add(webinar_button).add(diabetes_button)\
    .add(closed_club_button).add(culinary_library_button).add(thermofutlar_button)
