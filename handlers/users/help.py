from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp(), state='*')
async def bot_help(message: types.Message):
    text = ("Commands list: ",
            "/start - Begin the dialogue",
            "/help - Get info",
            "/update_name - Update your name",
            "/message_count - Show your message count",
            "/reset_count - Reset your message count(set it to 0)",
            "/stats - Show other person's message count")

    await message.answer("\n".join(text))