import asyncio
from datetime import datetime
from loader import bot, db


async def check_access(user_list):
    while True:
        for item in user_list:
            if item[5] == 1:
                date = item[6].split("-")
                year = datetime.now().year
                month = datetime.now().month
                day = datetime.now().day
                if month < 10:
                    month = "0" + str(month)
                if day < 10:
                    month = "0" + str(day)

                if str(year) == str(date[0]) and str(month) == str(date[1]) and str(day) == str(date[2]):
                    await bot.send_message(item[0], "❌Привет, твоя подписка, к сожалению, закончилась.\n"
                                                    "✔Если тебе понравился бот и ты хочешь продолжать пользование - напиши пользователю @Just_just11.\n"
                                                    "Он тебе объяснит, что делать дальше!\n\n"
                                                    "Hello, your subscription has expired unfortunately.\n"
                                                    "If you like the bot and want to continue using it, write to @ Just_just11.\n"
                                                    "He will explain to you what to do next.")
                    db.change_access(item[1], 0)
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
            else:
                await asyncio.sleep(1)
        else:
            await asyncio.sleep(1)
