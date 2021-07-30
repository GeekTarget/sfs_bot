from aiogram import types

from handlers.users import verification
from aiogram.dispatcher.filters.builtin import CommandStart
import asyncio

from loader import dp, db, bot
from data.config import ADMINS
from states import username

from keyboards.inline import cancel
from keyboards.default import admin_buttons


@dp.message_handler(text="/admin")
async def start_admin_panel(message: types.Message):
    if str(message.chat.id) in ADMINS:
        await message.answer("Вы попали в панель администратора", reply_markup=admin_buttons.adminPanelButtons)


@dp.message_handler(text="Дать доступ")
async def ask_username(message: types.Message):
    if str(message.chat.id) in ADMINS:
        await message.answer(
            "Введите username пользователя (в формате @Username), которому нужно дать доступ для пользования ботом",
            reply_markup=cancel.cancel_btn)
        await username.Username.name.set()


@dp.message_handler(state=username.Username.name)
async def give_access(message: types.Message):
    name = message.text
    await message.answer(db.change_access(name, 1))
    await bot.send_message(db.select_one_user(name), "🎊Ура! Ваша подписка продлена на месяц!\n✔Так же не забудьте "
                                                     "обновить свой аккаунт, выбрав /update\n\n "
                                                     "Hooray! Your subscription has been renewed for a month! Also, "
                                                     "do not update your account by selecting /update")


@dp.message_handler(text="Отнять доступ")
async def ask_username(message: types.Message):
    if str(message.chat.id) in ADMINS:
        await message.answer(
            "Введите username пользователя (в формате @Username), у которого нужно отнять доступ для пользования ботом",
            reply_markup=cancel.cancel_btn)
        await username.NoAccess.name.set()


@dp.message_handler(state=username.NoAccess.name)
async def give_access(message: types.Message):
    name = message.text
    await message.answer(db.change_access(name, 0))
