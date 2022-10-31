from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import token
from handlers import client, admin, lessons


storage = MemoryStorage()
bot = Bot(token, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)

client.client_handlers(dp)
admin.admin_handlers(dp)
lessons.lessons_handlers(dp)



