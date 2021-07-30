from aiogram import types
from aiogram.dispatcher.filters import Command

from handlers.users import verification
import asyncio

from loader import dp, db


@dp.message_handler(Command("update"))
async def update_account(message: types.Message):
    if db.check_verification(message.chat.id) == 0:
        await message.answer("⛔У вас нет действующего аккаунта!\n✔Чтобы верифицироваться выберите /start\n\n"
                             "You do not have a valid account!\nSelect /start to verify")
    else:
        await verification.ask_subscribers(message.chat.id)
