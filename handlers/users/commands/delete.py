from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.inline.check import check_btn
from loader import dp, db


@dp.message_handler(Command("delete"))
async def delete_account(message: types.Message):
    if db.check_verification(message.chat.id) == 0:
        await message.answer("⛔У вас нет действующего аккаунта!\n✔Чтобы верифицироваться выберите /start\n\n"
                             "You do not have a valid account!\nSelect /start to verify")
    else:
        await message.answer("Вы уверены?\n\nAre you sure?", reply_markup=check_btn)


@dp.callback_query_handler(text=['yes', 'no'])
async def yes_or_no(call: types.CallbackQuery):
    if call.data == "no":
        await call.message.edit_reply_markup()
        await call.message.edit_text("Действие отменено")
    else:
        db.delete_account(call.message.chat.id)
        await call.message.edit_reply_markup()
        await call.message.edit_text("❌Ваш аккаунт удален!\n✔Чтобы снова зарегистрироваться нажми /start")
