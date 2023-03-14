from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Regexp

from states.personalInfo import PersonalInfo

from keyboards.inline.choose_universityKeyboard import university_list
from keyboards.inline.choose_decisionKeyboard import decision_type_keyboard
from keyboards.inline.confirm_editKeyboard import confirm_edit

from keyboards.default.make_decisionKeyboard import make_decision
from utils.misc.send_email import send_email


@dp.message_handler(text="Make Decision")
async def enter_first_name(message: types.Message):
    await message.answer("Please, share your First name", reply_markup=ReplyKeyboardRemove(selective=True))
    await PersonalInfo.first_name.set()


@dp.message_handler(state=PersonalInfo.first_name)
async def answer_first_name(message: types.Message, state: FSMContext):
    first_name = message.text
    await state.update_data(
        {'first_name': first_name}
    )

    await message.answer("The letter will be sent to you via email. Please, share your email")
    await PersonalInfo.email.set()

EMAIL_REGEX = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'


@dp.message_handler(Regexp(EMAIL_REGEX), state=PersonalInfo.email)
async def answer_first_name(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(
        {'email': email}
    )

    await message.answer("Choose university :", reply_markup=university_list)
    await PersonalInfo.university.set()


@dp.message_handler(state=PersonalInfo.email)
async def answer_first_name(message: types.Message):

    await message.answer("Invalid email format. Please, enter valid email!")
    await PersonalInfo.email.set()


@dp.callback_query_handler(lambda c: c.data in ['stanford', 'harvard', 'yale', 'nyuad', 'uchicago', 'princeton', 'dartmouth', 'duke'], state=PersonalInfo.university)
async def process_callback_query(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['university'] = call.data

        await call.message.answer("Choose decision type :", reply_markup=decision_type_keyboard)
        await call.answer(cache_time=60)
        await PersonalInfo.decision_type.set()


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


@dp.callback_query_handler(text="edit", state=PersonalInfo.confirm_edit)
async def edit_query(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Please, share your First name")
    await call.answer(cache_time=60)
    await state.finish()
    await PersonalInfo.first_name.set()


@dp.callback_query_handler(text="confirm", state=PersonalInfo.confirm_edit)
async def confirm_query(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Alright! Please, check your email inbox :) \n \n<b>Please, check your spam folder if you don't receive the email!</b>", reply_markup=make_decision)
    await call.answer(cache_time=60)

    info = await state.get_data()
    first_name = info.get('first_name')
    email = info.get('email')
    university = info.get('university')
    decision = info.get('decision_type')
    university_cap = university.capitalize()

    send_email(sender_name=university_cap, sender_email="collegedecisionsimulator@gmail.com", receiver_email=email, first_name=first_name, decision=decision, university=university)

    await state.finish()
