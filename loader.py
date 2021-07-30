import psycopg2
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.database.sfs_db import Database

from data import config

bot = Bot(token=config.BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

con = psycopg2.connect(
    database=config.DATABASE,
    user=config.USER,
    password=config.PASSWORD,
    host=config.HOST
)

db = Database(con)
