from aiogram.dispatcher.filters.state import StatesGroup, State

class PersonalInfo(StatesGroup):
    first_name = State()
    email = State()
    university = State()
    decision_type = State()
    confirm_edit = State()