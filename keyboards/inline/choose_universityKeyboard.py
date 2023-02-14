from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

university_list = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Stanford", callback_data="stanford"),
            InlineKeyboardButton(text="Harvard", callback_data="harvard"),
        ],
        [
            InlineKeyboardButton(text="Yale", callback_data="yale"),
            InlineKeyboardButton(text="NYUAD", callback_data="nyuad"),
        ],
        [
            InlineKeyboardButton(text="UChicago", callback_data="uchicago"),
            InlineKeyboardButton(text="Princeton", callback_data="princeton"),
        ],
        [
            InlineKeyboardButton(text="Duke", callback_data="duke"),
            InlineKeyboardButton(text="Dartmouth", callback_data="dartmouth"),
        ],
    ]
)