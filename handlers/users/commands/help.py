from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message, state: FSMContext):
    await state.finish()
    text = ("List command: ",
            "/start - launch dialog (начать диалог)",
            "/help - display help (показать справку)",
            "/update - update account (обновить данные аккаунта)",
            "/delete - delete account (удалить аккаунт)",
            "/profile - show profile (посмотреть свой профиль)")

    await message.answer("\n".join(text))
