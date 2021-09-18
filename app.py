from loader import dp
import handlers
from aiogram import executor
from utils.misc import logging
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dp):
    # await on_startup_notify(dp)
    await set_default_commands(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    