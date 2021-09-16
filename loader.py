from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.config import API_TOKEN


bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot)