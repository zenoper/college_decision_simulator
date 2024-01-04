from aiogram import types
from loader import dp, db, bot
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Regexp
import asyncpg.exceptions
from data.config import ADMINS

from states.personalInfo import PersonalInfo

from keyboards.inline.choose_universityKeyboard import university_list
from keyboards.inline.choose_decisionKeyboard import decision_type_keyboard
from keyboards.inline.confirm_editKeyboard import confirm_edit

from keyboards.default.make_decisionKeyboard import make_decision
from utils.misc.send_email import send_email
from utils.misc.send_email2 import send_email2


@dp.message_handler(text="Make Decision", state=PersonalInfo.start)
async def enter_first_name(message: types.Message):
    await message.answer("Please, share your First name", reply_markup=ReplyKeyboardRemove(selective=True))
    await PersonalInfo.first_name.set()


@dp.message_handler(state=PersonalInfo.start, content_types=types.ContentTypes.ANY)
async def say_no(message: types.Message):
    await message.answer("Please, click the button 'Make Decision' below to generate a decision letter!", reply_markup=make_decision)


@dp.message_handler(state=PersonalInfo.first_name, content_types=types.ContentTypes.TEXT)
async def answer_first_name(message: types.Message, state: FSMContext):
    first_name = message.text
    if len(first_name) <= 3:
        await message.answer("Cmon! Your name can't be -3 characters long!🤥 \n\nI need your real first name!")
    else:
        user_name = message.from_user.username
        telegram_id = message.from_user.id
        await state.update_data(
            {'first_name': first_name,
             "username": user_name,
             "telegram_id": telegram_id}
        )

        await message.answer("The letter will be sent to you via email. \n\nShare your email!")
        await PersonalInfo.email.set()


@dp.message_handler(state=PersonalInfo.first_name, content_types=types.ContentTypes.ANY)
async def say_no(message: types.Message):
    await message.answer("Please, use text only.")

EMAIL_REGEX = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'


@dp.message_handler(Regexp(EMAIL_REGEX), state=PersonalInfo.email)
async def answer_first_name(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(
        {'email': email}
    )

    await message.answer("Choose university :", reply_markup=university_list)
    await PersonalInfo.university.set()


@dp.message_handler(state=PersonalInfo.email, content_types=types.ContentTypes.ANY)
async def answer_first_name(message: types.Message):

    await message.answer("BRUUUH, I am just asking for an email. 😕 \n\nNothing more :)")


@dp.callback_query_handler(lambda c: c.data in ['stanford', 'harvard', 'yale', 'nyuad', 'uchicago', 'princeton', 'dartmouth', 'duke'], state=PersonalInfo.university)
async def process_callback_query(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['university'] = call.data

        await call.message.answer("Choose decision type :", reply_markup=decision_type_keyboard)
        await call.answer(cache_time=60)
        await PersonalInfo.decision_type.set()


@dp.message_handler(state=PersonalInfo.university, content_types=types.ContentTypes.ANY)
async def answer_first_name(message: types.Message):
    await message.answer("😑😑😑 \n\nJust choose one of the universities!", reply_markup=university_list)


@dp.callback_query_handler(lambda c: c.data in ['acceptance', 'rejection'], state=PersonalInfo.decision_type)
async def answer_check(call: CallbackQuery, state: FSMContext):
    decision_type = call.data
    await state.update_data(
        {'decision_type': decision_type}
    )

    # confirmation
    info = await state.get_data()
    first_name = info.get('first_name')
    email = info.get('email')
    university = info.get('university')
    decision = info.get('decision_type')

    msg = "Please, confirm your personal info is correct: \n \n"
    msg += f"First name - {first_name} \n"
    msg += f"Email - {email} \n"
    msg += f"University - {university} \n"
    msg += f"Decision Type - {decision} \n"
    await call.message.answer(msg, reply_markup=confirm_edit)
    await call.answer(cache_time=60)
    await PersonalInfo.confirm_edit.set()


@dp.message_handler(state=PersonalInfo.decision_type, content_types=types.ContentTypes.ANY)
async def answer_first_name(message: types.Message):
    await message.answer("You are frustrating me! 😡 \n\nClick buttons 'acceptance' or 'rejection'", reply_markup=decision_type_keyboard)



@dp.callback_query_handler(text="edit", state=PersonalInfo.confirm_edit)
async def edit_query(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Please, share your First name")
    await call.answer(cache_time=60)
    await PersonalInfo.first_name.set()


@dp.callback_query_handler(text="confirm", state=PersonalInfo.confirm_edit)
async def confirm_query(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Alrighty! Now, check your email inbox :) \n \n<b>‼️ Check your spam folder if you don't receive the email ‼️</b>", reply_markup=make_decision)
    await call.answer(cache_time=60)

    info = await state.get_data()
    first_name = info.get('first_name')
    email = info.get('email')
    university1 = info.get('university')
    decision = info.get('decision_type')
    university_cap = university1.capitalize() + ' ' + "Office of Undergraduate Admissions"

    send_email2(sender_name=university_cap, receiver_email=email, first_name=first_name, decision=decision, university=university1)

    try:
        user = await db.add_user(
            first_name=first_name,
            username=info.get("username"),
            telegram_id=info.get("telegram_id"),
            email=email,
            university=university1,
            decision_type=decision
        )
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=info.get("telegram_id"))

    count = await db.count_users()
    msg = f"User '{user[1]}' has been added to the database! We now have {count} users."
    await bot.send_message(chat_id=ADMINS[0], text=msg)

    await PersonalInfo.start.set()

@dp.message_handler(state=PersonalInfo.confirm_edit, content_types=types.ContentTypes.ANY)
async def answer_first_name(message: types.Message, state: FSMContext):

    info = await state.get_data()
    first_name = info.get('first_name')
    email = info.get('email')
    university = info.get('university')
    decision = info.get('decision_type')

    msg = "Just confirm your info is correct: \n \n"
    msg += f"First name - {first_name} \n"
    msg += f"Email - {email} \n"
    msg += f"University - {university} \n"
    msg += f"Decision Type - {decision} \n"

    await message.answer(f"BRUHH, again? \n\n{msg} \nOr, I will shoot you in the head!", reply_markup=confirm_edit)