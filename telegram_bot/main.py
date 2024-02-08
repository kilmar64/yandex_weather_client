import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from aiogram.filters import StateFilter

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
    dp.message.register(handlers.set_search_state, F.text.lower() == 'узнать погоду')
    dp.message.register(handlers.get_weather, StateFilter('SearchCity:searching_city'))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start_bot())
