import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from keyboards.default import menu
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("""🇺🇿 Assalomu aleykum, keling, avvaliga xizmat ko’rsatish tilini tanlab olaylik.\n
🇷🇺 Здравствуйте! Давайте для начала выберем язык обслуживания!
""", reply_markup=menu.menu_language)
    user_id = message.from_user.id
    try:
        db.add_user(id=user_id)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    # Send Admin
    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)



