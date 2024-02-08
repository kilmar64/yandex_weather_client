import unittest
from typing import Callable
from unittest.mock import AsyncMock

import handlers


class HandlersTestCase(unittest.IsolatedAsyncioTestCase):
    async def bot_call(self, handler: Callable, data: str) -> AsyncMock:
        '''
        Calls bot handler with data
        '''
        message_mock = AsyncMock(text=data)
        bot_mock = AsyncMock
        await handler(message_mock, bot_mock)
        return message_mock

    async def test_start(self):
        msg = await self.bot_call(handlers.start, '/start')
        msg.answer.assert_awaited_with('Бот для получения текущей погоды\nВведите название города')

    async def test_help(self):
        msg = await self.bot_call(handlers.help, '/help')
        msg.answer.assert_awaited_with('Напишите название города на русском языке, чтобы получить текущую погоду')

    async def test_get_weather(self):
        msg = await self.bot_call(handlers.get_weather, 'not a city')
        msg.answer.assert_awaited_with('Город не найден')

        msg = await self.bot_call(handlers.get_weather, 'Москва')
        response_data = msg.answer.call_args[0][0]
        self.assertIn('Температура', response_data)


if __name__ == '__main__':
    unittest.main()