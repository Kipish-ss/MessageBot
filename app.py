from loader import dp
import handlers
from aiogram import executor
from utils.misc import logging


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)