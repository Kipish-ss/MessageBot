from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Start the bot"),
            types.BotCommand("help", "Get info"),
            types.BotCommand("reset_for_all", "Reset all counts"),
            types.BotCommand("pohui", "Да и похуй"),
            types.BotCommand("joke", "Шутка от Димы"),
            types.BotCommand("update_name", "Update your name"),
            types.BotCommand("message_count", "Show your message count"),
            types.BotCommand("reset_count", "Reset your message count(set "
                                            "it to 0)"),
            types.BotCommand("count_by_name", "Message count of a particular user"),
            types.BotCommand("top_users", "Show top users by message count"),
            types.BotCommand("destroy", "Destroy your opponent")


        ]
    )
