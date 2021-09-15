from aiogram.dispatcher.filters.state import StatesGroup, State


class Answer(StatesGroup):
    language = State()
    phone = State()
    name = State()