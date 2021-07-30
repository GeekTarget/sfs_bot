from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

cancel_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Cancel (Отмена)', callback_data='Cancel')]
    ]
)