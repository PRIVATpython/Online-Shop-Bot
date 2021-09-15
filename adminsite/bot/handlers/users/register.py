import time

from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext

from keyboards.default import menu
from loader import dp, db
from states.answer import Answer
from utils.other.questions import questions


@dp.message_handler(state=None)
async def get_weather(message: types.Message):
    if message.chat.type == "private":
        if message.text == "🇺🇿UZ" or message.text == "🇷🇺RU":
            user_id = message.from_user.id

            db.update_language(language=message.text, id=user_id)
            time.sleep(1)
            db_language = db.user_language(id=user_id)[0]

            question = questions[db_language]["get_tel"]
            markup = menu.menu_tel[db_language]
            await message.answer(question, reply_markup=markup)
            await Answer.language.set()
        else:
            await message.reply("""Tilni tanlang ❗️❗️❗️
Выберите язык ❗️❗️❗️""")


@dp.message_handler(content_types="contact", state=Answer.language)
async def get_tel(message: types.Message):
    if message.chat.type == "private":
        user_id = message.from_user.id
        db_language = db.user_language(id=user_id)[0]
        question = questions[db_language]["get_name"]
        if message.contact:
            time.sleep(1)
            tel = message.contact.phone_number
            db.update_tel(tel=tel, id=user_id)

            await message.answer(question, reply_markup=ReplyKeyboardRemove())
            await Answer.next()
        else:
            await message.answer(question, reply_markup=ReplyKeyboardRemove())


@dp.message_handler(content_types="text", state=Answer.phone)
async def get_tel(message: types.Message, state=FSMContext):
    if message.chat.type == "private":
        user_id = message.from_user.id
        db_language = db.user_language(id=user_id)[0]
        error_name = questions[db_language]["error_name"]
        main_menu_text = questions[db_language]["main_menu"]
        menu_main_markup = menu.menu_main[db_language]
        if len(message.text.split(" ")) == 2:
            time.sleep(1)
            name = message.text
            db.update_name(name=name, id=user_id)

            await message.answer(main_menu_text, reply_markup=menu_main_markup)
            await state.reset_state()
        else:
            await message.reply(error_name)
