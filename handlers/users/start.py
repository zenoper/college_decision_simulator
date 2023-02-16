import asyncpg.exceptions
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db, bot
from keyboards.default.make_decisionKeyboard import make_decision

from data.config import ADMINS


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username)
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    await message.answer(f"Hey, {message.from_user.full_name}! Welcome to College Decision Simulator bot. This is a bot where we simulate the acceptance and rejection letters from established US universities. To continue, press the 'Make Decision' button below!", reply_markup=make_decision)

    count = await db.count_users()
    msg = f"{user[1]} was added to database. \nIn database, we have {count} users"
    await bot.send_message(chat_id=ADMINS[0], text=msg)
