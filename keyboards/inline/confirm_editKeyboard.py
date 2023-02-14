from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

confirm_edit = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Confirm ✅", callback_data="confirm"),
            InlineKeyboardButton(text="Edit ✏️", callback_data="edit"),
        ]
    ]
)