from loader import dp
from aiogram import types
from keyboards.inline.stats import get_names_keyboard
from utils.db_api.msg_count import get_msg_count, reset_count, reset_for_all, get_top
from utils.db_api.user_operations import others_present
from utils.db_api.names import get_all_names, get_name
from keyboards.inline.callback_data import stats_callback
from utils.db_api.states_operations import get_state, set_state
from states.state_storage import States
from data.config import ADMINS


@dp.message_handler(lambda message: str(message.from_user.id) in ADMINS, commands=["reset_for_all"])
async def reset_all(message: types.Message):
        await reset_for_all()
        await message.reply("All message counts are set to 0")


@dp.message_handler(lambda message: get_state(message.from_user.id) == States.type_msg.value, commands=['reset_count'])
async def reset_msg_count(message: types.Message):
    await reset_count(message.from_user.id)
    await message.reply("Your message count is now 0. Type messages to increase it.")


@dp.message_handler(lambda message: get_state(message.from_user.id) == States.type_msg.value, commands=["message_count"])
async def show_msg_count(message: types.Message):
    count = await get_msg_count(message.from_user.id)
    await message.reply(f"Your current message count is {count}.")


@dp.message_handler(lambda message: get_state(message.from_user.id) == States.type_msg.value, commands=["count_by_name"])
async def show_name_count(message: types.Message):
    await message.reply("Enter the name of the user:")
    await set_state(user_id=message.from_user.id, state=States.type_user.value)


@dp.message_handler(lambda message: get_state(message.from_user.id) == States.type_user.value)
async def show_user_count(message: types.Message):
    msg_count = await get_msg_count(user_name=message.text)
    if msg_count is None:
        await message.reply("There is no user with such name. Try another name.")
    else:
        await message.reply(f"{message.text} has sent {msg_count} messages.")
        await set_state(user_id=message.from_user.id, state=States.type_msg.value)


@dp.message_handler(lambda message: get_state(message.from_user.id) == States.type_msg.value, commands=["top_users"])
async def choose_name(message: types.Message):
    others = await others_present()
    if not others:
        await message.answer("You are currently the only user of this bot. Try again later.")
    else:
        names = await get_all_names()
        if len(names) >= 10:
            length = 10
        else:
            length = len(names)
        count_list = await get_top(length)
        name_list = []
        for count in count_list:
            name = await get_name(count)
            name_list.append(name)
        reply_keyboard = await get_names_keyboard(name_list)
        await message.answer("Choose any of the people below to see their message count:", reply_markup=reply_keyboard)


@dp.callback_query_handler(lambda message: get_state(message.from_user.id), stats_callback.filter())
async def show_top_10(call: types.CallbackQuery, callback_data: dict):
    msg_count = await get_msg_count(user_name=callback_data.get("name"))
    await call.message.answer(f"{callback_data.get('name')} has sent {msg_count} messages.")

