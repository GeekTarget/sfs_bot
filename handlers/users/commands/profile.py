from aiogram import types
from aiogram.dispatcher.filters import Command

from handlers.users import verification
import asyncio

from loader import dp, db


@dp.message_handler(Command("profile"))
async def update_account(message: types.Message):
    if db.check_verification(message.chat.id) == 0:
        await message.answer("⛔У вас нет действующего аккаунта!\n✔Чтобы верифицироваться выберите /start\n\n"
                             "You do not have a valid account!\nSelect /start to verify")
    else:
        data = db.show_data_user(message.chat.id)
        username = data[1]
        number_of_subs = data[2]
        percent = data[3]
        date = data[6].split("-")
        text = f"Ваш профиль:\nYour profile:\n\n👤Username:{username}\n📈Number of subscribers: {number_of_subs}\n" \
               f"📊Popularity percentage: {percent}\n\n📅Срок подписки до:\nSubscription period until:\n" \
               f"{date[2]}.{date[1]}.{date[0]}"
        await message.answer(text)
