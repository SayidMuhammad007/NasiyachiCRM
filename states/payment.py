from aiogram.dispatcher.filters.state import State, StatesGroup

class PaymenState(StatesGroup):
    partnerId = State()
    price = State()
    change = State()
    confirming = State()
    img = State()
    id = State()