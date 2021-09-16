from aiogram.types import ContentType

from loader import dp
from aiogram import types
from utils.db_api.msg_count import update_count, get_msg_count, reset_count
from states import States
from utils.db_api.states_operations import get_state


@dp.message_handler(lambda message: get_state(message.from_user.id) == States.type_msg.value, commands=['reset_count'])
async def reset_msg_count(message: types.Message):
    text = await reset_count(message.from_user.id)
    await message.reply(text)


@dp.message_handler(lambda message: get_state(message.from_user.id) == States.type_msg.value, commands=["message_count"])
async def show_msg_count(message: types.Message):
    count = await get_msg_count(message.from_user.id)
    await message.reply(f"Your current message count is {count}.")


@dp.message_handler(lambda message: get_state(message.from_user.id) == States.type_msg.value, content_types=ContentType.ANY)
async def update_msg_count(message: types.Message):
    await update_count(message.from_user.id)