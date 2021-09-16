from aiogram import types
from loader import dp


@dp.message_handler(commands=["pohui"])
async def send_sticker_poh(message: types.Message):
    await message.reply_sticker("CAACAgIAAxkBAAEC6WhhQzQdw3nzzd3kRkJ8egaaWjU0bwACJBEAAjjPCErozPuz2LIq6CAE")


@dp.message_handler(commands=["joke"])
async def send_sticker_joke(message: types.Message):
    await message.reply_sticker("CAACAgIAAxkBAAEC6XFhQzcUx_r7JNRlEJsw8Jnu5Y-GywAC1Q8AAjk7AUoNfyFxcAquzCAE")