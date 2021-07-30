import asyncio
from aiogram import executor
import handlers
from loader import dp, db
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from handlers.users import send_sfs, check_access


async def on_startup(dispatcher):
    # Пишет сообщения по расписанию
    asyncio.create_task(send_sfs.scheduler(db.select_users()))

    # Проверяет подписку
    asyncio.create_task(check_access.check_access(db.select_users()))

    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
