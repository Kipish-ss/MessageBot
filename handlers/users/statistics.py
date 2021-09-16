from loader import dp
from aiogram import types
from keyboards.inline.stats import get_names_keyboard
from utils.db_api.msg_count import get_msg_count
from utils.db_api.user_operations import others_present
from utils.db_api.names import get_other_names
from keyboards.inline.callback_data import stats_callback
from utils.db_api.states_operations import get_state
from states.state_storage import States


@dp.message_handler(lambda message: get_state(message.from_user.id) == States.type_msg.value, commands=["stats"])
async def choose_name(message: types.Message):
    others = await others_present()
    if not others:
        await message.answer("You are currently the only user of this bot. Try again later.")
    else:
        names = await get_other_names()
        reply_keyboard = await get_names_keyboard(names)
        await message.answer("Choose any of the people below to see their message count:", reply_markup=reply_keyboard)


@dp.callback_query_handler(lambda message: get_state(message.from_user.id), stats_callback.filter())
async def show_stats(call: types.CallbackQuery, callback_data: dict):
    msg_count = await get_msg_count(user_name=callback_data.get("name"))
    await call.message.answer(f"{callback_data.get('name')} has sent {msg_count} messages.")

