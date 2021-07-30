import asyncio
from collections import defaultdict
from random import randint
from loader import bot
from datetime import datetime


async def scheduler(user_list):
    while True:
        if datetime.now().hour == 10 and datetime.now().minute == 21:
            new_list = list()

            for i in user_list:
                elem = i[2], i[3]
                if i[5] == 1:
                    new_list.append(elem)

            D = defaultdict(list)
            for i, item in enumerate(new_list):
                D[item].append(i)
            D = [v for k, v in D.items() if len(v) > 1]

            for i in D:
                if len(i) == 1:
                    await bot.send_message(user_list[i[0]][0],
                                           "😔Извините, сегодня в вашей категории нету новых предложений.\n\n"
                                           "Sorry, there are no new offers in your category today.")
                elif len(i) == 2:
                    await bot.send_message(user_list[i[0]][0],
                                           f"💥Привет, сегодня у тебя такие предложения для sfs : \nHi, today you "
                                           f"have the "
                                           f"following suggestions for sfs:\n\n👤 - {user_list[i[1]][1]}\n📈Количество подписчиков "
                                           f"(Number of subscribers): {user_list[i[1]][2]}\n📊Процент популярности (Popularity "
                                           f"percentage):{user_list[i[1]][3]}")
                    await bot.send_video(user_list[i[0]][0], user_list[i[1]][4])

                    await bot.send_message(user_list[i[1]][0],
                                           f"💥Привет, сегодня у тебя такие предложения для sfs : \nHi, today you "
                                           f"have the "
                                           f"following suggestions for sfs:\n\n👤 - {user_list[i[0]][1]}\n📈Количество подписчиков "
                                           f"(Number of subscribers): {user_list[i[0]][2]}\n📊Процент популярности (Popularity "
                                           f"percentage):{user_list[i[0]][3]}")
                    await bot.send_video(user_list[i[1]][0], user_list[i[0]][4])

                else:

                    for j in i:

                        def sort(x):
                            if x != j:
                                return 1
                            else:
                                return 0

                        sorted_list = list(filter(sort, i))
                        user_index = -1
                        iteration = 0
                        while iteration != 2:
                            index = randint(0, len(sorted_list) - 1)
                            if user_index != index:
                                users_number = sorted_list[index]
                                await bot.send_message(user_list[j][0],
                                                       f"💥Привет, сегодня у тебя такие предложения для sfs : \nHi, "
                                                       f"today you "
                                                       f"have the "
                                                       f"following suggestions for sfs:\n\n👤 - {user_list[users_number][1]}\n📈Количество подписчиков "
                                                       f"(Number of subscribers): {user_list[users_number][2]}\n📊Процент "
                                                       f"популярности (Popularity "
                                                       f"percentage):{user_list[users_number][3]}")
                                await bot.send_video(user_list[j][0], user_list[users_number][4])
                                iteration += 1
                                user_index = index
            await asyncio.sleep(60)
        else:
            await asyncio.sleep(60)
