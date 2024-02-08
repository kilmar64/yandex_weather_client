import aiohttp
from aiogram import Bot
from aiogram.types import Message

import config
import messages


async def start(message: Message, bot: Bot):
    await message.answer(messages.START)


async def help(message: Message, bot: Bot):
    await message.answer(messages.HELP)


async def get_weather(message: Message, bot: Bot):
    city = str(message.text)
    status = 404
    response = {}

    # Query
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(config.WEATHER_API_URL, params={'city': city}) as resp:
                status = resp.status
                response = await resp.json()
    except:
        await message.answer(messages.ERR_CONNECT)
        return

    # Process bad response
    if status == 404:
        await message.answer(messages.ERR_404)
        return
    elif status != 200:
        await message.answer(messages.ERR_OTHER)
        return

    # Fetch weather data
    temp = response.get('temp')
    pressure = response.get('pressure')
    wind_speed = response.get('wind_speed')

    response_text = f'Температура: {temp} °C\nДавление: {pressure} мм рт.ст.\nСкорость ветра: {wind_speed} м/c'
    await message.answer(response_text)