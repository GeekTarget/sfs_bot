from aiogram import types

from handlers.users import verification
from aiogram.dispatcher.filters.builtin import CommandStart
import asyncio

from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if db.check_verification(message.chat.id) == 0:
        text = "🤚Здравствуйте, это SFS Bot и я помогу тебе находить людей для sfs со схожими параметрами\n\n " \
               "Hello, this is SFS Bot and I will help you find people for sfs with similar parameters"
        await message.answer(text)
        await asyncio.sleep(1)
        await verification.ask_subscribers(message.chat.id)
    else:
        text = "✔Вы уже верифицированы. Ждите предложения для взаимного пиара!\nЕсли хотите обновить свой аккаунт " \
               "выберите команду /update \n\n" \
               "You are already verified. Wait for proposals for mutual PR!\nIf you want to update your account, " \
               "select the command /update "

        await message.answer(text)
