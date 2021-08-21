from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callback_data import stats_callback


async def get_names_keyboard(names: list):
    name_keyboard = InlineKeyboardMarkup()
    for i in range(len(names)):
        name_keyboard.insert(InlineKeyboardButton(text=names[i], callback_data=stats_callback.new(
            name=names[i])))
    return name_keyboard





