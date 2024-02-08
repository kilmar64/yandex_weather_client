import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command

import config
import handlers
from commands import set_commands


async def bot_init(bot: Bot):
    await set_commands(bot)


async def start_bot():
    bot = Bot(config.TG_API_KEY)
    dp = Dispatcher()

    dp.startup.register(bot_init)
    dp.message.register(handlers.start, Command('start'))
    dp.message.register(handlers.help, Command('help'))
    dp.message.register(handlers.get_weather)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start_bot())
