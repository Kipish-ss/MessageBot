from aiogram import types
from loader import dp


@dp.message_handler()
async def answer_invalid_output(message: types.Message):
    await message.answer("Type /start command to run the bot")
