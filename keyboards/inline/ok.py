from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ok_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='OK', callback_data='OK')]
    ]
)