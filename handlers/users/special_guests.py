from aiogram import types
from loader import dp
from keyboards.default.make_decisionKeyboard import make_decision

GIRLS = [5816759846, 105057764, 719304456, 775433231, 538800450, 430853870, 727487571, 1029746208, 1714255322, 794134904, 1997168961, 5572243095, 951931338, 1378248439, 748242055]


#GIRLS
@dp.message_handler(chat_id=GIRLS, commands='start')
async def valera(message: types.Message):
    await message.answer(f"<b>Oh, another beautiful lady :)</b> \nWelcome to College Decision Simulator bot. This is a bot where we simulate the acceptance and rejection letters from established US universities. To continue, press the 'Make Decision' button below!", reply_markup=make_decision)

#Valera
@dp.message_handler(chat_id="178942136", commands='start')
async def valera(message: types.Message):
    await message.answer(f"<b>Hey, Andrew Tate is the real TOPG, not socrates :)</b> \nWelcome to College Decision Simulator bot. This is a bot where we simulate the acceptance and rejection letters from established US universities. To continue, press the 'Make Decision' button below!", reply_markup=make_decision)

#Abdulloh
@dp.message_handler(chat_id="718229036", commands='start')
async def valera(message: types.Message):
    await message.answer(f"<b>YOOOOO, Fernando, nima gap?</b> \nWelcome to College Decision Simulator bot. This is a bot where we simulate the acceptance and rejection letters from established US universities. To continue, press the 'Make Decision' button below!", reply_markup=make_decision)

#Levsha
@dp.message_handler(chat_id="1632137931", commands='start')
async def valera(message: types.Message):
    await message.answer(f"<b>Hey, Asadchik, surprised?</b> \nWelcome to College Decision Simulator bot. This is a bot where we simulate the acceptance and rejection letters from established US universities. To continue, press the 'Make Decision' button below!", reply_markup=make_decision)


#Donik
@dp.message_handler(chat_id="417933861", commands='start')
async def valera(message: types.Message):
    await message.answer(f"<b>Iyee, Rolton Bosh keb qoptiyu</b> \nWelcome to College Decision Simulator bot. This is a bot where we simulate the acceptance and rejection letters from established US universities. To continue, press the 'Make Decision' button below!", reply_markup=make_decision)

#Rustam
@dp.message_handler(chat_id="933388976", commands='start')
async def valera(message: types.Message):
    await message.answer(f"<b>It seems you don't deserve to use the actual purpose of this bot as you lost yours. But, if you want to:</b> \nRepeat after me.... \nAshhadu alla....")

#Aleksandr
@dp.message_handler(chat_id="249794047", commands='start')
async def valera(message: types.Message):
    await message.answer(f"<b>Hey, HITMAN!</b> \nWelcome to College Decision Simulator bot. This is a bot where we simulate the acceptance and rejection letters from established US universities. To continue, press the 'Make Decision' button below!", reply_markup=make_decision)


#Islom memchi
@dp.message_handler(chat_id="844687626", commands='start')
async def valera(message: types.Message):
    await message.answer(f"<b>Are you not the guy who makes a lot of memes and has an existential crisis?</b> \nWelcome to College Decision Simulator bot. This is a bot where we simulate the acceptance and rejection letters from established US universities. To continue, press the 'Make Decision' button below!", reply_markup=make_decision)

#Shakhzod
@dp.message_handler(chat_id="310366883", commands='start')
async def valera(message: types.Message):
    await message.answer(f"<b>Do you remember losing in PlayStation?</b> \nWelcome to College Decision Simulator bot. This is a bot where we simulate the acceptance and rejection letters from established US universities. To continue, press the 'Make Decision' button below!", reply_markup=make_decision)

#Javohir Utkirov
@dp.message_handler(chat_id="801154063", commands='start')
async def valera(message: types.Message):
    await message.answer(f"<b>What's up American boy? How is your edu academy doing?</b> \nWelcome to College Decision Simulator bot. This is a bot where we simulate the acceptance and rejection letters from established US universities. To continue, press the 'Make Decision' button below!", reply_markup=make_decision)

#Kamol
@dp.message_handler(chat_id="923225671", commands='start')
async def valera(message: types.Message):
    await message.answer(f"<b>Your cat is so cute! How do you take care of its fur?</b> \nWelcome to College Decision Simulator bot. This is a bot where we simulate the acceptance and rejection letters from established US universities. To continue, press the 'Make Decision' button below!", reply_markup=make_decision)

#Yale Guys
@dp.message_handler(chat_id=[1048121890, 225085311], commands='start')
async def valera(message: types.Message):
    await message.answer(f"<b>Another Yalie!</b> \nWelcome to College Decision Simulator bot. This is a bot where we simulate the acceptance and rejection letters from established US universities. To continue, press the 'Make Decision' button below!", reply_markup=make_decision)
