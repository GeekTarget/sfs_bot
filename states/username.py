from aiogram.dispatcher.filters.state import State, StatesGroup


class Username(StatesGroup):
    name = State()


class NoAccess(StatesGroup):
    name = State()
