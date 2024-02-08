from aiogram.fsm.state import StatesGroup, State

class SearchCity(StatesGroup):
    searching_city = State()
    not_searching_city = State()