from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

adminPanelButtons = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Дать доступ'),
         KeyboardButton(text='Отнять доступ')]
    ],
    resize_keyboard=True
)
