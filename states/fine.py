from aiogram.dispatcher.filters.state import State, StatesGroup

class FineState(StatesGroup):
    reason = State()
    comment = State()
    confirm = State()