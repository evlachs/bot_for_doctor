from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputMediaPhoto

from loader import dp, bot
from messages import MESSAGES
from keyboards import make_a_post_keyboard, cancel_photo_keyboard, confirm_post_keyboard
from states import Form


@dp.message_handler(commands=['start', 'help'])
async def start_message(message: types.Message):
    await dp.bot.send_message(
        message.chat.id,
        MESSAGES['start'].format(message.from_user.username),
        reply_markup=make_a_post_keyboard
    )
    with open('data/users_id.txt', 'r+') as file:
        if not str(message.from_user.id) in file.read().split('\n'):
            file.seek(0, 2)
            file.write(str(message.from_user.id)+'\n')


@dp.message_handler(commands=['post'])
async def make_a_post_command(message: types.Message):
    await Form.title.set()
    await bot.send_message(message.from_user.id, MESSAGES['set_title'])


@dp.message_handler(commands=['cancel'], state='*')
async def make_a_post_command(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    elif current_state in ['Form:title', 'Form:description', 'Form:photo']:
        await state.finish()
        await bot.send_message(message.from_user.id, MESSAGES['canceled'], reply_markup=make_a_post_keyboard)
    else:
        await state.finish()
        await bot.send_message(message.from_user.id, MESSAGES['canceled'])


@dp.message_handler(state=Form.title)
async def set_post_title(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = f'<b>{message.text}</b>\n\n'
    await Form.description.set()
    await bot.send_message(message.from_user.id, MESSAGES['set_description'])


@dp.message_handler(state=Form.description)
async def set_post_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await Form.photo.set()
    await bot.send_message(message.from_user.id, MESSAGES['set_photo'], reply_markup=cancel_photo_keyboard)


@dp.message_handler(state=Form.photo, content_types='photo')
async def set_post_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id
    await bot.send_message(message.from_user.id, MESSAGES['confirm_post'])
    await bot.send_photo(
        message.from_user.id,
        data['photo'],
        f"{data['title']}{data['description']}",
        reply_markup=confirm_post_keyboard
    )
