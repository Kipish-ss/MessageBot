from loader import dp
from aiogram import types
from .greeting import greet_user
from states import States
from utils.db_api.user_operations import exists
from aiogram.dispatcher.filters.builtin import CommandStart
from utils.db_api.states_operations import set_state, get_state
from utils.db_api.user_operations import insert_user


@dp.message_handler(lambda message: get_state(message.from_user.id) == States.start.value, CommandStart())
async def start_handler(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.reply("Hi!\nI am MessageBot! I will show your message count.\nLet me check "
                         "if you have already used me...")
    is_present = await exists(message.from_user.id)
    if not is_present:
        if message.from_user.username is not None:
            await insert_user(user_id=message.from_user.id, user_name=message.from_user.username)
            await message.reply(f"It seems you are new. Welcome to the club, {message.from_user.username}")
        else:
            await insert_user(user_id=message.from_user.id, user_name=message.from_user.full_name)
            await message.reply(f"It seems you are new. Welcome to the club, {message.from_user.full_name}")
    # else:
    #     text = await greet_user(user_id=message.from_user.id, is_present=True)
    #     await message.answer(text)
    await set_state(message.from_user.id, States.type_msg.value)
