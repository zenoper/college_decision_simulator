from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

decision_type_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Acceptance", callback_data='acceptance'),
            InlineKeyboardButton(text="Rejection", callback_data='rejection'),
        ],
    ]
)