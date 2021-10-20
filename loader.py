from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)
# storage = MemoryStorage()
dp = Dispatcher(bot)