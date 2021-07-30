from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

check_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Yes (да)', callback_data='yes')],
        [InlineKeyboardButton(text='No (нет)', callback_data='no')]
    ]
)
