from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Commands list: ",
            "/start - Start the bot",
            "/help - Get info",
            "/reset_for_all - Reset all counts",
            "/pohui - Да и похуй",
            "/joke - Шутка от Димы",
            "/update_name - Update your name",
            "/message_count - Show your message count",
            "/reset_count - Reset your message count(set it to 0)",
            "/count_by_name - Message count of a particular user",
            "/top_users - Show top users by message count",
            "/destroy - Destroy your opponent")

    await message.answer("\n".join(text))