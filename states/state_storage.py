from aiogram.dispatcher.filters.state import State, StatesGroup


class States(StatesGroup):
    start = State()
    enter_name = State()
    type_msg = State()
    update_name = State()