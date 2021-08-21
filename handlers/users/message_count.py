from aiogram.types import ContentType

from loader import dp
from aiogram import types
from utils.db_api.msg_count import update_count, get_msg_count, reset_count
from states import States


@dp.message_handler(commands=['reset_count'], state=States.type_msg)
async def reset_msg_count(message: types.Message):
    text = await reset_count(message.from_user.id)
    await message.answer(text)


@dp.message_handler(commands=["message_count"], state=States.type_msg)
async def show_msg_count(message: types.Message):
    count = await get_msg_count(message.from_user.id)
    await message.answer(f"Your current message count is {count}.")


@dp.message_handler(state=States.type_msg, content_types=ContentType.ANY)
async def update_msg_count(message: types.Message):
    await update_count(message.from_user.id)