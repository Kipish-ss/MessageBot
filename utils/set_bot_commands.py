from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("pohui", "Да и похуй"),
            types.BotCommand("joke", "Шутка от Димы"),
            types.BotCommand("start", "Begin the dialogue "),
            types.BotCommand("help", "Get info"),
            types.BotCommand("update_name", "Update your name"),
            types.BotCommand("message_count", "Show your message count"),
            types.BotCommand("reset_count", "Reset your message count(set "
                                            "it to 0)"),
            types.BotCommand("stats", "Show statistics"),
            types.BotCommand("destroy", "Destroy your opponent")


        ]
    )
