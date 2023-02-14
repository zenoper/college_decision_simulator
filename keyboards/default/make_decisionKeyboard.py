from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

make_decision = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Make Decision")
        ],
    ],
    resize_keyboard=True
)