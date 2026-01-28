from aiogram import Bot, Dispatcher
import asyncio
import logging
from core.db_settings import execute_query
from core.models import users,courses, registrations
from handlers import start
from core.config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def startup():
    logging.info('Bot started')

    # Bu jadvallar yaratilganligini tekshirish
    for table in [users, courses,registrations]:
        execute_query(table)
    print('Jadvallar yaratildi ')


async def shutdown():
    logging.info('Bot stopped')


async def main():
    dp.include_router(start.router)

    dp.startup.register(startup)
    dp.shutdown.register(shutdown)

    await dp.start_polling(bot, timeout=0)

if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        level=logging.INFO
    )

    asyncio.run(main())
