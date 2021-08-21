from loader import dp
from aiogram import types
from .greeting import greet_user
from states import States
from utils.db_api.user_operations import exists
from aiogram.dispatcher.filters.builtin import CommandStart


@dp.message_handler(CommandStart(), state='*')
async def start_handler(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.answer("Hi!\nI am MessageBot! I will show your message count.")
    await message.answer("Let me check if you have already used me...")
    is_present = await exists(message.from_user.id)
    if not is_present:
        await message.answer("It seems you are new. Welcome to the club, buddy! Enter your name:")
        await States.enter_name.set()
    else:
        text = await greet_user(user_id=message.from_user.id, is_present=True)
        await message.answer(text)
        await States.type_msg.set()