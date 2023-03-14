import asyncpg.exceptions
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot
from keyboards.default.make_decisionKeyboard import make_decision

from data.config import ADMINS


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

    await message.answer(f"Hey, {message.from_user.full_name}! Welcome to College Decision Simulator bot. This is a bot where we simulate the acceptance and rejection letters from established US universities. To continue, press the 'Make Decision' button below! \n \n<b>!! Check your spam folder if you don't receive the email!</b>", reply_markup=make_decision)

