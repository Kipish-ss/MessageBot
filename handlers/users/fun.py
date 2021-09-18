from aiogram import types
from loader import dp, bot
import re
from .convert import convert_text
from data.config import dictionary, reg_exp
from utils.db_api.msg_count import update_count


@dp.message_handler(commands=["pohui"])
async def send_sticker_poh(message: types.Message):
    message_rep = (message.reply_to_message if message.reply_to_message else message)
    await message_rep.reply_sticker("CAACAgIAAxkBAAEC6WhhQzQdw3nzzd3kRkJ8egaaWjU0bwACJBEAAjjPCErozPuz2LIq6CAE")
    try:
        await bot.delete_message(message.chat.id, message.message_id)
    except:
        print("Cannot delete")


@dp.message_handler(commands=["joke"])
async def send_sticker_joke(message: types.Message):
    await message.reply_sticker("CAACAgIAAxkBAAEC6XFhQzcUx_r7JNRlEJsw8Jnu5Y-GywAC1Q8AAjk7AUoNfyFxcAquzCAE")


@dp.message_handler(commands=["destroy"])
async def send_punch_sticker(message: types.Message):
    message_rep = (message.reply_to_message if message.reply_to_message else message)
    await message_rep.reply_sticker("CAACAgIAAxkBAAEC7WdhRj9pPGb1sEwBOhEN1CiIkAwM6wACfREAAiyAIErNYOoAAeq-Ep8gBA")
    try:
        await bot.delete_message(message.chat.id, message.message_id)
    except:
        print("Cannot delete")


@dp.message_handler(regexp=reg_exp)
async def replace_six_or_nine(message: types.Message):
    await update_count(message.from_user.id)
    rep = dict((re.escape(k), v) for k, v in dictionary.items())
    regex = "|".join(rep.keys())
    pattern: re.Pattern = re.compile(regex)
    text = message.text.lower()
    end = 0
    answer = list(message.text)
    new_end = 0
    while text:
        temp_end = end
        if re.search(pattern, text) is None:
            break
        match = re.search(pattern, text)
        start = match.start() + end
        end_relative = match.end()
        end = match.end() + end
        new_start = start + (new_end - temp_end)
        new_end += end - temp_end
        span = end - start
        new_word = convert_text(message.text[start: end], rep)  # this function works properly
        if len(new_word) > span:
            new_end += len(new_word) - span
        word_start = 0
        count_minus = 0
        for i in range(new_start, new_end):
            if (i - new_start) >= len(new_word):
                answer.pop(i - count_minus)
                count_minus += 1
                new_end -= 1
            else:
                if new_start + span <= i:
                    answer.insert(i, new_word[word_start])
                    i += 1
                else:
                    answer[i] = new_word[word_start]
                word_start += 1
        print(f"Answer = {''.join(answer)}")
        print(f'End = {end}')
        print(f"New end = {new_end}")
        print(f'Start = {start}')
        print(f'New start = {new_start}')
        print(new_word)
        print(f'Text before: {text}')
        text = text[end_relative:]
        print(f'Text after: {text}')
    answer = "".join(answer)
    await message.reply(answer)