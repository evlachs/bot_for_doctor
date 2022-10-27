from aiogram.dispatcher.filters.state import StatesGroup, State


class Form(StatesGroup):
    title = State()
    description = State()
    photo = State()
    second_photo = State()
    third_photo = State()
