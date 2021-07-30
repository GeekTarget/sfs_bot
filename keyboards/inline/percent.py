from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

percent_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='10%+', callback_data='10%+')],
        [InlineKeyboardButton(text='< 10%', callback_data='< 10%')],
        [InlineKeyboardButton(text='< 5%', callback_data='< 5%')],
        [InlineKeyboardButton(text='< 2,5%', callback_data='< 2,5%')],
        [InlineKeyboardButton(text='< 1%', callback_data='< 1%')],
        [InlineKeyboardButton(text='< 0.5%', callback_data='< 0.5%')],
        [InlineKeyboardButton(text='Cancel (Отмена)', callback_data='Cancel')]
    ]
)
