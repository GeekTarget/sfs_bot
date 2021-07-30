from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

num_of_subs = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='< 100', callback_data='< 100')],
        [InlineKeyboardButton(text='< 500', callback_data='< 500')],
        [InlineKeyboardButton(text='< 1000', callback_data='< 1000')],
        [InlineKeyboardButton(text='< 2 500', callback_data='< 2 500')],
        [InlineKeyboardButton(text='< 5 000', callback_data='< 5 000')],
        [InlineKeyboardButton(text='< 10 000', callback_data='< 10 000')],
        [InlineKeyboardButton(text='< 20 000', callback_data='< 20 000')],
        [InlineKeyboardButton(text='20000+', callback_data='20000+')],
        [InlineKeyboardButton(text='Cancel (Отмена)', callback_data='Cancel')]
    ]
)
