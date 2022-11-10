from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot

from states import Form
from messages import MESSAGES
from conf import CHANNEL
from keyboards import confirm_post_keyboard, make_a_post_keyboard, post_keyboard, post_types_keyboard, go_to_quest_keyboard


@dp.callback_query_handler(lambda c: c.data in ['links_type', 'quest_type'])
async def cancel_photo(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        if callback_query.data == 'links_type':
            data['keyboard'] = post_keyboard
        else:
            data['keyboard'] = go_to_quest_keyboard
    await Form.title.set()
    await bot.send_message(callback_query.from_user.id, MESSAGES['set_title'])


@dp.callback_query_handler(lambda c: c.data == 'post')
async def make_a_post_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, MESSAGES['set_post_type'], reply_markup=post_types_keyboard)


@dp.callback_query_handler(lambda c: c.data == 'cancel_photo', state=Form.photo)
async def cancel_photo(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['photo'] = None
    await bot.send_message(callback_query.from_user.id, MESSAGES['confirm_post'])
    await bot.send_message(
        callback_query.from_user.id,
        f"{data['title']}{data['description']}",
        reply_markup=confirm_post_keyboard
    )


@dp.callback_query_handler(lambda c: c.data == 'cancel', state='*')
async def cancel_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    current_state = await state.get_state()
    if current_state is None:
        return
    elif current_state in ['Form:title', 'Form:description', 'Form:photo']:
        await state.finish()
        await bot.send_message(callback_query.from_user.id, MESSAGES['canceled'], reply_markup=make_a_post_keyboard)
    else:
        await state.finish()
        await bot.send_message(callback_query.from_user.id, MESSAGES['canceled'])


@dp.callback_query_handler(lambda c: c.data == 'confirm_post', state='*')
async def confirm_post(callback_query: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    async with state.proxy() as data:
        photo = data['photo']
        msg = f"{data['title']}{data['description']}"
    if photo:
        await bot.send_photo(CHANNEL, photo, msg, reply_markup=data['keyboard'])
    else:
        await bot.send_message(CHANNEL, msg, reply_markup=data['keyboard'])
    await state.finish()
    await bot.send_message(callback_query.from_user.id, MESSAGES['post_confirmed'], reply_markup=make_a_post_keyboard)
