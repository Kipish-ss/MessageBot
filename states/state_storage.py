from aiogram.dispatcher.filters.state import State, StatesGroup
from enum import Enum


# class States(StatesGroup):
#     start = State()
#     enter_name = State()
#     type_msg = State()
#     update_name = State()


class States(Enum):
    start = 0
    type_msg = 1
    update_name = 2
    type_user = 3
