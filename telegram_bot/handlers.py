import aiohttp
from aiogram import Bot
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.fsm.context import FSMContext

import config
import messages
import states


async def start(message: Message, bot: Bot, state: FSMContext):
    btn = KeyboardButton(text='Узнать погоду')
    kb = ReplyKeyboardMarkup(keyboard=[[btn]], resize_keyboard=True)

    await state.set_state(states.SearchCity.not_searching_city)
    await message.answer(messages.START, reply_markup=kb)


async def set_search_state(message: Message, bot: Bot, state: FSMContext):
    await state.set_state(states.SearchCity.searching_city)
    await message.answer(messages.INPUT_PROMPT)


async def get_weather(message: Message, bot: Bot, state: FSMContext):
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