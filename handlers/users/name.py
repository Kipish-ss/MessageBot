from aiogram import types
from loader import dp
from states.state_storage import States
from utils.db_api.user_operations import exists
from utils.db_api.names import update_user_name, get_user_name
from utils.db_api.states_operations import set_state, get_state


# @dp.message_handler(lambda message: get_state(message.from_user.id) == States.enter_name.value)
# async def add_user(message: types.Message):
#     if len(message.text) < 2 or not message.text.isalpha():
#         await message.answer('Please enter a valid name.')
#     is_present = await exists(user_name=message.text)
#     if is_present:
#         await message.answer("This name already exists. Enter a unique one.")
#     else:
#         text = await insert_user(message.from_user.id, message.text.capitalize())
#         greeting = await greet_user(message.text.capitalize(), user_id=message.from_user.id)
#         await message.answer(text)
#         await message.answer(greeting)
#         await set_state(user_id=message.from_user.id, state=States.type_msg.value)


@dp.message_handler(lambda message: get_state(message.from_user.id) == States.type_msg.value, commands=["update_name"])
async def update_handler(message: types.Message):
    """
            This handler will be called when user sends `/update` command
    """
    await message.answer('Enter the new name you want me to call you by:')
    await set_state(user_id=message.from_user.id, state=States.update_name.value)


@dp.message_handler(lambda message: get_state(message.from_user.id) == States.update_name.value)
async def update_name(message: types.Message):
    old_name = await get_user_name(message.from_user.id)
    is_present = await exists(user_name=message.text)
    if len(message.text) < 2 or not message.text.isalpha():
        await message.reply('Please enter a real name.')
    elif message.text == old_name:
        await message.reply("This name is your old name. Enter a new one.")
    elif is_present:
        await message.reply("This name already exists. Enter a unique one.")
    else:
        text = await update_user_name(message.text, message.from_user.id)
        await message.reply(text)
        await set_state(user_id=message.from_user.id, state=States.type_msg.value)