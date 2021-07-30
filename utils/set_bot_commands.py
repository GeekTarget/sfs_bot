from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Launch bot"),
            types.BotCommand("help", "Display help"),
            types.BotCommand("update", "Update account"),
            types.BotCommand("delete", "Delete account"),
            types.BotCommand("profile", "Show profile"),
        ]
    )
