from aiogram import types
from loader import dp
from keyboards.default.make_decisionKeyboard import make_decision
from states.personalInfo import PersonalInfo

@dp.message_handler(chat_id="5001636883", commands='start')
async def valera(message: types.Message):
    await message.answer("🤨")
    await message.answer("Look who is here 😍")
    await message.answer(f"<b>Hey beautiful! \n\nYou really thought I wouldn't prepare a special entry for you? I don't flirt, but this place is my exception for you!</b> \n\nWelcome to College Decision Simulator bot. This is a bot where we simulate the acceptance and rejection letters from established US universities. To continue, press the 'Make Decision' button below!", reply_markup=make_decision)
    await PersonalInfo.start.set()

@dp.message_handler(chat_id="871034682", commands='start')
async def valera(message: types.Message):
    await message.answer("🤨")
    await message.answer("Look who is here 😍")
    await message.answer(f"<b>Hey my beautiful! \n\nYou really thought I wouldn't prepare a special entry for you? I don't flirt, but this place is my exception for you!</b> \n\nWelcome to College Decision Simulator bot. This is a bot where we simulate the acceptance and rejection letters from established US universities. To continue, press the 'Make Decision' button below!", reply_markup=make_decision)
    await PersonalInfo.start.set()


#Valera
@dp.message_handler(chat_id="178942136", commands='start')
async def valera(message: types.Message):
    await message.answer(f"<b>Hey, Andrew Tate is the real TOPG, not Socrates :)</b> \n\nWelcome to College Decision Simulator bot. This is a bot where we simulate the acceptance and rejection letters from established US universities. To continue, press the 'Make Decision' button below!", reply_markup=make_decision)
    await PersonalInfo.start.set()

#Diyor
@dp.message_handler(chat_id="2086393228", commands='start')
async def diyor_reply(message: types.Message):
    await message.answer(
        f"<b>Iya, boy buva keling endi...</b> \n\nWelcome to College Decision Simulator bot. This is a bot where we simulate the acceptance and rejection letters from established US universities. To continue, press the 'Make Decision' button below!",
        reply_markup=make_decision)
    await PersonalInfo.start.set()

#Abdulloh
@dp.message_handler(chat_id="718229036", commands='start')
async def fernando(message: types.Message):
    await message.answer(f"<b>YOOOOO, Fernando, nima gap?</b> \nWelcome to College Decision Simulator bot. This is a bot where we simulate the acceptance and rejection letters from established US universities. To continue, press the 'Make Decision' button below!", reply_markup=make_decision)
    await PersonalInfo.start.set()


#Donik
@dp.message_handler(chat_id="417933861", commands='start')
async def valera(message: types.Message):
    await message.answer(f"<b>Iyee, Rolton Bosh keb qoptiyu</b> \nWelcome to College Decision Simulator bot. This is a bot where we simulate the acceptance and rejection letters from established US universities. To continue, press the 'Make Decision' button below!", reply_markup=make_decision)
    await PersonalInfo.start.set()


#Aleksandr
@dp.message_handler(chat_id="249794047", commands='start')
async def valera(message: types.Message):
    await message.answer(f"<b>Hey, HITMAN!</b> \nWelcome to College Decision Simulator bot. This is a bot where we simulate the acceptance and rejection letters from established US universities. To continue, press the 'Make Decision' button below!", reply_markup=make_decision)
    await PersonalInfo.start.set()

#Islom memchi
@dp.message_handler(chat_id="844687626", commands='start')
async def valera(message: types.Message):
    await message.answer(f"<b>Are you not the guy who makes a lot of memes and has an existential crisis?</b> \nWelcome to College Decision Simulator bot. This is a bot where we simulate the acceptance and rejection letters from established US universities. To continue, press the 'Make Decision' button below!", reply_markup=make_decision)
    await PersonalInfo.start.set()


#Shakhzod
@dp.message_handler(chat_id="310366883", commands='start')
async def valera(message: types.Message):
    await message.answer(f"<b>Do you remember losing in PlayStation?</b> \nWelcome to College Decision Simulator bot. This is a bot where we simulate the acceptance and rejection letters from established US universities. To continue, press the 'Make Decision' button below!", reply_markup=make_decision)
    await PersonalInfo.start.set()


#Kamol
@dp.message_handler(chat_id="923225671", commands='start')
async def valera(message: types.Message):
    await message.answer(f"<b>Your cat is so cute! How do you take care of its fur?</b> \nWelcome to College Decision Simulator bot. This is a bot where we simulate the acceptance and rejection letters from established US universities. To continue, press the 'Make Decision' button below!", reply_markup=make_decision)
    await PersonalInfo.start.set()
