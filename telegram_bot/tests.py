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
        bot_mock = AsyncMock()
        state_mock = AsyncMock()
        await handler(message_mock, bot=bot_mock, state=state_mock)
        return message_mock

    async def test_start(self):
        msg = await self.bot_call(handlers.start, '/start')
        response_data = msg.answer.call_args[0][0]

        self.assertEqual(response_data, 'Бот для получения текущей погоды')

    async def test_set_search_state(self):
        msg = await self.bot_call(handlers.set_search_state, 'Узнать погоду')
        msg.answer.assert_awaited_with('Введите город')

    async def test_get_weather(self):
        msg = await self.bot_call(handlers.get_weather, 'not a city')
        msg.answer.assert_awaited_with('Город не найден')

        msg = await self.bot_call(handlers.get_weather, 'Москва')
        response_data = msg.answer.call_args[0][0]
        self.assertIn('Температура', response_data)


if __name__ == '__main__':
    unittest.main()