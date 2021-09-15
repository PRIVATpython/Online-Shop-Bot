from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_language = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿UZ"),
            KeyboardButton(text="🇷🇺RU")
        ]
    ],
    resize_keyboard=True
)

menu_tel = {
    "🇺🇿UZ": ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Mening raqamim", request_contact=True)
            ]
        ],
        resize_keyboard=True

    ),
    "🇷🇺RU": ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Отправить номер", request_contact=True)
            ]
        ],
        resize_keyboard=True
    )
}

menu_main = {
    "🇺🇿UZ": ReplyKeyboardMarkup(
        keyboard=[

            [
                KeyboardButton(text="🛍  Buyurtma berish"),
                KeyboardButton(text="ℹ️Biz  haqimizda")
            ],
            [
                KeyboardButton(text="⚙️Sozlamalar")
            ]

        ],
        resize_keyboard=True,
        row_width=3
    ),
    "🇷🇺RU": ReplyKeyboardMarkup(
        keyboard=
        [
            [
                KeyboardButton(text="🛍 Заказать"),
                KeyboardButton(text="ℹ️ Информация")
            ],
            [
                KeyboardButton(text="⚙️Настройки")
            ]
        ],
        resize_keyboard=True,

    )

}
