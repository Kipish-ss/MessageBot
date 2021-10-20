# from aiogram import types
# from loader import dp
# from states.state_storage import States
# from utils.db_api.states_operations import get_state
#
#
# @dp.message_handler(lambda message: get_state(message.from_user.id) == States.start.value)
# async def answer_invalid_output(message: types.Message):
#     await message.reply("Type /start command to run the bot")
